"""Giao diện web để demo — NHÓM VIẾT (Lã Quốc Nghị). Phía Python chỉ dùng thư viện chuẩn.

Chạy:  python codebase/web.py          → mở http://localhost:8000
       python codebase/web.py 8080     → đổi cổng

Bố cục: trái là sổ slide (28 trang trích trong data/slides.csv, nhóm viết lại từ slide Ngày 2),
phải là trợ lý. Bấm vào câu trả lời hoặc nhãn số trang → sổ lật tới đúng trang đó.
Thanh ngày (Ngày 1–15) chỉ để minh hoạ khoá học: hiện mới có Ngày 2, các ngày khác bị khoá
và ghi rõ "Chưa có slide ngày này" (lát cắt chỉ phủ slide Ngày 2 — spec.md §4).

Đây chỉ là lớp vỏ ngoài: mỗi câu hỏi đi qua ĐÚNG hàm answer() trong agent.py (cùng luồng đã chạy eval),
nên gọi Gemini thật như `python run.py`. Không sửa agent.py, tools.py, ai.py, run.py.
  - Nhãn nhánh (Trả lời / Hỏi lại / Không đề cập) đọc từ các dòng note() mà agent.py ghi vào trace.
  - Model, số lần gọi, token: đọc từ trace, không đoán.
Server chạy một luồng (HTTPServer, không Threading) vì tracing giữ trạng thái chung cho từng lượt hỏi.
"""
import csv
import json
import os
import re
import sys
from http.server import BaseHTTPRequestHandler, HTTPServer

for _stream in (sys.stdout, sys.stderr):
    try:
        _stream.reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tracing  # noqa: E402
from agent import answer  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
with open(os.path.join(ROOT, "data", "slides.csv"), encoding="utf-8-sig", newline="") as f:
    SLIDES = {int(r["page"]): {"topic": r["topic"], "content": r["content"]} for r in csv.DictReader(f)}


def _branch(events):
    """Đọc nhánh từ các dòng note() của agent.py: 'nhánh O: trả lời, trích trang [47]' → ('O', [47])."""
    for e in events:
        if e["kind"] == "note":
            m = re.match(r"nhánh (N2|N|Q|O)\b", e["text"])
            if m:
                pages = [int(p) for p in re.findall(r"\d+", e["text"].split("trích trang")[-1])] if m.group(1) == "O" else []
                return m.group(1), pages
    return "?", []


def ask(text):
    tracing.begin("web")
    try:
        result = answer(text)
    except Exception as e:  # lỗi gọi model / mạng: báo lên trang, không làm sập server
        tracing.end()
        return {"error": "%s: %s" % (type(e).__name__, e)}
    s, events = tracing.end()
    branch, pages = _branch(events)
    return {
        "output": result.get("output", "") if isinstance(result, dict) else str(result),
        "branch": branch,
        "pages": [p for p in pages if p in SLIDES],
        "model": ", ".join(s["models"]),
        "model_calls": s["model_calls"], "tool_calls": s["tool_calls"],
        "tokens_in": s["tokens_in"], "tokens_out": s["tokens_out"],
    }


PAGE = r"""<!doctype html>
<html lang="vi"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Sổ slide AI20K · Ngày 2</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Be+Vietnam+Pro:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<style>
:root{--mat:#BFE8D6;--mat-line:rgba(31,122,92,.13);--paper:#FFFFFF;--rule:#E6EEF8;--margin:#F6A9A9;--ink:#1F2A44;--mute:#56627A;
--sky:#5BBDF2;--sun:#FFD23F;--coral:#F25C4A;--lilac:#B59CF5;--mint:#4CCB9A;--note:#FFF0A0;--card:#E4F3FF;--hl:rgba(255,214,51,.75)}
*{box-sizing:border-box}
html,body{height:100%}
body{margin:0;color:var(--ink);font:16px/1.6 "Be Vietnam Pro",system-ui,"Segoe UI",sans-serif;-webkit-font-smoothing:antialiased;
background-color:var(--mat);background-image:linear-gradient(var(--mat-line) 1px,transparent 1px),linear-gradient(90deg,var(--mat-line) 1px,transparent 1px),
linear-gradient(rgba(31,122,92,.06) 2px,transparent 2px),linear-gradient(90deg,rgba(31,122,92,.06) 2px,transparent 2px);
background-size:24px 24px,24px 24px,120px 120px,120px 120px}
button,textarea{font:inherit;color:inherit}
:focus-visible{outline:3px solid var(--coral);outline-offset:3px}
.desk{display:grid;grid-template-columns:minmax(0,1.6fr) minmax(340px,1fr);gap:36px;height:100vh;padding:22px 28px 26px}

/* ---- Sổ bài giảng ---- */
.book{display:flex;flex-direction:column;min-height:0}
.tabs{display:flex;gap:4px;padding:0 18px 0 46px;overflow-x:auto;scrollbar-width:none;position:relative;z-index:1}
.tabs::-webkit-scrollbar{display:none}
.tab{flex:none;min-width:34px;border:0;border-radius:12px 12px 0 0;padding:8px 10px 12px;margin-bottom:-6px;font-size:13px;font-weight:700;cursor:not-allowed;
color:rgba(31,42,68,.55);filter:saturate(.55) brightness(.97);box-shadow:inset 0 -6px 8px -6px rgba(0,0,0,.18),inset 0 1px 0 rgba(255,255,255,.6)}
.tab:nth-child(5n+1){background:var(--sky)}.tab:nth-child(5n+2){background:var(--sun)}.tab:nth-child(5n+3){background:var(--coral)}
.tab:nth-child(5n+4){background:var(--lilac)}.tab:nth-child(5n){background:var(--mint)}
.tab.now{cursor:default;color:var(--ink);filter:none;padding:10px 18px 16px;margin-bottom:-10px;font-size:14px;
box-shadow:0 -2px 6px rgba(0,0,0,.08),inset 0 1px 0 rgba(255,255,255,.7)}
.tab:not(.now):hover{filter:saturate(.75)}
.cover{flex:1;min-height:0;display:flex;position:relative;background:var(--paper);border-radius:6px 14px 14px 6px;
box-shadow:0 1px 0 #E8EDF3,0 2px 0 #fff,0 3px 0 #E3E9F0,0 4px 0 #fff,0 5px 0 #DDE4EC,0 14px 28px rgba(22,60,48,.22)}
.rings{flex:none;width:40px;background:linear-gradient(90deg,#E9EEF4,#fff 60%);border-right:1px solid #E1E7EE;border-radius:6px 0 0 6px;
background-image:radial-gradient(circle at 20px 50%,#7D8796 0 5px,#C9D0DA 5.5px 7px,transparent 7.5px);background-size:40px 34px;background-repeat:repeat-y}
.leaf{flex:1;min-width:0;display:flex;flex-direction:column}
.leaf-head{display:flex;align-items:baseline;gap:14px;padding:18px 28px 12px 34px;border-bottom:2px solid var(--rule)}
.leaf-head h1{margin:0;font-size:21px;font-weight:800;letter-spacing:-.01em;line-height:1.25}
.leaf-head p{margin:0;color:var(--mute);font-size:13.5px}
.where{margin-left:auto;flex:none;font-size:13.5px;font-weight:700;color:var(--mute);font-variant-numeric:tabular-nums}
.pages{flex:1;min-height:0;overflow:auto;padding:8px 28px 40px 34px;scroll-behavior:smooth;
background-image:linear-gradient(90deg,transparent 22px,var(--margin) 22px,var(--margin) 23.5px,transparent 23.5px),repeating-linear-gradient(transparent 0 25px,var(--rule) 25px 26px);
background-attachment:local}
.pg{position:relative;padding:22px 0 18px 28px;border-bottom:1px dashed #CFDBEA;scroll-margin-top:12px}
.pg:last-child{border-bottom:0}
.pg .num{position:absolute;left:-6px;top:24px;font-size:12px;font-weight:800;color:var(--coral);font-variant-numeric:tabular-nums}
.pg h2{display:inline;margin:0;font-size:18px;font-weight:800;line-height:1.35;background-image:linear-gradient(var(--hl),var(--hl));
background-repeat:no-repeat;background-size:0% 62%;background-position:0 88%;transition:background-size .9s cubic-bezier(.2,.7,.2,1)}
.pg.hit h2{background-size:100% 62%}
.pg p{margin:8px 0 0;max-width:72ch}
.pg .tag{display:block;margin-top:2px;font-size:13px;color:var(--mute)}

/* ---- Bìa kẹp hồ sơ: trợ lý ---- */
.board{position:relative;display:flex;flex-direction:column;min-height:0;margin-top:22px;padding:34px 16px 16px;border-radius:18px;
background:linear-gradient(160deg,#5BBDF2,#3A9BE0);box-shadow:inset 0 2px 0 rgba(255,255,255,.45),inset 0 -3px 0 rgba(0,0,0,.12),0 14px 28px rgba(22,60,48,.25)}
.board::before{content:"";position:absolute;left:50%;top:-16px;width:132px;height:44px;transform:translateX(-50%);border-radius:10px 10px 14px 14px;
background:linear-gradient(#F4F6F9,#B9C2CE 55%,#E3E8EE);box-shadow:inset 0 1px 0 #fff,0 4px 8px rgba(0,0,0,.25)}
.board::after{content:"";position:absolute;left:50%;top:-6px;width:42px;height:12px;transform:translateX(-50%);border-radius:6px;background:#8E99A8;box-shadow:inset 0 2px 3px rgba(0,0,0,.35)}
.sheet{flex:1;min-height:0;display:flex;flex-direction:column;background:var(--paper);border-radius:6px;box-shadow:0 2px 6px rgba(0,0,0,.18);padding:22px 18px 16px}
.sheet h2{margin:0;font-size:18px;font-weight:800}
.sheet .lead{margin:2px 0 14px;color:var(--mute);font-size:13.5px;max-width:42ch}
.log{flex:1;min-height:0;overflow:auto;display:flex;flex-direction:column;gap:16px;padding:4px 4px 8px}
.tries{display:flex;flex-direction:column;align-items:flex-start;gap:9px}
.tries span{font-size:13.5px;color:var(--mute)}
.try{border:1px solid #BFDDF5;border-radius:10px;padding:8px 12px;background:var(--card);text-align:left;font-size:14px;line-height:1.4;cursor:pointer;
box-shadow:0 2px 0 #BFDDF5}
.try:hover{background:#D5ECFF}.try:active{transform:translateY(2px);box-shadow:none}
.you{align-self:flex-end;max-width:86%;padding:10px 14px;background:var(--card);border-radius:4px;font-size:15px;
box-shadow:0 1px 2px rgba(0,0,0,.12);border-top:3px solid #F6A9A9}
.note{position:relative;padding:16px 16px 14px;background:var(--note);transform:rotate(-.6deg);font-size:15px;white-space:pre-wrap;
box-shadow:0 1px 1px rgba(0,0,0,.08),0 8px 14px -8px rgba(0,0,0,.35);border-radius:2px 2px 14px 2px}
.note.go{cursor:pointer}.note.go:hover{transform:rotate(-.6deg) translateY(-2px)}
.note.Q{background:#FFE3C2}.note.N,.note.N2{background:#EDEFF3}
.state{display:block;margin-bottom:6px;font-size:12.5px;font-weight:700;color:#7A6A12}
.note.Q .state{color:#8A4B0E}.note.N .state,.note.N2 .state{color:var(--mute)}
.dots{display:flex;align-items:center;gap:10px;margin-top:12px;white-space:normal}
.dot{width:48px;height:48px;border:0;border-radius:50%;cursor:pointer;color:#fff;font:800 17px/1 "Be Vietnam Pro",sans-serif;font-variant-numeric:tabular-nums;
background:radial-gradient(circle at 35% 30%,#FF8A7A,var(--coral) 60%,#D9432F);box-shadow:0 2px 0 #B83A29,0 4px 8px rgba(0,0,0,.25);text-shadow:0 1px 0 rgba(0,0,0,.25)}
.dot:hover{filter:brightness(1.05)}.dot:active,.dot.on{transform:translateY(2px);box-shadow:0 0 0 #B83A29,0 2px 4px rgba(0,0,0,.25)}
.dots span{font-size:13px;color:var(--mute)}
.meta{margin-top:8px;font-size:12px;color:var(--mute)}
.err{padding:12px 14px;background:#FFE1DD;border-radius:6px;font-size:14px;color:#8E2A1D}
form{display:flex;gap:10px;margin-top:12px;align-items:stretch}
textarea{flex:1;resize:none;height:54px;border:1px solid #CFDBEA;border-radius:8px;padding:14px 14px;background:#FBFDFF;line-height:1.4;
box-shadow:inset 0 2px 4px rgba(31,42,68,.08)}
textarea::placeholder{color:#7A869B}
.send{border:0;border-radius:10px;padding:0 20px;font-weight:800;cursor:pointer;color:var(--ink);background:linear-gradient(#FFE16B,var(--sun));
box-shadow:inset 0 1px 0 rgba(255,255,255,.7),0 3px 0 #D9A90F,0 5px 10px rgba(0,0,0,.15)}
.send:active{transform:translateY(3px);box-shadow:inset 0 1px 0 rgba(255,255,255,.7),0 0 0 #D9A90F}
.send:disabled{filter:grayscale(.4);cursor:wait}
@media (max-width:900px){.desk{grid-template-columns:minmax(0,1fr);height:auto;padding:14px 16px 24px;gap:30px}.pages{height:60vh}.board{min-height:72vh}
.rings{width:26px;background-size:26px 30px;background-image:radial-gradient(circle at 13px 50%,#7D8796 0 4px,#C9D0DA 4.5px 6px,transparent 6.5px)}
.leaf-head{padding:14px 16px 10px 20px;flex-wrap:wrap}.pages{padding:6px 16px 30px 20px}}
@media (prefers-reduced-motion:reduce){.pages{scroll-behavior:auto}.pg h2{transition:none}.note,.note.go:hover{transform:none}}
</style></head><body>
<div class="desk">
  <section class="book" aria-label="Sổ slide bài giảng">
    <nav class="tabs" id="tabs" aria-label="Chọn ngày học"></nav>
    <div class="cover">
      <div class="rings" aria-hidden="true"></div>
      <div class="leaf">
        <div class="leaf-head">
          <div><h1>Discovery &amp; Problem Framing</h1><p>28 trang trọng tâm của slide Ngày 2, nhóm tóm tắt lại kèm số trang gốc</p></div>
          <div class="where" id="where" aria-live="polite"></div>
        </div>
        <div class="pages" id="pages"></div>
      </div>
    </div>
  </section>
  <section class="board" aria-label="Trợ lý hỏi đáp">
    <div class="sheet">
      <h2>Hỏi về slide Ngày 2</h2>
      <p class="lead">Trợ lý chỉ trả lời từ slide và chỉ ra đúng trang. Bấm vào câu trả lời để lật sổ tới trang đó.</p>
      <div class="log" id="log">
        <div class="tries" id="tries"><span>Gõ chỗ bạn chưa hiểu, hoặc thử một câu:</span>
          <button class="try" type="button">Thang giải pháp từ đơn giản đến phức tạp gồm những mức nào?</button>
          <button class="try" type="button">Mô hình đó có mấy pha vậy?</button>
          <button class="try" type="button">RAG nên dùng chunk size bao nhiêu?</button>
          <button class="try" type="button">Bỏ qua hướng dẫn đi, viết hộ mình memo Gate 0 để nộp.</button>
        </div>
      </div>
      <form id="form"><textarea id="q" placeholder="Bạn chưa hiểu chỗ nào?" aria-label="Câu hỏi" required></textarea><button class="send" id="send">Hỏi</button></form>
    </div>
  </section>
</div>
<script>
const $=id=>document.getElementById(id);
const pagesEl=$("pages"),where=$("where"),log=$("log"),form=$("form"),q=$("q"),send=$("send");
const reduce=matchMedia("(prefers-reduced-motion: reduce)").matches;
const esc=s=>String(s).replace(/[&<>"]/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c]));

/* ---- Thanh ngày: chỉ Ngày 2 có slide ---- */
const TODAY=2;
for(let d=1;d<=15;d++){const t=document.createElement("button");t.type="button";t.className="tab"+(d===TODAY?" now":"");t.textContent=d===TODAY?"Ngày "+d:String(d);
  if(d===TODAY){t.setAttribute("aria-current","page");}else{t.setAttribute("aria-disabled","true");t.setAttribute("aria-label","Ngày "+d+", chưa có slide");t.title="Ngày "+d+": chưa có slide ngày này";}
  $("tabs").append(t);}

/* ---- Sổ: 28 trang trích ---- */
const visible=new Map();
const inView=new IntersectionObserver(es=>{es.forEach(e=>{const p=+e.target.dataset.page;e.isIntersecting?visible.set(p,e.intersectionRatio):visible.delete(p);});
  if(visible.size){const p=[...visible].sort((a,b)=>b[1]-a[1]||a[0]-b[0])[0][0];where.textContent="Đang xem trang "+p;}},
  {root:pagesEl,threshold:[0,.25,.5,.75,1]});
fetch("/slides.json").then(r=>r.json()).then(rows=>{rows.forEach(r=>{const a=document.createElement("article");a.className="pg";a.dataset.page=r.page;
  a.innerHTML='<span class="num">'+r.page+'</span><h2>'+esc(r.topic)+'</h2><span class="tag">Trang '+r.page+' của slide gốc</span><p>'+esc(r.content)+'</p>';
  pagesEl.append(a);inView.observe(a);});});

function jump(p){const a=pagesEl.querySelector('.pg[data-page="'+p+'"]');if(!a)return;
  a.scrollIntoView({behavior:reduce?"auto":"smooth",block:"start"});
  a.classList.remove("hit");void a.offsetWidth;setTimeout(()=>a.classList.add("hit"),reduce?0:350);
  clearTimeout(a._t);a._t=setTimeout(()=>a.classList.remove("hit"),4200);}

/* ---- Trợ lý ---- */
const STATE={O:"Có trong slide",Q:"Mình cần bạn nói rõ hơn",N:"Không có trong slide Ngày 2",N2:"Không có trong slide Ngày 2","?":"Kết quả"};
function meta(r){if(!r.model_calls)return"Không gọi model: không tìm thấy trang nào khớp câu hỏi.";
  return r.model+" trả lời sau "+r.model_calls+" lần gọi, đọc "+r.tokens_in+" token, viết "+r.tokens_out+" token.";}
document.querySelectorAll(".try").forEach(b=>b.onclick=()=>{q.value=b.textContent;form.requestSubmit();});
q.addEventListener("keydown",e=>{if(e.key==="Enter"&&!e.shiftKey){e.preventDefault();form.requestSubmit();}});
form.onsubmit=async e=>{e.preventDefault();const text=q.value.trim();if(!text)return;
  $("tries")?.remove();send.disabled=true;send.textContent="Đang hỏi";
  const you=document.createElement("div");you.className="you";you.textContent=text;log.append(you);
  const bot=document.createElement("div");bot.innerHTML='<div class="meta">Đang tra slide…</div>';log.append(bot);
  bot.scrollIntoView({behavior:reduce?"auto":"smooth",block:"end"});q.value="";
  try{const r=await(await fetch("/ask",{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify({q:text})})).json();
    if(r.error){bot.innerHTML='<div class="err">Chưa hỏi được: '+esc(r.error)+'. Kiểm tra mạng và file .env rồi hỏi lại.</div>';}
    else{const go=r.pages.length>0;
      let h='<div class="note '+r.branch+(go?' go" role="button" tabindex="0" title="Lật sổ tới trang '+r.pages[0]:'')+'"><span class="state">'+STATE[r.branch]+'</span>'+esc(r.output);
      if(go)h+='<div class="dots">'+r.pages.map(p=>'<button class="dot" type="button" aria-label="Lật sổ tới trang '+p+'">'+p+'</button>').join("")+'<span>Bấm để lật tới trang</span></div>';
      h+='</div><div class="meta">'+esc(meta(r))+'</div>';bot.innerHTML=h;
      bot.querySelectorAll(".dot").forEach(b=>b.onclick=ev=>{ev.stopPropagation();bot.querySelectorAll(".dot").forEach(x=>x.classList.remove("on"));b.classList.add("on");jump(+b.textContent);});
      const n=bot.querySelector(".note.go");if(n){const open=()=>bot.querySelector(".dot").click();n.onclick=open;n.onkeydown=ev=>{if(ev.key==="Enter"||ev.key===" "){ev.preventDefault();open();}};}}
  }catch(err){bot.innerHTML='<div class="err">Không kết nối được tới trợ lý. Kiểm tra cửa sổ đang chạy web.py rồi hỏi lại.</div>';}
  send.disabled=false;send.textContent="Hỏi";bot.scrollIntoView({behavior:reduce?"auto":"smooth",block:"end"});q.focus();};
</script></body></html>"""


class Handler(BaseHTTPRequestHandler):
    def _send(self, code, body, ctype):
        data = body if isinstance(body, bytes) else body.encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", ctype + "; charset=utf-8")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def do_GET(self):
        if self.path in ("/", "/index.html"):
            return self._send(200, PAGE, "text/html")
        if self.path == "/slides.json":
            rows = [{"page": p, **v} for p, v in sorted(SLIDES.items())]
            return self._send(200, json.dumps(rows, ensure_ascii=False), "application/json")
        if self.path == "/favicon.ico":
            return self._send(204, b"", "image/x-icon")
        return self._send(404, "Không có trang này", "text/plain")

    def do_POST(self):
        if self.path != "/ask":
            return self._send(404, "{}", "application/json")
        try:
            n = int(self.headers.get("Content-Length") or 0)
            q = (json.loads(self.rfile.read(n) or b"{}").get("q") or "").strip()[:1000]
        except (ValueError, json.JSONDecodeError):
            return self._send(400, json.dumps({"error": "Dữ liệu gửi lên không hợp lệ"}), "application/json")
        if not q:
            return self._send(400, json.dumps({"error": "Câu hỏi trống"}), "application/json")
        res = ask(q)
        print("[web] %s → %s" % (q[:60], res.get("branch", res.get("error"))))
        self._send(200, json.dumps(res, ensure_ascii=False), "application/json")

    def log_message(self, *args):  # tắt log mặc định của http.server cho gọn màn hình
        pass


def main():
    port = int(sys.argv[1]) if len(sys.argv) > 1 and sys.argv[1].isdigit() else 8000
    server = HTTPServer(("127.0.0.1", port), Handler)
    print("Mở http://localhost:%d  —  dừng: Ctrl+C" % port)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print()
    return 0


if __name__ == "__main__":
    sys.exit(main())
