import os
os.chdir(os.path.dirname(__file__))

import turtle as trtl
import random as rand
import leaderboard as lb

leaderboard_file_name = "a125_leaderboard.txt"
leader_names_list = lb.get_names(leaderboard_file_name)
leader_scores_list = lb.get_scores(leaderboard_file_name)
#setup
bird_image = "bird3.gif"
counting_down = False
score = 0
bird_speed = 1   
max_chars = 7
font_setup = ("Arial", 20, "normal")

#screen setup
wn = trtl.Screen()
wn.setup(width=0.68, height=0.75)
wn.addshape(bird_image)
wn.bgpic("background.gif")

# get player name
player_name = trtl.textinput("Name", "enter your name (max " + str(max_chars)+ " chars):")
player_name = player_name[:max_chars]
while "," in player_name:
    player_name = trtl.textinput("Name", "your name cannot contain ','")

# bird setup
bird = trtl.Turtle()
bird.penup()
bird.speed(bird_speed)
bird.shape(bird_image)
bird.hideturtle()
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

# leaderboard display turtle
leader_writer = trtl.Turtle()
leader_writer.hideturtle()
leader_writer.penup()
leader_writer.goto(-150, 200)

# leaderboard display turtle
leader_turtle = trtl.Turtle()
leader_turtle.hideturtle()
leader_turtle.penup()

# start screen writer
writer = trtl.Turtle()
writer.hideturtle()
writer.penup()

#functions
#Start Screen
def show_start_screen(x=None, y=None):
    writer.clear()
    writer.goto(0, 50)
    writer.write("Click Defense", align="center", font=("Arial", 28, "bold"))
    writer.goto(0, -20)
    writer.write("Click anywhere to start", align="center", font=("Arial", 18, "normal"))
    wn.onclick(show_instruction_screen)

# Instruction screen
def show_instruction_screen(x=None, y=None):
    writer.clear()
    writer.goto(0, 50)
    writer.write("Instructions", align="center", font=("Arial", 28, "bold"))
    writer.goto(0, -20)
    writer.write("Click the bird to score points!\nGame ends when time runs out.", align="center", font=("Arial", 16, "normal"))
    wn.onclick(start_game)

# Start the actual game
def reset_bird(active_bird):
    x = rand.randint(-250, 250)
    y = rand.randint(-50, 150)
    active_bird.goto(x, y)

def respawn_bird(active_bird):
    reset_bird(active_bird)
    active_bird.showturtle()

def start_game(x=None, y=None):
    global counting_down, timer, score, bird_speed
    if counting_down:  # prevent multiple starts
        return
    writer.clear()
    counting_down = True
    timer = 12
    score = 0
    bird_speed = 1
    score_writer.clear()
    score_writer.write(score, font=font_setup)
    respawn_bird(bird)  # sets position and shows the bird
    wn.update()         # force turtle to appear
    countdown()
    bird.onclick(shoot_bird)



def shoot_bird(x, y):
    global score, bird_speed, counting_down
    if not counting_down:
        return
    score += 1
    score_writer.clear()
    score_writer.write(score, font=font_setup)
    bird_speed += 1
    bird.speed(bird_speed)
    bird.hideturtle()
    reset_bird(bird)
    bird.showturtle()
    wn.update()

def countdown():
    global timer, counting_down
    timer_writer.clear()
    if timer <= 0:
        timer_writer.write("Game Over!", font=font_setup)
        counting_down = False
        bird.hideturtle()
        lb.update_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list, player_name, score)
        new_names = lb.get_names(leaderboard_file_name)
        new_scores = lb.get_scores(leaderboard_file_name)
        leader_turtle.clear()
        lb.draw_leaderboard(player_name in new_names, new_names, new_scores, leader_turtle, score)
        return
    else:
        timer_writer.write("Time: " + str(timer), font=font_setup)
        timer -= 1
        wn.ontimer(countdown, 1000)

def end_game():
    global counting_down
    counting_down = False
    bird.hideturtle()
    timer_writer.clear()
    score_writer.clear()
    timer_writer.write("Game Over!", font=font_setup)
    lb.update_leaderboard(leaderboard_file_name, leader_scores_list, leader_names_list, score, player_name)
    show_leaderboard()

def show_leaderboard():
    leader_writer.clear()
    leader_writer.write("LEADERBOARD", font=font_setup)
    y_pos = 600
    for i in range(len(leader_names_list)):
        leader_writer.goto(-150, y_pos)
        leader_writer.write(str(i+1) + ". " + leader_names_list[i] + ": " + str(leader_scores_list[i]), font=font_setup)
        y_pos -= 35

#start game
leader_names_list = lb.get_names(leaderboard_file_name)
leader_scores_list = lb.get_scores(leaderboard_file_name)
show_start_screen()
wn.listen()
wn.mainloop()
