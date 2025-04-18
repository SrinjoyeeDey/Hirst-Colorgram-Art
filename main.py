# import colorgram

# # Extract 6 colors from an image.
# rgb_colors=[]
# colors = colorgram.extract('image.jpeg', 30)

# for color in colors:
#     r=color.rgb.r
#     g=color.rgb.g
#     b=color.rgb.b
#     new_color=(r,g,b)
#     rgb_colors.append(new_color)

import turtle as turtle_module
tim=turtle_module.Turtle()
screen=turtle_module.Screen()
tim.speed("fastest")
tim.penup()
tim.hideturtle()

import random
turtle_module.colormode(255)

color_list=[(208, 163, 109), (21, 28, 56), (141, 61, 93), (226, 207, 130), (207, 130, 145), (84, 116, 98), (211, 78, 104), (61, 92, 138), (129, 152, 141), (69, 22, 41), (125, 34, 56), (41, 52, 104),
(141, 74, 57), (226, 181, 165), (138, 156, 176),(229, 163, 178), (93, 126, 171), (114, 135, 123), (183, 189, 208),
(175, 112, 97), (39, 82, 63), (184, 197, 188), (199, 119, 51), (26, 59, 54), (44, 69, 78), (117, 132, 136)]

tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots=100

for dot_count in range(1,number_of_dots+1):
    tim.dot(20,random.choice(color_list))
    tim.forward(50)

    if dot_count%10==0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)







screen.exitonclick()