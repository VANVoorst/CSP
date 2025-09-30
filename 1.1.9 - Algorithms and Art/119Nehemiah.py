import turtle as trtl
#function to scale coords
def scale_shape(name, coords, scale):
    scaled = tuple((x * scale, y * scale) for x, y in coords)
    trtl.addshape(name, scaled)

#import/make custom turtles 
trtl.addshape("six", ((0,8), (-2,7.7), (-3,6.8), (-4,5), (-3.8,3), (-2,2.5), (-1,2.7), (0,3), (0,4), (-1.5,5), (-1,6), (0,7), (-2,4), (-1,4), (-1,3), (-1,3))) #6
trtl.addshape("seven", ((0,7), (-4,7), (3.8,5), (-2,3), (-1,2), (0,2), (0,3), (-1,5), (0,5))) #7
trtl.addshape("I", ((3,-2), (0,-2), (-3,-2), (0,-2), (0,7), (3,7), (0,7), (-3,7))) #i
#coords
six_coords = ((0,8), (-2,7.7), (-3,6.8), (-4,5), (-3.8,3), (-2,2.5), (-1,2.7), (0,3), (0,4), (-1.5,5), (-1,6), (0,7), (-2,4), (-1,4), (-1,3), (-1,3))
seven_coords = ((0,7), (-4,7), (3.8,5), (-2,3), (-1,2), (0,2), (0,3), (-1,5), (0,5))
I_coords = ((3,-2), (0,-2), (-3,-2), (0,-2), (0,7), (3,7), (0,7), (-3,7))
#scale factors
scale_factor = 2
scale_shape("six", six_coords, scale_factor)
scale_shape("seven", seven_coords, scale_factor)
scale_shape("I", I_coords, scale_factor)



#color list
turtle_shapes = ["six", "seven", "I", "six", "seven", "I"]
turtle_colors = ["red", "blue", "green", "orange", "purple", "gold"]
my_turtles = []

#trtl colors and shape 
for s in turtle_shapes:
  t = trtl.Turtle(shape=s)
  t.penup()
  my_turtles.append(t)

#start postion 1
startx = 0
starty = 0

#trtl movemnet
for t in my_turtles:
  t.goto(startx, starty)
  t.pendown()
  t.right(180)     
  t.forward(50)
  startx = startx + 50
  starty = starty + 50

wn = trtl.Screen()
wn.mainloop()