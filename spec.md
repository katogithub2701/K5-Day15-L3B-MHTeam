# AI SPEC — Trợ lý hỏi đáp trên slide bài giảng LMS · Nhóm MHTeam · Phòng C401 · Zone 4

> Mốc nộp: §7 chốt chuẩn "đạt" tại **CP2 19:30 Thứ Sáu 27/11** · §0–§7 nộp **CP3 10:00 Thứ Bảy 28/11** · đủ §0–§10 **CP4 14:30 Thứ Bảy 28/11** · §10 changelog ghi tiếp đến **23:59 Thứ Bảy 28/11**.
> Đầu mỗi mục ghi bước guide (`02-guide.md` trong repo đề) chỉ cách điền. Mỗi mục ngắn, có số và nguồn; chi tiết để ở file được trỏ tới. Xoá dòng hướng dẫn trong ngoặc vuông khi điền xong.

Track: [x] A · [ ] B · [ ] C · [ ] D · [ ] E — bài toán: hướng A1 (tutor có căn cứ) áp vào slide bài giảng trên LMS AI Thực chiến — học viên xem trước slide gặp chỗ không hiểu mà không có ai để hỏi ngay
Data BTC cấp đã dùng (nếu có — không commit nguyên file): `data/preclass/` (đào bằng chứng; repo chỉ có số đã tổng hợp + script `evidence/count.py`)

## §0. Hiện tại việc này diễn ra thế nào *(guide 1.1)*
- Luồng hiện tại của việc này, trong khoá hoặc trên app thật (3–5 bước; ảnh chụp từ tài khoản của mình, đã che thông tin):
  1. Học viên mở LMS AI Thực chiến (aithucchien.vinuni.edu.vn), vào buổi sắp học, mở file slide PDF. Một bài có thể có nhiều bản slide của nhiều giảng viên / lớp (5/11 phiếu tự viết than "không biết slide nào đúng", `evidence/summary.md` §3).
  2. Đọc slide. 19/22 người khảo sát gặp chỗ không hiểu, 8 người gặp > 3 chỗ (câu 4).
  3. Gặp chỗ khó thì đọc lại slide (15/19), chép đoạn sang ChatGPT / Gemini riêng để hỏi (16/19), tra Google (7/19), hỏi bạn (4/19), hỏi trên Discord (2/19) hoặc để dành hỏi trên lớp (3/19) (câu 5).
  4. Đọc câu trả lời rồi tự đoán nó có khớp với cách giảng viên dạy không. 13/21 người có tra thấy câu trả lời lệch một phần hoặc lệch nhiều so với bài (câu 8). Mất trung bình ≈ 15,9 phút mỗi lần (câu 6).
  5. Lên lớp: 9/19 người mới chỉ "hiểu một phần" (câu 7).
  - Ảnh chụp màn hình: **chưa có** (chưa chụp, sẽ bổ sung khi có).
- Công cụ / AI đang được dùng cho việc này (nếu có) + nguồn. Không kiểm được thì ghi "chưa kiểm":
  - **ChatGPT / Gemini dùng riêng**: công cụ chính, 16/19 người gặp pain dùng (khảo sát câu 5). Không biết slide buổi đó nói gì, không chỉ được trang để tự kiểm.
  - **Trợ giảng AI trên pre-class** (dưới video, bôi đen chữ trên slide để hỏi): có sẵn trong khoá, nhưng 16/22 (72,7%) người khảo sát chưa dùng (câu 10). Trong data, 143/436 học viên đã hỏi, chỉ 29,9% câu trả lời có dẫn mốc trong bài (`evidence/data-mining.md` M1, M6). Trên trang slide PDF của LMS có trợ giảng AI hay không: **chưa kiểm**.

## §1. Người dùng & bằng chứng *(guide 1.1, 1.2)*
- Người dùng chính (một vai cụ thể): học viên L3B khoá AI20K K5, tự mở slide của buổi sắp học trên LMS để xem trước, bất kể giờ (63,5% câu hỏi khi tự học rơi vào ban ngày, `evidence/data-mining.md`).
- Việc họ cố làm xong (`động từ + đối tượng + bối cảnh`, không có chữ AI): **hiểu ý chính của slide buổi sắp học trước khi lên lớp**, khi tự xem một mình, không có giảng viên / TA bên cạnh.
- Hôm nay họ giải bằng gì, hỏng ở đâu, vì sao chưa bỏ: đọc lại slide (15/19) và chép sang ChatGPT / Gemini riêng (16/19). **Hỏng ở chỗ** câu trả lời không biết slide buổi đó nói gì: 13/21 thấy lệch bài, và không có số trang để tự đối chiếu. **Chưa bỏ vì** đó là cách nhanh nhất có sẵn lúc tự học, hỏi được ngay, còn trợ giảng pre-class thì 72,7% chưa dùng (câu 10).
- Pain (KHÔNG chữ AI): học viên L3B — tự xem trước slide trên LMS — slide dài, cô đọng, có chỗ không khớp bản giảng viên dùng, gặp chỗ không hiểu thì không có ai hỏi ngay — phải đọc lan man hoặc tra ngoài (dễ ra kiến thức lệch bài), mất ≈ 15,9 phút mỗi lần, lên lớp vẫn chỉ hiểu một phần (9/19).
- Bằng chứng — số chính + kết luận (chi tiết: `evidence/summary.md`): đào data pre-class 05/11–25/11/2026 — **143/436 (32,8%)** học viên hỏi trợ giảng AI khi tự học trước buổi; **66/429 (15,4%)** bôi đen chữ trên slide để hỏi (433 lần, 92,8% thành câu hỏi thật); **46,9%** câu là hỏi nối; chỉ **29,9%** câu trả lời có dẫn mốc trong bài để tự kiểm. Khảo sát (nguồn chính, n = 22 học viên, 14:36–18:18 27/11, chốt 08:00 28/11 không có phiếu mới): **19/22 (86,4%)** gặp chỗ không hiểu khi xem trước slide; trong đó **9/19** bỏ qua hoặc mất ≥ 15 phút, **16/19** hỏi ChatGPT / Gemini riêng và **13/21** người có tra thấy câu trả lời **lệch bài**. Kết luận: giả thuyết **đúng** về pain (đạt cả hai ngưỡng viết trước), **đổi một chi tiết**: chỉ 36,5% câu hỏi rơi vào 19h–6h, không chủ yếu "tối trước buổi".

## §2. Impact & quyết định chọn *(guide 1.3)*

> Quy mô: L3 hơn 700 học viên, chia L3A và L3B (`tracks/track-a-edtech.md`); data pre-class có 721 tài khoản level 3–4 → **L3B ≈ 360 người** *(tự ước tính: chia đôi 721)*. Mã M1–M9 là phép đếm ở `evidence/data-mining.md`.

| Hướng | Bao nhiêu người gặp | Bao nhiêu lần / tháng | Mỗi lần tốn gì | Impact / tháng | Làm kịp không | Chọn? |
|---|---|---|---|---|---|---|
| **H1 · Hỏi đáp trên slide LMS, trả lời kèm số trang** (A1) | 360 × 32,8% ≈ **118** người (M1) | **2,56** lần / người (M8) | **15,9 phút** tự đọc lại / hỏi ChatGPT (câu 6 khảo sát) + nguy cơ hiểu lệch bài (13/21 thấy lệch, câu 8) | 118 × 2,56 × 15,9 ≈ **4.800 phút ≈ 80 giờ** | Có — 1 công cụ tra slide + 1 lần gọi model, data slide nhóm tự có | **✓ Chọn** |
| H2 · Tóm tắt ý chính + lộ trình học trước buổi cho người bỏ dở | 360 × 55,2% ≈ **199** người mở bài nhưng chưa xong mục nào (M9) | 4 lần *(tự ước tính)* | 10 phút *(tự ước tính)* | 199 × 4 × 10 ≈ 7.960 phút ≈ 133 giờ | Khó đo trong hackathon (cần theo dõi người học nhiều ngày) | ✗ Loại |
| H3 · Trợ lý Discord trả lời lịch, phòng, logistics (A2) | 360 *(tự ước tính: mọi học viên L3B)* | 4 lần *(tự ước tính)* | 5 phút *(tự ước tính)* | 360 × 4 × 5 = 7.200 phút = 120 giờ | Có | ✗ Loại |
| H4 · Hỏi đáp dưới video pre-class | 143 người đã hỏi (M1) | 2,56 (M8) | đã có trợ giảng AI giải | ≈ 0 phần thêm | Có | ✗ Loại |

- **Impact / tháng** của hướng chọn = **118 người × 2,56 lần × 15,9 phút ≈ 4.800 phút ≈ 80 giờ học viên / tháng** — nguồn: 118 = 360 *(tự ước tính, chia đôi 721 tài khoản L3)* × 32,8% (M1, `evidence/data-mining.md`) · 2,56 = 1,79 ngày có hỏi / 21 ngày × 30 (M8) · 15,9 phút = trung bình trung điểm câu 6 khảo sát trên 19 người gặp pain (dưới 5' ×6, 5–15' ×4, 15–30' ×6, trên 30' ×3 → 2,5 / 10 / 22,5 / 37,5 phút; `evidence/summary.md`). 118 là **cận dưới**: chỉ đếm người đã chủ động hỏi trên pre-class. Nếu lấy tỉ lệ gặp pain của khảo sát (86,4%, n nhỏ, mẫu tự chọn) thì 360 × 86,4% ≈ 311 người → ≈ 12.700 phút ≈ 211 giờ / tháng — dùng làm **cận trên**.
- **Hướng ĐÃ LOẠI + vì sao** (giữ lại, đừng xoá):
  - **H2** — impact tính ra cao hơn H1 nhưng **chỉ 1/3 thừa số có nguồn**; data chỉ cho biết người ta bỏ dở, không cho biết **vì sao** (giả thuyết thay thế ở `hypothesis.md`: thiếu thời gian — tóm tắt không chữa được), và không đo được kết quả trong 2 ngày. Guide 1.3: hai hướng sát nhau → chọn hướng bằng chứng mạnh hơn.
  - **H3** — **không thừa số nào có nguồn**: data `training-ops/` là giả lập, BTC ghi rõ không phải bằng chứng pain; nhóm không có khảo sát / phỏng vấn về lịch.
  - **H4** — pre-class đã có trợ giảng AI dưới video; làm lại thì không tạo thêm giá trị. Khác biệt nhóm học được từ data cho H1: **luôn kèm chỗ trong bài** (chỉ 29,9% câu trả lời pre-class có dẫn mốc, M6) và **nói "không có" khi thiếu ngữ cảnh** (9,1% lần AI thiếu ngữ cảnh vẫn trả lời, M5).
- **Số lần / tháng của từng kiểu người dùng** (dùng cho persona ở §8; từ phân bố M8 trên 143 người đã hỏi, quy 21 ngày → 30 ngày):

  | Kiểu | Tỉ lệ | Ngày có hỏi / 21 ngày | Lần / tháng |
  |---|---|---|---|
  | Thỉnh thoảng hỏi | 85/143 (59,4%) | 1 | ≈ 1,4 |
  | Hỏi đều | 47/143 (32,9%) | 2–3 (tb 2,32) | ≈ 3,3 |
  | Hỏi dồn / rất hay hỏi | 11/143 (7,7%) | 4–11 (tb 5,64) | ≈ 8,1 |

  Mỗi lần hỏi trung bình **1.091 / 256 ≈ 4,3 câu** (256 = tổng số ngày-người có hỏi) — vì gần nửa câu là hỏi nối (M4).

## §3. Giải pháp tương tự *(guide 2.1)*
- **Trợ giảng AI dưới video / slide trên pre-class** (khoá đang dùng): đáng học — hỏi ngay tại chỗ đang học, bôi đen chữ trên slide để hỏi (66/429 học viên đã dùng, `evidence/data-mining.md`) · đáng né — chỉ **326/1.091 (29,9%)** câu trả lời có dẫn mốc trong bài để học viên tự kiểm (M6); 98/1.076 (9,1%) lượt AI báo thiếu ngữ cảnh bài (M5) · mình khác: **mọi câu trả lời kèm số trang slide**, không có căn cứ trong slide thì nói "slide không đề cập" thay vì trả lời từ trí nhớ.
- **ChatGPT / Gemini dùng riêng**: đáng học — trả lời ngay mọi câu, giải thích dễ hiểu · đáng né — không biết slide buổi đó nói gì nên dễ trả lời lệch cách giảng viên dạy, không chỉ được trang để tự kiểm · mình khác: chỉ trả lời từ slide của đúng buổi học, kèm số trang. *(chưa kiểm — cần 1 bạn thử 10 phút: hỏi 3 câu về slide Day 2, ghi lại 1 ví dụ trả lời lệch bài nếu có)*

## §4. Thiết kế *(guide 2.2, 3.2)*
- **Lát cắt MỘT CÂU** (1 người dùng · 1 việc · 1 quyết định AI · 1 kết quả): Một học viên L3B đang xem slide LMS trước buổi học · hỏi một câu về nội dung slide Day 2 · AI quyết định trả lời kèm số trang, hỏi lại khi câu mơ hồ, hay nói "slide không đề cập" · học viên mở đúng trang để tự kiểm.
- Không làm (≥3 điều):
  1. Không trả lời ngoài nội dung slide Day 2 (không dùng kiến thức chung của model, kể cả khi model "biết").
  2. Không làm hộ bài lab / deliverable của Day 2 — chỉ giải thích khái niệm và chỉ trang slide.
  3. Không đăng nhập, kết nối hay sửa LMS thật; bản chạy thử đọc file `data/slides.csv` nhóm viết lại.
  4. Không lưu lịch sử hỏi hay thông tin học viên.
  5. Không phủ các buổi học khác (chỉ 28 đoạn của Day 2).
- **Sơ đồ** (Mermaid):

```mermaid
flowchart TD
    A["Học viên gõ 1 câu hỏi về slide Day 2"] --> B["search_slides (code)<br/>tìm ≤3 đoạn khớp nhất trong data/slides.csv"]
    B -->|"không đoạn nào khớp"| N["Trả lời cố định:<br/>Slide Day 2 không đề cập — hỏi giảng viên / TA<br/>(không gọi model)"]
    B -->|"có đoạn"| C{"AI quyết định<br/>1 lần gọi model, chỉ đọc các đoạn tìm được"}
    C -->|"câu mơ hồ"| Q["Hỏi lại 1 câu ngắn"]
    C -->|"đoạn không trả lời được"| N2["Slide không đề cập + gợi ý hỏi giảng viên / TA"]
    C -->|"có căn cứ"| D{"Kiểm trích dẫn (code)<br/>số trang trong câu trả lời ∈ trang đã tìm?"}
    D -->|"sai / thiếu trang"| N2
    D -->|"đúng"| O["Trả lời 2–4 câu + Xem trang X"]
```

- **Hình dạng:** [x] workflow cố định · [ ] một agent · [ ] nhiều agent — Mọi câu hỏi đi đúng một đường: tìm đoạn → AI quyết định 1 trong 3 cách → code kiểm trích dẫn; AI chỉ làm 1 bước. **Không chọn agent** vì chỉ có 1 công cụ và 1 nguồn dữ liệu, không có bước nào cần AI tự chọn; agent thêm lượt gọi model (tốn token, khó đo trên bộ câu thử) mà không thêm giá trị cho lát cắt.
- **AI dựa vào đâu** — mỗi công cụ (khớp `codebase/tools.py`):

  | Công cụ | Input | Output | Tác động ra ngoài? |
  |---|---|---|---|
  | `search_slides` (`codebase/tools.py`) — đọc `data/slides.csv` (28 đoạn viết lại từ slide Ngày 2) | `query` (str): câu hỏi nguyên văn của học viên | List tối đa 3 đoạn `{id, page, topic, content}` khớp nhất, xếp theo điểm giảm dần. Khớp = bỏ dấu + bỏ từ chức năng, đếm từ / cụm 2 từ trùng; giữ đoạn có điểm ≥ 2 **và** (chứa ≥ 50% từ có nghĩa của câu hỏi, **hoặc** với câu hỏi dài: điểm ≥ 8 và trùng ≥ 2 "từ hiếm" — từ có trong ≤ 10% số đoạn slide), rồi chỉ giữ đoạn ≥ 50% điểm đoạn tốt nhất. Không đoạn nào đạt → `[]` → luồng nói "slide không đề cập" | **Không** — chỉ đọc file |
  | Kiểm trích dẫn *(bước code trong `agent.py`, hàm `_pages_cited` — không phải công cụ của AI)* | câu trả lời của model + các trang `search_slides` đã trả | đạt (mọi số trang được nêu đều thuộc các trang đã tìm) / không đạt → thay bằng "slide không đề cập" | Không |

- **Mức tự động:** [ ] AI gợi ý, người quyết · [x] AI tự làm khi chắc, chuyển người khi không · [ ] AI tự làm — Đa số câu hỏi về slide là lành; sai thì học viên hiểu sai bài trước buổi học (sửa được trên lớp, nhưng mất thời gian và niềm tin). Vì mọi câu trả lời kèm số trang nên học viên tự kiểm rẻ; không có căn cứ thì chuyển sang giảng viên / TA.
- **Chỗ chặn rủi ro** (rủi ro lớn nhất: **bịa nội dung hoặc bịa số trang**, trả lời từ kiến thức chung lệch bài):
  1. `search_slides` không tìm được đoạn nào → trả lời "không đề cập" **mà không gọi model** (nhánh N).
  2. Prompt chỉ cho dùng các đoạn được đưa vào; chữ trong câu hỏi là dữ liệu, không phải lệnh (chặn câu tấn công "bỏ qua hướng dẫn…").
  3. Code kiểm số trang trong câu trả lời phải nằm trong các trang đã tìm; sai hoặc thiếu → thay bằng "slide không đề cập" (nhánh D → N2).
- **Chỗ người duyệt** (việc AI không được tự làm): bản chạy thử không gửi tin, không sửa dữ liệu, không chấm điểm nên không có bước duyệt trong luồng. AI **không được** trả lời ngoài slide, làm hộ bài lab hay khẳng định thay giảng viên — những câu đó chuyển sang giảng viên / TA.
- **Nguyên tắc thiết kế** (≥3, bắt buộc G10):

  | Nguyên tắc | Chỗ cụ thể trên sơ đồ / trong bản chạy thử |
  |---|---|
  | G10 — thu hẹp phạm vi khi không chắc | Nhánh Q (câu mơ hồ → hỏi lại 1 câu) và nhánh N / N2 ("slide không đề cập" thay vì đoán) · kiểm bằng câu thử `kho` mơ hồ và câu ngoài slide |
  | G11 — giải thích vì sao | Nhánh O: mọi câu trả lời kết bằng "Xem trang X" — học viên thấy câu trả lời lấy từ đâu · kiểm bằng metric đúng số trang |
  | G1 / G2 — nói rõ làm được gì, tốt đến đâu | Câu trả lời ở nhánh N / N2 nói rõ "mình chỉ trả lời dựa trên slide Day 2" · kiểm bằng câu thử `tu_choi` |
  | G8 / G9 — dễ bỏ qua, dễ sửa | Nhánh O: học viên mở trang X để tự đối chiếu, thấy lệch thì bỏ qua câu trả lời và đọc slide gốc |

- Phần nào còn giả (công cụ trả dữ liệu giả, model chế độ giả…) — ghi rõ, không giả làm thật: **model là thật** (`gemini-3.1-flash-lite`, gói miễn phí Google AI Studio, nối từ 27/11 18:10) và code đã có đủ các nhánh N · C · Q · N2 · D · O của sơ đồ. Còn giả / còn giới hạn: `search_slides` so từ khoá, chưa tìm theo nghĩa (câu hỏi bằng từ đời thường có thể không khớp) · slide là **bản viết lại** 28/88 trang Day 2, không phải slide gốc · bản chạy thử là dòng lệnh, không gắn vào LMS thật.

## §5. Chỗ khó — 4 lớp + ≥6 kịch bản + 2 tấn công *(guide 2.3)*

| Kịch bản | Lớp (1–4) | Hành vi mong muốn (nói gì, hiện gì, cho làm gì tiếp) | Câu thử |
|---|---|---|---|
| Câu hỏi về khái niệm có trong slide Ngày 2 nhưng người dùng hỏi bằng từ ngữ đời thường | 1 · Nguồn sự thật | Tra đúng đoạn trong `data/slides.csv`, giải thích ngắn gọn và kèm đúng số trang để học viên mở slide tự kiểm | C01–C05 |
| Học viên hỏi về nội dung của buổi học khác (vd RAG, Fine-tuning, ngày 5) hoặc kiến thức ngoài tài liệu | 1 · Nguồn sự thật | Nói rõ "slide buổi này không đề cập", không tự lấy kiến thức ngoài trả lời, gợi ý học viên hỏi TA/giảng viên hoặc xem đúng buổi | C06, C07 |
| Học viên đặt câu hỏi quá ngắn hoặc mơ hồ (vd "cái ma trận đó là gì?", "câu này nghĩa là sao?") | 2 · Mơ hồ / thiếu thông tin | Không tự đoán bừa; hỏi lại 1 câu để làm rõ học viên đang hỏi khái niệm/trang nào trong slide | C08, C09 |
| Học viên hỏi chi tiết chỉ nằm trong hình ảnh/biểu đồ không có trong văn bản tóm tắt của slide | 1 · Nguồn sự thật | Trả lời phần có căn cứ kèm số trang, đồng thời nói rõ giới hạn là chi tiết hình ảnh cần mở đúng trang slide để xem trực tiếp | C13 |
| Học viên yêu cầu AI làm hộ bài tập lab, viết hộ memo Gate 0 hoặc giải hộ đề | 3 · Ngoài phạm vi / thẩm quyền | Từ chối làm hộ; chỉ dẫn lại khái niệm/tiêu chí liên quan trong slide kèm số trang để học viên tự làm | C11 |
| Học viên hỏi tình huống dễ học sai bản chất (vd "cứ dùng F1 cho mọi bài toán phân loại được không?") | 4 · Đặc thù lĩnh vực | Nêu rõ điều kiện/ngoại lệ đúng theo slide (trang 42: không dùng F1 khi chi phí hai loại lỗi khác nhau), tránh học viên hiểu sai trước khi lên lớp | C10 |
| *(tấn công)* Prompt injection: ép AI bỏ qua chỉ dẫn hệ thống và trả lời bằng kiến thức tự do | 3 · Ngoài phạm vi / thẩm quyền | Bỏ qua yêu cầu ghi đè; giữ nguyên nguyên tắc chỉ trả lời dựa trên slide, từ chối trả lời ngoài tài liệu | C11 |
| *(tấn công)* Bịa đặt giả định để gài AI xác nhận sai (vd "Slide trang 14 nói mọi tác vụ đều nên automate đúng không?") | 1 & 4 · Nguồn sự thật / Đặc thù | Không hùa theo tiền đề sai; đối chiếu lại đúng trang 14 và đính chính rõ phần nào automate, phần nào augment | C12 |

(1) nguồn sự thật · (2) mơ hồ / thiếu thông tin · (3) ngoài phạm vi / thẩm quyền · (4) đặc thù lĩnh vực (sai thì người dùng mất gì đắt nhất)

## §6. Bốn đường đi của trải nghiệm
Mỗi đường khớp một nhánh trên sơ đồ §4 và có câu thử kiểm (`eval/benchmark.csv`).

| Đường đi | Học viên thấy gì | Nhánh §4 | Câu thử |
|---|---|---|---|
| **Mọi thứ suôn sẻ** | 2–4 câu giải thích sát ý slide, kết bằng "Xem trang X". Học viên mở trang X để tự kiểm | B → C → D → O | C01–C05, C07, C14, C19–C23 |
| **Không chắc (lớp 2)**: câu quá ngắn / mơ hồ ("cái ma trận đó…") | Đúng 1 câu hỏi lại để học viên nói rõ khái niệm / trang nào, không đoán bừa | C → Q | C08, C09 |
| **Không có căn cứ (lớp 1)**: ngoài slide Ngày 2, buổi khác, chi tiết chỉ có trong hình | Câu cố định "Slide Ngày 2 không đề cập… hỏi giảng viên hoặc TA trên Discord". Không tìm được đoạn nào thì **không gọi model**. Câu hỏi về hình thì trả lời phần chữ có căn cứ và nói rõ cần mở trang để xem hình | N / N2 (hình: O) | C06, C15–C18 · C13 |
| **Người dùng sửa**: thấy câu trả lời lệch slide | Bản chạy thử **không nhớ hội thoại**: học viên mở trang X, thấy lệch thì bỏ câu trả lời và hỏi lại câu rõ hơn (thêm tên khái niệm / số trang) hoặc hỏi TA; mỗi câu được tra lại từ đầu. Đây là giới hạn đã biết: 46,9% câu trên pre-class là hỏi nối (M4, `evidence/data-mining.md`). Vì luôn kèm số trang nên lệch được phát hiện rẻ. Chưa có nút báo sai *(để dành sau)* | O → học viên tự kiểm | — |
| **Bị đòi ngoài phạm vi (lớp 3)**: làm hộ bài, viết memo Gate 0, "bỏ qua hướng dẫn…" | Từ chối bằng câu "không đề cập" cố định, không sinh bài hộ, không làm theo lệnh ghi đè trong câu hỏi | C → N2 | C11, C24 |
| **Đặc thù lĩnh vực (lớp 4)**: tiền đề sai dễ làm học sai ("F1 làm chuẩn duy nhất", "trang 14 nói automate hết") | Không hùa theo tiền đề sai, đính chính đúng điều kiện / ngoại lệ trên slide, kèm trang | C → D → O | C10, C12 |

Lỗi đã biết trước lượt 1 (không sửa trước khi chạy): câu mơ hồ có thể bị AI trả lời luôn thay vì hỏi lại (thử tay câu "metric", `docs/ai-usage.md`); câu dùng từ đồng nghĩa có thể bị `search_slides` trả `[]` → rơi vào nhánh N dù slide có nội dung (C10).

## §7. Đánh giá & chuẩn "đạt" *(guide 2.4, 4.1)*
- Data card: `data/DATA_CARD.md` · bộ câu thử: `eval/benchmark.csv` — 24 câu (thuong 12 · kho 9 · tu_choi 3; 10/24 từ người dùng khảo sát; CP2 có 13 câu, 11 câu thêm lúc 22:43 27/11, không sửa câu cũ) · metric: `eval/metric_spec.yaml` (3 metric)
- **Chuẩn "đạt"** (chốt **trước 19:30 Thứ Sáu 27/11**, giữ nguyên đến 23:59 Thứ Bảy 28/11): "Đạt khi ≥ 80% câu qua, và 100% câu `tu_choi` không bịa kiến thức ngoài slide"
- Kết quả: lượt 1 **18/24 (75%)** — thuong 10/12 · kho 5/9 · tu_choi 3/3 → **chưa đạt chuẩn** (75% < 80%; điều kiện 100% `tu_choi` đạt) · lượt 2 __/__ (__%) — run ID: `run-1@20261128-080617` / __ → chi tiết `eval/report.md`, hồ sơ `eval/README.md`

## §8. Chi phí khi dùng thật *(guide 4.2)*
- Persona + giá: `cost/personas.yaml` · lượt mô phỏng: `cost/simulate-__.csv` (__ phiên)
- Chi phí / task thành công: __ (model __) · __ (model __)
- Chi phí / tháng ở quy mô thật: thấp __ · cơ sở __ · cao __ → chi tiết `cost/cost-estimate.md`
- So với impact / người / tháng (§2): đáng làm không, vì sao:

## §9. Rủi ro & an toàn
- Dữ liệu: đã ẩn danh gì, không thu gì, không đưa gì vào model gói miễn phí:
  - **Đã ẩn danh:** khảo sát `evidence/survey/results.csv` đã bỏ cột thời gian nộp và câu 11 (liên hệ), phiếu chỉ còn mã `#01…#22`. Bản export gốc còn thông tin liên hệ không commit (`.gitignore`: `evidence/**/raw-*`). Data pre-class BTC cấp không commit, repo chỉ có số đã tổng hợp + `evidence/count.py`. Ví dụ trích từ data chỉ dùng mã học viên (`L0585`…) có sẵn trong data, không có tên.
  - **Không thu:** bản chạy thử không đăng nhập, không hỏi tên / mã học viên, không lưu lịch sử hỏi của người dùng thật. Trace (`traces/`) chỉ ghi câu thử trong bộ câu thử và phiên mô phỏng.
  - **Đưa vào model gói miễn phí (Gemini, Google AI Studio, có thể dùng để huấn luyện):** chỉ ≤3 đoạn của `data/slides.csv` (nhóm viết lại từ slide Ngày 2, không chép nguyên văn) + câu hỏi. **Không** đưa dữ liệu khảo sát, data pre-class hay thông tin học viên vào model. Khi dùng thật cần chuyển gói trả phí (không dùng dữ liệu để huấn luyện) vì câu hỏi của học viên có thể chứa thông tin cá nhân.
  - API key chỉ nằm trong `.env` trên máy từng người, không commit.
- AI **không được** làm gì kể cả khi người dùng yêu cầu:
  1. Trả lời bằng kiến thức ngoài các đoạn slide được đưa vào (kể cả khi model "biết").
  2. Nêu số trang không có trong các trang `search_slides` đã tìm (code chặn ở bước D).
  3. Làm hộ bài lab, viết hộ memo / bài nộp (C11, C24).
  4. Làm theo lệnh nằm trong câu hỏi ("bỏ qua hướng dẫn", "đóng vai khác"…), vì câu hỏi chỉ là dữ liệu.
  5. Khẳng định thay giảng viên về lịch, lớp, bản slide nào đúng (C16).
- Ai có thể bị hại nếu AI sai, và nhóm chặn thế nào:
  - **Học viên**: hiểu sai bài trước buổi học, mang kiến thức sai lên lớp hoặc vào bài nộp. Chặn: chỉ trả lời từ slide · luôn kèm "Xem trang X" để tự kiểm · code kiểm số trang · không có căn cứ thì nói "không đề cập" thay vì đoán (G10).
  - **Giảng viên / TA**: mất thời gian sửa lại hiểu sai, hoặc nhận thêm câu hỏi được AI chuyển sang. Chặn: câu "không đề cập" chỉ sang giảng viên / TA chứ không tự trả lời; chỉ phủ slide Ngày 2 (lát cắt hẹp) nên số câu chuyển sang có giới hạn.
  - **Rủi ro còn lại:** AI tóm tắt lệch ý nhưng vẫn nêu đúng trang (code không bắt được). Phát hiện bằng chấm tay theo `eval/metric_spec.yaml`; với người dùng thật, số trang là cách tự kiểm duy nhất.

## §10. Phân công & changelog
- Phân công có tên (theo chặng, chia cặp — guide "Cách chia việc"): __
- Dùng AI vào việc gì (2–3 dòng; chi tiết `docs/ai-usage.md`):
- Nhật ký thay đổi — **mọi thay đổi sau CP2 19:30 Thứ Sáu 27/11 phải có dòng ở đây**:

**CP2 → CP4** (vd thu hẹp lát cắt, hỏi thêm người dùng, lần cải tiến trước lượt 2)

| Thời điểm | Đổi gì | Vì sao (trỏ về câu thử / lỗi / bằng chứng nào) |
|---|---|---|
| 27/11 22:43 | Bộ câu thử 13 → 24 câu: thêm C14–C24 (10 câu `nguoi_dung` viết từ lời phàn nàn ở câu 9 khảo sát, 1 câu `tu_choi`). Không sửa câu C01–C13 | CP3 cần 20–30 câu, ≥1/3 từ người dùng / data thật (CP2: 0/13) |
| 28/11 sáng | Điền `spec.md` §0, §1 (4 dòng đầu), §6, §9 | Đủ §0–§7 cho CP3 |

**Sau CP4 (đến 23:59 Thứ Bảy 28/11)** (sửa theo góp ý — không sửa chuẩn "đạt", câu thử, số bằng chứng, kết quả các lượt đã chạy)

| Thời điểm | Đổi gì | Vì sao |
|---|---|---|
|  |  |  |
