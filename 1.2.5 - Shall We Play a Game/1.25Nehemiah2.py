#   a123_apple_1.py
import turtle as trtl
import random as rand

#-----setup-----
bird_image = "bird2.gif" # Store the file name of your shape
#pear_image = "pear.gif"


wn = trtl.Screen()
wn.setup(width=.7, height=.7)
wn.addshape(bird_image) # Make the screen aware of the new file

#wn.addshape(pear_image)

letter_list = ["A", "B", "C", "D","E"]
current_letter = "A"


drawer = trtl.Turtle()
drawer.hideturtle()
drawer.penup
apple = trtl.Turtle()
apple.penup()
apple.speed(1)
wn.tracer(False)

#-----functions-----
# given a turtle, set that turtle to be shaped by the image file
def reset_apple(active_bird):
  global current_letter
  lenght_of_list= len(letter_list)
  if (lenght_of_list != 0 ):
    index = rand.randint(0, lenght_of_list)
    active_bird.goto(rand.randint(-200,200), 200)
    current_letter = letter_list.pop(index)


def draw_apple(active_apple):
  active_apple.shape(bird_image)
  wn.update()

#apple to fall or move
def drop_apple():
    new_x = rand.randint(-230, 230)
    new_y = rand.randint(-180, 180)
    bird_image.goto(new_x, new_y)







#-----function calls-----
draw_apple(apple)


wn.onclick()

wn.listen()

wn.bgpic("background.gif")
wn.mainloop()