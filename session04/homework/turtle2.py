from turtle import *

speed(-1)
shape("turtle")
color("blue")


right(130)
x = 40
y = 200



for i in range(x):
    
    for k in range(4):
        forward(y)
        right(90)
        
    right(360/x)
    y -= 5

mainloop()