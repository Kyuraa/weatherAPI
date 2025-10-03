from fastapi import FastAPI
from pydantic import BaseModel, Field
import requests
import os
from dotenv import load_dotenv
from fastapi_mcp import FastApiMCP
from fastapi.middleware.cors import CORSMiddleware


load_dotenv()  # Load environment variables from .env

app = FastAPI() 

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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

# MCP setup - this handles the stdio communication
#mcp = FastApiMCP(app)
#mcp.mount_http()

if __name__ == "__main__":
    # Run as MCP server (stdio mode)
    # This is what Claude desktop will execute
    
    
    # NOTE: If you want to test as a regular HTTP server instead,
    # comment out mcp.run() above and uncomment the lines below:
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8599)