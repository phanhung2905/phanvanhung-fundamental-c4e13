from turtle import *

shape('turtle')
colors = ['red', 'blue', 'brown', 'yellow', 'grey']
colors_i = 0

for rect in range(5):
    count = 4
    color(colors[colors_i])
    begin_fill()
    while count > 0:
        count -= 1
        if count % 2 == 1:        
            forward(45)
            left(90)
        else:
            forward(80)
            left(90)
    end_fill()
    forward(45)
    colors_i += 1

mainloop()