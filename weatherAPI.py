from fastapi import FastAPI
from pydantic import BaseModel, Field
import requests
import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env

app = FastAPI()

WEATHERAPI_KEY = os.getenv("WEATHERAPI_KEY")  # Read from .env

class CityRequest(BaseModel):
    city: str
    days: int = Field(default=1, ge=1, le=14, description="Number of forecast days (1-14)")

@app.get("/")
def read_root():
    return {"message": "Welcome to the WeatherAPI Service!"}

@app.post("/get_weather")
def get_weather(request: CityRequest):
    city = request.city
    url = f"http://api.weatherapi.com/v1/current.json?key={WEATHERAPI_KEY}&q={city}&aqi=no"
    response = requests.get(url).json()
    return {
        "city": response["location"]["name"],
        "country": response["location"]["country"],
        "temperature_c": response["current"]["temp_c"],
        "condition": response["current"]["condition"]["text"],
        "humidity": response["current"]["humidity"]
    }

@app.post("/get_forecast")
def get_forecast(request: CityRequest):
    city = request.city
    days = request.days
    url = f"http://api.weatherapi.com/v1/forecast.json?key={WEATHERAPI_KEY}&q={city}&days={days}&aqi=no&alerts=no"
    response = requests.get(url).json()
    forecast_days = response.get("forecast", {}).get("forecastday", [])
    forecast_list = []
    for day in forecast_days:
        forecast_list.append({
            "date": day["date"],
            "avg_temp_c": day["day"]["avgtemp_c"],
            "condition": day["day"]["condition"]["text"],
            "humidity": day["day"]["avghumidity"]
        })
    return {
        "city": response["location"]["name"],
        "country": response["location"]["country"],
        "forecast": forecast_list
    }

if __name__ == "__main__": 
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)