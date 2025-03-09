import turtle #importing turtle

paper = turtle.Screen()#make the paper or the screen
paper.bgcolor("cyan") #set the 'paper'bg color
paper.setup(300,400) #widht = 300 height = 400 
paper.title("star of david")

pen = turtle.Turtle()# make the pen 

# first triangle for star
pen.pendown()
pen.forward(100)# draw base

pen.left(120)
pen.forward(100)

pen.left(120)
pen.forward(100)

#change the position of the pen 
pen.penup()
pen.right(150)
pen.forward(50)

#second triangle for star 
pen.pendown()
pen.right(90)
pen.forward(100)

pen.right(120)
pen.forward(100)

pen.right(120)
pen.forward(100)

turtle.done()