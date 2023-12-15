<img src="https://github.com/JarettSutula/Weatherman119/assets/31451228/d45cc503-40c4-405f-9c9f-780b3d29711f" alt="banner">

A python script that reads data from a weather API and displays a hologram-style Castform using optical illusions using a Raspberry Pi.

<p align="center">
  <img src="https://github.com/JarettSutula/Weatherman119/assets/31451228/34e72f47-c32e-4ff8-876e-4176a06fa137" alt="sunny castform" align="center"/>
  <img src="https://github.com/JarettSutula/Weatherman119/assets/31451228/b0fe1650-103e-41b8-95dc-dbdb3edcf517" alt="rainy castform"/>
</p>

# Design and Inspiration
I was inspired by a FANTASTIC video by Josua Ellingson [here](https://www.youtube.com/watch?v=eB4kup3oKY0) that goes into depth on how to set up a popular optical illusion called **Pepper's Ghost**.
Disney has used these types of illusions to make a realistic emulation of a hologram (which a proper one is well out of my budget) and I thought this would be a cool approach. The idea for Castform came directly from [Jamie Nelsn](https://www.tiktok.com/@jme.nelsn) on TikTok, I take no credit for the idea, only the implementation that I've created here.

# Materials and How It Works
- Raspberry Pi 4 Model B
- Waveshare 4 inch 720x720 touch screen found [here](https://www.waveshare.com/4inch-dpi-lcd-c.htm)
- Some sort of transparency film that will be clear but have a little bit of rigidity to place at a 45 degree angle inside the jar (I used overhead projector clear sheets)
- A Cloche Dome / Bell Jar (I used [this particular one](https://www.amazon.com/gp/product/B09K3NX9KW/ref=ppx_yo_dt_b_search_asin_title?ie=UTF8&th=1) that fit well for the size of the screen)
- mp4s/h264s of Castform - I made my own that loop incredibly well and fluid, you are welcome to have them if you are looking to replicate this.

I signed up for a free key from [OpenWeatherAPI](https://openweathermap.org/api) that more than covers a 2 minute polling interval for 24/7 usage. When **weatherman.py** is called, it gets a weather report response given an api key and a zipcode declared in a local .env file.
I have a folder called **playing** that has the current form of Castform (defaults to normal) and another folder called **videos** that holds the other .h264 files of Castform's forms - when the weather switches, the script brings the video file in **playing** and moves it to **videos**, and then moves the appropriate form video into the playing folder.

I'm using [pi_video_looper](https://github.com/adafruit/pi_video_looper) which is a fantastic resource for this sort of project - with the .h264 files, it produces a sub .5s transition between switching forms, which is more than enough for my satisfaction. I have a crontab schedule that runs **weatherman.py** every 2 minutes and I am very satisified with the result. The 

If you have any questions or ideas please make an issue and let me know! I'm planning to make a sleeping version after certain times and maybe even a small chance the castform will spawn shiny.
