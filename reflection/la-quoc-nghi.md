# Reflection — Lã Quốc Nghị

> Đội trưởng MHTeam · L3B · Track A. Trợ lý hỏi đáp trên slide Ngày 2, trả lời kèm số trang.

1. **Vai trò + phần mình làm (trỏ tới file / commit):**
   Mình là đội trưởng. Mình điều phối nhóm và nộp CP1–CP4. Mình viết `spec.md` đầu file, §3 và §4 (sơ đồ luồng cố định B → N/C → Q/N2/D → O) ở commit `8dc2b2a`. Mình viết luồng chính `codebase/agent.py`: `SYSTEM` prompt chọn 1 trong 3 nhãn, nhánh N không gọi model, bước kiểm số trang `_pages_cited`. Mình cũng nối Gemini thật trong `codebase/ai.py`, lấy token từ `usageMetadata` (commit `5513090`). Mình chốt chuẩn "đạt" ở §7 theo đề xuất của An (commit `4dcd8d7`). Mình chạy lượt 1, được 18/24 (`e98d531`). Mình làm cải tiến hỏi lại (`a70f3e0`) và chạy lượt 2, được 21/24 (`e1facb6`). Cuối cùng mình viết giao diện demo `codebase/web.py` (`e2d1011`).

2. **AI hỗ trợ mình thế nào (việc gì, công cụ gì, chỗ nào phải sửa lại output AI):**
   Mình dùng Claude Code (Claude Opus 5.5) để soạn nháp §3–§4, viết `agent.py`, `ai.py`, `web.py` và nháp các mục spec/README. Bảng chi tiết nằm ở `docs/ai-usage.md`. Mình phải sửa và kiểm lại output ở mấy chỗ:
   - Mình đọc lại và chỉnh §3–§4, rồi chạy 6 câu với Gemini thật. Câu mơ hồ "metric" bị AI trả lời luôn thay vì hỏi lại, nên mình giữ nó làm câu thử thay vì giấu đi.
   - Với `web.py`, mình bỏ kiểu neumorphism AI đề xuất. Mình cũng bỏ phần hiển thị PDF, vì slide gốc của BTC không được commit.
   - Khi soạn sổ tay chuẩn bị demo, AI kết luận con số 211 giờ "không có nguồn". Mình grep lại thì thấy nó nằm ở `spec.md` §2 dòng 39. Lý do là lệnh grep trước đó đã bị cắt bớt output.

   Bài học là phải tự grep hoặc chạy lại để xác minh mọi con số và mọi kết luận AI đưa ra, rồi mới dùng.

3. **Một câu thử trượt của nhóm và mình học được gì từ nó:**
   Ở lượt 1, C08 ("Cái ma trận đó dùng như thế nào?") và C09 ("Trang đó nói gì về lỗi vậy?") đều trượt. AI không hỏi lại mà tự đoán. C09 còn ghép 2 trang không liên quan nhau (trang 35 và trang 53) thành một câu trả lời trông rất tự tin. Câu trả lời vẫn có số trang và vẫn qua bước kiểm `_pages_cited`, vì cả 2 trang đều nằm trong kết quả tìm được. Như vậy bước kiểm của code chỉ bắt được trang bịa, không bắt được câu trả lời lệch ý. Để sửa nhóm lỗi này, mình chỉ đổi đúng 1 chỗ: thêm vào `SYSTEM` prompt quy tắc bắt buộc HỎI LẠI khi câu có từ chỉ trỏ ("đó / này / kia") tới thứ chưa gọi tên. Ví dụ trong prompt cố ý không lấy từ bộ câu thử. Lượt 2 cả C08 và C09 đều đạt (nhánh Q), tổng tăng từ 18/24 lên 21/24. Mình học được hai điều: (1) nhìn trace để gom lỗi thành nhóm rồi sửa đúng một nguyên nhân, thay vì vá từng câu; (2) prompt chỉ sửa được lỗi suy luận của model. C10 và C14 vẫn trượt vì `search_slides` chỉ so từ, không hiểu đồng nghĩa, nên phải sửa ở công cụ tìm kiếm (vd tìm theo nghĩa bằng embedding).
