import pandas as pd

url = "https://raw.githubusercontent.com/guipsamora/pandas_exercises/master/02_Filtering_%26_Sorting/Euro12/Euro_2012_stats_TEAM.csv"

euro12 = pd.read_csv(url, sep=",")

print("Goals:")
print(euro12["Goals"])

num_teams = len(euro12["Team"].unique())
print("Number of unique teams:")
print(num_teams)

num_columns = len(euro12.columns)
print("Number of columns:")
print(num_columns)

discipline = euro12[["Team", "Yellow Cards", "Red Cards"]]
discipline = discipline.sort_values(["Red Cards", "Yellow Cards"], ascending=False)
print("Discipline:")
print(discipline)

mean_yellow_cards = euro12["Yellow Cards"].mean()
print("Mean yellow cards:")
print(mean_yellow_cards)

high_scoring_teams = euro12[euro12["Goals"] > 6]
print("High scoring teams:")
print(high_scoring_teams)

g_teams = euro12[euro12["Team"].str.startswith("G")]
print("Teams starting with 'G':")
print(g_teams)

first_7_cols = euro12.iloc[:, :7]
print("First 7 columns:")
print(first_7_cols)

all_cols_except_last_3 = euro12.iloc[:, :-3]
print("All columns except last 3:")
print(all_cols_except_last_3)

relevant_cols = ["Team", "Shooting Accuracy"]
relevant_teams = euro12[euro12["Team"].isin(["England", "Italy", "Russia"])]
shooting_accuracy = relevant_teams[relevant_cols]
print("Shooting accuracy for relevant teams:")
print(shooting_accuracy)
