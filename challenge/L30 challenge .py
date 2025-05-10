import turtle

# Set up screen
win = turtle.Screen()
win.title("Ping Pong Game")
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0)  # Turns off screen updates

# Left paddle
left_paddle = turtle.Turtle()
left_paddle.speed(0)
left_paddle.shape("square")
left_paddle.color("white")
left_paddle.shapesize(stretch_wid=5, stretch_len=1)
left_paddle.penup()
left_paddle.goto(-350, 0)

# Right paddle
right_paddle = turtle.Turtle()
right_paddle.speed(0)
right_paddle.shape("square")
right_paddle.color("white")
right_paddle.shapesize(stretch_wid=5, stretch_len=1)
right_paddle.penup()
right_paddle.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.2  # Ball movement
ball.dy = 0.2

# Functions to move paddles
def left_up():
    y = left_paddle.ycor()
    if y < 250:
        left_paddle.sety(y + 20)

def left_down():
    y = left_paddle.ycor()
    if y > -240:
        left_paddle.sety(y - 20)

def right_up():
    y = right_paddle.ycor()
    if y < 250:
        right_paddle.sety(y + 20)

def right_down():
    y = right_paddle.ycor()
    if y > -240:
        right_paddle.sety(y - 20)

# Keyboard bindings
win.listen()
win.onkeypress(left_up, "w")
win.onkeypress(left_down, "s")
win.onkeypress(right_up, "Up")
win.onkeypress(right_down, "Down")

# Main game loop
while True:
    win.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Top and bottom wall collision
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.dy *= -1

    # Left and right wall reset
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1

    # Paddle collision
    if (340 < ball.xcor() < 350) and (right_paddle.ycor() - 50 < ball.ycor() < right_paddle.ycor() + 50):
        ball.setx(340)
        ball.dx *= -1

    if (-350 < ball.xcor() < -340) and (left_paddle.ycor() - 50 < ball.ycor() < left_paddle.ycor() + 50):
        ball.setx(-340)
        ball.dx *= -1

