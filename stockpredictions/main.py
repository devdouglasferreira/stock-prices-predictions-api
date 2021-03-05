
from fastapi import FastAPI
import uvicorn
from routers import prediction_router
from routers import data_router

import mysql.connector
import os

dbConnection = mysql.connector.connect(
            host=os.environ['MYSQL_HOST'],
            user=os.environ['MYSQL_USER'],
            password=os.environ['MYSQL_PASSWORD'],
            database=os.environ['MYSQL_DATABASE'])

cursor = dbConnection.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS StockPricesPrediction;")
cursor.close()
dbConnection.close()

app=FastAPI()
app.description='Stock Prices Predcition API'
app.include_router(prediction_router)
app.include_router(data_router)

@app.get("/")
async def root():
    return {"status": "Application is running. Check /docs"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)