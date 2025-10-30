# a121_catch_a_turtle.py
# ----- import statements -----
import turtle as trtl
import random as rand
import leaderboard as lb


# ----- game configuration -----
fill_color = "NavajoWhite"
size = 10
shape = "turtle"
score = 0
timer = 12  
max_chars = 7         
counting_down = True
font_setup = ("Arial", 20, "normal")
# ----- game configuration two -----
leaderboard_file_name = "a125_leaderboard.txt"
leader_names_list = []
leader_scores_list = []
player_name = trtl.textinput("Name", "enter your name (max" + str(max_chars)+ " chars:")
player_name = player_name[:max_chars]

while "," in player_name:
    player_name = trtl.textinput("Name", "your name can not contanin a comma (,) please renter it also Nehemiah likes men")



leader_names_list = lb.get_names("a125_leaderboard.txt") 
leader_scores_list = lb.get_scores("a125_leaderboard.txt")

# ----- initialize turtles -----
spot = trtl.Turtle(shape=shape)
spot.turtlesize(size)
spot.fillcolor(fill_color)
spot.penup()

# score writer
score_writer = trtl.Turtle()
score_writer.hideturtle()
score_writer.penup()
score_writer.goto(220, 170)
score_writer.write(score, font=font_setup)

# timer writer
timer_writer = trtl.Turtle()
timer_writer.hideturtle()
timer_writer.penup()
timer_writer.goto(-240, 170)

# ----- game functions -----
def spot_clicked(x, y):
    global score
    if counting_down:
        change_score()
        spot.hideturtle()
        change_size()
        change_position()
        spot.showturtle()

def change_position():
    new_x = rand.randint(-230, 230)
    new_y = rand.randint(-180, 180)
    spot.goto(new_x, new_y)

def change_size():
    new_size = rand.randint(1, 6)
    spot.turtlesize(new_size)

def change_score():
    global score
    score += 1
    score_writer.clear()
    score_writer.write(score, font=font_setup)

def countdown():
    global timer, counting_down
    timer_writer.clear()
    if timer <= 0:
        timer_writer.write("Game over!", font=font_setup)
        counting_down = False
        manage_leaderboard()
        spot.hideturtle()
    else:
        timer_writer.write(f"Time: {timer}", font=font_setup)
        timer -= 1
        wn.ontimer(countdown, 1000)

# Add this function to your game code manages the leaderboard for top 5 scorers
def manage_leaderboard():

  global score
  global spot

  # get the names and scores from the leaderboard file
  leader_names_list = lb.get_names(leaderboard_file_name)
  leader_scores_list = lb.get_scores(leaderboard_file_name)

  # show the leaderboard with or without the current player
  if (len(leader_scores_list) < 5 or score >= leader_scores_list[4]):
    lb.update_leaderboard(leaderboard_file_name, leader_names_list, leader_scores_list, player_name, score)
    lb.draw_leaderboard(True, leader_names_list, leader_scores_list, spot, score)

  else:
    lb.draw_leaderboard(False, leader_names_list, leader_scores_list, spot, score)



# ----- events -----
spot.onclick(spot_clicked)

# setup window
wn = trtl.Screen()
wn.setup(width=500, height=450)
wn.cv._rootwindow.resizable(False, False)
countdown()
wn.mainloop()
