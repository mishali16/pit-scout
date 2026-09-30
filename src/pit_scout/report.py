def render(rankings):
    lines = ["PIT SCOUT REPORT", "================", ""]
    for index, team in enumerate(rankings, start=1):
        lines.append(
            f"{index}. Team {team['team']} | score {team['score']} | "
            f"auto {team['auto_avg']} | teleop {team['teleop_avg']} | "
            f"endgame {team['endgame_avg']} | reliability {team['reliability']}"
        )
        if team["notes"]:
            lines.append(f"   notes: {team['notes']}")
    if len(rankings) >= 3:
        top = ", ".join(team["team"] for team in rankings[:3])
        lines.extend(["", f"Suggested first picklist: {top}"])
    return "
".join(lines)
