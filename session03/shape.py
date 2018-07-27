from turtle import *

shape('turtle')
colors = ['red', 'blue', 'brown', 'yellow', 'grey']
color_i = 0

for shape in range(3,8):
    color(colors[color_i])
    forward(100)
    for i in range(shape - 1):
        left(360 / shape)
        forward(100)
    left(360 / shape)
    color_i += 1
        
mainloop()