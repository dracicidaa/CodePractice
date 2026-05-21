#The purpose of this code is to figure out how to render text and images to a display
#resolution agnostic
#Default screen resolution will be 1920 x 1080 internally, but should correctly size to whatever
#the monitor resolution is

#importations
import sys, pygame

pygame.init()

#setting internal resolution
int_width = 1920
int_height = 1080

#setting initial window size, can be ignored when drawing full screen
window_width = 640
window_height = 480

#Can put whatever else is needed for the program
