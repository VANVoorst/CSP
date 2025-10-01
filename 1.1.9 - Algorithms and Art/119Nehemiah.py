import turtle as trtl
#function to scale coords
def scale_shape(name, coords, scale):
    scaled = tuple((x * scale, y * scale) for x, y in coords)
    trtl.addshape(name, scaled)

#import/make custom turtles 
trtl.addshape("six", ((0,8), (-2,7.7), (-3,6.8), (-4,5), (-3.8,3), (-2,2.5), (-1,2.7), (0,3), (0,4), (-1.5,5), (-1,6), (0,7), (-2,4), (-1,4), (-1,3), (-1,3))) #6
trtl.addshape("seven", ((0,7), (-4,7), (3.8,5), (-2,3), (-1,2), (0,2), (0,3), (-1,5), (0,5))) #7
trtl.addshape("I", ((3,-2), (0,-2), (-3,-2), (0,-2), (0,7), (3,7), (0,7), (-3,7))) #i
trtl.addshape("person", ((-3,-1), (0,2), (3,-1), (0,5), (-3,5), (3,5), (0,7), (1,7), (2,9), (0,11), (-2,9), (-1,7)))

#coords
six_coords = ((0,8), (-2,7.7), (-3,6.8), (-4,5), (-3.8,3), (-2,2.5), (-1,2.7), (0,3), (0,4), (-1.5,5), (-1,6), (0,7), (-2,4), (-1,4), (-1,3), (-1,3))
seven_coords = ((0,7), (-4,7), (3.8,5), (-2,3), (-1,2), (0,2), (0,3), (-1,5), (0,5))
I_coords = ((3,-2), (0,-2), (-3,-2), (0,-2), (0,7), (3,7), (0,7), (-3,7))
person_coords = ((-3,-1), (0,2), (3,-1), (0,5), (-3,5), (3,5), (0,7), (1,7), (2,9), (0,11), (-2,9), (-1,7))

#scale factors
scale_factor = 2
scale_shape("six", six_coords, scale_factor)
scale_shape("seven", seven_coords, scale_factor)
scale_shape("I", I_coords, scale_factor)
scale_shape("person", person_coords, scale_factor)
# ask user for colors
turtle_colors = []
while True:
    color_input = input("Enter a color 6 is the max number (or type 'done' to finish): ")
    if color_input.lower() == 'done':
        break
    else:
        turtle_colors.append(color_input)

print("Your final list of colors:", turtle_colors)

# color list
turtle_shapes = ["six", "seven", "I", "person", "seven", "I"]
my_turtles = []

# trtl colors and shape 
for s in turtle_shapes:
    t = trtl.Turtle(shape=s)
    if turtle_colors:
        color = turtle_colors.pop(0)  
    else:
        color = "black" 
    t.color(color)
    t.penup()
    my_turtles.append(t)

# start position
startx = 0
starty = 0

# trtl movement
for t in my_turtles:
    t.goto(startx, starty)
    t.pendown()
    t.right(180)     
    t.forward(50)
    startx = startx + 50
    starty = starty + 50

wn = trtl.Screen()
wn.mainloop()