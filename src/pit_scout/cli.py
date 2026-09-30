import argparse

from .loader import load_matches
from .metrics import rank_teams
from .report import render


def main():
    parser = argparse.ArgumentParser(description="Rank FTC-style teams from match scouting CSV data.")
    parser.add_argument("csv")
    args = parser.parse_args()
    print(render(rank_teams(load_matches(args.csv))))


if __name__ == "__main__":
    main()
