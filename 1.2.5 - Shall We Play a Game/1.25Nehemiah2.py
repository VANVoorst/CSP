import turtle as trtl
import random as rand
import leaderboard as lb



#-----setup-----
bird_image = "bird3.gif"
timer = 12
counting_down = True
max_chars= 7
font_setup = ("Arial", 20, "normal")

#screen setup
wn = trtl.Screen()
wn.setup(width=0.68, height=0.75)
wn.addshape(bird_image)
wn.bgpic("background.gif")

#leader board
leaderboard_file_name = "a125_leaderboard.txt"
leader_names_list = []
leader_scores_list = []
player_name = trtl.textinput("Name", "enter your name (max" + str(max_chars)+ " chars:")
player_name = player_name[:max_chars]
while "," in player_name:
    player_name = trtl.textinput("Name", "your name can not contanin a comma (,)")

leader_names_list = lb.get_names("a122_leaderboard.txt") 
leader_scores_list = lb.get_scores("a122_leaderboard.txt")




bird = trtl.Turtle()
bird.penup()
bird.speed(1)
bird.shape(bird_image)
wn.tracer(False)

# Timer writer
timer_writer = trtl.Turtle()
timer_writer.hideturtle()
timer_writer.penup()
timer_writer.goto(360, 280)

# score writer
score_writer = trtl.Turtle()
score_writer.hideturtle()
score_writer.penup()
score_writer.goto(220, 170)
score_writer.write(score, font=font_setup)

#-----functions-----
#makes the bird move
def reset_bird(active_bird):
    if counting_down:
        x = rand.randint(-250, 250)
        y = rand.randint(-50, 150)
        active_bird.goto(x, y)
    wn.update()
#shows the bird on the screen
def draw_bird(active_bird):
    active_bird.shape(bird_image)
    wn.update()
#lets you click on the bird
def shoot_bird(x, y):
    bird.hideturtle()
    wn.update()
    wn.ontimer(lambda: respawn_bird(bird), 800)
#respawns the bird
def respawn_bird(active_bird):
    reset_bird(active_bird)
    active_bird.showturtle()
    draw_bird(active_bird)
#timer
def countdown():
    global timer, counting_down
    timer_writer.clear()

    if timer <= 0:
        timer_writer.write("Game Over!", font= font_setup)
        counting_down = False
    else:
        timer_writer.write("Time: " + str(timer), font= font_setup)
        timer -= 1
        wn.ontimer(countdown, 1000)  

#-----function calls-----
reset_bird(bird)
draw_bird(bird)
bird.onclick(shoot_bird)
countdown() 

wn.listen()
wn.mainloop()
