# Tóm tắt mô phỏng simulate-1@20261128-112922

Do `python run.py simulate` sinh ra — không sửa tay. Chép bảng sang `cost/cost-estimate.md`.

| Persona | Số phiên mô phỏng | Lượt hỏi / phiên | Token vào / phiên | Token ra / phiên | Gọi model / phiên | Gọi công cụ / phiên |
|---|---:|---:|---:|---:|---:|---:|
| thinh_thoang_hoi | 31 | 4 | 2343 | 235 | 3.4 | 4.0 |
| hoi_deu | 14 | 4 | 2154 | 222 | 3.1 | 4.0 |
| hoi_don | 2 | 4 | 2546 | 229 | 3.5 | 4.0 |

Tỉ lệ đạt dùng để tính: 21/24 (88%) — lượt run-2@20261128-101825

- Tỉ lệ đạt lấy từ lượt nhóm chọn: eval/run-2.csv (--rate-from).

| Model (giá) | Chi phí / phiên | Chi phí / task thành công | Chi phí / câu hỏi đạt | Chi phí / tháng — thấp (118 người) | Chi phí / tháng — cơ sở (236 người) | Chi phí / tháng — cao (864 người) | Chi phí / người / tháng (cơ sở) |
|---|---:|---:|---:|---:|---:|---:|---:|
| gemini-3.1-flash-lite (vào 0.25 · ra 1.5 $/1M) | $0.00092 | $0.0011 | $0.00026 | $0.2758 | $0.5516 | $2.02 | $0.0023 |
| gemini-3.8-flash (vào 1.5 · ra 7.5 $/1M) | $0.0052 | $0.0059 | $0.0015 | $1.55 | $3.10 | $11.37 | $0.0132 |
| gemini-4-argon (vào 4.0 · ra 20.0 $/1M) | $0.0138 | $0.0158 | $0.0039 | $4.14 | $8.28 | $30.31 | $0.0351 |

- Chi phí / task thành công = chi phí / phiên ÷ tỉ lệ đạt. Chi phí / câu hỏi đạt = chi phí / phiên ÷ số lượt hỏi trung bình mỗi phiên (4.0) ÷ tỉ lệ đạt — tỉ lệ đạt đo theo từng câu thử.
- Token đo trên model: gemini-3.1-flash-lite. Giá tính theo từng model trong bảng — model khác bộ tách token thì số token thật có thể lệch; ghi rõ "đo trên model X, tính giá model Y" trong cost/cost-estimate.md.
- Phiên lỗi (không tính vào trung bình): 3/50.
