# Khai báo dùng AI

README của nhóm có mục "Dùng AI vào việc gì" (2–3 dòng, bắt buộc). Ghi chi tiết vào bảng dưới đây.

> Luật của đề: dùng AI để làm bài thoải mái, nhưng **ai không giải thích được phần có tên mình thì phần đó nhận 0 điểm**. Khai thiếu không bị trừ; giấu mới bị.

| Việc | Công cụ AI | AI làm gì | Người kiểm/sửa gì | Ai phụ trách |
|---|---|---|---|---|
| Code bản chạy thử | | | | |
| Prompt / thiết kế lời gọi mô hình | | | | |
| Đào data (viết script đếm, gợi ý nhãn) | Claude Code (Claude Opus 5.5) | Đọc từ điển cột `data/preclass/`, đề xuất 9 phép đếm, viết `evidence/count.py`, soạn nháp `evidence/data-mining.md`, `evidence/summary.md` (phần data), `spec.md` §2, `canvas.md` dòng 4 | Toàn đọc lại định nghĩa từng phép đếm (mẫu số, ngưỡng 20 ký tự / 3 phút / 5 phút) · chạy lại `count.py` ra cùng số · kiểm tay bằng Excel trên `chat.csv` (lọc `kind = question`, `agent_id = teaching_assistant`): __ câu, __ người — khớp M1 (1.091 câu, 143 người) __ · đối chiếu 7 ví dụ với dòng gốc: khớp __/7 | Nguyễn Quốc Toàn |
| Rà câu hỏi phỏng vấn / khảo sát | | Chỉ rà câu dẫn dắt | | |
| Viết câu thử (benchmark) | | | Mỗi câu thử có `source`; câu thử AI viết được ghi rõ | |
| Sinh data `synthetic` (nếu có) | | | Seed __ · kiểm tay __ dòng | |
| Chấm cột `pass` bằng LLM (nếu có) | | | Kiểm tra thủ công __ câu thử, khớp __/__ | |
| Slide, văn bản | | | | |

**Không dùng AI để:** tạo người được phỏng vấn, trích dẫn, câu trả lời khảo sát; sửa kết quả các lượt đã chạy (`eval/run-*.csv`, `cost/simulate-*.csv`, `traces/`).
