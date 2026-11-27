# Tổng hợp bằng chứng pain

> Điền ở guide bước 1.2, xong trước **CP3 10:00 Thứ Bảy 28/11**. Chấm ở rubric R1. Người tổng hợp: Nguyễn Quốc Toàn.
> Ba nguồn ngang nhau — tối thiểu **≥1 nguồn đạt ngưỡng**. Nhóm làm: **khảo sát (nguồn chính) + đào data (kiểm lại)**.

## 1. Nguồn đã dùng

| Nguồn | Đạt ngưỡng? | File |
|---|---|---|
| Đào data (x/N, %, cách đếm chạy lại được, ≥5 ví dụ) | ☑ 9 phép đếm x/N, script `evidence/count.py`, 7 ví dụ | `evidence/data-mining.md` |
| Phỏng vấn (≥3 người ngoài nhóm, đúng người dùng) | ☐ không làm (người đồng ý ở câu 11 khảo sát có thể hỏi thêm) | — |
| Khảo sát (≥20 người ngoài nhóm, đúng người dùng) | ☐ **đang thu** — n = __ | `evidence/survey/questions.md` · `results.csv` |

## 2. Số chính

**Đào data** (`data/preclass/`, 05/11 → 25/11/2026, 436 học viên có hoạt động — chi tiết `evidence/data-mining.md`):
- **143/436 (32,8%)** học viên đã hỏi trợ giảng AI khi tự học trước buổi — 1.091 câu hỏi.
- **66/429 (15,4%)** người mở bài giảng đã **bôi đen chữ trên slide để hỏi** (433 lần), và **402/433 (92,8%)** lần đó có câu hỏi thật gửi đi trong 3 phút.
- **512/1.091 (46,9%)** câu là hỏi nối (cùng video, ≤ 5 phút sau câu trước) — một câu trả lời thường chưa đủ.
- **173/1.091 (15,9%)** câu hỏi ≤ 20 ký tự (dễ mơ hồ) · **98/1.076 (9,1%)** lần AI báo thiếu ngữ cảnh bài · chỉ **326/1.091 (29,9%)** câu trả lời có dẫn mốc trong bài để học viên tự kiểm.
- **398/1.091 (36,5%)** câu hỏi lúc 19h–6h (giờ VN), khi không có TA / giảng viên để hỏi ngay.
- Người đã hỏi: trung bình **1,79 ngày có hỏi / 21 ngày ≈ 2,56 lần / tháng**.

**Khảo sát** (`evidence/survey/`, cách đếm viết trước ở `questions.md`) — *điền khi chốt form, không sửa cách đếm*:
- n hợp lệ = __ (học viên, ngoài nhóm, câu 2 ≠ "Chưa bao giờ")
- Gặp chỗ không hiểu (câu 4 ≠ "Không có"): __/__ (__%)
- Pain nặng (gặp pain **và** (câu 7 ≠ "Hiểu" **hoặc** câu 6 ≥ 15–30 phút)): __/__ (__%)
- Đã tra Google / ChatGPT thấy lệch bài (câu 8 = lệch một phần / lệch nhiều): __/__ (__%)
- Thời gian lần gần nhất (câu 6): dưới 5' __ · 5–15' __ · 15–30' __ · trên 30' __ → **phút / lần** dùng cho `spec.md` §2 = __
- Chưa dùng pre-class (câu 10 = chưa nghe / biết nhưng chưa dùng): __/__ (__%)
- Số buổi xem trước trong 2 tuần (câu 3): trung vị __ → __ lần / tháng (cho `cost/personas.yaml`)

## 3. ≥5 trích dẫn hoặc ví dụ nguyên văn (có nguồn, bỏ tên)

Ví dụ từ data (data không có chữ học viên viết, nên đây là ví dụ hành vi):
1. `L0585` bôi đen 47 ký tự ở **slide 9** bài Day01 lúc **22:28** → hỏi `C00600` → AI trả lời 348 ký tự, **không dẫn mốc** nào trong bài — data dòng `slide_text_asked` 08/11.
2. `L0643` bôi đen ở **slide 36** bài Day07 lúc **00:30** → hỏi `C00265` → trả lời 505 ký tự, không dẫn mốc — data 16/11.
3. `C00983` (Day01, video `d01-r1-v05`): AI báo **thiếu ngữ cảnh bài** nhưng vẫn trả lời 182 ký tự — data `agent_replied` 05/11.
4. `C01059` câu hỏi **14 ký tự**, AI báo thiếu ngữ cảnh, vẫn trả lời 261 ký tự — data 10/11.
5. `C01056` câu hỏi chỉ **2 ký tự** → AI trả lời 171 ký tự, không hỏi lại — data Day01.

Trích nguyên văn từ khảo sát (câu 9, bỏ tên) — *chép khi có kết quả, ≥3 câu*:
6. "…" — phiếu khảo sát #__
7. "…" — phiếu khảo sát #__
8. "…" — phiếu khảo sát #__

## 4. Các nguồn có khớp nhau không

Data nói: khi có chỗ hỏi ngay trong bài, **1/3** học viên dùng, gần **một nửa** câu là hỏi nối, và **70%** câu trả lời không trỏ về chỗ nào trong bài để tự kiểm. Data **không** nói được người không hỏi có gặp chỗ không hiểu không, mất bao lâu, có hiểu ra không.

Người dùng nói (khảo sát): __ — *điền khi có kết quả*. Chỗ cần đối chiếu:
- Câu 4 so với M1: nếu tỉ lệ "gặp chỗ không hiểu" ở khảo sát cao hơn hẳn 32,8% → nhiều người gặp nhưng **không hỏi** (đúng hướng pain "không có ai để hỏi ngay").
- Câu 5 so với M1: bao nhiêu người hỏi ChatGPT / Google riêng thay vì trợ giảng trong bài.
- Câu 8 so với M6: nếu nhiều người thấy Google / ChatGPT lệch bài → khớp với lý do "luôn kèm số trang".
- Đã biết lệch: data cho thấy **63,5%** câu hỏi lúc 6h–19h, không phải chủ yếu buổi tối như persona ban đầu.

## 5. Kết luận

Giả thuyết ở `evidence/hypothesis.md`: **phải đổi một phần** (bản tạm từ data, chốt lại khi có khảo sát) — vì:
- **Đúng:** có nhu cầu hỏi ngay khi tự học trước buổi (32,8% hỏi, 15,4% hỏi thẳng trên slide), câu hỏi thường ngắn / hỏi nối, và đa số câu trả lời hiện có không trỏ về bài để tự kiểm.
- **Phải đổi:** "tối trước buổi học" chỉ đúng với ~1/3 câu hỏi (36,5% lúc 19h–6h); persona nên là "khi tự xem slide trước buổi, bất kể giờ".
- Ngưỡng đúng/sai trong `hypothesis.md` (≥50% gặp chỗ không hiểu, ≥1/3 trong đó bỏ qua hoặc mất >15 phút) **chỉ kiểm được bằng khảo sát** — kết luận cuối: **đúng / sai / phải đổi** = __.

Điều vẫn chưa biết: mỗi lần mất bao nhiêu phút (câu 6); người không dùng pre-class có gặp pain giống không (câu 10); câu trả lời của ChatGPT / Google có thật sự lệch bài không (câu 8).

## Lịch hẹn (dùng cho CP2 — chỉ ghi vai và giờ, không tên)

| Vai | Giờ hẹn | Đã xong? |
|---|---|---|
| Khảo sát Google Form — học viên L3A / L3B | mở 27/11 __:__ · chốt 28/11 __:__ | đang thu |
