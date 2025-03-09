import turtle #importing turtle

paper = turtle.Screen()#make the paper or the screen
paper.bgcolor("blue") #set the 'paper'bg color
paper.setup(300,400) #widht = 300 height = 400 
paper.title("polygon")

pen = turtle.Turtle()#make pen

num_sides = 6 # number of hexagon's side
side_length = 70

angel = 360 / num_sides

for i in range(num_sides):
    pen.forward(side_length)
    pen.right(angel)

turtle.done()