# Hồ sơ đánh giá — một trang

> Điền ở guide bước 2.4 (mục 1–4, trước CP2) và 4.1 (mục 5–6, trước CP4). Ôn lại: ngày 9, ngày 14 · lab ngày 9. Chấm ở rubric R4, R5.
> Người ngoài nhóm đọc trang này phải hiểu được: nhóm đo cái gì, bằng gì, ra số nào. Trang slide "Đánh giá thế nào" lấy từ đây.

## 1. Dataset → xử lý

- Dữ liệu `data/slides.csv`: viết lại bằng lời của nhóm từ 28 trang nội dung trọng tâm của slide **Ngày 2 — Discovery & Problem Framing** (bản PDF 88 trang trên LMS, bỏ các trang bìa/giải lao/lịch trình).
- Mỗi đoạn dài 2–4 câu, không chép nguyên văn slide gốc, gắn kèm số trang gốc (`page`) và chủ đề (`topic`) để công cụ `search_slides` tra cứu. Chi tiết xem `data/DATA_CARD.md`.

## 2. Bộ câu thử dựng ra sao

- `eval/benchmark.csv`: 13 câu (thuong 6 · kho 5 · tu_choi 2, trong đó 2 câu tấn công) *(bản CP2; sẽ mở rộng lên 20–30 câu trước CP3)*.
- Nguồn (`python run.py check` in sẵn): nguoi_dung 0 · data_that 0 · tu_viet 13 · sinh_seed 0 → từ người dùng / data thật 0/13 *(đang chờ kết quả khảo sát/phỏng vấn của Toàn lúc 19:00 để bổ sung ≥1/3 câu từ `nguoi_dung` cho CP3)*.
- Độ phủ — lưới input 4 chiều: loại câu hỏi (khái niệm có trong slide / ngoài slide / mơ hồ / gài tiền đề sai) × hành vi mong đợi (trả lời kèm trang / hỏi lại / nói không có / từ chối) × mức độ rõ ngữ cảnh × rủi ro học sai kiến thức.
- Câu `kho` trỏ về 4 lớp chỗ khó (`spec.md` §5): lớp 1 (ngoài slide / giới hạn dữ liệu): C06, C13 · lớp 2 (mơ hồ): C08, C09 · lớp 3 (ngoài phạm vi/tấn công): C11 · lớp 4 (đặc thù học sai): C10, C12.

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
