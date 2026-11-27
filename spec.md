# AI SPEC — [Tên lát cắt] · Nhóm [tên nhóm] · Phòng [XXX] · Zone [X]

> Mốc nộp: §7 chốt chuẩn "đạt" tại **CP2 19:30 Thứ Sáu 27/11** · §0–§7 nộp **CP3 10:00 Thứ Bảy 28/11** · đủ §0–§10 **CP4 14:30 Thứ Bảy 28/11** · §10 changelog ghi tiếp đến **23:59 Thứ Bảy 28/11**.
> Đầu mỗi mục ghi bước guide (`02-guide.md` trong repo đề) chỉ cách điền. Mỗi mục ngắn, có số và nguồn; chi tiết để ở file được trỏ tới. Xoá dòng hướng dẫn trong ngoặc vuông khi điền xong.

Track: [ ] A · [ ] B · [ ] C · [ ] D · [ ] E — bài toán: [đề gợi ý trong file track, hoặc bài toán nhóm tự mở rộng] __
Data BTC cấp đã dùng (nếu có — không commit nguyên file): __

## §0. Hiện tại việc này diễn ra thế nào *(guide 1.1)*
- Luồng hiện tại của việc này, trong khoá hoặc trên app thật (3–5 bước; ảnh chụp từ tài khoản của mình, đã che thông tin):
- Công cụ / AI đang được dùng cho việc này (nếu có) + nguồn. Không kiểm được thì ghi "chưa kiểm":

## §1. Người dùng & bằng chứng *(guide 1.1, 1.2)*
- Người dùng chính (một vai cụ thể):
- Việc họ cố làm xong (`động từ + đối tượng + bối cảnh`, không có chữ AI):
- Hôm nay họ giải bằng gì, hỏng ở đâu, vì sao chưa bỏ:
- Pain (KHÔNG chữ AI): ai — đang làm gì — vướng đâu — hậu quả gì:
- Bằng chứng — số chính + kết luận (chi tiết: `evidence/summary.md`): đào data pre-class 05/11–25/11/2026 — **143/436 (32,8%)** học viên hỏi trợ giảng AI khi tự học trước buổi; **66/429 (15,4%)** bôi đen chữ trên slide để hỏi (433 lần, 92,8% thành câu hỏi thật); **46,9%** câu là hỏi nối; chỉ **29,9%** câu trả lời có dẫn mốc trong bài để tự kiểm. Khảo sát (nguồn chính): n = __ · gặp chỗ không hiểu __/__ (__%). Kết luận tạm: giả thuyết **phải đổi một phần** — nhu cầu hỏi có thật, nhưng chỉ 36,5% câu hỏi rơi vào 19h–6h, không chủ yếu "tối trước buổi".

## §2. Impact & quyết định chọn *(guide 1.3)*

> Quy mô: L3 hơn 700 học viên, chia L3A và L3B (`tracks/track-a-edtech.md`); data pre-class có 721 tài khoản level 3–4 → **L3B ≈ 360 người** *(tự ước tính: chia đôi 721)*. Mã M1–M9 là phép đếm ở `evidence/data-mining.md`.

| Hướng | Bao nhiêu người gặp | Bao nhiêu lần / tháng | Mỗi lần tốn gì | Impact / tháng | Làm kịp không | Chọn? |
|---|---|---|---|---|---|---|
| **H1 · Hỏi đáp trên slide LMS, trả lời kèm số trang** (A1) | 360 × 32,8% ≈ **118** người (M1) | **2,56** lần / người (M8) | **15 phút** tự đọc lan man / tra Google *(tự ước tính — thay bằng câu 6 khảo sát)* + nguy cơ hiểu lệch bài | 118 × 2,56 × 15 ≈ **4.530 phút ≈ 75 giờ** | Có — 1 công cụ tra slide + 1 lần gọi model, data slide nhóm tự có | **✓ Chọn** |
| H2 · Tóm tắt ý chính + lộ trình học trước buổi cho người bỏ dở | 360 × 55,2% ≈ **199** người mở bài nhưng chưa xong mục nào (M9) | 4 lần *(tự ước tính)* | 10 phút *(tự ước tính)* | 199 × 4 × 10 ≈ 7.960 phút ≈ 133 giờ | Khó đo trong hackathon (cần theo dõi người học nhiều ngày) | ✗ Loại |
| H3 · Trợ lý Discord trả lời lịch, phòng, logistics (A2) | 360 *(tự ước tính: mọi học viên L3B)* | 4 lần *(tự ước tính)* | 5 phút *(tự ước tính)* | 360 × 4 × 5 = 7.200 phút = 120 giờ | Có | ✗ Loại |
| H4 · Hỏi đáp dưới video pre-class | 143 người đã hỏi (M1) | 2,56 (M8) | đã có trợ giảng AI giải | ≈ 0 phần thêm | Có | ✗ Loại |

- **Impact / tháng** của hướng chọn = **118 người × 2,56 lần × 15 phút ≈ 4.530 phút ≈ 75 giờ học viên / tháng** — nguồn: 118 = 360 *(tự ước tính, chia đôi 721 tài khoản L3)* × 32,8% (M1, `evidence/data-mining.md`) · 2,56 = 1,79 ngày có hỏi / 21 ngày × 30 (M8) · 15 phút *(tự ước tính, chờ khảo sát câu 6 — trung điểm của "5–15" và "15–30 phút")*. 118 là **cận dưới**: chỉ đếm người đã chủ động hỏi trên pre-class, chưa đếm người gặp chỗ không hiểu mà không hỏi ai.
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
- [sản phẩm / tính năng gần giống]: một điều đáng học · một điều đáng né · mình khác gì

## §4. Thiết kế *(guide 2.2, 3.2)*
- **Lát cắt MỘT CÂU** (1 người dùng · 1 việc · 1 quyết định AI · 1 kết quả):
- Không làm (≥3 điều):
- **Sơ đồ** (ảnh / Mermaid / draw.io): [chèn ở đây]
- **Hình dạng:** [ ] workflow cố định · [ ] một agent · [ ] nhiều agent — 2 dòng lý do, và vì sao **không** chọn hình dạng phức tạp hơn:
- **AI dựa vào đâu** — mỗi công cụ (khớp `codebase/tools.py`):

  | Công cụ | Input | Output | Tác động ra ngoài? |
  |---|---|---|---|
  | `search_slides` (`codebase/tools.py`) — đọc `data/slides.csv` (28 đoạn viết lại từ slide Ngày 2) | `query` (str): câu hỏi nguyên văn của học viên | List tối đa 3 đoạn `{id, page, topic, content}` khớp nhất, xếp theo điểm giảm dần. Khớp = bỏ dấu + bỏ từ chức năng, đếm từ / cụm 2 từ trùng; giữ đoạn có điểm ≥ 2 **và** chứa ≥ 50% từ có nghĩa của câu hỏi, rồi chỉ giữ đoạn ≥ 50% điểm đoạn tốt nhất. Không đoạn nào đạt → `[]` → luồng nói "slide không đề cập" | **Không** — chỉ đọc file |

- **Mức tự động:** [ ] AI gợi ý, người quyết · [ ] AI tự làm khi chắc, chuyển người khi không · [ ] AI tự làm — lý do (sai thì ai chịu gì, sửa đắt hay rẻ):
- **Chỗ chặn rủi ro** (rủi ro lớn nhất của lát cắt bị chặn ở đâu, bằng gì):
- **Chỗ người duyệt** (việc AI không được tự làm):
- **Nguyên tắc thiết kế** (≥3, bắt buộc G10):

  | Nguyên tắc | Chỗ cụ thể trên sơ đồ / trong bản chạy thử |
  |---|---|
  | G10 — thu hẹp phạm vi khi không chắc |  |
  |  |  |
  |  |  |

- Phần nào còn giả (công cụ trả dữ liệu giả, model chế độ giả…) — ghi rõ, không giả làm thật:

## §5. Chỗ khó — 4 lớp + ≥6 kịch bản + 2 tấn công *(guide 2.3)*

| Kịch bản | Lớp (1–4) | Hành vi mong muốn (nói gì, hiện gì, cho làm gì tiếp) | Câu thử |
|---|---|---|---|
|  |  |  |  |
| *(tấn công)* |  |  |  |
| *(tấn công)* |  |  |  |

(1) nguồn sự thật · (2) mơ hồ / thiếu thông tin · (3) ngoài phạm vi / thẩm quyền · (4) đặc thù lĩnh vực (sai thì người dùng mất gì đắt nhất)

## §6. Bốn đường đi của trải nghiệm
- Mọi thứ suôn sẻ: · Không chắc (lớp 2): · Không có căn cứ (lớp 1): · Người dùng sửa:
- Bị đòi ngoài phạm vi (lớp 3): · Trường hợp đặc thù lĩnh vực (lớp 4):

## §7. Đánh giá & chuẩn "đạt" *(guide 2.4, 4.1)*
- Data card: `data/DATA_CARD.md` · bộ câu thử: `eval/benchmark.csv` — __ câu (thuong __ · kho __ · tu_choi __) · metric: `eval/metric_spec.yaml` (__ metric)
- **Chuẩn "đạt"** (chốt **trước 19:30 Thứ Sáu 27/11**, giữ nguyên đến 23:59 Thứ Bảy 28/11): "Đạt khi ≥ __% câu qua, và __"
- Kết quả: lượt 1 __/__ (__%) · lượt 2 __/__ (__%) — run ID: __ / __ → chi tiết `eval/report.md`, hồ sơ `eval/README.md`

## §8. Chi phí khi dùng thật *(guide 4.2)*
- Persona + giá: `cost/personas.yaml` · lượt mô phỏng: `cost/simulate-__.csv` (__ phiên)
- Chi phí / task thành công: __ (model __) · __ (model __)
- Chi phí / tháng ở quy mô thật: thấp __ · cơ sở __ · cao __ → chi tiết `cost/cost-estimate.md`
- So với impact / người / tháng (§2): đáng làm không, vì sao:

## §9. Rủi ro & an toàn
- Dữ liệu: đã ẩn danh gì, không thu gì, không đưa gì vào model gói miễn phí:
- AI **không được** làm gì kể cả khi người dùng yêu cầu:
- Ai có thể bị hại nếu AI sai, và nhóm chặn thế nào:

## §10. Phân công & changelog
- Phân công có tên (theo chặng, chia cặp — guide "Cách chia việc"): __
- Dùng AI vào việc gì (2–3 dòng; chi tiết `docs/ai-usage.md`):
- Nhật ký thay đổi — **mọi thay đổi sau CP2 19:30 Thứ Sáu 27/11 phải có dòng ở đây**:

**CP2 → CP4** (vd thu hẹp lát cắt, hỏi thêm người dùng, lần cải tiến trước lượt 2)

| Thời điểm | Đổi gì | Vì sao (trỏ về câu thử / lỗi / bằng chứng nào) |
|---|---|---|
|  |  |  |

**Sau CP4 (đến 23:59 Thứ Bảy 28/11)** (sửa theo góp ý — không sửa chuẩn "đạt", câu thử, số bằng chứng, kết quả các lượt đã chạy)

| Thời điểm | Đổi gì | Vì sao |
|---|---|---|
|  |  |  |
