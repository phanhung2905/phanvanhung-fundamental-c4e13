from turtle import *

speed(-1)
shape("turtle")
color("blue")


right(130)
y = 200



for i in range(40):
    
    for k in range(4):
        forward(y)
        right(90)
        
    right(360/40)
    y -= 5

mainloop()
