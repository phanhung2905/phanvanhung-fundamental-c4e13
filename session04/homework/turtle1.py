from turtle import *
shape("turtle")
color("blue")

for i in range( 30 ):
    for z in range(4):
        forward(100)
        right(90)
    left(360/30)
mainloop()