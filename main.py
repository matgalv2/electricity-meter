from fastapi import FastAPI


from model import Tariff, Accounting, UserID
from fastapi.middleware.cors import CORSMiddleware
from service import Service

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/users/{userID}")
async def get_user(userID: UserID):
    return Service.getUser(userID)


@app.get("/users/{userID}/settings")
async def get_user(userID: UserID):
    return Service.getUserSettings(userID)

@app.get("/users")
async def get_users():
    return Service.getAll()

@app.post("/users/{userID}/change-tariff")
async def change_tariff(userID: UserID, tariff: Tariff):
    return {"updated": Service.updateUserTariff(userID, tariff)}

@app.post("/users/{userID}/change-accounting")
async def change_accounting(userID: UserID, accounting: Accounting):
    return {"updated": Service.updateUserAccounting(userID, accounting)}


@app.get("/users/{userID}/get-usage")
async def get_usage(userID: UserID):
    return Service.getLastNDaysUsage(7)


@app.get("/users/{userID}/get-predicted-usage")
async def get_predicted_usage(userID: UserID):
    return Service.getNDaysPredictedUsage(7, True)

@app.get("/users/{userID}/get-future-usage")
async def get_predicted_usage(userID: UserID):
    return Service.getNDaysPredictedUsage(7)

