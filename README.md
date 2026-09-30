# Pit Scout

FTC-style match scouting analyzer that turns CSV notes into team rankings and alliance suggestions.

Scouting data gets messy fast during competitions. Pit Scout keeps the workflow simple: record matches in a CSV, compute useful team metrics, and print a readable strategy report.

```bash
PYTHONPATH=src python3 -m pit_scout samples/matches.csv
PYTHONPATH=src python3 -m unittest discover -s tests
```

## How It Works

```mermaid
flowchart LR
  A[Match CSV] --> B[Parser]
  B --> C[Team metrics]
  C --> D[Ranking model]
  D --> E[Strategy report]
```

The ranking balances autonomous points, teleop points, endgame points, penalties, and reliability. The weights are visible in code so a drive team can tune them.

## Architecture

- `loader.py`: CSV parsing and validation
- `metrics.py`: team aggregation and scoring
- `report.py`: concise terminal report
- `cli.py`: command-line entry point

## Demo

```bash
PYTHONPATH=src python3 -m pit_scout samples/matches.csv
```

## Why I Built This

I wanted a project connected to FTC robotics that is practical but still technical. It is small enough to use at an event and structured enough to extend with a web UI later.

## Future Ideas

- QR-code match entry
- Streamlit or Flask dashboard
- Alliance compatibility scoring
- Exportable picklist sheets

## GitHub

Description: FTC-style scouting analyzer that ranks teams from match CSV data.

Topics: `ftc`, `robotics`, `python`, `data-analysis`, `csv`, `competition-scouting`
