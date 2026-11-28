# MHTeam — Kế hoạch CP4 (14:30) · Thứ Bảy 28/11

> Nguồn yêu cầu: `kickoff/README.md` mục CP4 · `kickoff/02-guide.md` 4.1–4.4, 5.1–5.3 · `kickoff/03-rubric.md` Phần 0, R5–R7, Trừ điểm · `kickoff/01-challenge-brief.md` 7 hạng mục.
> CP3 đã nộp (lượt 1 **18/24 = 75%**, `run-1@20261128-080617`). Lập lúc 09:15.
> **14:00 có mặt C401** · rời nhà: **Nghị 12:15** · **Thành 13:15** · **An 13:30** · **Toàn 13:45**.

---

## 0. Hiện trạng repo 09:15 so với yêu cầu CP4

| # | CP4 cần (README checkpoint · guide 4.4) | Hiện có | Còn thiếu | Ai |
|---|---|---|---|---|
| 1 | Phòng demo + link repo | C401 · repo công khai (kiểm 08:53) | — | Nghị (form) |
| 2 | Tích **7 hạng mục** bắt buộc | 1 bằng chứng ✅ · 2 impact ✅ · 3 thiết kế ✅ · 4 bản chạy thử ✅ · 5 bộ câu thử + lượt 1 ✅ | 6 chi phí ❌ · 7 slide PDF + video dự phòng ❌ | — |
| 3 | **Lượt 1 → lượt 2** + `eval/report.md` + `eval/README.md` | Lượt 1 đã chấm · `report.md` §1–§2 (6 câu trượt, 4 nhóm lỗi) · `eval/README.md` §1–§5 dòng lượt 1 | Cải tiến · `run-2.csv` + chấm · `report.md` §3–§4 · `eval/README.md` dòng lượt 2 + §6 | Nghị · An · Toàn |
| 4 | **Chi phí / task thành công** + tên model (kịch bản cơ sở) | `personas.yaml` ✅ (3 persona M8 · 3 kịch bản 118/236/864 · 3 model, giá sau khi tăng) | `simulate` ≥50 phiên **dùng tỉ lệ lượt 2** · `cost-estimate.md` · `spec.md` §8 | Thành |
| 5 | `demo-slides.pdf` ở thư mục gốc + **link video demo dự phòng** | `slides/outline.md` (khung 8 trang) · video 30 giây CP3 (không thay được video demo) | 8 trang slide · PDF · video demo 1–2 phút | cả nhóm · Toàn (video) |
| 6 | `spec.md` đủ §0–§9 | §0–§7, §9 ✅ | **§8** · §10 dòng cải tiến + dòng "Phân công", "Dùng AI" | Thành · Nghị |
| 7 | Tự khai phần chưa xong | — | ghi vào form | Nghị |
| + | *(bonus)* `validation/log.md` | khung | 2–3 người ngoài nhóm dùng thử | Toàn (nếu kịp) |

**Điều kiện cứng (rubric Phần 0, kiểm 14:30 — thiếu là không xét giải):** AI thật ✅ · bằng chứng ✅ · ≥20 câu + % đạt ✅ · **slide PDF ❌ ← đường găng**.

---

## 1. Quyết định lúc 10:00 — một cải tiến cho lượt 2

Nguyên nhân gốc 6 câu trượt (đã đo lại `search_slides`, đọc trace):

| Nhóm lỗi | Câu | Nguyên nhân | Sửa ở | Ai sửa |
|---|---|---|---|---|
| **A · Tìm kiếm bỏ sót trang** | C10, C14 | Đường phụ câu dài cần ≥2 từ hiếm; trang 42 (F1) và 35 (lệch pha) chỉ trùng 1 từ hiếm → bị loại | `tools.py`: `MIN_RARE_HITS = 2 → 1` | Thành |
| **B · Không hỏi lại khi câu mơ hồ** | C08, C09 | Câu chỉ còn 1 từ nội dung ("tran", "loi") vẫn tìm ra đoạn → model đoán; C09 ghép 2 trang không liên quan | `agent.py`: thêm luật HỎI LẠI vào `SYSTEM` (câu chỉ trỏ "đó / này / trang đó" mà không nêu khái niệm) | Nghị |
| Từ chối cả câu khi chỉ thiếu một phần | C13 | Tìm đúng trang 20, model chọn KHÔNG ĐỀ CẬP | prompt | — |
| Trả lời thiếu ý | C20 | Tìm đúng trang 31, model bỏ ý OST | prompt / model | — |

- **A** đã thử trong bộ nhớ (không sửa file): C10 → [42], C14 → [34, 35]; không câu nào mất trang đúng; 8 câu ngoài slide tự đặt thêm vẫn `[]`. C11 (tấn công) kéo thêm trang 29, 35 → prompt vẫn phải chặn, lượt 2 sẽ kiểm.
- **B** nhắm đúng rủi ro số 1 nhóm đã viết ở `spec.md` §4 ("trả lời lệch bài") → dễ bảo vệ "nhóm lỗi đau nhất với người dùng" (rubric R5). Phụ thuộc model nghe prompt → thử tay trước khi chạy lượt 2.
- Mỗi phương án cứu tối đa 2 câu → **20/24 (83%) ≥ chuẩn 80%**. Guide 4.1 chỉ cho **một** cải tiến nhắm **một** nhóm lỗi → không gộp A + B. Phương án không chọn → slide trang 8 "Nếu có thêm 1 tuần".
- **Đề xuất: B.** Nhóm chốt lúc 10:00, ghi vào `eval/report.md` §3 dòng "Nhắm vào nhóm lỗi … vì sao đau nhất".

---

## 2. Lịch theo người

**Đường găng:** cải tiến push 11:10 → **lượt 2 chạy 11:15** → **chấm xong 11:50** → **`simulate` 11:50–12:10** (cần lượt 2 đã chấm: `--rate-from` kiểm trước khi chạy) → `cost-estimate.md` + slide 6 trước 13:10 → **PDF trước 13:25**.

| Giờ | Nghị (rời 12:15) | Thành (rời 13:15) | An (rời 13:30) | Toàn (rời 13:45) |
|---|---|---|---|---|
| **09:15–10:00** | Gửi bảng mục 1 lên nhóm · `docs/ai-usage.md` dòng tự giải thích của mình | **Kiểm key Gemini chạy được** (`python run.py` hỏi 1 câu) — cần cho `simulate` · đọc lại vì sao C10, C14 trượt | Dựng **khung slide** (8 trang, 1 file chung Google Slides / Canva, chia quyền sửa) | **Lấy key Gemini riêng** → `.env` → `python run.py` hỏi 1 câu · slide 1–2 |
| **10:00–10:30** | **Họp online: chốt 1 cải tiến** (mục 1) · chốt người nói từng trang (mục 4) | ← | ← | ← |
| 10:30–11:10 | Sửa `agent.py` (nếu chọn B) · thử tay ~5 câu: C08, C09, 2 câu thường, 1 câu mơ hồ mới ngoài bộ · push | Sửa `tools.py` (nếu chọn A), push trước 11:10 · **slide 3** (lát cắt · sơ đồ §4 · vì sao workflow, không agent · 3 chỗ chặn rủi ro) | **Slide 5 khung** (dataset · 24 câu · 3 metric · người thứ hai chấm khớp 5/5 · lượt 1 18/24) | **Slide 4** (1 ca thường + 1 ca khó, lấy từ bộ câu thử) · slide 1–2 xong |
| **11:15** | **Chạy lượt 2** `python run.py eval --wait 4` → push `eval/run-2.csv` + `traces/run-2.jsonl` · `spec.md` §10 dòng cải tiến (giờ · đổi gì · vì sao, trỏ câu thử) | | | |
| 11:20–11:50 | `spec.md` §10 dòng "Phân công", "Dùng AI" · đọc slide 3 (khớp code chưa) | Slide 6 khung (bảng 3 kịch bản, chờ số) | **Chấm `pass` lượt 2** C01–C12 | **Chấm `pass` lượt 2** C13–C24 |
| **11:50** | | | `python run.py score eval/run-2.csv` → **push ngay** → báo nhóm | |
| 11:50–12:15 | Nếu Thành chưa có key: **chạy `simulate` trên máy mình** · nếu Toàn chưa có key: **quay video demo dự phòng** (5 phút) · **rời 12:15** | **`python run.py simulate --rate-from eval/run-2.csv --wait 4`** (~15–20 phút, 50 phiên) → push `cost/simulate-N.csv` + `-summary.md` + `traces/simulate-N.jsonl` | `eval/report.md` §1 dòng lượt 2 · §3 · §4 · `eval/README.md` dòng lượt 2 + §6 · `spec.md` §7 dòng lượt 2 | **Quay video demo dự phòng** (`git pull` → `python run.py`, 2 ca của slide 4 + 1 câu tấn công, 1–2 phút) → YouTube "Không công khai" → link vào README hạng mục 7 |
| 12:15–13:10 | *(đi đường: đọc lại `agent.py`, trace 2 câu trượt, mục 4)* | `cost/cost-estimate.md` (chép bảng từ `simulate-N-summary.md`, 3 kịch bản · ≥2 model · so impact) · `spec.md` §8 · **slide 6** → push → **rời 13:15** | **Slide 5** (lượt 1 → lượt 2) · **slide 8** (phương án không chọn + C13, C20 + "không nhớ câu trước") | **Slide 7** (go / iterate / stop, dẫn số trang 1, 5, 6) · *(bonus)* `validation/log.md` |
| 13:10–13:25 | | *(đi đường)* | Ghép · **xuất `demo-slides.pdf` → push thư mục gốc trước 13:25** → **rời 13:30** | Soát mục 5 (số trong slide = số trong file) |
| 13:25–13:45 | *(mở PDF trên điện thoại)* | | *(đi đường)* | Soát checklist mục 3 · mở PDF + 2 video bằng tab ẩn danh · sửa nhỏ → push → **rời 13:45** |
| **14:00–14:25** | **Tới C401:** `git pull` · `python run.py` hỏi 1 câu · mở video ẩn danh · **nộp Form CP4** (mục 6) | Tới C401 | Tới C401 | Tới C401 |

**Dự phòng key:** chỉ máy Nghị chắc chắn có key. Thành / Toàn báo lên nhóm **trước 10:00** đã chạy được hay chưa → chưa thì Nghị nhận `simulate` / video ở khung 11:50–12:15 (simulate ~20 phút: bắt đầu muộn nhất 11:55).

---

## 3. Checklist theo người (xong khi)

**Nghị**
- [ ] Cải tiến trong `agent.py` (nếu B) — tự giải thích được từng dòng đã đổi
- [ ] `eval/run-2.csv` + `traces/run-2.jsonl` đã push (0 lỗi kỹ thuật; lỗi → chạy lại thành `run-3`, không sửa file)
- [ ] `spec.md` §10: dòng cải tiến · dòng "Phân công" · dòng "Dùng AI"
- [ ] `docs/ai-usage.md`: dòng tự giải thích của mình
- [ ] Form CP4 nộp trước 14:25

**Thành**
- [ ] (nếu A) `tools.py` sửa + giải thích được vì sao 1 từ hiếm là đủ
- [ ] `cost/simulate-N.csv` ≥50 phiên, seed 42, tỉ lệ đạt từ **lượt 2** (summary ghi `--rate-from eval/run-2.csv`)
- [ ] `cost/cost-estimate.md`: 3 kịch bản · ≥2 model · chi phí / task thành công · "đo trên model X, tính giá model Y" · 1 dòng so với impact / người / tháng (`spec.md` §2: 80 giờ ÷ 118 người)
- [ ] `spec.md` §8 điền đủ 4 dòng
- [ ] Slide 3, 6 · `docs/ai-usage.md` dòng chi phí / slide nếu dùng AI

**An**
- [ ] Chấm lượt 2 cùng cách chấm lượt 1 (`metric_spec.yaml`), cột `pass` + `ghi_chu` — **không sửa cột khác**
- [ ] `eval/report.md` §1 lượt 2 · §3 (nhóm lỗi đã chọn, đã sửa gì, nhóm đó x/2 → y/2, câu nào tệ đi) · §4 (lỗi còn lại, 1 tuần)
- [ ] `eval/README.md` §5 dòng lượt 2 · §6 lỗi chính · `spec.md` §7 dòng lượt 2
- [ ] Slide 5, 8 · **`demo-slides.pdf` ở thư mục gốc trước 13:25**

**Toàn**
- [ ] Key chạy được trước 10:00
- [ ] Chấm lượt 2 C13–C24
- [ ] Slide 1, 2, 4, 7
- [ ] Video demo dự phòng 1–2 phút, YouTube "Không công khai", link trong README
- [ ] Soát chốt mục 5 · *(bonus)* `validation/log.md`

---

## 4. Slide 8 trang (guide 5.1 · rubric R7: mỗi trang ≥1 số / trích dẫn / kết quả đo, **số phải truy được về file**)

| # | Trang | Số có sẵn ngay | Lấy từ | Làm | Nói |
|---|---|---|---|---|---|
| 1 | Người dùng & pain | 19/22 (86,4%) gặp chỗ không hiểu · 13/21 thấy câu trả lời ngoài lệch bài · ≈15,9 phút / lần · trích phiếu #03 | `evidence/summary.md` | Toàn | Toàn |
| 2 | Vì sao chọn bài này | 118 người × 2,56 lần × 15,9 phút ≈ **80 giờ / tháng** · H2, H3, H4 bị loại + lý do | `spec.md` §2 | Toàn | Toàn |
| 3 | Giải pháp | Lát cắt 1 câu · sơ đồ §4 · workflow (1 công cụ, 1 nguồn, AI làm 1 bước) · 3 chỗ chặn · không gọi model khi không tìm thấy | `spec.md` §4 | Thành | Thành |
| 4 | Demo live | Ca thường: "Thang giải pháp … gồm những mức nào?" → trang 47 · ca khó: câu ngoài slide / câu tấn công C11 → từ chối, 0 lần gọi model | `eval/benchmark.csv`, video | Toàn | **Nghị** (máy có key) |
| 5 | Đánh giá thế nào | 28 đoạn slide · 24 câu (10 từ khảo sát) · 3 metric · chấm chéo 5/5 · **18/24 → __/24** so với chuẩn 80% · lỗi chính | `eval/README.md`, `report.md` | An | An |
| 6 | Chi phí khi dùng thật | chi phí / task thành công · 3 kịch bản 118 / 236 / 864 người · ≥2 model · so 80 giờ | `cost/cost-estimate.md` | Thành | Thành |
| 7 | Kết luận | go / iterate / stop — dẫn số trang 1, 5, 6 | — | Toàn | **Nghị** |
| 8 | Nếu có thêm 1 tuần | phương án không chọn ở mục 1 · C13, C20 · không nhớ câu trước (46,9% hỏi nối, M4) · mở rộng buổi khác | `report.md` §4 | An | An |

Điền bảng "Ai nói trang nào" trong `slides/outline.md` cho khớp.

**Ai cũng thuộc 4 câu (rubric R7, 3 điểm):**
1. *Vì sao workflow?* — 1 công cụ, 1 nguồn dữ liệu, AI chỉ chọn 1 trong 3 nhãn; agent thêm lượt gọi, khó kiểm thử, dễ cộng dồn lỗi — đúng "thang giải pháp" slide Ngày 2 trang 47.
2. *Lỗi nguy hiểm nhất?* — trả lời lệch bài (vd C09 ghép 2 trang không liên quan) → học viên hiểu sai trước buổi. Chặn: chỉ đọc slide · bắt buộc "Xem trang X" · code kiểm số trang. Còn hở: tóm tắt lệch ý nhưng đúng trang (`spec.md` §9).
3. *Chi phí / task thành công?* — chi phí trung bình mỗi phiên (token đo thật qua 50 phiên mô phỏng × giá gói trả phí) ÷ tỉ lệ đạt lượt 2, cùng model.
4. *Phần bạn làm?* — đúng cột "Phần việc chính" trong `TEAMS.md` + dòng của mình trong `docs/ai-usage.md`.

Giám khảo có thể đưa **1 câu lạ**, mở **trace 1 câu trượt**, hỏi *"câu này vì sao trượt?"* → mỗi người đọc trước 1–2 câu trượt của lượt 2 trong `run-2.csv` + `traces/run-2.jsonl`.

---

## 5. Soát chốt (Toàn, 13:25–13:45)

- [ ] `git status` sạch · không có `.env`, `kickoff/`, `raw-*` · `python run.py check` không cảnh báo
- [ ] `demo-slides.pdf` ở **thư mục gốc**, mở được trên GitHub
- [ ] Mọi số trong slide khớp file (18/24 · số lượt 2 · chi phí) — số không truy được = khối đó 0 điểm
- [ ] README hạng mục 7: link video demo dự phòng, mở bằng tab ẩn danh xem được
- [ ] `spec.md` không còn `__` ở §0–§9 · §10 có dòng cải tiến
- [ ] `eval/run-1.csv`, `run-2.csv` chỉ khác bản chạy ở cột `pass`, `ghi_chu`
- [ ] `cost/` có `simulate-N.csv` + `simulate-N-summary.md` + `cost-estimate.md`

---

## 6. Form CP4 (Nghị nộp 14:00–14:25)

- **Phòng:** C401 (Zone 4) · **Repo:** https://github.com/katogithub2701/K5-Day15-L3B-MHTeam
- **7 hạng mục:** tick cái nào thật sự có trên repo lúc nộp
- **Lượt 1 → lượt 2:** 18/24 (75%) → __/24 (__%) · run ID `run-1@20261128-080617` → `run-2@…`
- **Chi phí / task thành công (kịch bản cơ sở):** __ USD · model `gemini-3.1-flash-lite` (+ mức model thứ hai)
- **Slide:** `demo-slides.pdf` · **video demo dự phòng:** link
- **Phần chưa xong:** khai thật (vd bonus người dùng thử, ảnh chụp §0)

---

## 7. Sau 14:30 → 23:59 (không nộp form)

- [ ] Sửa theo góp ý của giám khảo → **mỗi thay đổi 1 dòng `spec.md` §10** (giờ · đổi gì · vì sao) · chạy thêm thì thành `run-3.csv`
- [ ] `reflection/<ten-khong-dau>.md` — **mỗi người 1 file** (`la-quoc-nghi.md`, `nguyen-quang-thanh.md`, `nguyen-quoc-toan.md`, `hoang-duc-an.md`): vai trò + file / commit · AI hỗ trợ thế nào, chỗ phải sửa · 1 bài học từ 1 câu thử trượt
- [ ] `docs/ai-usage.md` đủ dòng của 4 người (các dòng trống: rà câu hỏi khảo sát, slide / văn bản)
- [ ] Dọn dòng hướng dẫn còn sót của khung mẫu (đầu README, `spec.md` dòng 4)

## 8. Luật (rubric "Trừ điểm")

- **Không sửa** chuẩn "đạt" (§7) · `eval/metric_spec.yaml` · `expected` · câu thử (không xoá câu trượt) · `run-*.csv`, `simulate-*.csv`, `traces/` (chỉ điền `pass`, `ghi_chu`) · số liệu bằng chứng.
- Cải tiến **không được nhắm nguyên văn câu thử** (`AGENTS.md`): luật phải đúng cho câu học viên thật hỏi, thử thêm câu ngoài bộ.
- Lỗi kỹ thuật giữa chừng → lượt mới, ghi vào bảng các lượt.
- Trước mỗi push: `git pull --rebase` · `git add` từng file · `git status` không có `.env`, `kickoff/`. **Hai người không sửa cùng một file cùng lúc** — `spec.md`: chỉ Nghị (§10), Thành (§8), An (§7 dòng lượt 2); báo nhóm trước khi push.
