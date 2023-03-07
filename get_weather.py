import requests
import os
from dotenv import load_dotenv

# get zip code and API key from .env file.
# if running locally and not distributing, you can just set them here.
# you can grab an API key from open weather here:
# https://home.openweathermap.org/users/sign_up
load_dotenv()
ZIP = os.getenv('ZIP')
API_KEY = os.getenv('API_KEY')

api_url = "https://api.openweathermap.org/data/2.5/weather?zip="+ZIP+"&appid="+API_KEY
response = requests.get(api_url)
print(response.json())

# response from openweathermap has lots of interesting data.
# since there are only 4 forms of Castform (normal, sunny, rainy, snowy)
# we should designate certain ranges that OWM returns in weather->main
# to react appropriately to the weather.

# Group 2xx - Thunderstorm >>> 'Rainy'
# Group 3xx - Drizzles >>> 'Rainy'
# Group 5xx - Rain >>> 'Rainy'
# Group 6xx - Snow >>> 'Snowy'
# Group 7xx - Atmosphere (mist, haze, fog, etc) >>> 'Normal'
# Group 800 - Clear >>> 'Sunny'
# Group 80x - Clouds >>> 'Normal'

# notable - 801 == 11-25% clouds (partly cloudy) and 802 == 25-50% clouds,
# which I think I will count as Sunny Castform as it may not be marked
# "Clear sky" very often and therefore not showing Sunny form much.
