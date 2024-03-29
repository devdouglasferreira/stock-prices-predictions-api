from fastapi import APIRouter
from stockpredictions.services import PredictionService
from stockpredictions.services.service_models.model_responses import PredictNextDayResponse


prediction_router = APIRouter()
prediction_service = PredictionService()

@prediction_router.get('/prediction/nextday/{ticker}',  response_model=PredictNextDayResponse, tags=['Prediction'])
async def predict_next_day(ticker: str, save_log: bool = False):
    return prediction_service.predict_next_day(ticker, save_log)

# @prediction_router.get('/predict/nextweek/{ticker}', tags=['Prediction'])
# async def predic_next_week(ticker: str):
#     return { "Message" : "Not implemented"}
#     # return prediction_service.predict_next_day(ticker)

# @prediction_router.get('/predict/nextmonth/{ticker}', tags=['Prediction'])
# async def predic_next_month(ticker: str):
#     return { "Message" : "Not implemented"}
#     # return prediction_service.predict_next_day(ticker)
