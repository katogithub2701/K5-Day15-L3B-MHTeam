"""Đếm bằng chứng pain từ data pre-class BTC cấp (evidence/data-mining.md).

Chạy:  python evidence/count.py [đường-dẫn-tới-data/preclass]
Mặc định đọc ../data/preclass (repo đề BTC đặt cạnh repo nhóm). Data KHÔNG commit vào repo nhóm.
Chỉ dùng thư viện chuẩn. Giờ trong data là UTC, đổi sang giờ Việt Nam = UTC + 7.
"""
import csv
import json
import sys
from collections import Counter, defaultdict
from datetime import datetime, timedelta
from pathlib import Path

DATA = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(__file__).resolve().parents[2] / "data" / "preclass"
VN = timedelta(hours=7)
SHORT_Q = 20            # câu hỏi ≤ 20 ký tự = câu ngắn, dễ mơ hồ
FOLLOW_UP = timedelta(minutes=5)   # hỏi tiếp cùng video trong 5 phút = hỏi nối
SLIDE_TO_CHAT = timedelta(minutes=3)


def read(name):
    with open(DATA / name, encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def t(s):
    return datetime.fromisoformat(s)


def pct(x, n):
    return f"{x}/{n} ({100 * x / n:.1f}%)" if n else f"{x}/0"


def main():
    events = read("events.csv")
    chat = read("chat.csv")
    completed = read("completed_items.csv")

    # Mẫu số chung: học viên có ít nhất 1 việc do chính họ làm (actor = learner)
    active = {e["hv"] for e in events if e["actor"] == "learner"}
    opened_lecture = {e["hv"] for e in events if e["type"] == "lecture_opened"}

    # Câu hỏi học viên tự hỏi trợ giảng AI khi tự học (không tính reply / mention bạn học AI)
    questions = [c for c in chat if c["kind"] == "question" and c["agent_id"] == "teaching_assistant"]
    askers = {c["hv"] for c in questions}
    replies = {e["ref_id"]: json.loads(e["data"]) for e in events if e["type"] == "agent_replied"}

    # M1. Bao nhiêu người hỏi khi tự học trước buổi
    print("M1 hỏi trợ giảng AI >=1 lần / học viên có hoạt động:", pct(len(askers & active), len(active)))
    print("   số câu hỏi:", len(questions))

    # M2. Hỏi ngay trên slide: bôi đen chữ trên slide rồi bấm hỏi
    slide = [e for e in events if e["type"] == "slide_text_asked"]
    slide_users = {e["hv"] for e in slide}
    print("M2 bôi đen slide để hỏi >=1 lần / người đã mở bài giảng:", pct(len(slide_users), len(opened_lecture)))
    print("   số lần bôi đen slide để hỏi:", len(slide))
    chat_times = defaultdict(list)
    for e in events:
        if e["type"] == "chat_sent":
            chat_times[e["hv"]].append(t(e["occurred_at"]))
    followed = sum(
        any(timedelta(0) <= x - t(e["occurred_at"]) <= SLIDE_TO_CHAT for x in chat_times[e["hv"]]) for e in slide
    )
    print("   lần bôi đen slide có gửi câu hỏi trong 3 phút sau:", pct(followed, len(slide)))

    # M3. Câu hỏi ngắn (dễ mơ hồ)
    short = [c for c in questions if int(c["do_dai_cau_hoi"]) <= SHORT_Q]
    print(f"M3 câu hỏi <= {SHORT_Q} ký tự / câu hỏi:", pct(len(short), len(questions)))
    print("   trung vị độ dài câu hỏi:", sorted(int(c["do_dai_cau_hoi"]) for c in questions)[len(questions) // 2])

    # M4. Hỏi nối: câu kế tiếp cùng người, cùng video, cách câu trước <= 5 phút
    by_hv = defaultdict(list)
    for c in questions:
        by_hv[c["hv"]].append(c)
    follow_ups = 0
    for lst in by_hv.values():
        lst.sort(key=lambda c: c["asked_at"])
        for a, b in zip(lst, lst[1:]):
            if a["transcript"] == b["transcript"] and t(b["asked_at"]) - t(a["asked_at"]) <= FOLLOW_UP:
                follow_ups += 1
    print("M4 câu hỏi nối (cùng video, <= 5 phút sau câu trước) / câu hỏi:", pct(follow_ups, len(questions)))

    # M5. AI thiếu ngữ cảnh bài để trả lời; M6. câu trả lời có dẫn mốc trong bài
    with_reply = [c for c in questions if c["id"] in replies and replies[c["id"]].get("missing_context") is not None]
    missing = sum(1 for c in with_reply if replies[c["id"]]["missing_context"])
    print("M5 AI báo thiếu ngữ cảnh / câu có ghi missing_context:", pct(missing, len(with_reply)))
    cited = sum(1 for c in questions if replies.get(c["id"], {}).get("moc_trich_dan"))
    print("M6 câu trả lời có dẫn mốc bài giảng / câu hỏi:", pct(cited, len(questions)))

    # M7. Giờ hỏi (giờ Việt Nam)
    hours = Counter()
    for c in questions:
        h = (t(c["asked_at"]) + VN).hour
        hours["19h-24h" if h >= 19 else ("0h-6h" if h < 6 else "6h-19h")] += 1
    for k in ("6h-19h", "19h-24h", "0h-6h"):
        print(f"M7 câu hỏi lúc {k} / câu hỏi:", pct(hours[k], len(questions)))

    # M8. Tần suất: số ngày khác nhau có hỏi, trên mỗi người đã hỏi (data 05/11 -> 25/11 = 21 ngày)
    ask_days = defaultdict(set)
    for c in questions:
        ask_days[c["hv"]].add((t(c["asked_at"]) + VN).date())
    d = sorted(len(v) for v in ask_days.values())
    mean = sum(d) / len(d)
    print(f"M8 số ngày có hỏi / người đã hỏi: trung vị {d[len(d) // 2]}, trung bình {mean:.2f} "
          f"-> quy ra 30 ngày: {mean * 30 / 21:.2f} lần / tháng")
    print("   phân bố:", dict(sorted(Counter(d).items())))

    # M9. Mở bài nhưng chưa xong mục nào (dùng cho hướng bị loại ở spec §2)
    done = {r["hv"] for r in completed}
    print("M9 mở bài giảng nhưng chưa đánh dấu xong mục nào / người đã mở:",
          pct(len(opened_lecture - done), len(opened_lecture)))


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    main()
