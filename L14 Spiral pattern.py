import turtle #importing turtle

paper = turtle.Screen()#make the paper or the screen
paper.bgcolor("light blue") #set the 'paper'bg color
paper.title("turtle")

pen = turtle.Turtle()#make pen
size = 0

while True:
    for i in range(4):
        pen.forward(size + 1)
        pen.left(90)
        size = size - 5

    size = size + 1