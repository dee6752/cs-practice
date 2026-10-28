def read_rows(lines: list[str]) -> list[dict]:
    rows = []
    header = []

    for line in lines:
        line = line.strip()
        if not line:
            continue

        f = [value.strip() for value in line.split(",")]

        if not header:
            header = f
            continue
        if len(f) != len(header):
            continue

        rows.append(dict(zip(header, f)))

    return rows


def count_types(rows: list[dict]) -> dict:
    counts = {}
    for row in rows:
        kind = row["тип"]
        counts[kind] = counts.get(kind, 0) + 1
    return counts


def total_minutes(rows: list[dict], kind: str) -> float:
    t = 0.0
    for row in rows:
        if row.get('тип', None) != kind:
            continue
        try:
            minutes =  float(row['минуты'].replace(",", "."))
        except ValueError:
            continue
        t += minutes
    return round(t, 1)


def to_csv(counts: dict) -> str:
    lines = ["тип,количество"]
    for kind in sorted(counts):
        lines.append(f"{kind},{counts[kind]}")
    return "\n".join(lines) + "\n"
