import sys
import datetime
# First python exercise 
# Source for this exercise: https://www.w3resource.com/python-exercises/python-basic-exercises.php
# Write a Python program to print the following string in a specific format 
omagad = 'Twinkle, twinkle little star, \n\t How i wonder what you are! \n\t\t Up above the world so high, \n\t\t Like a Diamond in the sky. \n Twinkle-twinkle little star, \n\t How i wonder what you are'
print(omagad)
# Write a Python program to find out what version of Python you are using.
print(sys.version)
# Write a Python program to display the current date and time.
tanggaldanwaktu = datetime.datetime.now()
print(tanggaldanwaktu.strftime("%Y-%m-%d %H:%M:%S"))