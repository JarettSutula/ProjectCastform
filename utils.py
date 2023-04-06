"""
This file contains util functions for weatherman.py to run.
"""
import requests
import os
import shutil
from dotenv import load_dotenv

def get_weather(debug):
    """
    This function grabs weather data given an .env file with
    a ZIP code and an api key from openweathermap.org. It then returns
    the Castform equivalent string from the current weather at that area.

    :param debug: whether to print ID and description to console
    """
    # get zip code and API key from .env file.
    # if running locally and not distributing, you can just set them here.
    # you can grab an API key from open weather here:
    # https://home.openweathermap.org/users/sign_up
    load_dotenv()
    ZIP = os.getenv('ZIP')
    API_KEY = os.getenv('API_KEY')

    url = "https://api.openweathermap.org/data/2.5/weather?zip="+ZIP+"&appid="+API_KEY
    response = requests.get(url)
    result = response.json()
    weather_report = result['weather'][0]
    weather_id = int(weather_report['id'])
    weather_desc = weather_report['description']

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

    # notable - 801 == 11-25% clouds (partly cloudy) 
    # I think I will count as Sunny Castform as it may not be reported as
    # "clear sky" very often and therefore not showing Sunny form much.
    if(debug):
        print(f'OWM ID is {weather_id}, desc is {weather_desc}.')

    if 200 <= weather_id <= 599:
        return 'rainy'
    elif 600 <= weather_id <= 699:
        return 'snowy'
    elif 800 <= weather_id <= 801:
        return 'sunny'
    else:
        return 'normal'
    
def move_file(weather):
    current_file = os.listdir("./playing")[0]
    current_weather = current_file.split('.')[0]

    # file_format = ".mp4"
    file_format = ".h264"
    
    # if our current weather is the same as the weather being passed in,
    # just leave it be and do nothing. Wait for next call.
    if current_weather == weather:
        # print(f'no need to change - weather is still {weather}')
        pass
    else:
        # move the file back into the 'videos' folder.
        source = f"./playing/{current_file}"
        destination = "./videos"
        # print(source)
        shutil.move(source, destination)

        # pick new video from 'videos'
        new_video = f'{weather}{file_format}'
        new_source = f"./videos/{new_video}"
        # print(new_video, new_source)
        
        # move video from videos --> playing
        new_destination = "./playing"
        shutil.move(new_source, new_destination)
