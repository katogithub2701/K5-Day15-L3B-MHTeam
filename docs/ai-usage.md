# Khai báo dùng AI

README của nhóm có mục "Dùng AI vào việc gì" (2–3 dòng, bắt buộc). Ghi chi tiết vào bảng dưới đây.

> Luật của đề: dùng AI để làm bài thoải mái, nhưng **ai không giải thích được phần có tên mình thì phần đó nhận 0 điểm**. Khai thiếu không bị trừ; giấu mới bị.

| Việc | Công cụ AI | AI làm gì | Người kiểm/sửa gì | Ai phụ trách |
|---|---|---|---|---|
| Code bản chạy thử — công cụ `search_slides` | Claude Code (Claude Opus 5.5) | Viết `search_slides` trong `codebase/tools.py` (bỏ dấu, danh sách từ chức năng, chấm điểm từ / cụm 2 từ trùng, ngưỡng điểm ≥ 2 + phủ ≥ 50%, lọc tương đối 50%); đổi `codebase/agent.py` sang gọi `search_slides`; điền bảng công cụ `spec.md` §4 | Chạy thử 15 câu: 10 câu trong slide ra đúng trang (vd baseline → tr.17, 5 Whys → tr.24, PRD v0 → tr.54), 5 câu ngoài slide / tấn công / mơ hồ → `[]` · `python run.py` với AI giả chạy hết luồng · Thành đọc lại code và giải thích được từng ngưỡng: __ | Nguyễn Quang Thành |
| Prompt / thiết kế lời gọi mô hình — luồng chính, nối model, thiết kế §3–§4 | Claude Code (Claude Opus 5.5) | Soạn nháp `spec.md` §3 (so với pre-class, ChatGPT) và §4 (sơ đồ Mermaid, hình dạng, chỗ chặn rủi ro, nguyên tắc G10/G11/G1-G2/G8-G9); viết `codebase/agent.py` (`SYSTEM` prompt 3 nhãn TRẢ LỜI / HỎI LẠI / KHÔNG ĐỀ CẬP, nhánh N không gọi model, bước kiểm số trang `_pages_cited`); viết `call_gemini` trong `codebase/ai.py` (token lấy từ `usageMetadata`, cộng token suy nghĩ) | Nghị đọc và chỉnh §3–§4 · chạy `python run.py` với Gemini thật 6 câu: 5 Whys → tr.24 ✓, Precision/Recall → tr.42 ✓, RAG → không đề cập, 0 lần gọi model ✓, làm hộ lab → không đề cập ✓, câu tấn công → không đề cập ✓, `metric` (mơ hồ) → AI trả lời thay vì hỏi lại ✗ (giữ làm câu thử, chưa sửa prompt) · tự giải thích được từng nhánh: __ | Lã Quốc Nghị |
| Đào data (viết script đếm, gợi ý nhãn) | Claude Code (Claude Opus 5.5) | Đọc từ điển cột `data/preclass/`, đề xuất 9 phép đếm, viết `evidence/count.py`, soạn nháp `evidence/data-mining.md`, `evidence/summary.md` (phần data), `spec.md` §2, `canvas.md` dòng 4 | Toàn đọc lại định nghĩa từng phép đếm (mẫu số, ngưỡng 20 ký tự / 3 phút / 5 phút) · chạy lại `count.py` ra cùng số · kiểm tay bằng Excel trên `chat.csv` (lọc `kind = question`, `agent_id = teaching_assistant`): __ câu, __ người — khớp M1 (1.091 câu, 143 người) __ · đối chiếu 7 ví dụ với dòng gốc: khớp __/7 | Nguyễn Quốc Toàn |
| Rà câu hỏi phỏng vấn / khảo sát | | Chỉ rà câu dẫn dắt | | |
| Viết câu thử (benchmark) | | | Mỗi câu thử có `source`; câu thử AI viết được ghi rõ | |
| Sinh data `synthetic` (nếu có) | | | Seed __ · kiểm tay __ dòng | |
| Chấm cột `pass` bằng LLM (nếu có) | | | Kiểm tra thủ công __ câu thử, khớp __/__ | |
| Slide, văn bản | | | | |

**Không dùng AI để:** tạo người được phỏng vấn, trích dẫn, câu trả lời khảo sát; sửa kết quả các lượt đã chạy (`eval/run-*.csv`, `cost/simulate-*.csv`, `traces/`).
