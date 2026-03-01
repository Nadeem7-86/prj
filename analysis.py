import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -----------------------------
# Load Data
# -----------------------------
def load_data(path):
    try:
        df = pd.read_csv(path)
        print("Data loaded successfully ✅")
        return df
    except Exception as e:
        print("Error loading file:", e)
        return None

# -----------------------------
# Batting Analysis
# -----------------------------
def batting_analysis(df):
    print("\n--- Batting Analysis ---")

    df["strike_rate"] = (df["runs"] / df["balls"]) * 100
    df["strike_rate"] = df["strike_rate"].fillna(0)

    top_batsmen = df.groupby("player")["runs"].sum().sort_values(ascending=False).head(5)

    print("\nTop 5 Run Scorers:")
    print(top_batsmen)

    plt.figure()
    sns.barplot(x=top_batsmen.values, y=top_batsmen.index)
    plt.title("Top 5 Run Scorers")
    plt.xlabel("Runs")
    plt.ylabel("Player")
    plt.tight_layout()
    plt.show()

# -----------------------------
# Bowling Analysis
# -----------------------------
def bowling_analysis(df):
    print("\n--- Bowling Analysis ---")

    df["economy_rate"] = df["runs_conceded"] / df["overs"]
    df["economy_rate"] = df["economy_rate"].replace([float("inf")], 0)
    df["economy_rate"] = df["economy_rate"].fillna(0)

    top_bowlers = df.groupby("player")["wickets"].sum().sort_values(ascending=False).head(5)

    print("\nTop 5 Wicket Takers:")
    print(top_bowlers)

    plt.figure()
    sns.barplot(x=top_bowlers.values, y=top_bowlers.index)
    plt.title("Top 5 Wicket Takers")
    plt.xlabel("Wickets")
    plt.ylabel("Player")
    plt.tight_layout()
    plt.show()

# -----------------------------
# Team Performance
# -----------------------------
def team_performance(df):
    print("\n--- Team Performance ---")

    team_runs = df.groupby("team")["runs"].sum()

    print("\nTotal Runs by Team:")
    print(team_runs)

    plt.figure()
    team_runs.plot(kind="bar")
    plt.title("Team Total Runs")
    plt.ylabel("Runs")
    plt.tight_layout()
    plt.show()

# -----------------------------
# Main Function
# -----------------------------
def main():
    df = load_data("data/t20_data.csv")
    if df is not None:
        batting_analysis(df)
        bowling_analysis(df)
        team_performance(df)

if __name__ == "__main__":
    main()