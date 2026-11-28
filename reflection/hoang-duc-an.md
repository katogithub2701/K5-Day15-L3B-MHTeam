# Reflection — Hoàng Đức An

> Làm ở guide bước 5.3. Mỗi người một file: chép file này thành `reflection/<ten-khong-dau>.md` (viết thường, không dấu). Hạn: **23:59 Thứ Bảy 28/11**. Mỗi câu 3–6 dòng.

1. Vai trò + phần mình làm (trỏ tới file / commit):
- Vai trò: Thành viên cặp Y (đánh giá), phụ trách dữ liệu slide, bộ câu thử, metric và báo cáo đánh giá (`TEAMS.md`).
- Dữ liệu & thiết kế chỗ khó: Tóm tắt 28 trang trọng tâm từ slide Ngày 2 thành `data/slides.csv` và viết `data/DATA_CARD.md` (`441130c`); viết 8 kịch bản 4 lớp chỗ khó ở `spec.md` §5 và đề xuất chuẩn "đạt" ở `spec.md` §7 (`4dcd8d7`).
- Bộ câu thử & metric: Viết `eval/metric_spec.yaml` (3 metric), `eval/README.md` mục 1–4, khởi tạo 13 câu thử CP2 (`0694c70`, `441130c`) và mở rộng lên 24 câu trong `eval/benchmark.csv` (`27226fd`, thêm 10 câu từ tình huống khảo sát).
- Đánh giá & báo cáo: Chấm chéo 5 output với Toàn (khớp 5/5), viết `eval/report.md` lượt 1 (`5924b65`), chấm `pass` lượt 2 trên `eval/run-2.csv` (`77308c3`, `0a9bc55`), hoàn thiện `eval/report.md` + `eval/README.md` (`71a7dee`), làm slide trang 5, 8 và xuất `demo_slide.pdf`.

2. AI hỗ trợ mình thế nào (việc gì, công cụ gì, chỗ nào phải sửa lại output AI):
- Công cụ: Antigravity (model Gemini 4 Hydrogen), đã khai báo tại `docs/ai-usage.md`.
- AI hỗ trợ đọc PDF 88 trang Ngày 2 trong `data-btc/` để chọn và tóm tắt 28 đoạn vào `data/slides.csv` + `data/DATA_CARD.md`, đồng thời soạn nháp 8 kịch bản chỗ khó (`spec.md` §5), 3 metric (`eval/metric_spec.yaml`), 13 câu thử CP2 (`eval/benchmark.csv`) và `eval/README.md`.
- Phần tự kiểm và sửa lại: Đối chiếu lại từng số trang và nội dung 28 đoạn với PDF gốc để không chép nguyên văn và chạy script kiểm tra CSV hợp lệ 28/28 dòng; rà lại từng câu thử + `expected`, sửa ánh xạ câu `C13` vào đúng kịch bản ở `spec.md` §5 và kiểm tra bằng `python run.py check`.
- Khi chấm lượt 2, tự chấm tay cả 24 câu đặc biết các ca lệch (`C08`, `C09`).

3. Một câu thử trượt của nhóm và mình học được gì từ nó:
- Câu `C09` (*"Trang đó nói gì về lỗi vậy?"*, loại `kho`) ở lượt 1 (`eval/run-1.csv`): câu hỏi mơ hồ không nêu tên loại lỗi hay số trang, nhưng `search_slides` vẫn trả về 2 đoạn ở trang 35 và 53 nên model tự ghép nội dung hai trang không liên quan (lệch pha lợi ích và acceptance test) thành câu trả lời nghe rất chắc chắn thay vì hỏi lại.
- Bài học 1: Công cụ tìm kiếm trả về kết quả không đồng nghĩa câu hỏi đã đủ ngữ cảnh — cần kiểm tra độ rõ của câu hỏi trước khi cho AI tổng hợp câu trả lời, nếu không hệ thống sẽ rơi vào rủi ro nặng nhất là làm học viên hiểu sai kiến thức.
- Bài học 2: Thiết kế câu thử `kho` nhắm đúng tình huống mơ hồ giúp lộ lỗi thực tế mà câu `thuong` không bắt được; giữ nguyên bộ câu thử và chọn một cải tiến tập trung vào luật `HỎI LẠI` (`a70f3e0`) đã đưa nhóm câu mơ hồ từ `0/2` lên `2/2` và tổng đạt chuẩn `21/24` (88%) ở lượt 2.
