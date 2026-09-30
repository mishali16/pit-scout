import csv


FIELDS = {"match", "team", "auto", "teleop", "endgame", "penalties", "notes"}


def load_matches(path):
    with open(path, newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        missing = FIELDS - set(reader.fieldnames or [])
        if missing:
            raise ValueError(f"missing columns: {', '.join(sorted(missing))}")
        rows = []
        for row in reader:
            rows.append(
                {
                    "match": int(row["match"]),
                    "team": row["team"],
                    "auto": int(row["auto"]),
                    "teleop": int(row["teleop"]),
                    "endgame": int(row["endgame"]),
                    "penalties": int(row["penalties"]),
                    "notes": row["notes"],
                }
            )
        return rows
