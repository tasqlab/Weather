import requests
import sys
import time
import os
import pyfiglet
from pyfiglet import FigletFont
from ascii_magic import AsciiArt

def resource_path(filename):
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, filename)

my_art = AsciiArt.from_image(resource_path('weather.png'))
my_art.to_terminal(columns=60)
RED = "\033[31m"
GREEN = "\033[32m"
BLUE = "\033[34m"
RESET = "\033[0m"
BOLD = "\033[1m"
UNDERLINE = "\033[4m"
mytime = time.localtime()


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
        location = data["location"]
        ascii_art = pyfiglet.figlet_format(f"{location['name']}, {location['region']}", font="ansi")
        current = data["current"]
        temperature = current["temp_c"]
        feels_like = current["feelslike_c"]
        humidity = current["humidity"]
        UV = current["uv"]
        weather_description = current["condition"]["text"]
        vis = current["vis_km"]
        if mytime.tm_hour < 6 or mytime.tm_hour > 18:
             icon = AsciiArt.from_image(resource_path('night.png'))
        else:
             icon = AsciiArt.from_image(resource_path('morning.png'))

        write(f"{GREEN}Weather in \n {ascii_art}, {location['country']} at {location['localtime']}:{RESET}", 0.001)
        write(f"Temperature: {temperature}°C")
        write(f"Feels like: {feels_like}°C")
        write(f"Condition: {weather_description}")
        icon.to_terminal(columns=30)
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
input("Press enter to continue")
