import datetime

import pandas as pd
from keras import Sequential
from keras.layers import Dense, Flatten
from pandas import DataFrame
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor

from utils import quarter

dataset = pd.read_csv('resources/power_usage_2016_to_2020.csv', sep=',')


dataset["weekend"] = dataset["notes"].map(lambda x: 1 if x == "weekend" else 0)
dataset["date"] = pd.to_datetime(dataset["StartDate"]).map(lambda x: x.date())

df: DataFrame = dataset[["date","weekend", "value"]].groupby(["date", "weekend"]).sum()
df = df.reset_index()
df["quarter"] = df["date"].map(lambda x: quarter(x)).astype(int)
df["month"] = df["date"].map(lambda x: x.month).astype(int)
df["day"] = df["date"].map(lambda x: x.day).astype(int)
df["value"] = df["value"].astype(float)
df["weekend"] = df["weekend"].astype(int)

df.sort_values(by="date").to_csv("resources/usage.csv", index=False)


Y = df["value"]
X = df.drop(columns=["value", "date"])
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=1)


input_features_number = len(X_train.columns)

model = DecisionTreeRegressor(random_state=10)
model.fit(X_train, Y_train)


# from joblib import dump
# dump(model, 'resources/model.joblib')

# model2 = load('resources/model.joblib')
# predicted2 = model2.predict(X_test)
# mseV = model2.score(X_test, Y_test)
# print(mseV)