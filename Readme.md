# WeatherMCP

A simple FastAPI service to get current weather and forecast data using the WeatherAPI.com API.

## Setup

1. **Clone or download this repository.**

2. **Install dependencies:**
   ```
   pip install fastapi uvicorn requests python-dotenv
   ```

3. **Create a `.env` file** in the project directory with your WeatherAPI key:
   ```
   WEATHERAPI_KEY=your_api_key_here
   ```

4. **Run the server:**
   ```
   python weatherAPI.py
   ```
   or (recommended for development):
   ```
   uvicorn weatherAPI:app --reload
   ```

## Endpoints

### Get Current Weather

- **POST** `/get_weather`
- **Body (JSON):**
  ```json
  {
    "city": "Istanbul"
  }
  ```
- **Response:**
  ```json
  {
    "city": "Istanbul",
    "country": "Turkey",
    "temperature_c": 20.3,
    "condition": "Partly cloudy",
    "humidity": 68
  }
  ```

### Get Weather Forecast

- **POST** `/get_forecast`
- **Body (JSON):**
  ```json
  {
    "city": "Istanbul",
    "days": 7
  }
  ```
  - `days` can be from 1 to 14.
- **Response:**
  ```json
  {
    "city": "Istanbul",
    "country": "Turkey",
    "forecast": [
      {
        "date": "2025-10-02",
        "avg_temp_c": 20.3,
        "condition": "Partly cloudy",
        "humidity": 68
      },
      ...
    ]
  }
  ```

## API Documentation

Visit [http://localhost:8000/docs](http://localhost:8000/docs) for interactive Swagger UI.

---
```# WeatherAPI

A simple FastAPI service to get current weather and forecast data using the WeatherAPI.com API.

## Setup

1. **Clone or download this repository.**

2. **Install dependencies:**
   ```
   pip install fastapi uvicorn requests python-dotenv
   ```

3. **Create a `.env` file** in the project directory with your WeatherAPI key:
   ```
   WEATHERAPI_KEY=your_api_key_here
   ```

4. **Run the server:**
   ```
   python weatherAPI.py
   ```
   or (recommended for development):
   ```
   uvicorn weatherAPI:app --reload
   ```

## Endpoints

### Get Current Weather

- **POST** `/get_weather`
- **Body (JSON):**
  ```json
  {
    "city": "Istanbul"
  }
  ```
- **Response:**
  ```json
  {
    "city": "Istanbul",
    "country": "Turkey",
    "temperature_c": 20.3,
    "condition": "Partly cloudy",
    "humidity": 68
  }
  ```

### Get Weather Forecast

- **POST** `/get_forecast`
- **Body (JSON):**
  ```json
  {
    "city": "Istanbul",
    "days": 7
  }
  ```
  - `days` can be from 1 to 14.
- **Response:**
  ```json
  {
    "city": "Istanbul",
    "country": "Turkey",
    "forecast": [
      {
        "date": "2025-10-02",
        "avg_temp_c": 20.3,
        "condition": "Partly cloudy",
        "humidity": 68
      },
      ...
    ]
  }
  ```

## API Documentation

Visit [http://localhost:8000/docs](http://localhost:8000/docs) for interactive Swagger UI.

---