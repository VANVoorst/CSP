#   a123_apple_1.py
import turtle as trtl
import random as rand

#-----setup-----
apple_image = "bird.gif" # Store the file name of your shape
#pear_image = "pear.gif"


wn = trtl.Screen()
wn.setup(width=1.0, height=1.0)
wn.addshape(apple_image) # Make the screen aware of the new file

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
def reset_apple(active_apple):
  global current_letter
  lenght_of_list= len(letter_list)
  if (lenght_of_list != 0 ):
    index = rand.randint(0, lenght_of_list)
    active_apple.goto(rand.randint(-200,200), 200)
    current_letter = letter_list.pop(index)


def draw_apple(active_apple):
  active_apple.shape(apple_image)
  draw_letter("A", active_apple)
  wn.update()

#apple to fall or move
def drop_apple():
  wn.tracer(True)
  apple.goto(apple.xcor(), -200)
  apple.clear()
  apple.hideturtle()
  wn.tracer(False)


def draw_letter(letter, active_apple):
  active_apple.color("white")
  remember_postion = active_apple.position()
  active_apple.setpos(active_apple.xcor()-25, active_apple.ycor()-50)
  active_apple.write(letter, font=("Arial", 74, "bold"))
  active_apple.setpos(remember_postion)



#-----function calls-----
draw_apple(apple)


wn.onkeypress(drop_apple, "a")

wn.listen()

wn.bgpic("background.gif")
wn.mainloop()