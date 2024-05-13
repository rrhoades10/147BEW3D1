# Using modules in python
# imports should be at the top of the file for ease of access and readability
# ======== YOU WILL ONLY USE ONE VERSION OF THESE IMPORTS =======
import math # import the entirety of the math module
from math import sqrt as sq # importing specific functions with an alia
# alias - renaming the function we're importing for readability or ease or use

import datetime as dt # import the entirety of the datetime module
import os # import the entirety of the os module

import re

# importing a customer module
import modules.geometry as geo #importing the whole custom module
# specific imports separated by a comma
# from geometry import area_rectangle, perimeter_rectangle


# using modules and methods from those modules
#getting the square root of a number using the math module
print(math.sqrt(16)) #4.0
print(math.pi)
print(math.ceil(5.3))

# only import the sqrt 
print(sq(81)) # 9.0

# using the datetime module to get the current time
current_time = dt.datetime.now() #using the dt alias for datetime
print(current_time)
# using re module to reformat the date 
formatted_date = re.sub(r"(\d{4})-(\d{2})-(\d{2})", r"\2/\3/\1", str(current_time))
print(formatted_date)

# using the os module to get the current working directory
os.getcwd()


# using modules to make our code easier to write and read
print(geo.area_rectangle(5, 3))
print(geo.perimeter_rectangle(5, 3))

