from datetime import datetime


def quarter(date: datetime):
    if date.month in (1, 2, 3):
        return 1
    elif date.month in (4, 5, 6):
        return 2
    elif date.month in (7,8,9):
        return 3
    else:
        return 4