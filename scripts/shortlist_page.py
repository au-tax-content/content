"""Build engage/shortlist.html (a phone-friendly comment checklist) from engage/picks.json.
The weekly run updates picks.json, runs this, and republishes the artifact (slug in CLAUDE.md)."""
import json, html, os
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
d = json.load(open(os.path.join(ROOT, "engage", "picks.json")))
ACC = {"retained": ("@retained.au", "#C9A15F"), "returnpolicy": ("@returnpolicy.au", "#3FD07F")}

def cards(key):
    handle, col = ACC[key]
    out = []
    for i, p in enumerate(d[key]):
        cid = f"{key}-{i}"
        out.append(f"""<div class="card" id="c-{cid}">
  <div class="top"><span class="who">{html.escape(p['who'])}</span><label class="done"><input type="checkbox" data-id="{cid}"> Done</label></div>
  <div class="what">{html.escape(p['what'])}</div>
  <div class="cm" id="t-{cid}">{html.escape(p['comment'])}</div>
  <div class="btns"><a class="btn open" href="{html.escape(p['url'])}" target="_blank" rel="noopener">Open post</a>
  <button class="btn copy" data-t="t-{cid}" style="--c:{col}">Copy comment</button></div>
</div>""")
    return f"""<section id="{key}" class="tab"><div class="switch" style="border-color:{col}">Switch Instagram to <b style="color:{col}">{handle}</b> first</div>{''.join(out)}</section>"""

page = f"""<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Comment shortlist</title><style>
*{{box-sizing:border-box}} body{{margin:0;background:#0F1B2D;color:#F4F0E8;font:16px/1.45 -apple-system,Segoe UI,Inter,sans-serif}}
header{{padding:20px 18px 6px}} h1{{margin:0;font-size:22px}} .sub{{color:#9A9384;font-size:14px;margin-top:4px}}
.tabs{{display:flex;gap:8px;padding:12px 18px;position:sticky;top:0;background:#0F1B2D;z-index:2}}
.tabs button{{flex:1;padding:12px;border-radius:12px;border:1px solid #2B3A52;background:#16243A;color:#F4F0E8;font-weight:600;font-size:15px}}
.tabs button.on{{background:#F4F0E8;color:#0F1B2D}} .tab{{display:none;padding:0 18px 30px}} .tab.on{{display:block}}
.switch{{border:1px dashed;border-radius:12px;padding:10px 12px;margin:6px 0 14px;font-size:14px}}
.card{{background:#16243A;border:1px solid #2B3A52;border-radius:16px;padding:14px;margin-bottom:12px}} .card.is-done{{opacity:.45}}
.top{{display:flex;justify-content:space-between;align-items:center}} .who{{font-weight:700}} .done{{font-size:14px;color:#9A9384}}
.what{{color:#C9C2B4;font-size:14px;margin:2px 0 10px}} .cm{{background:#0F1B2D;border-radius:10px;padding:10px 12px;font-size:15px}}
.btns{{display:flex;gap:8px;margin-top:10px}} .btn{{flex:1;text-align:center;padding:12px;border-radius:12px;font-weight:600;font-size:15px;text-decoration:none;border:0}}
.open{{background:#F4F0E8;color:#0F1B2D}} .copy{{background:var(--c);color:#0F1B2D}}
.rules{{color:#9A9384;font-size:13px;padding:0 18px 30px}}
</style></head><body>
<header><h1>Comment shortlist</h1><div class="sub">{html.escape(d['week'])} · about 10 minutes a day · tweak the wording so it sounds like you</div></header>
<div class="tabs"><button data-tab="retained" class="on">Retained</button><button data-tab="returnpolicy">Return Policy</button></div>
{cards('retained')}{cards('returnpolicy')}
<div class="rules">Spread these over a few days. Never add "follow us", links or DMs. If someone asks a personal question, keep it general: "depends on your situation, worth asking a registered tax agent".</div>
<script>
const K='shortlist-done-{html.escape(d['week'])}';
let done={{}}; try{{done=JSON.parse(localStorage.getItem(K)||'{{}}')}}catch(e){{}}
function save(){{try{{localStorage.setItem(K,JSON.stringify(done))}}catch(e){{}}}}
document.querySelectorAll('input[data-id]').forEach(cb=>{{const id=cb.dataset.id;cb.checked=!!done[id];
 document.getElementById('c-'+id).classList.toggle('is-done',cb.checked);
 cb.addEventListener('change',()=>{{done[id]=cb.checked;save();document.getElementById('c-'+id).classList.toggle('is-done',cb.checked)}})}});
function show(t){{document.querySelectorAll('.tab').forEach(s=>s.classList.toggle('on',s.id===t));document.querySelectorAll('.tabs button').forEach(b=>b.classList.toggle('on',b.dataset.tab===t))}}
document.querySelectorAll('.tabs button').forEach(b=>b.addEventListener('click',()=>show(b.dataset.tab)));
show(document.getElementById('retained').classList.contains('on')?'retained':'retained');
document.getElementById('retained').classList.add('on');
document.querySelectorAll('.copy').forEach(b=>b.addEventListener('click',async()=>{{
 const el=document.getElementById(b.dataset.t);const txt=el.textContent;
 try{{await navigator.clipboard.writeText(txt);b.textContent='Copied ✓'}}
 catch(e){{const r=document.createRange();r.selectNodeContents(el);const s=getSelection();s.removeAllRanges();s.addRange(r);b.textContent='Selected: tap Copy'}}
 setTimeout(()=>b.textContent='Copy comment',1800)}}));
</script></body></html>"""
open(os.path.join(ROOT, "engage", "shortlist.html"), "w").write(page)
print("engage/shortlist.html written")
