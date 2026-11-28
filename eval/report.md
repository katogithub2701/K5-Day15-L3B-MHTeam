# Báo cáo đánh giá — lượt 1 → một cải tiến → lượt 2

> Điền ở guide bước 4.1. Lượt 1 trước **CP3 10:00 Thứ Bảy 28/11**, lượt 2 trước **CP4 14:30 Thứ Bảy 28/11**, cùng bộ câu thử, cùng cách chấm. Chấm ở rubric R5.
> Số lấy từ `python run.py score eval/run-1.csv` (và `run-2.csv`) sau khi điền cột `pass`. **Kết quả thấp ghi thật vẫn đủ điểm.**
> Không được: sửa chuẩn "đạt", bỏ câu thử trượt, sửa `expected` cho khớp output, sửa kết quả lượt đã chạy.

## 1. Kết quả

| Lượt | Run ID | Đạt / tổng | % | thuong | kho | tu_choi | So với chuẩn "đạt" |
|---|---|---|---|---|---|---|---|
| 1 | `run-1@20261128-080617` | 18/24 | 75% | 10/12 (83%) | 5/9 (56%) | 3/3 (100%) | **chưa** (75% < 80%; đạt điều kiện cứng 100% `tu_choi`) |
| 2 | | __/__ | | __/__ | __/__ | __/__ | đạt / chưa |

- Model lượt 1: `gemini-3.1-flash-lite` · lỗi kỹ thuật: `0/24`.
- Kết quả từng câu: `eval/run-1.csv`, `eval/run-2.csv`. Trace: `traces/run-1.jsonl`, `traces/run-2.jsonl`.

## 2. Lỗi lượt 1 — gom thành nhóm có tên

Tổng cộng **6/24 câu trượt** ở lượt 1 (`C08`, `C09`, `C10`, `C13`, `C14`, `C20`), gom thành **4 nhóm lỗi**:

| Nhóm lỗi | Số câu | Câu |
|---|---|---|
| Không hỏi lại khi câu mơ hồ (tự đoán và trả lời luôn) | 2 | C08, C09 |
| Tìm kiếm từ khoá bỏ sót / thiếu đoạn (`search_slides`) | 2 | C10, C14 |
| Từ chối cả câu khi chỉ một phần không có căn cứ | 1 | C13 |
| Trả lời thiếu ý khi câu hỏi gồm 2 khái niệm | 1 | C20 |

**Chi tiết 6 câu trượt lượt 1 (≥3 lỗi cụ thể):**

| Câu | Input | Output | Vì sao sai |
|---|---|---|---|
| **C08** *(kho)* | Cái ma trận đó dùng như thế nào? | Bạn hãy đặt các đề bài lên trục tác động và nỗ lực để nhận diện những việc dễ thắng nên làm ngay hoặc các "hố tiền" cần tránh. Lưu ý mỗi thành viên cần tự chấm điểm độc lập trước khi thảo luận để tránh hiệu ứng đám đông, đồng thời tính cả chi phí vận hành sau bàn giao vào cột nỗ lực. Xem trang 28. | Vi phạm metric `hoi_lai_khi_mo_ho`. Câu hỏi thiếu ngữ cảnh ("cái ma trận đó"), nhưng `search_slides` trả đoạn trang 28 (`N2-15`) nên AI đi vào nhánh `TRẢ LỜI` (nhánh O), tự đoán là Ma trận Tác động – Nỗ lực thay vì hỏi lại 1 câu để làm rõ. |
| **C09** *(kho)* | Trang đó nói gì về lỗi vậy? | Lỗi trong hệ thống AI thường xuất phát từ việc lệch pha lợi ích giữa người sử dụng và người chịu thiệt, hoặc từ các tình huống dữ liệu gốc bị gán nhãn sai. Bạn cần viết trước bộ tiêu chuẩn nghiệm thu và các giả thuyết lỗi để kiểm soát rủi ro trước khi bắt đầu code. Xem trang 35, 53. | Vi phạm metric `hoi_lai_khi_mo_ho`. Học viên không nêu số trang hay loại lỗi nào ("trang đó"), nhưng `search_slides` trả 2 đoạn trang 35 và 53 nên AI tự ghép nội dung 2 trang không liên quan (lệch pha lợi ích và acceptance test) thay vì hỏi lại để làm rõ ngữ cảnh. |
| **C10** *(kho)* | Nếu muốn đánh giá mô hình phân loại đơn hàng thì cứ lấy chỉ số F1 làm chuẩn duy nhất là ổn đúng không? | Slide Ngày 2 không đề cập nội dung này, nên mình không trả lời để tránh nói sai bài. Mình chỉ trả lời dựa trên slide Ngày 2 — bạn hỏi giảng viên hoặc TA trên Discord nhé. | Vi phạm `dung_so_trang` và kịch bản đặc thù lĩnh vực (lớp 4). Slide trang 42 (`N2-22`) nói rõ không nên dùng F1 đơn lẻ khi chi phí báo nhầm và bỏ sót khác nhau, nhưng `search_slides` lọc từ khoá quá chặt nên trả `[]` (`model_calls = 0`, nhánh N), khiến hệ thống báo "không đề cập" sai. |
| **C13** *(kho)* | Trong sơ đồ Kim cương đôi ở trang 20, màu sắc và mũi tên giữa các ô được vẽ cụ thể như thế nào? | Slide Ngày 2 không đề cập nội dung này, nên mình không trả lời để tránh nói sai bài. Mình chỉ trả lời dựa trên slide Ngày 2 — bạn hỏi giảng viên hoặc TA trên Discord nhé. | Trace cho thấy `search_slides` đã tìm đúng trang 20 (`N2-09`), nhưng vì dữ liệu tóm tắt không mô tả màu sắc/hình vẽ nên AI chọn `KHÔNG ĐỀ CẬP` cho cả câu (nhánh N2). Không bịa màu sắc, nhưng chưa trả lời phần chữ có căn cứ (2 kim cương, pha mở rộng/thu hẹp kèm trang 20) và chưa nói rõ giới hạn hình vẽ để học viên tự mở trang 20 xem. |
| **C14** *(thuong)* | Mình đọc slide thấy có phần Stakeholder map 5 vai rồi sang phần rủi ro lệch pha, hai phần này liên kết với nhau như thế nào? | Slide Ngày 2 không đề cập nội dung này, nên mình không trả lời để tránh nói sai bài. Mình chỉ trả lời dựa trên slide Ngày 2 — bạn hỏi giảng viên hoặc TA trên Discord nhé. | Cả hai phần đều có trong slide Ngày 2 (trang 34 `N2-18` và trang 35 `N2-19`), nhưng trace cho thấy `search_slides` chỉ trả 1 đoạn trang 34, bỏ sót trang 35. Thiếu căn cứ vế sau nên AI chọn `KHÔNG ĐỀ CẬP` (nhánh N2) và từ chối một câu `thuong`. |
| **C20** *(thuong)* | Mình đọc slide thấy nhắc đến Opportunity Solution Tree và Jobs to be Done mà chưa hiểu khi phỏng vấn khám phá nên hỏi người dùng như thế nào? | Khi phỏng vấn, bạn không nên hỏi người dùng muốn tính năng AI nào vì câu trả lời sẽ không phản ánh đúng nỗi đau thực tế. Thay vào đó, hãy áp dụng khung Jobs to be Done để hỏi về lần gần nhất họ gặp khó khăn trong công việc, giúp làm rõ quy trình thực tế mà họ đang thực hiện. Xem trang 31. | `search_slides` tìm đúng trang 31 (`N2-17`) và AI trả lời đúng ý không hỏi tính năng AI + JTBD kèm trang 31, nhưng bỏ sót ý **Opportunity Solution Tree** (đi tuần tự từ mục tiêu → cơ hội → giải pháp → kiểm chứng giả định) dù có ngay trong cùng đoạn `N2-17` và được yêu cầu trong `pass_criterion`. |

## 3. Một lần cải tiến

*(Chốt cùng cả nhóm lúc 10:00–10:30 sau CP3, cập nhật kết quả sau lượt 2)*

- Nhắm vào nhóm lỗi: __ — vì sao là nhóm **đau nhất với người dùng**: __
- Đã sửa gì (có thể vài thay đổi cùng nhắm nhóm lỗi đó): __
- Kết quả: nhóm lỗi đó __/__ → __/__ · tổng __% → __%
- Câu nào **tệ đi** sau khi sửa: __

## 4. Còn lại

- Lỗi chưa sửa + nguy hiểm thế nào: __
- Nếu có thêm 1 tuần: __
