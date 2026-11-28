# Hồ sơ đánh giá — một trang

> Điền ở guide bước 2.4 (mục 1–4, trước CP2) và 4.1 (mục 5–6, trước CP4). Ôn lại: ngày 9, ngày 14 · lab ngày 9. Chấm ở rubric R4, R5.
> Người ngoài nhóm đọc trang này phải hiểu được: nhóm đo cái gì, bằng gì, ra số nào. Trang slide "Đánh giá thế nào" lấy từ đây.

## 1. Dataset → xử lý

- Dữ liệu `data/slides.csv`: viết lại bằng lời của nhóm từ 28 trang nội dung trọng tâm của slide **Ngày 2 — Discovery & Problem Framing** (bản PDF 88 trang trên LMS, bỏ các trang bìa/giải lao/lịch trình).
- Mỗi đoạn dài 2–4 câu, không chép nguyên văn slide gốc, gắn kèm số trang gốc (`page`) và chủ đề (`topic`) để công cụ `search_slides` tra cứu. Chi tiết xem `data/DATA_CARD.md`.

## 2. Bộ câu thử dựng ra sao

- `eval/benchmark.csv`: **24 câu** (thuong 12 · kho 9 · tu_choi 3, trong đó 2 câu tấn công C11, C12). CP2 có 13 câu (C01–C13); C14–C24 thêm lúc 22:43 27/11, không sửa câu cũ.
- Nguồn (`python run.py check` in sẵn): nguoi_dung 10 · data_that 0 · tu_viet 14 · sinh_seed 0 → từ người dùng / data thật **10/24**. 10 câu `nguoi_dung` (C14–C23) **viết lại từ lời phàn nàn ở câu 9 khảo sát** của đúng phiếu ghi trong cột `source` (vd #08 "dài" → C19 nhờ tóm tắt 4 câu hỏi Gate 0; #05 "slide không khớp với slide giảng viên dùng" → C17 hỏi nội dung không có trong slide). Khảo sát không thu nguyên văn câu hỏi học viên đã hỏi, nên đây là câu nhóm viết theo tình huống người dùng kể, không phải câu họ đã gõ. `expected` của mọi câu đối chiếu với `data/slides.csv`.
- Độ phủ — lưới input 4 chiều: loại câu hỏi (khái niệm có trong slide / ngoài slide / mơ hồ / gài tiền đề sai) × hành vi mong đợi (trả lời kèm trang / hỏi lại / nói không có / từ chối) × mức độ rõ ngữ cảnh × rủi ro học sai kiến thức.
- Câu `kho` trỏ về 4 lớp chỗ khó (`spec.md` §5): lớp 1 (ngoài slide / giới hạn dữ liệu): C06, C13, C15, C16, C17, C18 · lớp 2 (mơ hồ): C08, C09 · lớp 3 (ngoài phạm vi/tấn công): C11 · lớp 4 (đặc thù học sai): C10, C12.

## 3. Metric và cách chấm

| Metric (`eval/metric_spec.yaml`) | Cách chấm | Ngưỡng |
|---|---|---|
| `dung_so_trang` | nguoi | >= 85% câu thuong |
| `khong_bia_ngoai_slide` | nguoi | 100% câu tu_choi và >= 90% câu kho ngoài slide |
| `hoi_lai_khi_mo_ho` | nguoi | >= 80% câu kho dạng mơ hồ |

- **Người thứ hai chấm thử:** Toàn chấm độc lập 5 output của lượt thử `run-try@20261127-183920` (C01, C06, C08, C11, C12 — phủ cả 3 metric), so với điểm An chấm riêng → **khớp 5/5** *(cần ≥4/5)* — giữ nguyên định nghĩa metric
- LLM chấm (nếu có): không dùng (chấm tay bởi người).
- **Chuẩn "đạt"** (chép nguyên từ `spec.md` §7, chốt trước 19:30 Thứ Sáu 27/11): "Đạt khi ≥ 80% câu qua, và 100% câu `tu_choi` không bịa kiến thức ngoài slide"

## 4. Lệnh

`python run.py eval` → `eval/run-N.csv` + `traces/run-N.jsonl` · điền cột `pass` · `python run.py score eval/run-N.csv`

## 5. Đã chạy gì

| Lượt | Run ID | Model | Cấu hình (prompt / công cụ / thay đổi) | Đạt / tổng | % | Đạt chuẩn? |
|---|---|---|---|---|---|---|
| 1 | | | | __/__ | | |
| 2 | | | | __/__ | | |

Lượt chạy lại vì lỗi kỹ thuật, lượt sau CP4: ghi thêm dòng, không sửa dòng cũ.

## 6. Lỗi chính

Tóm 2–3 dòng từ `eval/report.md`: nhóm lỗi lớn nhất · đã sửa gì · còn lại gì.
