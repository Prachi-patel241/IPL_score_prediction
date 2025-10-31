import pandas as pd

# Load your IPL ball-by-ball data
df = pd.read_csv('ballbyball.csv')  # Make sure this matches your file name

ml_rows = []

# Group by match and inning (each team's batting in a game)
for (match_id, inning), group in df.groupby(['match_id', 'inning']):
    group = group.sort_values(['over', 'ball'])
    total_score = group['total_runs'].sum()  # The actual final score for this inning
    max_over = int(group['over'].max())
    # For each over after the 5th
    for over in range(5, max_over + 1):
        so_far = group[group['over'] <= over]
        runs = so_far['total_runs'].sum()
        wickets = so_far['is_wicket'].sum()
        last5 = group[(group['over'] > (over-5)) & (group['over'] <= over)]
        runs_last_5 = last5['total_runs'].sum()
        wickets_last_5 = last5['is_wicket'].sum()
        ml_rows.append([runs, wickets, over, runs_last_5, wickets_last_5, total_score])

# Create and save the DataFrame
ml_df = pd.DataFrame(ml_rows, columns=[
    'runs', 'wickets', 'overs', 'runs_last_5', 'wickets_last_5', 'total_score'
])
ml_df.to_csv('ipl_data.csv', index=False)
print("Saved ML-ready data as ipl_data.csv")