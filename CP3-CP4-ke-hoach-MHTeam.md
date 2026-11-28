# MHTeam — Kế hoạch CP3 (10:00) & CP4 (14:30) · Thứ Bảy 28/11

> Nguồn yêu cầu: `kickoff/README.md` mục CP3, CP4 · `kickoff/02-guide.md` bước 3.4, 4.1–4.4, 5.1–5.3 · `kickoff/03-rubric.md`.
> Ràng buộc: sáng T7 **không có lớp** · **14:00 có mặt phòng C401** (Zone 4) · Giờ rời nhà (đến C401 lúc 14:00): **Nghị ≥1,5 giờ → rời 12:15** (dư 15 phút vì "tiếng rưỡi trở lên") · **Thành ~45 phút → rời 13:15** · **An 15–30 phút → rời 13:30** · **Toàn ~15 phút → rời 13:45**.

---

## 0. Tình trạng repo tối 27/11 (19:37)

| Hạng mục | Có rồi | Còn thiếu |
|---|---|---|
| Bằng chứng pain | Khảo sát n = 22 (đạt ngưỡng ≥20), 8 trích dẫn, đào data xong | Chốt form 08:00, cập nhật số cuối |
| Bộ câu thử | 13 câu, 3 metric, chấm thử khớp 5/5 | **Lên 20–30 câu**, ≥1/3 từ khảo sát (đang **0/13**) |
| Bản chạy thử | Gemini thật, `agent.py` đủ nhánh | — (lỗi đã biết để dành cho lượt 2) |
| `spec.md` | §1–§5, §7 (chuẩn "đạt" đã khoá) | **§0, §6** (CP3) · §8, §9 (CP4) · §10 (changelog) |
| `cost/` | khung | `personas.yaml` còn 7 dòng "(ví dụ)" · `cost-estimate.md` |
| README repo | | Ô `Model: ____` · mục "Dùng AI vào việc gì" · link video |
| Slide, video, `eval/report.md`, `reflection/` | | Chưa có |

---

## 1. Điểm nghẽn phải gỡ ngay tối nay

**Chỉ máy Nghị có API key.** Lượt 1, lượt 2 và `simulate` đều cần gọi model. Nghị rời nhà lúc 12:15, nên:

- [ ] **Thành lấy key Gemini miễn phí riêng** tối nay (aistudio.google.com/apikey, chỉ cần tài khoản Google thường, **không cần pro**) → tạo `.env` giống Nghị (`MODEL_PROVIDER=gemini`, `MODEL_NAME=gemini-3.1-flash-lite`). Thành tự chạy `simulate` được.
- [ ] **An cũng lấy 1 key** làm dự phòng (nếu lượt 2 trễ sau 12:15 thì An chạy).
- [ ] Mỗi người tự chạy `python run.py` hỏi 1 câu để chắc chắn nối được. **Không gửi key cho nhau, không dán lên chat.**

---

## 2. Tối nay (tuỳ sức, càng làm được nhiều sáng mai càng nhẹ)

| Ai | Việc | Vì sao nên làm tối nay |
|---|---|---|
| **An** | Mở rộng `eval/benchmark.csv` lên **22–25 câu**: thêm ≥8 câu lấy từ câu hỏi thật trong khảo sát (`source: nguoi_dung: phiếu #__`), giữ ≥5 `kho`, ≥2 `tu_choi`. **Chỉ thêm câu, không sửa câu cũ.** `python run.py check` hết cảnh báo | **Đường găng:** chưa có bộ câu thử cuối thì chưa chạy lượt 1 được |
| **Thành** | Lấy key · nháp `cost/personas.yaml` (≥3 kiểu, số lần/tháng lấy từ `spec.md` §2 của Toàn, giá ≥2 model từ `kickoff/further-reading/model-prices.md` kèm link + ngày xem) · `python run.py simulate --try` (10 phiên) | Guide: "CP3 thử trước 10 phiên để kiểm khung" |
| **Nghị** | `spec.md` §0, §6, §9 · README: ô Model, mục "Dùng AI vào việc gì" | Thuần chữ, không phụ thuộc ai |
| **Toàn** | Nháp nội dung slide trang 1–2 (pain + impact, số đã có) | Không phụ thuộc kết quả eval |

---

## 3. Sáng T7 → CP3 (10:00)

| Giờ | Ai | Việc |
|---|---|---|
| **07:00–07:45** | An | Chốt bộ câu thử (nếu tối chưa xong) → **push trước 07:45, sau đó không ai sửa** |
| 07:00–08:00 | Nghị | Quay **video 30 giây** (`python run.py`: 1 câu có trong slide + 1 câu ngoài slide) → YouTube "Không công khai" / Drive "Bất kỳ ai có liên kết" → mở thử ẩn danh |
| 07:00–08:30 | Toàn | **08:00 chốt form** → xuất lại → `count_survey.py` → cập nhật `summary.md`, canvas dòng 4, §1 |
| 07:00–08:00 | Thành | `simulate --try` nếu tối chưa chạy · hoàn thiện `personas.yaml` |
| **08:00** | Nghị | `git pull` → **`python run.py eval --wait 4`** → `eval/run-1.csv` + `traces/run-1.jsonl` → **push ngay** |
| **08:15–09:15** | An + Toàn | **Chấm cột `pass`** từng câu theo `metric_spec.yaml` (chia đôi bộ câu, câu khó thì hỏi nhau) → `python run.py score eval/run-1.csv` → push |
| 09:15–09:40 | Nghị | §7 dòng "Kết quả lượt 1" + run ID · `eval/README.md` mục 5 (bảng các lượt) · kiểm §0–§7 đủ · `run.py check` |
| 09:15–09:40 | An | Bắt đầu `eval/report.md`: liệt kê câu trượt lượt 1 (input · output · vì sao sai) |
| **09:40–09:55** | Nghị | Push cuối → **nộp Form 2 nhánh CP3**: link `summary.md` · số câu · **x/N + run ID** · link video · link `spec.md` · phần chưa xong |

**Tự soát CP3 (guide 3.4):**
- [ ] Bằng chứng ≥1 nguồn đạt ngưỡng + ≥5 trích dẫn · bảng impact
- [ ] 20–30 câu thử, ≥5 `kho`, ≥2 `tu_choi`
- [ ] AI thật · video 30 giây mở được ẩn danh
- [ ] `eval/run-1.csv` đã chấm + kết quả `score`
- [ ] `spec.md` §0–§7 đã commit

**Lượt 1 thấp là bình thường.** Không sửa prompt / code trước lượt 1.

---

## 4. Sau CP3 → CP4 (14:30) — làm online, tính cả giờ đi đường

| Giờ | Nghị (rời 12:15) | Thành (rời 13:15) | An (rời 13:30) | Toàn (rời 13:45) |
|---|---|---|---|---|
| **10:00–10:30** | **Cả nhóm gọi online, đọc các câu trượt lượt 1 → gom ≥3 nhóm lỗi có tên → chọn 1 nhóm lỗi đau nhất → 1 cải tiến** | ← | ← | ← |
| 10:30–11:15 | Sửa `agent.py` (prompt / luồng) theo cải tiến đã chọn · thử tay 3–4 câu | Nếu cải tiến chạm `search_slides` thì sửa `tools.py`; nếu không: hoàn thiện `personas.yaml` | Viết `eval/report.md` phần lượt 1 + nhóm lỗi | Slide trang 1–2 · *(bonus)* 2 bạn ngoài nhóm dùng thử qua Discord → `validation/log.md` |
| **11:15** | **Chạy lượt 2**: `python run.py eval --wait 4` → `eval/run-2.csv` → push · ghi `spec.md` §10 (giờ · đổi gì · vì sao) | | | |
| 11:20–12:00 | Slide trang 3 (giải pháp + sơ đồ) và 4 (demo) | Slide trang 6 khung | **Chấm `pass` lượt 2** (cùng Toàn) → `score` → push **trước 12:00** | Chấm `pass` lượt 2 cùng An |
| 12:00–12:15 | Quay **video demo dự phòng** (1 ca thường + 1 ca khó, ~1–2 phút) → upload → link vào README · **rời nhà 12:15** | **`python run.py simulate --rate-from eval/run-2.csv --wait 4`** (≥50 phiên) → push | `eval/report.md` phần lượt 2 + `eval/README.md` mục 5–6 · §7 dòng lượt 2 | Slide trang 7 (kết luận go / iterate / stop, dẫn số trang 1, 5, 6) |
| 12:15–13:15 | *(đi đường — đọc lại code để trả lời giám khảo)* | `cost/cost-estimate.md` (3 kịch bản, chi phí / task thành công, so impact) · `spec.md` §8 · slide trang 6 → push → **rời 13:15** | Slide trang 5 (đánh giá) và 8 (nếu có thêm 1 tuần) | Ghép slide, chờ trang 6 của Thành (≤13:10) |
| 13:15–13:30 | *(đi đường)* | *(đi đường)* | **Xuất `demo-slides.pdf` → push vào thư mục gốc repo trước 13:25** → **rời 13:30** | Soát lại repo theo checklist 5.2 · mở PDF + video bằng tab ẩn danh |
| 13:30–13:45 | *(đi đường)* | *(đi đường)* | *(đi đường)* | Sửa lỗi nhỏ cuối nếu có → push → **rời 13:45** |
| **14:00** | **Tới C401:** `git pull` · gọi thử 1 câu (`.env` còn chạy) · mở video ẩn danh · **nộp Form 2 nhánh CP4 trước 14:25** | Tới C401 | | |

**Tự soát CP4 (guide 4.4):**
- [ ] Lượt 2 + `eval/report.md` (≥3 lỗi: input · output · vì sao sai) + `eval/README.md`
- [ ] `cost/cost-estimate.md` 3 kịch bản + chi phí / task thành công (tên model)
- [ ] `spec.md` đủ §0–§9 · §10 có dòng cải tiến
- [ ] `demo-slides.pdf` ở thư mục gốc · link video demo dự phòng (ẩn danh mở được)
- [ ] Form CP4: phòng C401 + link repo · tick 7 hạng mục · lượt 1 → lượt 2 · chi phí / task thành công + tên model · phần chưa xong

---

## 5. Demo (14:30) — chuẩn bị trên đường đi

- Mỗi người nói **2 trang slide**, ai cũng thuộc 4 câu: *vì sao chọn workflow · lỗi nguy hiểm nhất · chi phí / task thành công tính thế nào · phần mình làm*.
- Giám khảo có thể đưa **1 câu lạ**, mở **trace của 1 câu trượt**, hỏi bất kỳ ai *"câu này vì sao trượt?"* → mỗi người đọc trước 1–2 câu trượt trong `run-1.csv`.
- Mạng / API lỗi >30 giây → **bật video dự phòng ngay**.

## 6. Đến 23:59 T7 (không nộp form)

- [ ] `reflection/<ten-khong-dau>.md` — **mỗi người 1 file**: vai trò · AI hỗ trợ thế nào · 1 bài học từ 1 câu thử trượt
- [ ] `spec.md` §10: mọi thay đổi sau 14:30 (giờ · đổi gì · vì sao) · chạy thêm thì thành `run-3.csv`
- [ ] `docs/ai-usage.md` đủ dòng của 4 người

## 7. Luật nhắc lại

- **Không sửa** `spec.md` §7, `eval/metric_spec.yaml` · **không xoá câu trượt** · **không sửa `expected`** · **không sửa tay** `eval/run-*.csv`, `cost/simulate-*.csv`, `traces/` (chỉ điền cột `pass`, `ghi_chu`).
- Lỗi kỹ thuật giữa chừng → chạy lại thành lượt mới, không sửa file cũ.
- Trước mỗi push: `git pull --rebase` · `git add` từng file · `git status` không có `.env`, `kickoff/`.
