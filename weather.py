import requests
import sys
import time
import os

def write(text, delay=0.01, newline=True):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    if newline:
        sys.stdout.write("\n")
        sys.stdout.flush()


def get_weather(city_name, api_key):
    base_url = "http://api.weatherapi.com/v1/current.json"
    complete_url = f"{base_url}?key={api_key}&q={city_name}&aqi=no"
    #http://api.weatherapi.com/v1/current.json?key=12c6187643f94fa1abe65823252210&q=sydney&aqi=no
    response = requests.get(complete_url)
    data = response.json()

    if "current" in data:
        current = data["current"]
        location = data["location"]
        temperature = current["temp_c"]
        feels_like = current["feelslike_c"]
        humidity = current["humidity"]
        UV = current["uv"]
        weather_description = current["condition"]["text"]
        vis = current["vis_km"]

        write(f"Weather in {location['name']}, {location['region']}, {location['country']} at {location['localtime']}:")
        write(f"Temperature: {temperature}°C")
        write(f"Feels like: {feels_like}°C")
        write(f"Condition: {weather_description}")
        write(f"Humidity: {humidity}%")
        write(f"Visibility: {vis} km")
        write(f"UV: {UV}")
    else:
        write("City not found or an error occurred.")

api_key = "12c6187643f94fa1abe65823252210"
weather = """██╗    ██╗███████╗ █████╗ ████████╗██╗  ██╗███████╗██████╗ 
██║    ██║██╔════╝██╔══██╗╚══██╔══╝██║  ██║██╔════╝██╔══██╗
██║ █╗ ██║█████╗  ███████║   ██║   ███████║█████╗  ██████╔╝
██║███╗██║██╔══╝  ██╔══██║   ██║   ██╔══██║██╔══╝  ██╔══██╗
╚███╔███╔╝███████╗██║  ██║   ██║   ██║  ██║███████╗██║  ██║
 ╚══╝╚══╝ ╚══════╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
 """
write(f"\033[96m{weather}\033[0m", 0.001)
city = input("Enter city name: ")
get_weather(city, api_key)
