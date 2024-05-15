import datetime

import pandas as pd
from pandas import DataFrame
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor

from utils import quarter

usage = pd.read_csv('resources/power_usage_2016_to_2020.csv', sep=',')
weather = pd.read_csv('resources/weather_2016_2020_daily.csv', sep=',').drop(columns=["Day", "day_of_week"])
weather["date"] = weather["Date"]
weather = weather.drop(columns=["Date"])



usage["weekend"] = usage["notes"].map(lambda x: 1 if x == "weekend" else 0)
usage["date"] = pd.to_datetime(usage["StartDate"]).map(lambda x: x.date())

df: DataFrame = usage[["date","weekend", "value"]].groupby(["date", "weekend"]).sum()
df = df.reset_index()
df["quarter"] = df["date"].map(lambda x: quarter(x)).astype(int)
df["month"] = df["date"].map(lambda x: x.month).astype(int)
df["day"] = df["date"].map(lambda x: x.day).astype(int)
df["value"] = df["value"].astype(float)
df["weekend"] = df["weekend"].astype(int)

dataset = df.merge(weather, on=["date"], how="left")


Y = dataset["value"]
X = dataset.drop(columns=["value", "date"])
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=1)


input_features_number = len(X_train.columns)

model = DecisionTreeRegressor(random_state=10)
model.fit(X_train, Y_train)
print(model.score(X_test, Y_test))


from joblib import dump
dump(model, 'resources/model_weather.joblib')

# model2 = load('resources/model.joblib')
# predicted2 = model2.predict(X_test)
# mseV = model2.score(X_test, Y_test)
# print(mseV)