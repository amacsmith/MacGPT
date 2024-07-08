import random
import requests

def get_weather(longitude, latitude) -> str:
    
    if not longitude or not latitude:
        return "longitude and or latitude was not set."
    
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m,wind_speed_10m",
        "hourly": "temperature_2m,relative_humidity_2m,wind_speed_10m"
    }
    
    response = requests.get(url, params=params)
    # Rest of the code...
    # Check if the request was successful
    if response.status_code == 200:
        # Extract the relevant weather information from the response
        weather_data = response.json()
        temperature = weather_data["current"]["temperature_2m"]
        condition = weather_data["current"]["weathercode"]
        return f"The weather in {location} is {condition} with a temperature of {temperature}°C."
    else:
        return "Failed to retrieve weather information."