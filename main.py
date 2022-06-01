## Ali Jafarbeglou
## bet game - user input = turtle color | Total 6 turtle in rainbow color

from turtle import Turtle,Screen
import random

is_race_on = False # to start and finish the game
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="MAke Your Bet", prompt="Which turtle will win the race? Enter a color: ").lower()
color = ["red", "green", "blue", "orange", "yellow", "purple"]
turtle_list = []

y_position = -100

for i in range(6):
    new_turtle = Turtle(shape="turtle")
    tim_color = random.choice(color)
    new_turtle.color(tim_color)
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_position)
    y_position += 40
    color.remove(tim_color)
    turtle_list.append(new_turtle)

if user_bet:
    is_race_on = True


while is_race_on:

    for turtle in turtle_list:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if user_bet == winning_color:
                print(f"You've won, the {winning_color} turtle is winner")
            else:
                print(f"You've lost, the {winning_color} turtle is winner")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)






screen.exitonclick()