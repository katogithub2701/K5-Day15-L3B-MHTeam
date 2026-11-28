# Tổng hợp bằng chứng pain

> Điền ở guide bước 1.2, xong trước **CP3 10:00 Thứ Bảy 28/11**. Chấm ở rubric R1. Người tổng hợp: Nguyễn Quốc Toàn.
> Ba nguồn ngang nhau — tối thiểu **≥1 nguồn đạt ngưỡng**. Nhóm làm: **khảo sát (nguồn chính) + đào data (kiểm lại)**.
> **Đã chốt 08:00 28/11:** form đóng, **không có phiếu mới** sau phiếu cuối lúc 18:18 27/11 (Toàn kiểm trên Google Form) → số cuối vẫn là **22 phiếu nộp từ 14:36 đến 18:18 ngày 27/11**, không đổi so với bản CP2. Chạy lại `python evidence/survey/count_survey.py` cho đúng các số dưới đây.

## 1. Nguồn đã dùng

| Nguồn | Đạt ngưỡng? | File |
|---|---|---|
| Đào data (x/N, %, cách đếm chạy lại được, ≥5 ví dụ) | ☑ 9 phép đếm x/N, script `evidence/count.py`, 7 ví dụ | `evidence/data-mining.md` |
| Phỏng vấn (≥3 người ngoài nhóm, đúng người dùng) | ☐ không làm (người đồng ý ở câu 11 khảo sát có thể hỏi thêm) | — |
| Khảo sát (≥20 người ngoài nhóm, đúng người dùng) | ☑ **n = 22** học viên (16 L3B · 6 L3A), **không thành viên nhóm nào điền** (nhóm xác nhận 27/11), log từng phiếu, script đếm | `evidence/survey/questions.md` · `results.csv` · `count_survey.py` |

## 2. Số chính

**Khảo sát** (nguồn chính · Google Form gửi Discord [L34] AI-20K · cách đếm viết trước ở `questions.md` · chạy `python evidence/survey/count_survey.py`):
- **n = 22** — cả 22 là học viên và đã từng xem trước slide (câu 2 ≠ "Chưa bao giờ") → mẫu số chính = 22.
- **Gặp chỗ không hiểu** (câu 4 ≠ "Không có"): **19/22 (86,4%)** — 8 người gặp > 3 chỗ, 7 người 2–3 chỗ, 4 người 1 chỗ.
- **Pain nặng** (gặp pain **và** (câu 7 ≠ "Hiểu" **hoặc** câu 6 ≥ 15–30 phút)): **15/22 (68,2%)** · trong số gặp pain: 15/19 (78,9%).
- **Ngưỡng giả thuyết** — trong số gặp pain, bỏ qua hoặc mất ≥ 15 phút: **9/19 (47,4%)**.
- **Đang xoay xở bằng** (câu 5, trên 19 người gặp pain): hỏi ChatGPT / Gemini riêng **16/19 (84,2%)** · đọc lại slide 15/19 (78,9%) · tra Google 7/19 (36,8%) · hỏi bạn 4/19 · để dành hỏi trên lớp 3/19 · hỏi Discord 2/19 · bỏ qua 1/19.
- **Câu trả lời Google / ChatGPT lệch bài** (câu 8 = lệch một phần / lệch nhiều, trên người có tra): **13/21 (61,9%)**.
- **Thời gian lần gần nhất** (câu 6, 19 người gặp pain): dưới 5' **6** · 5–15' **4** · 15–30' **6** · trên 30' **3** → **phút / lần ≈ 15,9** (trung bình trung điểm 2,5 / 10 / 22,5 / 37,5 phút; trung vị 10) → dùng cho `spec.md` §2.
- **Cuối cùng có hiểu không** (câu 7, 19 người): hiểu 9 · **hiểu một phần 9** · không hiểu 0.
- **Chưa dùng pre-class** (câu 10 = chưa từng nghe / biết nhưng chưa dùng): **16/22 (72,7%)** — đã dùng 1–2 lần 4, dùng thường xuyên 2.
- **Số buổi xem trước / 2 tuần** (câu 3): trung vị **3** · trung bình 3,41 → **≈ 6,4 lần / tháng** (cho `cost/personas.yaml`).
- **Phiếu tự mâu thuẫn** (đếm đúng theo cách đã viết, không sửa): #07, #15 chọn câu 4 = "Không có" nhưng vẫn ghi câu 6 = 5–15 phút; #17 chọn câu 4 = "2–3 chỗ" nhưng câu 7 = "Không gặp chỗ nào". Nếu bỏ 3 phiếu này, gặp pain = 18/19 — kết luận không đổi.

**Đào data** (kiểm lại · `data/preclass/`, 05/11 → 25/11/2026, 436 học viên có hoạt động — chi tiết `evidence/data-mining.md`):
- **143/436 (32,8%)** học viên đã hỏi trợ giảng AI khi tự học trước buổi — 1.091 câu hỏi.
- **66/429 (15,4%)** người mở bài giảng đã **bôi đen chữ trên slide để hỏi** (433 lần), và **402/433 (92,8%)** lần đó có câu hỏi thật gửi đi trong 3 phút.
- **512/1.091 (46,9%)** câu là hỏi nối (cùng video, ≤ 5 phút sau câu trước) — một câu trả lời thường chưa đủ.
- **173/1.091 (15,9%)** câu hỏi ≤ 20 ký tự (dễ mơ hồ) · **98/1.076 (9,1%)** lần AI báo thiếu ngữ cảnh bài · chỉ **326/1.091 (29,9%)** câu trả lời có dẫn mốc trong bài để học viên tự kiểm.
- **398/1.091 (36,5%)** câu hỏi lúc 19h–6h (giờ VN), khi không có TA / giảng viên để hỏi ngay.
- Người đã hỏi: trung bình **1,79 ngày có hỏi / 21 ngày ≈ 2,56 lần / tháng**.

## 3. ≥5 trích dẫn hoặc ví dụ nguyên văn (có nguồn, bỏ tên)

Trích nguyên văn từ khảo sát (câu 9, giữ nguyên chính tả; 11/22 phiếu có viết):
1. "Slide trên lms đôi khi không cung cấp thông tin chi tiết, mà chỉ là một bộ dàn ý để giảng viên giảng lại cho học viên. Vì vây, mình vẫn cần tự tìm thông tin bên ngoài slide" — phiếu #03 (L3B)
2. "Có rất nhiều nội dung, kèm slide, đôi khi bị mất kết nối giữa các phần" — phiếu #02 (L3A)
3. "slide dài, nhiều chỗ không hiểu" — phiếu #10 (L3B)
4. "slide cô đọng đôi khi khiến khó hiểu" — phiếu #17 (L3B)
5. "Nhiều slide trong cùng 1 bài, không biết đâu là slide đúng, thậm chí có mấy ngày học slide không nằm trong dán sách" — phiếu #07 (L3B)
6. "Slide không khớp với slide giảng viên dùng" — phiếu #05 (L3B)
7. "Quá nhiều slide ko biết nên chọn cái nào" — phiếu #16 (L3A)
8. "Tôi ko thấy khó chịu" — phiếu #18 (L3B) *(giữ lại câu ngược chiều)*

Gom nhãn câu 9 (11 phiếu có viết): **nội dung dài / cô đọng / thiếu chi tiết, khó hiểu** 5/11 (#02, #03, #08, #10, #17) · **không biết slide nào đúng / khớp lớp, giảng viên** 5/11 (#04, #05, #07, #12, #16) · không khó chịu 1/11 (#18). (#12 có thêm "khá lag, khó zoom".)

Ví dụ hành vi từ data (data không có chữ học viên viết):
9. `L0585` bôi đen 47 ký tự ở **slide 9** bài Day01 lúc **22:28** → hỏi `C00600` → AI trả lời 348 ký tự, **không dẫn mốc** nào trong bài — data `slide_text_asked` 08/11.
10. `L0643` bôi đen ở **slide 36** bài Day07 lúc **00:30** → hỏi `C00265` → trả lời 505 ký tự, không dẫn mốc — data 16/11.
11. `C00983` (Day01, video `d01-r1-v05`): AI báo **thiếu ngữ cảnh bài** nhưng vẫn trả lời 182 ký tự — data `agent_replied` 05/11.
12. `C01059` câu hỏi **14 ký tự**, AI báo thiếu ngữ cảnh, vẫn trả lời 261 ký tự — data 10/11.
13. `C01056` câu hỏi chỉ **2 ký tự** → AI trả lời 171 ký tự, không hỏi lại — data Day01.

## 4. Các nguồn có khớp nhau không

**Khớp:**
- Khảo sát: **86,4%** gặp chỗ không hiểu khi xem trước slide. Data: chỉ **32,8%** học viên có hỏi trợ giảng trên pre-class. Chỗ chênh **được giải thích bởi chính khảo sát**: 84,2% người gặp pain hỏi **ChatGPT / Gemini riêng**, và 72,7% chưa dùng pre-class → phần lớn gặp chỗ không hiểu nhưng **không hỏi ở nơi có căn cứ bài giảng**. Vì vậy 32,8% trong data là **cận dưới**.
- Khảo sát: **61,9%** người đã tra thấy câu trả lời Google / ChatGPT **lệch bài**. Data: chỉ **29,9%** câu trả lời của trợ giảng pre-class trỏ về chỗ trong bài. Hai nguồn cùng chỉ ra: thiếu một câu trả lời **bám đúng slide và kiểm lại được** → khớp với lý do lát cắt **luôn kèm số trang** và nói "slide không đề cập" khi không có căn cứ.
- Khảo sát: phút / lần ≈ 15,9 — khớp với số 15 phút nhóm tự ước tính ở `spec.md` §2 trước khi có khảo sát.

**Lệch / điều mới:**
- Data cho thấy **63,5%** câu hỏi lúc 6h–19h, không chủ yếu buổi tối như persona ban đầu (đã sửa canvas dòng 2).
- Khảo sát đếm **người**, data đếm **hành vi**; mẫu khảo sát nhỏ (n = 22) và tự chọn (người trả lời form trên Discord thường chủ động hơn) → % khảo sát có thể **cao hơn** thực tế toàn khoá.
- **Insight không có trong giả thuyết:** 5/11 câu 9 than **không biết slide nào là đúng** (nhiều bản slide của nhiều giảng viên / lớp). Lát cắt không giải pain này, nhưng nó là một rủi ro nguồn sự thật: trợ lý phải ghi rõ đang dựa vào **bộ slide nào** (buổi, bản) — gợi ý cho `spec.md` §5 lớp 1.

## 5. Kết luận

Giả thuyết ở `evidence/hypothesis.md`: **đúng** (về pain) và **phải đổi một chi tiết** (về thời điểm) — vì:
- **Đạt cả hai ngưỡng đã viết trước:** ≥ 50% người xem slide gặp chỗ không hiểu → **19/22 (86,4%)**; trong số đó ≥ 1/3 bỏ qua hoặc mất > 15 phút → **9/19 (47,4%)**.
- Hậu quả đúng như giả thuyết: 9/19 chỉ **hiểu một phần** trước khi lên lớp; cách xoay xở chính là ChatGPT riêng, và 13/21 thấy lệch bài.
- **Cách giải thích khác bị loại một phần:** "ChatGPT riêng đã đủ dùng" — có dùng (84,2%) nhưng 61,9% thấy lệch bài và một nửa chỉ hiểu một phần → chưa đủ.
- **Phải đổi:** "tối trước buổi học" → "khi tự xem slide trước buổi, bất kể giờ" (data: 36,5% câu hỏi lúc 19h–6h).

Điều vẫn chưa biết: người không trả lời form có gặp pain giống không; pain "không biết slide nào đúng" lớn tới đâu (mới có 5 phiếu tự viết, chưa có câu hỏi riêng).

## Lịch hẹn (dùng cho CP2 — chỉ ghi vai và giờ, không tên)

| Vai | Giờ hẹn | Đã xong? |
|---|---|---|
| Khảo sát Google Form — học viên L3A / L3B, gửi Discord [L34] AI-20K | mở 27/11 14:30 · chốt 28/11 08:00 | ☑ đã chốt — 22 phiếu (phiếu cuối 18:18 27/11, không có phiếu mới đến 08:00 28/11) |
