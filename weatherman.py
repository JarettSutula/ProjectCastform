import utils

# This will serve as the main script that runs at a set interval
# and changes the Castform form if the api call returns something
# different than the previous one.
# print(utils.get_weather(True))
weather = utils.get_weather(False)
utils.move_file(weather)