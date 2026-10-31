"""Animated Reels: kinetic captions, count-up numbers, stamps, a mascot, progress bar.

Each scene is an HTML page whose elements carry animation hints:
  <div class="a" data-a="pop" data-t="0.2" data-d="0.4">…</div>
  data-a: pop | up | stamp | count | bar | fill | wave
  data-t: start time within the scene (s), data-d: duration (s)
  count: data-to="20000" data-pre="$"   (counts up)
  words: wrap text with words("…", start, step) to reveal word by word
A JS render(t, g) function sets every element for local time t and global time g. Frames are captured
with Playwright and piped straight into ffmpeg (one encoded file per scene), scenes are joined with
the concat demuxer, and a silent audio bed is added (Instagram's Audio API attaches real music at publish).
"""
import asyncio, os, subprocess, tempfile, shutil
from playwright.async_api import async_playwright

HERE = os.path.dirname(os.path.abspath(__file__))
W, H, FPS = 1080, 1920, 30
NAVY, BONE, BRASS, GREEN, RED = "#0F1B2D", "#F4F0E8", "#C9A15F", "#3FD07F", "#FF5A4E"

FONTS = f"""
@font-face{{font-family:'DM Serif Display';src:url('file://{HERE}/fonts/dmserif.woff2')}}
@font-face{{font-family:'IBM Plex Mono';src:url('file://{HERE}/fonts/ibm-plex-mono-latin-600-normal.woff2');font-weight:600}}
"""

JS = r"""
const C=(x)=>Math.max(0,Math.min(1,x));
const out3=(x)=>1-Math.pow(1-x,3);
const back=(x)=>{const c1=1.9,c3=c1+1;return 1+c3*Math.pow(x-1,3)+c1*Math.pow(x-1,2)};
function render(t,g,total){
  document.querySelectorAll('.a').forEach(el=>{
    const s=+el.dataset.t||0, d=+el.dataset.d||0.4, a=el.dataset.a, p=C((t-s)/d);
    if(a==='pop'){el.style.opacity=p>0?1:0;el.style.transform=`scale(${0.4+0.6*back(p)})`}
    else if(a==='up'){el.style.opacity=out3(p);el.style.transform=`translateY(${(1-out3(p))*70}px)`}
    else if(a==='stamp'){el.style.opacity=p>0?1:0;el.style.transform=`rotate(-7deg) scale(${2.4-1.4*out3(p)})`}
    else if(a==='count'){const to=+el.dataset.to;el.textContent=(el.dataset.pre||'')+Math.round(to*out3(p)).toLocaleString('en-AU')+(el.dataset.post||'');el.style.opacity=t>=s?1:0}
    else if(a==='bar'){el.style.width=(out3(p)*(+el.dataset.w||100))+'%'}
    else if(a==='fill'){const kids=[...el.children];kids.forEach((k,i)=>{const q=C((t-s-i*d/kids.length)/0.15);k.style.background=q>0.5?el.dataset.on:'transparent';k.style.transform=`scale(${0.8+0.2*back(q)})`})}
    else if(a==='shake'){const q=C((t-s)/d);el.style.transform=`translateX(${Math.sin(q*40)*14*(1-q)}px)`}
  });
  document.querySelectorAll('.mascot').forEach(m=>{
    const bob=Math.sin(g*5)*10; m.style.transform=`translateY(${bob}px) rotate(${Math.sin(g*2.5)*3}deg)`;
    const blink=(g%2.6)<0.12?0.1:1; m.querySelectorAll('.eye').forEach(e=>e.setAttribute('transform',`translate(0 ${e.dataset.cy*(1-blink)}) scale(1 ${blink})`));
    const arm=m.querySelector('.arm'); if(arm) arm.setAttribute('transform',`rotate(${Math.sin(g*9)*(m.dataset.wave==='1'?28:6)} ${arm.dataset.ox} ${arm.dataset.oy})`);
  });
  const pb=document.getElementById('pbar'); if(pb) pb.style.width=(100*g/total)+'%';
}
"""


def words(text, start=0.0, step=0.12, cls=""):
    """Reveal text word by word. Wrap a word in [[…]] to highlight it."""
    out, i = [], 0
    for w in text.split():
        hl = w.startswith("[[") and w.rstrip(".,!?").endswith("]]")
        clean = w.replace("[[", "").replace("]]", "")
        style = f"background:{BRASS};color:{NAVY};padding:0 14px;border-radius:10px;" if hl else ""
        out.append(f'<span class="a {cls}" data-a="pop" data-t="{start + i*step:.2f}" data-d="0.28" style="display:inline-block;{style}">{clean}</span>')
        i += 1
    return " ".join(out)


def coin_mascot(size=300, wave=False, x=0, y=0, extra=""):
    """'Penny', an original brass-coin accountant with round glasses and a navy bow tie (Retained's character)."""
    return f"""<div class="mascot" data-wave="{1 if wave else 0}" style="position:absolute;left:{x}px;top:{y}px;width:{size}px;height:{size*1.25}px;{extra}">
<svg viewBox="0 0 200 250" width="{size}" height="{size*1.25}">
 <defs><radialGradient id="cg" cx="40%" cy="35%"><stop offset="0" stop-color="#F6D58E"/><stop offset=".65" stop-color="#C9A15F"/><stop offset="1" stop-color="#8E6A2E"/></radialGradient></defs>
 <line x1="80" y1="185" x2="70" y2="232" stroke="#0F1B2D" stroke-width="9" stroke-linecap="round"/>
 <line x1="120" y1="185" x2="130" y2="232" stroke="#0F1B2D" stroke-width="9" stroke-linecap="round"/>
 <ellipse cx="66" cy="236" rx="16" ry="7" fill="#0F1B2D"/><ellipse cx="134" cy="236" rx="16" ry="7" fill="#0F1B2D"/>
 <line x1="22" y1="112" x2="2" y2="150" stroke="#F4F0E8" stroke-width="9" stroke-linecap="round"/><circle cx="2" cy="152" r="9" fill="#F4F0E8"/>
 <g class="arm" data-ox="178" data-oy="112"><line x1="178" y1="112" x2="198" y2="70" stroke="#F4F0E8" stroke-width="9" stroke-linecap="round"/><circle cx="198" cy="66" r="9" fill="#F4F0E8"/></g>
 <circle cx="100" cy="110" r="84" fill="url(#cg)" stroke="#7A5C2E" stroke-width="6"/>
 <circle cx="100" cy="110" r="66" fill="none" stroke="#E8C77D" stroke-width="3" stroke-dasharray="4 7"/>
 <g class="eye" data-cy="92"><ellipse cx="76" cy="92" rx="11" ry="14" fill="#0F1B2D"/><circle cx="80" cy="87" r="4" fill="#fff"/></g>
 <g class="eye" data-cy="92"><ellipse cx="124" cy="92" rx="11" ry="14" fill="#0F1B2D"/><circle cx="128" cy="87" r="4" fill="#fff"/></g>
 <circle cx="76" cy="92" r="23" fill="none" stroke="#0F1B2D" stroke-width="5"/><circle cx="124" cy="92" r="23" fill="none" stroke="#0F1B2D" stroke-width="5"/>
 <line x1="99" y1="92" x2="101" y2="92" stroke="#0F1B2D" stroke-width="5"/>
 <path d="M70 66 q8 -8 18 -3" stroke="#0F1B2D" stroke-width="5" fill="none" stroke-linecap="round"/><path d="M112 63 q10 -5 18 3" stroke="#0F1B2D" stroke-width="5" fill="none" stroke-linecap="round"/>
 <path d="M76 132 q24 22 48 0" stroke="#0F1B2D" stroke-width="6" fill="#7A2E2E" stroke-linecap="round"/>
 <path d="M84 176 l16 10 l16 -10 l0 22 l-16 -10 l-16 10 z" fill="#0F1B2D"/><circle cx="100" cy="187" r="5" fill="#C9A15F"/>
</svg></div>"""


def scene(body, bg=NAVY, fg=BONE):
    """Full-frame scene with a top progress bar and the RETAINED tag. Keep key text between y=260 and y=1550."""
    return f"""<!doctype html><html><head><meta charset="utf-8"><style>{FONTS}
body{{margin:0}} .a{{will-change:transform,opacity}}
.wrap{{width:{W}px;height:{H}px;position:relative;overflow:hidden;background:{bg};color:{fg};font-family:Inter,sans-serif}}
.grain{{position:absolute;inset:0;background:radial-gradient(1200px 900px at 20% 10%,rgba(201,161,95,.18),transparent 60%),radial-gradient(900px 900px at 90% 90%,rgba(63,208,127,.08),transparent 60%)}}
</style></head><body><div class="wrap"><div class="grain"></div>
<div style="position:absolute;left:0;top:0;height:14px;width:100%;background:rgba(255,255,255,.12)"><div id="pbar" style="height:100%;width:0;background:{BRASS}"></div></div>
<div style="position:absolute;left:80px;top:150px;font-family:'IBM Plex Mono',monospace;font-weight:600;font-size:30px;letter-spacing:.16em;color:{BRASS}">RETAINED</div>
{body}
</div><script>{JS}</script></body></html>"""


def render_motion(scenes, make_file, cover_scene=0, cover_t=None):
    """scenes: list of (html, seconds). Writes reel.mp4 and cover.jpg next to make_file."""
    folder = os.path.dirname(os.path.abspath(make_file))
    tmp = tempfile.mkdtemp()
    total = sum(d for _, d in scenes)
    clips = []

    async def go():
        async with async_playwright() as p:
            b = await p.chromium.launch()
            pg = await b.new_page(viewport={"width": W, "height": H})
            g0 = 0.0
            for si, (html, dur) in enumerate(scenes):
                f = os.path.join(HERE, "_motion.html"); open(f, "w").write(html)
                await pg.goto("file://" + f); await pg.evaluate("document.fonts.ready")
                part = os.path.join(tmp, f"s{si}.part.mp4")
                ff = subprocess.Popen(["ffmpeg", "-y", "-loglevel", "error", "-f", "image2pipe", "-framerate", str(FPS),
                                       "-c:v", "mjpeg", "-i", "-", "-c:v", "libx264", "-preset", "veryfast", "-crf", "18",
                                       "-pix_fmt", "yuv420p", "-r", str(FPS), part], stdin=subprocess.PIPE)
                n = int(round(dur * FPS))
                for i in range(n):
                    t = i / FPS
                    await pg.evaluate(f"render({t},{g0 + t},{total})")
                    ff.stdin.write(await pg.screenshot(type="jpeg", quality=92))
                    if si == cover_scene and ((cover_t is None and i == n - 1) or (cover_t is not None and abs(t - cover_t) < 1 / FPS / 2)):
                        await pg.screenshot(path=os.path.join(tmp, "cover.png"))
                ff.stdin.close(); ff.wait()
                if ff.returncode != 0:
                    raise RuntimeError(f"ffmpeg failed on scene {si}")
                final = part.replace(".part.mp4", ".mp4"); os.rename(part, final); clips.append(final)
                g0 += dur
            await b.close()
            os.remove(os.path.join(HERE, "_motion.html"))
    asyncio.run(go())

    lst = os.path.join(tmp, "list.txt"); open(lst, "w").write("".join(f"file '{c}'\n" for c in clips))
    joined = os.path.join(tmp, "joined.mp4")
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", lst, "-c", "copy", joined], check=True)
    out = os.path.join(folder, "reel.part.mp4")
    subprocess.run(["ffmpeg", "-y", "-loglevel", "error", "-i", joined, "-f", "lavfi", "-i", "anullsrc=channel_layout=stereo:sample_rate=48000",
                    "-map", "0:v", "-map", "1:a", "-c:v", "copy", "-c:a", "aac", "-b:a", "128k", "-t", f"{total}",
                    "-movflags", "+faststart", out], check=True)
    os.replace(out, os.path.join(folder, "reel.mp4"))
    from PIL import Image
    Image.open(os.path.join(tmp, "cover.png")).convert("RGB").crop((0, 285, 1080, 1635)).save(os.path.join(folder, "cover.jpg"), "JPEG", quality=92)
    shutil.rmtree(tmp)
    print(f"reel.mp4 ({total:.1f}s) + cover.jpg -> {folder}")
