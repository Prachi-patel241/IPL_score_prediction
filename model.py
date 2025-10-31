import pandas as pd
import pickle
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

data = pd.read_csv("ipl_data.csv")

X = data[["runs", "wickets", "overs", "runs_last_5", "wickets_last_5"]]
y = data["total_score"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

with open("ipl_score_model.pkl", "wb") as f:
    pickle.dump(model, f)
    