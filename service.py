from datetime import datetime, timedelta
from typing import List, Any, Dict

import pandas as pd

from dao import Dao
from model import UserID, Tariff, Accounting
from joblib import load

from utils import quarter


class Service(object):
    __model = load('resources/model.joblib')
    __usage = pd.read_csv("resources/usage.csv", sep=',')
    __usage["date"] = pd.to_datetime(__usage["date"])

    @staticmethod
    def getUser(userID: UserID):
        return Dao.getUser(userID)

    @staticmethod
    def getAll():
        return Dao.getAll()

    @staticmethod
    def getUserSettings(userID: UserID):
        return Dao.getUserSettings(userID)

    @staticmethod
    def updateUserAccounting(userID: UserID, accounting: Accounting) -> bool:
        return Dao.updateUserAccounting(userID, str(accounting.accountingType))

    @staticmethod
    def updateUserTariff(userID: UserID, tariff: Tariff) -> bool:
        return Dao.updateUserTariff(userID, str(tariff.tariffType))

    @classmethod
    def getLastNDaysUsage(cls, n: int = 7) -> List[Dict[str, str | int]]:
        datetime_object = datetime.strptime("2016-06-18 00:00:00", '%Y-%m-%d %H:%M:%S')
        dates = [(datetime_object - timedelta(days=i)).date() for i in range(n)]

        usage_from_range = cls.__usage[cls.__usage["date"].isin(dates)]
        data = []
        for i in range(len(usage_from_range.values)):
            data.append({
                "date": usage_from_range.iloc[i]["date"].strftime('%Y-%m-%d'),
                "value": round(usage_from_range.iloc[i]["value"], 3)
            })

        return data

    @classmethod
    def getNDaysPredictedUsage(cls, n: int = 7, previous=False) -> List[Dict[str, str | int]]:
        datetime_object = datetime.strptime("2016-06-18 00:00:00", '%Y-%m-%d %H:%M:%S')
        dates = [(datetime_object - timedelta(days=i) if previous else datetime_object + timedelta(days=i)).date() for i
                 in range(n)]
        x = []
        for date in dates:
            weekend = 1 if date.weekday() in (5, 6) else 0
            quarter_ = quarter(date)
            x.append([weekend, quarter_, date.month, date.day])

        predicted_values = cls.__model.predict(x)
        return [
            {
                "date": dates[i],
                "value": round(predicted_values[i],3)
            } for i in range(len(predicted_values))
        ]


print(Service.getNDaysPredictedUsage(7, False))
