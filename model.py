from datetime import datetime

from pydantic import BaseModel
from enum import Enum

UserID = int
# class TariffType(Enum):
#     G11 = 'G11',
#     G12 = 'G12',
#     G13 = 'G13'
#
#     @staticmethod
#     def fromStr(tariffType: str):
#         match tariffType:
#             case 'TariffType.G11': return TariffType.G11
#             case 'TariffType.G12': return TariffType.G12
#             case 'TariffType.G13': return TariffType.G13


class Tariff(BaseModel):
    # tariffType: TariffType
    tariffType: str


# class AccountingType(Enum):
#     PER_MONTH = "PER_MONTH",
#     PER_2_MONTHS = "PER_2_MONTHS",
#     PER_6_MONTHS = "PER_6_MONTHS",
#
#     @staticmethod
#     def fromStr(accountingType: str):
#         match accountingType:
#             case 'AccountingType.PER_MONTH': return AccountingType.PER_MONTH
#             case 'AccountingType.PER_2_MONTHS': return AccountingType.PER_2_MONTHS
#             case 'AccountingType.PER_6_MONTHS': return AccountingType.PER_6_MONTHS


class Accounting(BaseModel):
    # accountingType: AccountingType
    accountingType: str


class User(BaseModel):
    userID: int
    tariff: Tariff
    accounting: Accounting

class Usage(BaseModel):
    lastDays: int
    previous: bool

