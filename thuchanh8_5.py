from tkinter import *
canvas_width =400
canvas_height=400
python_green = "476042"

def polygon_star(canvas, x,y,p,t, outline=python_green, fill='yellow',width =1):
    points = []
    for i in (1,-1):
        points.extend((x,y+i*p))
        points.extend((x+i*t, y+i*t))
        points.extend((x+i*p, y))
        points.extend((x+i*t, y-i*t))
