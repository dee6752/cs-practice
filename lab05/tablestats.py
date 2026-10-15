import csv
import io

def read_rows(lines: list[str]) -> list[dict]:
    text = "\n".join(lines)
    reader = csv.DictReader(io.StringIO(text))
    rows = []
    for row in reader:
        cleaned = {}
        for k, v in row.items():
            if k is None:
                continue
            cleaned[k.strip().lower()] = (v or '').strip()
        rows.append(cleaned)
    return rows

def count_types(rows: list[dict]) -> dict:
    counts = {}
    for row in rows:
        kind = row.get('тип')
        if kind:
            counts[kind] = counts.get(kind, 0) + 1
    return counts

def total_minutes(rows: list[dict], kind: str) -> float:
    total = 0.0
    for row in rows:
        if row.get('тип') == kind:
            minutes_str = row.get('минуты', '0').replace(',', '.')
            try:
                total += float(minutes_str)
            except ValueError:
                continue
    return round(total, 1)

def to_csv(counts: dict) -> str:
    lines = ["тип,количество"]
    for kind in sorted(counts.keys()):
        escaped = f'"{kind}"' if any(c in kind for c in ',"\n') else kind
        lines.append(f"{escaped},{counts[kind]}")
    return "\n".join(lines) + "\n"
