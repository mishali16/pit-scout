from collections import defaultdict


def rank_teams(matches):
    grouped = defaultdict(list)
    for match in matches:
        grouped[match["team"]].append(match)
    rankings = []
    for team, rows in grouped.items():
        count = len(rows)
        auto = average(row["auto"] for row in rows)
        teleop = average(row["teleop"] for row in rows)
        endgame = average(row["endgame"] for row in rows)
        penalties = average(row["penalties"] for row in rows)
        reliability = sum(1 for row in rows if row["penalties"] == 0) / count
        score = auto * 1.25 + teleop + endgame * 1.1 - penalties * 1.5 + reliability * 5
        rankings.append(
            {
                "team": team,
                "matches": count,
                "auto_avg": round(auto, 1),
                "teleop_avg": round(teleop, 1),
                "endgame_avg": round(endgame, 1),
                "penalty_avg": round(penalties, 1),
                "reliability": round(reliability, 2),
                "score": round(score, 1),
                "notes": "; ".join(row["notes"] for row in rows if row["notes"])[:120],
            }
        )
    return sorted(rankings, key=lambda item: item["score"], reverse=True)


def average(values):
    values = list(values)
    return sum(values) / len(values)
