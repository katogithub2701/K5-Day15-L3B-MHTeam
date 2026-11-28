# Chi phí khi dùng thật

> Guide bước 4.2 · rubric R6 · nộp CP4 14:30 Thứ Bảy 28/11. Người làm: Thành.
> Số **không điền tay**: `cost/personas.yaml` → `python run.py simulate --rate-from eval/run-2.csv --wait 4` → chép bảng trong `cost/simulate-1-summary.md` vào mục 2.
> Lúc build dùng gói miễn phí (Google AI Studio) nhưng ở đây tính theo **giá gói trả phí** — đây là chi phí cho lúc đưa vào dùng thật.

## 1. Đầu vào

- **Persona** (`cost/personas.yaml`): 3 kiểu, 4 lượt hỏi / phiên. Nguồn: phân bố M8 trên 143 người đã hỏi ở pre-class (`spec.md` §2, `evidence/data-mining.md`). Lượt hỏi / phiên ≈ 4,3 câu (M4), làm tròn 4 *(tự ước tính: chưa tách theo kiểu)*.

  | Persona | Tỉ lệ | Phiên / người / tháng | Lượt hỏi / phiên |
  |---|---|---|---|
  | `thinh_thoang_hoi` | 85/143 (59,4%) | 1,4 | 4 |
  | `hoi_deu` | 47/143 (32,9%) | 3,3 | 4 |
  | `hoi_don` | 11/143 (7,7%) | 8,1 | 4 |

- **Số người dùng thật**, 3 kịch bản:

  | Kịch bản | Người / tháng | Cách tính · nguồn |
  |---|---|---|
  | Thấp | **118** | L3B ≈ 360 *(tự ước tính: chia đôi 721 tài khoản L3 trong data pre-class)* × 32,8% đã chủ động hỏi trợ giảng AI (M1). Trùng số người ở `spec.md` §2 |
  | Cơ sở | **236** | 721 tài khoản L3 × 32,8% (M1) |
  | Cao | **864** | Cả khoá ≈ 1.000 học viên (README hackathon) × 86,4% gặp chỗ không hiểu (khảo sát câu 4, 19/22, n nhỏ, mẫu tự chọn) |

- **Giá** (USD / 1 triệu token, gói Paid · Standard, text). Model có lịch tăng giá thì dùng **giá sau khi tăng**, theo `further-reading/model-prices.md` của repo đề. Đối chiếu https://ai.google.dev/gemini-api/docs/pricing, **xem ngày 28/11/2026**.

  | Mức | Model | Vào | Ra | Ghi chú |
  |---|---|---:|---:|---|
  | Rẻ | `gemini-3.1-flash-lite` | 0,25 | 1,50 | model đang chạy trong bản chạy thử |
  | Giữa | `gemini-3.8-flash` | 1,50 | 7,50 | giá từ 01/01/2027 (đến 31/12/2026 là 0,75 / 3,75) |
  | Mạnh | `gemini-4-argon` | 4,00 | 20,00 | giá từ 01/12/2026 (đến 30/11/2026 là 2 / 10), không có gói miễn phí |

- **Tỉ lệ đạt** dùng để tính: **21/24 (88%)**, lượt `run-2@20261128-101825` (lượt 2, sau cải tiến hỏi lại).
- **Đo token trên model `gemini-3.1-flash-lite`**, tính giá cho `gemini-3.1-flash-lite`, `gemini-3.8-flash` và `gemini-4-argon`.
  - Giới hạn: tỉ lệ đạt chỉ đo thật trên `gemini-3.1-flash-lite`. Hai model kia dùng **cùng tỉ lệ đạt đó** *(giả định, chưa chạy bộ câu thử trên hai model này)*. Model khác có bộ tách token khác, nên số token thật có thể lệch.

## 2. Kết quả mô phỏng

Lượt mô phỏng: `cost/simulate-1.csv` · run ID `simulate-1@20261128-112922` · 50 phiên · seed 42 · phiên lỗi **3/50** (S007, S008, S009: Gemini gói miễn phí trả HTTP 503 "high demand" / hết thời gian chờ — lỗi kỹ thuật, khung không tính vào trung bình → trung bình trên **47 phiên**)
Bản tóm tắt máy sinh: `cost/simulate-1-summary.md` · trace: `traces/simulate-1.jsonl`

**Token đo được mỗi phiên** (chép từ summary):

| Persona | Số phiên mô phỏng | Lượt hỏi / phiên | Token vào / phiên | Token ra / phiên | Gọi model / phiên | Gọi công cụ / phiên |
|---|---:|---:|---:|---:|---:|---:|
| thinh_thoang_hoi | 31 | 4 | 2343 | 235 | 3.4 | 4.0 |
| hoi_deu | 14 | 4 | 2154 | 222 | 3.1 | 4.0 |
| hoi_don | 2 | 4 | 2546 | 229 | 3.5 | 4.0 |

Số phiên theo persona (31 / 14 / 2, không tính 3 phiên lỗi) là do bốc ngẫu nhiên theo tỉ lệ 59,4% / 32,9% / 7,7%. `hoi_don` chỉ có 2 phiên nên trung bình của kiểu này kém chắc — nhưng token / phiên của 3 kiểu sát nhau (2.154–2.546 vào), vì cả 3 cùng 4 lượt hỏi / phiên.

**Chi phí** (chép từ summary):

| Model | Chi phí / phiên | Chi phí / task thành công | Chi phí / câu hỏi đạt | / tháng · thấp (118) | / tháng · cơ sở (236) | / tháng · cao (864) | / người / tháng (cơ sở) |
|---|---:|---:|---:|---:|---:|---:|---:|
| `gemini-3.1-flash-lite` | $0.00092 | **$0.0011** | $0.00026 | $0.2758 | **$0.5516** | $2.02 | $0.0023 |
| `gemini-3.8-flash` | $0.0052 | $0.0059 | $0.0015 | $1.55 | $3.10 | $11.37 | $0.0132 |
| `gemini-4-argon` | $0.0138 | $0.0158 | $0.0039 | $4.14 | $8.28 | $30.31 | $0.0351 |

**Công thức:**
- Chi phí / phiên = token vào / phiên × giá vào ÷ 1.000.000 + token ra / phiên × giá ra ÷ 1.000.000. Token đọc từ `usage` của API, ghi trong trace, không ước lượng.
- **Chi phí / task thành công = chi phí trung bình mỗi phiên ÷ tỉ lệ đạt lượt 2**. Không coi như đạt 100%.
- Chi phí / câu hỏi đạt = chi phí / phiên ÷ số lượt hỏi trung bình mỗi phiên ÷ tỉ lệ đạt (tỉ lệ đạt đo theo từng câu thử).
- Chi phí / tháng = Σ theo persona (số người × tỉ lệ persona × phiên / người / tháng × chi phí / phiên).
- Phiên nhánh N (không tìm thấy slide) **không gọi model**, chi phí model = 0. Nhờ vậy số lần gọi model / phiên có thể thấp hơn số lượt hỏi.

**Kịch bản cơ sở (nộp CP4):** chi phí / task thành công = **$0.0011** trên `gemini-3.1-flash-lite` · **$0.0059** trên `gemini-3.8-flash` · $0.0158 trên `gemini-4-argon` (236 người → $0.55 / $3.10 / $8.28 mỗi tháng).

## 3. So với impact

- **Impact / người / tháng** (`spec.md` §2): 80 giờ ÷ 118 người = 2,56 lần × 15,9 phút ≈ **40,7 phút tiết kiệm / người / tháng**. Đây là cận dưới, vì 118 chỉ đếm người đã chủ động hỏi.
- **Chi phí / người / tháng** (cơ sở, `gemini-3.1-flash-lite`): **$0.0023**. Model mạnh nhất `gemini-4-argon`: **$0.0351**.
- Đổi ra: **$0.0023 cho 40,7 phút**, tức ≈ **$0.0034 / giờ** học viên tiết kiệm được (`gemini-4-argon`: ≈ $0.052 / giờ). Phép tính: chi phí / người / tháng ÷ (40,7 ÷ 60) giờ.
- **Kết luận một dòng, đáng làm không:** **Đáng làm về chi phí** — kể cả model mạnh nhất, cả khoá 864 người chỉ ≈ $30 / tháng, dưới 4 xu / người / tháng cho ≈ 40 phút tiết kiệm; rào cản không phải tiền model mà là chất lượng (lượt 2 còn 3/24 câu trượt) và giờ công giảng viên / TA nhận câu "slide không đề cập" (chưa tính).

## 4. Giới hạn của phép tính

- 3/50 phiên lỗi do gói miễn phí quá tải (HTTP 503) — ở gói trả phí ít gặp hơn; nếu gặp thì cần thử lại, làm tăng chi phí một chút (chưa tính).
- Chỉ tính **chi phí gọi model**. Chưa tính hosting, lưu trữ, giờ công giảng viên / TA nhận các câu "slide không đề cập".
- Lượt hỏi / phiên lấy đầu vào ngẫu nhiên từ `eval/benchmark.csv` (loại `thuong` và `kho`), nên độ dài câu hỏi theo bộ câu thử, chưa chắc giống câu thật.
- Chỉ phủ slide Day 2 (28 đoạn). Mở rộng ra cả khoá thì phần căn cứ đưa vào model có thể dài hơn, token vào tăng.
