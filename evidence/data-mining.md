# Đào data — cách đếm và kết quả

> Điền ở guide bước 1.2. Người làm: Nguyễn Quốc Toàn. Script: `evidence/count.py` — chạy `python evidence/count.py <đường-dẫn-tới-data/preclass>` ra đúng các số dưới đây.
> Repo chỉ chứa số đã tổng hợp và vài dòng ví dụ (mã đã ẩn danh của BTC) — không chép lại nguyên file data.

## 1. Cách đếm

- **Data dùng:** `data/preclass/` BTC cấp — `events.csv`, `chat.csv`, `completed_items.csv` · từ **05/11/2026 đến 25/11/2026** (21 ngày, Day01 → Day13) · 721 tài khoản khoá AI20K K5 level 3–4, **436 người có hoạt động**.
- **Vì sao dùng data này dù lát cắt là slide LMS:** data LMS không có. Trang pre-class là nơi **cùng nhóm học viên L3** tự học **trước buổi**, và có đúng hành vi mình cần đo: gặp chỗ không hiểu → hỏi trợ giảng AI, kể cả bôi đen chữ **trên slide** để hỏi (`slide_text_asked`). Đây là nguồn kiểm lại cho khảo sát (nguồn chính, xem `evidence/hypothesis.md`).
- **Đếm gì · trên tập nào · lọc gì · mẫu số:**

| Mã | Đếm gì | Lọc | Mẫu số |
|---|---|---|---|
| M1 | Người hỏi trợ giảng AI ≥1 lần | `chat.csv`: `kind = question`, `agent_id = teaching_assistant` (bỏ reply / mention bạn học AI) | 436 người có hoạt động (có ≥1 dòng `actor = learner`) |
| M2 | Người bôi đen chữ trên slide để hỏi ≥1 lần; và trong các lần đó, bao nhiêu lần gửi câu hỏi thật trong 3 phút sau | `events.csv` `type = slide_text_asked`; nối với `chat_sent` cùng `hv` | 429 người đã mở bài giảng (`lecture_opened`) · 433 lần bôi đen |
| M3 | Câu hỏi ngắn ≤ 20 ký tự (dễ mơ hồ, thiếu ngữ cảnh) | như M1, cột `do_dai_cau_hoi` | 1.091 câu hỏi |
| M4 | Câu hỏi nối: cùng người, cùng video (`transcript`), cách câu trước ≤ 5 phút | như M1 | 1.091 câu hỏi |
| M5 | AI báo thiếu ngữ cảnh bài để trả lời | `agent_replied` `missing_context = true` | 1.076 câu có ghi `missing_context` |
| M6 | Câu trả lời có dẫn mốc trong bài giảng (học viên tự kiểm được) | `agent_replied` có `moc_trich_dan` | 1.091 câu hỏi |
| M7 | Câu hỏi theo khung giờ Việt Nam (UTC + 7) | như M1 | 1.091 câu hỏi |
| M8 | Số ngày khác nhau có hỏi, trên mỗi người đã hỏi → quy ra / tháng (× 30 / 21) | như M1 | 143 người đã hỏi |
| M9 | Người mở bài giảng nhưng chưa đánh dấu xong mục nào | `lecture_opened` trừ người có dòng ở `completed_items.csv` | 429 người đã mở bài giảng |

- **Ghi chú trung thực:** các định nghĩa trên chốt sau khi đọc thử dòng đầu các file và từ điển cột (mục 2); ngưỡng 20 ký tự, 3 phút, 5 phút là nhóm tự chọn, ghi hằng số ở đầu `count.py` để người khác đổi và chạy lại.

## 2. Đọc trước, đếm sau

Đã đọc ~50 dòng đầu `events.csv`, `chat.csv`, toàn bộ `column_dictionary.csv` và `event_types.csv`. Các *kiểu* hành vi thấy được:
- Học viên mở bài giảng → xem video → hỏi trợ giảng AI ngay dưới video / slide (`channel = video_question`), thường hỏi **liền nhiều câu** cách nhau 1–2 phút trên cùng một video.
- Học viên **bôi đen một đoạn chữ trên slide** (≈ 40–50 ký tự) rồi bấm hỏi → ngay sau đó có một `chat_sent`.
- Có câu hỏi rất ngắn (2–10 ký tự), kiểu chỉ gõ một từ.
- Một phần câu trả lời có `missing_context = true` (AI không có đủ lời giảng quanh chỗ hỏi); chỉ một phần có `moc_trich_dan` (dẫn mốc giây trong bài).
- Số người mở bài giảm mạnh theo ngày học (Day01: 415 người → Day13: 49 người) — một phần vì các ngày sau mới mở, ghi ít ngày hơn.

## 3. Kết quả

| Mã | Đếm gì | x / N | % | Ghi chú |
|---|---|---|---|---|
| M1 | Học viên có hoạt động đã hỏi trợ giảng AI khi tự học trước buổi | 143 / 436 | 32,8% | 1.091 câu hỏi. Có chỗ để hỏi thì **1/3** học viên dùng |
| M2 | Người đã mở bài giảng có bôi đen chữ **trên slide** để hỏi | 66 / 429 | 15,4% | 433 lần; **402 / 433 (92,8%)** lần bôi đen có câu hỏi gửi đi trong 3 phút → hỏi trên slide là câu hỏi thật, không phải bấm nhầm |
| M3 | Câu hỏi ≤ 20 ký tự | 173 / 1.091 | 15,9% | trung vị độ dài câu hỏi 57 ký tự → cần nhánh **hỏi lại khi câu mơ hồ** |
| M4 | Câu hỏi nối (cùng video, ≤ 5 phút sau câu trước) | 512 / 1.091 | 46,9% | gần một nửa câu là hỏi tiếp → một câu trả lời thường chưa đủ để hiểu |
| M5 | AI báo thiếu ngữ cảnh bài | 98 / 1.076 | 9,1% | cần nhánh **"slide không đề cập"** thay vì trả lời từ trí nhớ |
| M6 | Câu trả lời có dẫn mốc trong bài giảng | 326 / 1.091 | 29,9% | **70,1%** câu trả lời học viên không có chỗ để tự kiểm lại trong bài → lý do lát cắt **luôn kèm số trang** |
| M7 | Câu hỏi lúc 19h–24h · 0h–6h · 6h–19h (giờ VN) | 251 · 147 · 693 / 1.091 | 23,0% · 13,5% · 63,5% | **36,5%** câu hỏi ngoài giờ hành chính — lúc không có TA / giảng viên để hỏi ngay. Đa số vẫn là ban ngày: **ngược một phần** với persona "tối trước buổi học" |
| M8 | Số ngày có hỏi / người đã hỏi | trung vị 1 · trung bình 1,79 trong 21 ngày | — | quy ra **≈ 2,56 lần / tháng** / người hay hỏi; phân bố lệch: 85 người hỏi đúng 1 ngày, 7 người hỏi ≥ 5 ngày |
| M9 | Mở bài giảng nhưng chưa xong mục nào | 237 / 429 | 55,2% | dùng cho hướng bị loại ở `spec.md` §2 |

## 4. ≥5 ví dụ cụ thể (mã ẩn danh của BTC, không đoán ai là ai)

1. `L0585` · Day01 *ai-llm-foundation* · **08/11 22:28** (giờ VN): bôi đen 47 ký tự ở **slide 9** → gửi câu hỏi `C00600` (96 ký tự) → AI trả lời 348 ký tự, **không dẫn mốc** nào trong bài.
2. `L0643` · Day07 *retrieval-context-engineering* · **16/11 00:30**: bôi đen 24 ký tự ở **slide 36** → câu hỏi `C00265` (73 ký tự) lúc nửa đêm → trả lời 505 ký tự, không dẫn mốc.
3. `L0643` · Day05 *ai-product-thinking-and-requirement* · **13/11 00:42**: bôi đen 51 ký tự ở **slide 22** → câu hỏi `C00742` (100 ký tự) → trả lời 420 ký tự, không dẫn mốc. Cùng một người, hai đêm khác nhau, hai bài khác nhau.
4. `C00983` · `L0213` · Day01 video `d01-r1-v05` · 05/11 19:56: câu hỏi 29 ký tự, AI báo **`missing_context = true`** (thiếu ngữ cảnh bài) nhưng vẫn trả lời 182 ký tự.
5. `C01059` · `L0054` · Day01 video `d01-r1-v05` · 10/11 20:26: câu hỏi **14 ký tự**, AI báo thiếu ngữ cảnh, vẫn trả lời 261 ký tự.
6. `C01056` · `L0057` · Day01 video `d01-r1-v01`: câu hỏi chỉ **2 ký tự** → AI trả lời 171 ký tự (không hỏi lại học viên muốn hỏi gì).
7. `L0616` · Day11 *guardrails-hitl-responsible-ai* · 20/11 08:19: bôi đen **111 ký tự** ở slide 14 → câu hỏi `C00665` (160 ký tự) → trả lời có dẫn mốc — ví dụ đường đi "tốt" mà lát cắt muốn thành mặc định.

## 5. Giới hạn của data

- **Không có chữ học viên viết** — chỉ có độ dài. Không biết họ hỏi gì, không biết câu trả lời có đúng không (`verdict` chỉ có ở 46 / 1.260 lượt).
- **Đây là trang pre-class, không phải slide LMS** của lát cắt. Lệch về phía học viên đã chủ động mở pre-class; người chỉ xem slide LMS và gặp chỗ không hiểu nhưng **không hỏi ai** thì không có trong data → M1 là **cận dưới** của số người gặp chỗ không hiểu.
- **Không lọc được L3A / L3B** — mã học viên đã thay, không có cột lớp. Số ở đây là cả level 3–4.
- **Không biết đã mất bao lâu, có hiểu ra không, có lên lớp vẫn chưa nắm ý chính không** — data cho biết người ta **làm gì**, không cho biết **vì sao** và **tốn bao nhiêu**.
- Ngày cuối (Day10–Day13) ghi ít ngày hơn nên số người / số câu thấp hơn, không phải vì học viên bỏ.

→ **Kiểm lại bằng khảo sát** `evidence/survey/questions.md`: câu 4 (có gặp chỗ không hiểu không) kiểm M1 từ phía người **không hỏi**; câu 5 (đã làm gì) kiểm xem ngoài pre-class họ có tra Google / ChatGPT không; câu 6 (mất bao lâu) cho thừa số "phút / lần" ở `spec.md` §2 mà data không có; câu 8 (Google / ChatGPT có lệch bài không) kiểm lý do "luôn kèm số trang"; câu 10 cho biết bao nhiêu người chưa dùng pre-class.
