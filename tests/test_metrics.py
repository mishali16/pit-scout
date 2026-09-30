import unittest
from pathlib import Path

from pit_scout.loader import load_matches
from pit_scout.metrics import rank_teams


class MetricsTest(unittest.TestCase):
    def test_rankings_put_strong_team_first(self):
        rows = load_matches(Path(__file__).parents[1] / "samples" / "matches.csv")
        rankings = rank_teams(rows)
        self.assertEqual(rankings[0]["team"], "8421")
        self.assertGreater(rankings[0]["score"], rankings[-1]["score"])


if __name__ == "__main__":
    unittest.main()
