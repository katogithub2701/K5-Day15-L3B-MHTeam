# Khảo sát — xem trước slide bài giảng trên LMS

- **Kênh gửi:** nhóm Discord **[L34] AI-20K** (học viên L3A, L3B)
- **Mở:** 27/11/2026 14:30 · **Chốt:** 28/11/2026 08:00
- **Người trả lời hợp lệ:** học viên AI20K K5, **ngoài nhóm**. Câu 1 dùng để lọc.
- Form **không thu** tên, email, số điện thoại, mã học viên. Kết quả xuất ra `results.csv` sau khi đã xoá mọi cột nhận ra người trả lời.

**Tạo form tự động:** chạy `create_form.gs` (hướng dẫn ở đầu file) — ra form đúng 11 câu dưới đây, có nhánh ở câu 2.

**Lời mở đầu form (chép nguyên):**
> Nhóm MHTeam (L3B) đang làm hackathon về việc xem trước slide bài giảng trên LMS. Form mất khoảng 2 phút, ẩn danh, chỉ hỏi về những lần bạn đã thực sự xem slide. Cảm ơn bạn!

| # | Câu hỏi | Kiểu trả lời |
|---|---|---|
| 1 | Bạn là: | Học viên L3A · Học viên L3B · Lab coach / TA · Khác |
| 2 | Lần gần nhất bạn mở slide của một buổi học trên LMS **trước khi** đến lớp là khi nào? | Hôm nay · Tuần này · Tuần trước · Lâu hơn · Chưa bao giờ (→ nhảy tới câu 9) |
| 3 | Trong 2 tuần qua, bạn đã xem trước slide trên LMS khoảng mấy buổi? | Số |
| 4 | Lần gần nhất đó, bạn có gặp chỗ nào trong slide mà bạn không hiểu không? | Không có · 1 chỗ · 2–3 chỗ · Nhiều hơn 3 chỗ |
| 5 | Với chỗ không hiểu đó, bạn đã làm gì? | Chọn nhiều: Không gặp chỗ nào không hiểu · Đọc lại slide · Tra Google · Hỏi ChatGPT / Gemini riêng · Hỏi bạn · Hỏi trên Discord · Để dành hỏi trên lớp · Bỏ qua · Khác |
| 6 | Lần đó bạn mất khoảng bao lâu để hiểu ra (hoặc bỏ cuộc)? | Không gặp chỗ nào không hiểu · Dưới 5 phút · 5–15 phút · 15–30 phút · Trên 30 phút |
| 7 | Cuối cùng bạn có hiểu được chỗ đó trước khi lên lớp không? | Không gặp chỗ nào không hiểu · Hiểu · Hiểu một phần · Không hiểu |
| 8 | Nếu đã tra Google hoặc ChatGPT: câu trả lời có khớp với nội dung giảng viên giảng trên lớp không? | Khớp · Lệch một phần · Lệch nhiều · Không để ý / không tra |
| 9 | Điều gì khó chịu nhất khi xem trước slide trên LMS? (kể một lần cụ thể nếu được) | Đoạn văn |
| 10 | Bạn có biết / có dùng trang pre-class (preclass-online.com, có video và khung chat hỏi trợ giảng AI) không? | Chưa từng nghe tới · Biết nhưng chưa dùng · Đã dùng 1–2 lần · Dùng thường xuyên |
| 11 | (tuỳ chọn) Bạn có sẵn lòng nhắn tin với nhóm 5 phút để kể thêm không? | Có, liên hệ qua: ____ (không bắt buộc) · Không |

**Cách đếm (viết trước khi xem kết quả):**
- Mẫu số chính = số người ở câu 1 là học viên **và** câu 2 không phải "Chưa bao giờ".
- "Gặp pain" = câu 4 ≠ "Không có".
- "Pain nặng" = gặp pain **và** (câu 7 ≠ "Hiểu" **hoặc** câu 6 ≥ "15–30 phút").
- Câu 10: đếm x/N người "Chưa từng nghe tới" hoặc "Biết nhưng chưa dùng" → trả lời câu "vì sao làm trên slide LMS khi đã có pre-class" (`spec.md` §3). Ghi đúng số đếm được, kể cả khi số đó cho thấy đa số đã dùng pre-class.
- Câu 3 dùng làm số lần / tháng cho persona chi phí (`cost/personas.yaml`).
- Câu 9 là nguồn trích dẫn nguyên văn (bỏ tên) cho `evidence/summary.md`, và nguồn câu thử `source: nguoi_dung` cho `eval/benchmark.csv`.
