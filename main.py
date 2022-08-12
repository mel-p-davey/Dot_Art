import colorgram
from turtle import Turtle, Screen
import random

# colors = colorgram.extract("image.jpg", 25)

# Color_List = []
# count =0

# for i in colors:
#     current_colour = colors[count]
#     count+=1
#     current_rgb = current_colour.rgb
#     r = current_rgb[0]
#     g = current_rgb[1]
#     b = current_rgb[2]
#     tup_col = (r, g, b)
#     Color_List.append(tup_col)

# print(Color_List)

color_list = [(190, 150, 89), (115, 40, 33), (231, 213, 119), (106, 43, 48), (216, 225, 231), (100, 120, 17), (50, 81, 109), (104, 75, 91), (104, 152, 199), (113, 176, 159), (57, 54, 53), (179, 150, 68), (43, 74, 51), (41, 63, 95), (242, 237, 240), (168, 201, 212), (60, 86, 66), (38, 67, 45), (80, 36, 40), (173, 150, 155), (35, 55, 83), (167, 113, 104), (172, 204, 192)]

screen = Screen()
screen.colormode(255)


timmy = Turtle()
timmy.ht()
timmy.penup()
timmy.goto(-200,-200)

for i in range(10):
    for i in range(10):
        randcolour = random.choice(color_list)
        timmy.dot(20, randcolour)
        timmy.fd(50)
    timmy.bk(500)
    timmy.left(90)
    timmy.fd(50)
    timmy.right(90)




screen.exitonclick()

