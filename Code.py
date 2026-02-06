import csv

# -------------------------------
# PlayerSeason class
# -------------------------------
class PlayerSeason:
    def __init__(self, row):
        self.player = row["Player"]
        self.season = row["Season"]

        self.fgm = float(row["FGM"])
        self.fga = float(row["FGA"])
        self.tpm = float(row["3PM"])
        self.tpa = float(row["3PA"])
        self.ftm = float(row["FTM"])
        self.fta = float(row["FTA"])

        self.pts = float(row["PTS"])
        self.minutes = float(row["MIN"])
        self.blocks = float(row["BLK"])
        self.steals = float(row["STL"])
        self.games = float(row["GP"])

    # --- Accuracy metrics ---
    def fg_accuracy(self):
        return self.fgm / self.fga if self.fga > 0 else None

    def tp_accuracy(self):
        return self.tpm / self.tpa if self.tpa > 0 else None

    def ft_accuracy(self):
        return self.ftm / self.fta if self.fta > 0 else None

    def overall_accuracy(self):
        total_made = self.fgm + self.ftm
        total_attempted = self.fga + self.fta
        return total_made / total_attempted if total_attempted > 0 else None

    # --- Performance metrics ---
    def points_per_minute(self):
        return self.pts / self.minutes if self.minutes > 0 else None

    def blocks_per_game(self):
        return self.blocks / self.games if self.games > 0 else None

    def steals_per_game(self):
        return self.steals / self.games if self.games > 0 else None


# -------------------------------
# Load CSV data
# -------------------------------
file_path = "players_stats_by_season_full_details.csv"
players = []

with open(file_path, newline='', encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:
        try:
            players.append(PlayerSeason(row))
        except:
            continue


# -------------------------------
# Helper function for top 100
# -------------------------------
def top_100(metric_function,
            min_attempts=None,
            attempt_attr=None,
            min_games=30,
            min_total=None,
            total_attr=None):

    results = []

    for p in players:
        # Minimum games filter
        if p.games < min_games:
            continue

        # Minimum attempt filter
        if min_attempts and attempt_attr:
            if getattr(p, attempt_attr) < min_attempts:
                continue

        # Minimum total stat filter
        if min_total and total_attr:
            if getattr(p, total_attr) < min_total:
                continue

        value = metric_function(p)
        if value is not None and value <= 1.0:
            results.append((p.player, p.season, value))

    results.sort(key=lambda x: x[2], reverse=True)
    return results[:100]


# -------------------------------
# Generate all top-100 lists
# -------------------------------
top_fg = top_100(lambda p: p.fg_accuracy(),
                 min_attempts=100,
                 attempt_attr="fga")

top_tp = top_100(lambda p: p.tp_accuracy(),
                 min_attempts=50,
                 attempt_attr="tpa")

top_ft = top_100(lambda p: p.ft_accuracy(),
                 min_attempts=50,
                 attempt_attr="fta")

top_ppm = top_100(lambda p: p.points_per_minute())

top_overall = top_100(lambda p: p.overall_accuracy(),
                      min_attempts=100,
                      attempt_attr="fga")

top_blocks = top_100(
    lambda p: p.blocks_per_game(),
    min_games=30,
    min_total=40,
    total_attr="blocks"
)

top_steals = top_100(
    lambda p: p.steals_per_game(),
    min_games=30,
    min_total=40,
    total_attr="steals"
)


# -------------------------------
# Print results
# -------------------------------
def print_top(title, data):
    print(f"\n--- Top 100 {title} ---")
    for player, season, value in data[:10]:
        print(f"{player} ({season}) - {value:.3f}")


print_top("Field Goal Accuracy", top_fg)
print_top("Three-Point Accuracy", top_tp)
print_top("Free Throw Accuracy", top_ft)
print_top("Points per Minute", top_ppm)
print_top("Overall Shooting Accuracy", top_overall)
print_top("Blocks per Game", top_blocks)
print_top("Steals per Game", top_steals)


