# creating python game created 21/09/2020 snake game @joshua

import turtle
import time
import random

delay = 0.1  # delays the timing to allow us to see the snake move

# score
score = 0

# high score
high_score = 0

# setup window screen
wn = turtle.Screen()
wn.title("snake Game by @joshua & Mark")  # joint operation between mark davidson and myself
wn.bgcolor("green")
wn.setup(width=600, height=600)  # def the board
wn.tracer(0)  # turns off the screen updates

# create snake head
head = turtle.Turtle()
head.speed(0)  # animation speed
head.shape("square")
head.color("black")
head.penup()  # do not draw line
head.goto(0, 0)  # start in the center of the screen
head.direction = "stop"

# snake food
food = turtle.Turtle()
food.speed(0)  # animation speed
food.shape("circle")
food.color("red")
food.penup()  # do not draw line
food.goto(0, 100)  # start in the center of the screen

segments = []

# pen for score
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 200)
pen.write("Score: 0    High Score: 0", align="center", font=("Courier", 24, "normal"))


# functions


def go_up():
    if head.direction != "down":
        head.direction = "up"


def go_down():
    if head.direction != "up":
        head.direction = "down"


def go_right():
    if head.direction != "left":
        head.direction = "right"


def go_left():
    if head.direction != "right":
        head.direction = "left"


def move():
    if head.direction == "up":  # move head up by 20px if up key is pushed
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":  # move head down by 20px if down key is pushed
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "right":  # move head right by 20px if right key is pushed
        x = head.xcor()
        head.setx(x + 20)

    if head.direction == "left":  # move head left by 20px if left key is pushed
        x = head.xcor()
        head.setx(x - 20)


# keyboard bindings
wn.listen()
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_right, "Right")
wn.onkeypress(go_left, "Left")

# main game loop
while True:
    wn.update()

    # check with collision with border
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "stop"

        # hide the seg
        for segment in segments:
            segment.goto(1000, 1000)

        # clear the seg list
        segments.clear()

        # reset the delay
        delay = 0.1

        # reset score
        score = 0
        pen.clear()
        pen.write("Score: {}    High Score: {}".format(score, high_score), align="center",
                  font=("Courier", 24, "normal"))

    # collision logic with food
    if head.distance(food) < 20:  # the body of the snake is 20 px wide and high
        # move the food to rnd spot on the screen
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        # add a segment to the snake
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)

        # shorten the delay
        delay -= 0.001

        # increase the score
        score += 10

        if score > high_score:
            high_score = score

        pen.clear()
        pen.write("Score: {}    High Score: {}".format(score, high_score), align="center",
                  font=("Courier", 24, "normal"))

    # move the end seg first in rev order
    for index in range(len(segments) - 1, 0, -1):
        x = segments[index - 1].xcor()
        y = segments[index - 1].ycor()
        segments[index].goto(x, y)  # shifts the last segment forward by 1 space and so on for the rest. eg moves pos 9
        # to 8 and so on

    # move seg 0 to where the head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    # check for snake collision with body part
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"

            # hide the seg
            for segment in segments:
                segment.goto(1000, 1000)

            # clear the seg list
            segments.clear()

            # reset the delay
            delay = 0.1

            # reset score
            score = 0
            pen.clear()
            pen.write("Score: {}    High Score: {}".format(score, high_score), align="center",
                      font=("Courier", 24, "normal"))

    time.sleep(delay)

wn.mainloop()  # keeps the window open
