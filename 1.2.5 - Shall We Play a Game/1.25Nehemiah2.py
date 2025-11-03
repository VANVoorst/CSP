import os
os.chdir(os.path.dirname(__file__))

import turtle as trtl
import random as rand
import leaderboard as lb

#-----setup-----
bird_image = "bird3.gif"
timer = 12
counting_down = True
score = 0
bird_speed = 1   # speed increases

max_chars = 7
font_setup = ("Arial", 20, "normal")

leaderboard_file_name = "a125_leaderboard.txt"

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

# leaderboard display turtle
leader_writer = trtl.Turtle()
leader_writer.hideturtle()
leader_writer.penup()
leader_writer.goto(-150, 200)

#-----functions-----
def reset_bird(active_bird):
    if counting_down:
        x = rand.randint(-250, 250)
        y = rand.randint(-50, 150)
        active_bird.goto(x, y)
    wn.update()

def respawn_bird(active_bird):
    reset_bird(active_bird)
    active_bird.showturtle()

def shoot_bird(x, y):
    global score, bird_speed, counting_down

    # ❗ Stop clicks after game ends
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
        timer_writer.write("Game Over!", font= font_setup)
        counting_down = False
        bird.hideturtle()   # <--- hides the bird
        wn.update()

    else:
        timer_writer.write("Time: " + str(timer), font=font_setup)
        timer -= 1
        wn.ontimer(countdown, 1000)

def end_game():
    global counting_down
    counting_down = False

    bird.hideturtle()  # <--- remove the bird

    timer_writer.clear()
    score_writer.clear()

    timer_writer.write("Game Over!", font=font_setup)

    # Update leaderboard
    lb.update_leaderboard(leaderboard_file_name, leader_scores_list, leader_names_list, score, player_name)

    show_leaderboard()

def show_leaderboard():
    leader_writer.clear()
    leader_writer.write("🏆 LEADERBOARD 🏆", font=("Arial", 24, "bold"))

    y_pos = 150
    for i in range(len(leader_names_list)):
        leader_writer.goto(-150, y_pos)
        leader_writer.write(str(i+1) + ". " + leader_names_list[i] + ": " + str(leader_scores_list[i]),
                            font=font_setup)
        y_pos -= 35

#-----start game-----
leader_names_list = lb.get_names(leaderboard_file_name)
leader_scores_list = lb.get_scores(leaderboard_file_name)

reset_bird(bird)
bird.onclick(shoot_bird)
countdown()

wn.listen()
wn.mainloop()
