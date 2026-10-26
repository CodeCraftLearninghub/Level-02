import requests

# Step 1: Define the API URL
url = "https://api.open-meteo.com/v1/forecast"

# Step 2: Specify the location and weather details
params = {
    "latitude": 17.6868,
    "longitude": 83.2185,
    "current": [
        "temperature_2m",
        "relative_humidity_2m",
        "apparent_temperature",
        "precipitation",
        "weather_code",
        "wind_speed_10m"
    ]
}

# Step 3: Send a request to the API
response = requests.get(url, params=params, timeout=10)

# Step 4: Check whether the request was successful
response.raise_for_status()

# Step 5: Convert the API response into Python data
data = response.json()

# Step 6: Extract the current weather information
weather = data["current"]

temperature = weather["temperature_2m"]
humidity = weather["relative_humidity_2m"]
feels_like = weather["apparent_temperature"]
wind_speed = weather["wind_speed_10m"]
rain = weather["precipitation"]
weather_code = weather["weather_code"]

# Step 7: Display the weather report
print("================================")
print("      WEATHER REPORT")
print("================================")
print("Location: Visakhapatnam")
print("Temperature:", temperature, "°C")
print("Feels Like:", feels_like, "°C")
print("Humidity:", humidity, "%")
print("Wind Speed:", wind_speed, "km/h")
print("Precipitation:", rain, "mm")
print("Weather Code:", weather_code)
print("================================")







