from turtle import *
shape("classic")
color("green")
speed(-1)
n = 50
for i in range (n):
    circle(100)
    left(360/n)

mainloop()