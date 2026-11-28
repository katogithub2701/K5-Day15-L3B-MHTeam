# Báo cáo đánh giá — lượt 1 → một cải tiến → lượt 2

> Điền ở guide bước 4.1. Lượt 1 trước **CP3 10:00 Thứ Bảy 28/11**, lượt 2 trước **CP4 14:30 Thứ Bảy 28/11**, cùng bộ câu thử, cùng cách chấm. Chấm ở rubric R5.
> Số lấy từ `python run.py score eval/run-1.csv` (và `run-2.csv`) sau khi điền cột `pass`. **Kết quả thấp ghi thật vẫn đủ điểm.**
> Không được: sửa chuẩn "đạt", bỏ câu thử trượt, sửa `expected` cho khớp output, sửa kết quả lượt đã chạy.

## 1. Kết quả

| Lượt | Run ID | Đạt / tổng | % | thuong | kho | tu_choi | So với chuẩn "đạt" |
|---|---|---|---|---|---|---|---|
| 1 | `run-1@20261128-080617` | 18/24 | 75% | 10/12 (83%) | 5/9 (56%) | 3/3 (100%) | **chưa** (75% < 80%; đạt điều kiện cứng 100% `tu_choi`) |
| 2 | `run-2@20261128-101825` | 21/24 | 88% | 11/12 (92%) | 7/9 (78%) | 3/3 (100%) | **đạt** (88% ≥ 80%; đạt điều kiện cứng 100% `tu_choi`) |

- Model lượt 1 & lượt 2: `gemini-3.1-flash-lite` · lỗi kỹ thuật: lượt 1 `0/24`, lượt 2 `0/24`.
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

- Nhắm vào nhóm lỗi: **Không hỏi lại khi câu mơ hồ (tự đoán và trả lời luôn)** (`C08`, `C09` ở lượt 1) — vì sao là nhóm **đau nhất với người dùng**: khớp trực tiếp rủi ro số 1 đã nêu ở `spec.md` §4 (trả lời lệch bài, khiến học viên hiểu sai kiến thức trước khi lên lớp). Ở lượt 1, khi học viên hỏi mơ hồ (*"Trang đó nói gì về lỗi vậy?"*, `C09`), hệ thống tự ghép 2 trang không liên quan (trang 35 và 53) thành câu trả lời có vẻ chắc chắn; còn `C08` tự đoán một ma trận duy nhất rồi giải thích luôn.
- Đã sửa gì (một thay đổi tập trung cho nhóm lỗi này): sửa mục `HỎI LẠI` trong `SYSTEM` prompt ở `codebase/agent.py` (commit `a70f3e0`): **bắt buộc hỏi lại đúng 1 câu ngắn** khi câu hỏi dùng từ chỉ trỏ (*"đó"*, *"này"*, *"kia"*) trỏ tới thứ chưa được gọi tên đầy đủ hoặc ghi số trang trong chính câu hỏi — kể cả khi `search_slides` chỉ trả 1 đoạn; nếu khái niệm đã nêu rõ trong câu thì không hỏi lại. Ví dụ minh hoạ trong prompt viết tổng quát, không lấy từ bộ câu thử. Giữ nguyên `search_slides`, sơ đồ, model và cách chấm.
- Kết quả: nhóm lỗi đó **0/2 → 2/2** (`C08` và `C09` đều chuyển từ nhánh `TRẢ LỜI` sang nhánh `HỎI LẠI` đúng 1 câu ngắn để làm rõ ý học viên thay vì tự đoán và trả lời luôn như lượt 1; lưu ý nhỏ ở `C08`: câu hỏi lại có nêu sẵn *Ma trận Tác động và Nỗ lực* theo đoạn duy nhất tìm được, có thể tiếp tục tinh chỉnh để hỏi mở hơn) · tổng **18/24 (75%) → 21/24 (88%)** (**đạt chuẩn** ≥ 80%; `tu_choi` giữ 3/3 = 100%). *Lưu ý trung thực:* `C20` chuyển từ trượt (lượt 1) sang đạt (lượt 2) do biến thiên sinh câu của model (lượt 2 nêu đủ cả JTBD lẫn Opportunity Solution Tree từ cùng đoạn `N2-17`), không phải tác động trực tiếp của thay đổi mục `HỎI LẠI`.
- Câu nào **tệ đi** sau khi sửa: **không có (0/18 câu đạt ở lượt 1 bị trượt ở lượt 2)**; toàn bộ 18 câu đạt ở lượt 1 đều giữ nguyên đạt, không phát sinh tình trạng hỏi lại thừa ở các câu `thuong` đã rõ khái niệm.

## 4. Còn lại

- Lỗi chưa sửa + nguy hiểm thế nào (còn **3/24 câu trượt** ở lượt 2: `C10`, `C13`, `C14`):
  - **Tìm kiếm từ khoá bỏ sót / thiếu đoạn (`C10`, `C14` — 2 câu):** `search_slides` đòi câu dài trùng ≥ 2 từ hiếm nên bỏ sót trang 42 (`F1`) và trang 35 (`lệch pha`), khiến hệ thống trả lời "slide không đề cập" dù bài có dạy. Mức nguy hiểm: **trung bình** — không gây hiểu sai bài, nhưng làm giảm độ hữu ích và khiến học viên mất thời gian tự tìm lại hoặc hỏi ngoài.
  - **Từ chối cả câu khi chỉ thiếu chi tiết hình ảnh (`C13` — 1 câu):** `search_slides` tìm đúng trang 20 nhưng vì dữ liệu tóm tắt không mô tả màu sắc/mũi tên nên AI chọn `KHÔNG ĐỀ CẬP` toàn bộ thay vì trả lời phần chữ có căn cứ kèm trang 20 và nhắc học viên tự mở slide xem hình. Mức nguy hiểm: **thấp** — an toàn không bịa màu sắc, nhưng trải nghiệm chưa tối ưu.
  - **Giới hạn đã biết ngoài lát cắt 1 câu:** bản chạy thử chưa nhớ câu hỏi trước (trong khi 46,9% câu trên pre-class là hỏi nối, `evidence/data-mining.md` M4) và mới phủ 28 đoạn trọng tâm của slide Ngày 2.
- Nếu có thêm 1 tuần:
  1. Sửa `search_slides` trong `codebase/tools.py` (`MIN_RARE_HITS = 2 → 1` — đã thử nháp cứu được `C10`, `C14` mà vẫn giữ 0 dương tính giả trên câu ngoài slide — hoặc kết hợp tìm theo ngữ nghĩa) để xử lý triệt để nhóm lỗi bỏ sót đoạn.
  2. Tinh chỉnh thêm prompt cho ca hỏi về hình vẽ (`C13`: trả lời phần chữ có căn cứ kèm số trang và nói rõ giới hạn không đọc được hình) và làm câu hỏi lại khi chỉ có 1 đoạn căn cứ (`C08`) hỏi mở hơn về tên khái niệm / số trang.
  3. Bổ sung ngữ cảnh hội thoại 2–3 lượt gần nhất (phục vụ 46,9% câu hỏi nối) và mở rộng dữ liệu sang các buổi học khác của khoá AI20K.
