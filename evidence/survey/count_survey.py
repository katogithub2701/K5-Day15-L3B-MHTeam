"""Đếm khảo sát theo đúng cách đếm viết trước ở evidence/survey/questions.md.

Chạy:
  python evidence/survey/count_survey.py                 # đếm trên results.csv (bản đã ẩn danh, có trong repo)
  python evidence/survey/count_survey.py raw-<tên>.csv   # tạo lại results.csv từ bản xuất Google Form rồi đếm
Bản xuất gốc (raw-*) có cột liên hệ ở câu 11 → không commit (.gitignore: evidence/**/raw-*).
results.csv bỏ cột Timestamp và câu 11, thay bằng mã phiếu #01, #02… theo thứ tự nộp.
"""
import csv
import statistics
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
RESULTS = HERE / "results.csv"
COLS = ["phieu", "q1_vai", "q2_lan_gan_nhat", "q3_so_buoi_2_tuan", "q4_cho_khong_hieu", "q5_da_lam_gi",
        "q6_mat_bao_lau", "q7_hieu_chua", "q8_google_chatgpt_khop", "q9_kho_chiu_nhat", "q10_preclass"]


def anonymize(raw_path):
    with open(raw_path, encoding="utf-8-sig", newline="") as f:
        rows = list(csv.reader(f))[1:]
    with open(RESULTS, "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(COLS)
        for i, r in enumerate(rows, 1):
            w.writerow([f"#{i:02d}"] + [c.strip() for c in r[1:11]])   # bỏ r[0] Timestamp và r[11] câu 11


def pct(x, n):
    return f"{x}/{n} ({100 * x / n:.1f}%)" if n else f"{x}/0"


def main():
    if len(sys.argv) > 1:
        anonymize(Path(sys.argv[1]))
    with open(RESULTS, encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f))
    print("Tổng số phiếu:", len(rows))

    # Mẫu số chính = học viên (câu 1) và câu 2 không phải "Chưa bao giờ"
    N = [r for r in rows if r["q1_vai"].startswith("Học viên") and not r["q2_lan_gan_nhat"].startswith("Chưa bao giờ")]
    n = len(N)
    print("Mẫu số chính (học viên, đã từng xem trước slide):", n)
    print("  theo lớp:", {k: sum(r["q1_vai"] == k for r in N) for k in sorted({r["q1_vai"] for r in N})})

    pain = [r for r in N if r["q4_cho_khong_hieu"] != "Không có"]
    print("Gặp pain (câu 4 ≠ Không có):", pct(len(pain), n))
    long_time = ("15–30 phút", "Trên 30 phút")
    heavy = [r for r in pain if r["q7_hieu_chua"] != "Hiểu" or r["q6_mat_bao_lau"] in long_time]
    print("Pain nặng (gặp pain và (câu 7 ≠ Hiểu hoặc câu 6 ≥ 15–30 phút)):", pct(len(heavy), n),
          "· trong số gặp pain:", pct(len(heavy), len(pain)))
    # Ngưỡng ở evidence/hypothesis.md: trong số gặp pain, ≥1/3 bỏ qua hoặc mất >15 phút
    skip_or_long = [r for r in pain if "Bỏ qua" in r["q5_da_lam_gi"] or r["q6_mat_bao_lau"] in long_time]
    print("Ngưỡng giả thuyết — gặp pain và (bỏ qua hoặc ≥15 phút):", pct(len(skip_or_long), len(pain)))

    print("Câu 4:", {k: sum(r["q4_cho_khong_hieu"] == k for r in N)
                     for k in ("Không có", "1 chỗ", "2–3 chỗ", "Nhiều hơn 3 chỗ")})
    acts = ("Đọc lại slide", "Tra Google", "Hỏi ChatGPT / Gemini riêng", "Hỏi bạn", "Hỏi trên Discord",
            "Để dành hỏi trên lớp", "Bỏ qua")
    for a in acts:
        print(f"Câu 5 — {a}:", pct(sum(a in r["q5_da_lam_gi"] for r in pain), len(pain)), "(trong số gặp pain)")
    q6 = ("Dưới 5 phút", "5–15 phút", "15–30 phút", "Trên 30 phút")
    print("Câu 6 (trong số gặp pain):", {k: sum(r["q6_mat_bao_lau"] == k for r in pain) for k in q6})
    mid = {"Dưới 5 phút": 2.5, "5–15 phút": 10, "15–30 phút": 22.5, "Trên 30 phút": 37.5}  # trung điểm; >30 lấy 37,5
    m = [mid[r["q6_mat_bao_lau"]] for r in pain if r["q6_mat_bao_lau"] in mid]
    print(f"  phút / lần — trung bình trung điểm: {statistics.mean(m):.1f} · trung vị: {statistics.median(m)}")
    print("Câu 7 (trong số gặp pain):", {k: sum(r["q7_hieu_chua"] == k for r in pain)
                                         for k in ("Hiểu", "Hiểu một phần", "Không hiểu", "Không gặp chỗ nào không hiểu")})
    tra = [r for r in N if r["q8_google_chatgpt_khop"] != "Không để ý / không tra"]
    lech = [r for r in tra if r["q8_google_chatgpt_khop"] in ("Lệch một phần", "Lệch nhiều")]
    print("Câu 8 — lệch một phần / lệch nhiều, trên người có tra:", pct(len(lech), len(tra)))
    no_pre = [r for r in N if r["q10_preclass"] in ("Chưa từng nghe tới", "Biết nhưng chưa dùng")]
    print("Câu 10 — chưa nghe / biết nhưng chưa dùng pre-class:", pct(len(no_pre), n))
    print("Câu 10:", {k: sum(r["q10_preclass"] == k for r in N)
                      for k in ("Chưa từng nghe tới", "Biết nhưng chưa dùng", "Đã dùng 1–2 lần", "Dùng thường xuyên")})
    q3 = [int(r["q3_so_buoi_2_tuan"]) for r in N if r["q3_so_buoi_2_tuan"].strip().isdigit()]
    print(f"Câu 3 — số buổi xem trước / 2 tuần: trung vị {statistics.median(q3)} · trung bình {statistics.mean(q3):.2f}"
          f" → ≈ {statistics.median(q3) * 30 / 14:.1f} lần / tháng (trung vị)")

    # Phiếu tự mâu thuẫn: ghi ra, không sửa
    for r in N:
        if r["q4_cho_khong_hieu"] == "Không có" and r["q6_mat_bao_lau"] != "Không gặp chỗ nào không hiểu":
            print("  ghi chú:", r["phieu"], "câu 4 = Không có nhưng câu 6 =", r["q6_mat_bao_lau"])
        if r["q4_cho_khong_hieu"] != "Không có" and r["q7_hieu_chua"] == "Không gặp chỗ nào không hiểu":
            print("  ghi chú:", r["phieu"], "câu 4 =", r["q4_cho_khong_hieu"], "nhưng câu 7 = Không gặp chỗ nào")
    print("Câu 9 có viết:", sum(bool(r["q9_kho_chiu_nhat"].strip()) for r in rows), "/", len(rows))


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    main()
