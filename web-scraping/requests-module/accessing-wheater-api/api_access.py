import requests
from dotenv import dotenv_values

# Get temperature in Kelvin, Celsius and Fahrenheit for a given city and state/country using OpenWeatherMap API.

config = dotenv_values('.env')
API_KEY = config.get('OPEN_WEATHER_MAP_API_KEY')

city_name, state_code, country_code = "San Francisco", "CA", "US"

geo_data = requests.get(
    f"https://api.openweathermap.org/geo/1.0/direct?q={city_name},{state_code},{country_code}&appid={API_KEY}"
).json()

lat = geo_data[0]["lat"]
lon = geo_data[0]["lon"]

weather_data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}"
).json()

temp_kelvin = weather_data["main"]["temp"]

print(f"{city_name}, {state_code}, {country_code}")
print(f"Latitude: {lat}")
print(f"Longitude: {lon}\n")
print(f"Temperature in Kelvin: {temp_kelvin}")
print(f"Temperature in Celsius: {round(temp_kelvin - 273.15, 1)}")
print(f"Temperature in Fahrenheit: {round(temp_kelvin * 9/5 - 459.67, 1)}")