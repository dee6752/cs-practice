def read_rows(lines: list[str]) -> list[dict]:
    rows = []
    header = None
    for line in lines:
        if not line.strip():
            continue
        if header is None:
            header = [h.strip() for h in line.strip().split(',')]
            continue
        parts = [p.strip() for p in line.strip().split(',')]
        if len(parts) != len(header):
            continue
        rows.append(dict(zip(header, parts)))
    return rows


def count_types(rows: list[dict]) -> dict:
    counts = {}
    for row in rows:
        kind = row.get('тип')
        if kind is not None:
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
        lines.append(f"{kind},{counts[kind]}")
    return "\n".join(lines) + "\n"
