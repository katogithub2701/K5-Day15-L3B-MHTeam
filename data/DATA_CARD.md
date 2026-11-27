# Data card — dữ liệu bản chạy thử dùng

> Điền ở guide bước 2.4 (bản đầu ở CP2, đủ ở CP3). Ôn lại: ngày 6 · lab ngày 6. Chấm ở rubric R4.
> Một trang. Mỗi dataset một mục. Dữ liệu chạy thử (bài mẫu, thông báo mẫu, đoạn transcript…) để trong thư mục `data/` này.
> Không commit nguyên tài liệu khoá, dữ liệu cá nhân thật hay nguyên file data BTC cấp — chỉ đoạn trích ngắn, bản viết lại, hoặc số đã tổng hợp.

## Dataset 1 · `data/slides.csv` — Slide Ngày 2 (Discovery & Problem Framing)

| | |
|---|---|
| Dùng để làm gì | Nguồn dữ liệu cho công cụ `search_slides` (`codebase/tools.py`) để tra cứu đoạn nội dung kèm số trang khi trả lời câu hỏi học viên |
| Từ đâu | Tài liệu khoá (viết lại): viết lại từ slide buổi **Ngày 2 — Discovery & Problem Framing** (AI20K · Giai đoạn 1 · Ngày 2, file PDF 88 trang trên LMS) |
| Xử lý những bước gì | Chọn lọc 28 trang nội dung trọng tâm (loại bỏ slide bìa, giải lao, lịch trình lớp); tóm tắt và viết lại bằng lời của nhóm (2–4 câu/đoạn, không chép nguyên văn slide gốc); gắn số trang gốc và lưu thành CSV 4 cột (`id, page, topic, content`). Người viết & kiểm: Hoàng Đức An |
| Số dòng / số đoạn | 28 đoạn (`N2-01` đến `N2-28`, mỗi đoạn 2–4 câu) |
| Phiên bản / ngày lấy | 27/11/2026 (bản đầu CP2) |
| Nhãn | Thật *(diễn đạt lại từ tài liệu khoá, không phải dữ liệu tổng hợp nhân tạo)* |
| Giới hạn | Mới phủ 1 buổi học (Ngày 2: 28/88 trang có khái niệm chính), chưa có nội dung các buổi khác trong khoá; chưa trích xuất các chi tiết chỉ thể hiện qua hình ảnh/biểu đồ không có chữ |

**Data `synthetic` (nhóm tự sinh):** không áp dụng cho Dataset 1 (không dùng làm bằng chứng pain).

## Dataset 2 · *(chưa bổ sung ở bản đầu CP2)*

Sẽ cập nhật nếu nhóm bổ sung thêm slide các buổi khác hoặc dữ liệu phụ trợ ở CP3.
