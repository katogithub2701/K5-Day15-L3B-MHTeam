"""Công cụ của bài toán — NHÓM VIẾT. Điền ở guide bước 2.2 (thiết kế) và 3.2 (code).

Mỗi công cụ là một hàm Python có @tool. Docstring ghi đúng 4 ý như sơ đồ ở spec.md §4:
    tên · input · output · có tác động ra ngoài không (gửi tin, sửa dữ liệu, chấm điểm…)
Khung tự ghi mỗi lần gọi công cụ vào trace (tên, input, output rút gọn, thời gian, lỗi).

Dữ liệu công cụ đọc: data/slides.csv (mô tả ở data/DATA_CARD.md).
"""
import csv
import os
import re
import unicodedata
from collections import Counter

from tracing import tool, TOOLS  # noqa: F401  (TOOLS: danh sách công cụ đã đăng ký)

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SLIDES_PATH = os.path.join(ROOT, "data", "slides.csv")

TOP_K = 3        # trả tối đa 3 đoạn
MIN_SCORE = 2      # điểm tối thiểu của một đoạn
MIN_COVERAGE = 0.5 # đoạn phải chứa ≥50% từ nội dung của câu hỏi
STRONG_SCORE = 8   # câu hỏi dài: điểm ≥ 8 …
MIN_RARE_HITS = 2  # … và trùng ≥ 2 từ hiếm thì giữ dù phủ < 50%
RARE_DF_RATIO = 0.1  # từ hiếm = có trong ≤ 10% số đoạn slide (28 đoạn → ≤ 2 đoạn), vd "f1", "kim cuong"
REL_CUTOFF = 0.5   # chỉ giữ đoạn có điểm ≥ 50% điểm đoạn tốt nhất
# Giữ đoạn khi: điểm ≥ MIN_SCORE và (phủ ≥ MIN_COVERAGE hoặc (điểm ≥ STRONG_SCORE và ≥ MIN_RARE_HITS từ hiếm)).
# Từ chung như "he thong", "thuc", "huong" có ở nhiều slide nên không đủ để vượt cửa phủ.
# Không đoạn nào được giữ → coi như slide không đề cập → trả []

# Từ chức năng / từ hỏi (đã bỏ dấu) — không mang nội dung nên không tính điểm.
STOPWORDS = set("""
la gi cua va voi cho cac nhung mot hai ba co khong duoc trong tren duoi ve tu den
nay do kia thi ma neu khi nao sao the nhu bao nhieu vi bi da dang se can phai hay
hoac de theo tai ra vao len lai rat qua nhat hon cung chi moi ai minh ban toi em anh
chi slide trang buoi hoc noi giai thich lam viec gom nhu vay nghia dung y nen
khac nhau cach cai gium giup xin hoi
""".split())


def _normalize(text: str) -> str:
    """Bỏ dấu tiếng Việt, đổi đ→d, chữ thường."""
    text = unicodedata.normalize("NFD", text.lower().replace("đ", "d"))
    return "".join(c for c in text if unicodedata.category(c) != "Mn")


def _tokens(text: str) -> list:
    return [t for t in re.findall(r"[a-z0-9]+", _normalize(text)) if t not in STOPWORDS]


def _bigrams(tokens: list) -> set:
    return {a + " " + b for a, b in zip(tokens, tokens[1:])}


_SLIDES = None


def _load_slides() -> list:
    global _SLIDES
    if _SLIDES is None:
        with open(SLIDES_PATH, encoding="utf-8-sig", newline="") as f:
            rows = list(csv.DictReader(f))
        for r in rows:
            topic_tok = _tokens(r["topic"])
            all_tok = topic_tok + _tokens(r["content"])
            r["_topic"] = set(topic_tok)
            r["_words"] = set(all_tok)
            r["_bigrams"] = _bigrams(topic_tok) | _bigrams(_tokens(r["content"]))
        # Từ hiếm = có mặt trong ≤ RARE_DF_RATIO số đoạn (tính từ data, không từ bộ câu thử)
        df = Counter(w for r in rows for w in r["_words"])
        limit = max(1, RARE_DF_RATIO * len(rows))
        rare = {w for w, c in df.items() if c <= limit}
        for r in rows:
            r["_rare"] = r["_words"] & rare
        _SLIDES = rows
    return _SLIDES


def _score(q_words: set, q_bigrams: set, slide: dict) -> int:
    hit = q_words & slide["_words"]
    return (len(hit)                               # mỗi từ trùng: 1 điểm
            + len(q_words & slide["_topic"])       # trùng tiêu đề: thêm 1 điểm
            + 2 * len(q_bigrams & slide["_bigrams"]))  # trùng cụm 2 từ: thêm 2 điểm


@tool
def search_slides(query: str) -> list:
    """search_slides — tra slide buổi học theo câu hỏi của học viên.
    Input: query (str) — câu hỏi nguyên văn của học viên.
    Output: list tối đa 3 đoạn khớp nhất, xếp theo điểm giảm dần, mỗi đoạn
        {"id", "page", "topic", "content"}; trả [] nếu không đoạn nào đạt MIN_SCORE
        và (MIN_COVERAGE hoặc STRONG_SCORE + MIN_RARE_HITS từ hiếm) (để luồng nói "slide không đề cập").
    Tác động ra ngoài: KHÔNG — chỉ đọc data/slides.csv."""
    q_tok = _tokens(query)
    q_words, q_bigrams = set(q_tok), _bigrams(q_tok)
    if not q_words:
        return []
    scored = []
    for s in _load_slides():
        coverage = len(q_words & s["_words"]) / len(q_words)
        score = _score(q_words, q_bigrams, s)
        strong = score >= STRONG_SCORE and len(q_words & s["_rare"]) >= MIN_RARE_HITS
        if score >= MIN_SCORE and (coverage >= MIN_COVERAGE or strong):
            scored.append((score, s))
    if scored:
        best = max(x[0] for x in scored)
        scored = [x for x in scored if x[0] >= REL_CUTOFF * best]
    scored.sort(key=lambda x: (-x[0], int(x[1]["page"])))
    return [{"id": s["id"], "page": int(s["page"]), "topic": s["topic"], "content": s["content"]}
            for _, s in scored[:TOP_K]]
