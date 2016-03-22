from turtle import *
class Ball(Turtle):
	def __init__ (self, x, y, dx, dy, radius, color="blue"):
		Turtle.__init__(self)
		self.penup()
		self.shape("circle")
		self.goto(x,y)
		self.dx = dx
		self.dy = dy
		self.radius = radius
		self.color("blue",color)
	
	def movement(self):
		self.goto(self.xcor()+self.dx,self.ycor()+self.dy)
		
	def ball_bounce(self):
		if (Ball.dx + radius == Skateboard.dx and Ball.dy + radius == Skateboard.dy) :
			Ball.angle(35,150)
	def get_radius(self):
		return self.radius
	
	def set_radius(self,new_radius):
		self.radius = new_radius


class Brick(Turtle):
	def __init__(self, color,x,y):
		Turtle.__init__(self)
		self.shape("square")
		self.color(color)
		self.shapesize(0.5, 1, 2)
		self.pu()
		self.goto(x,y)
   
class Skateboard(Turtle):
	def __init__(self, dx, x, y, width, height):
		Turtle.__init__(self)
		self.dx = dx
		self.goto(x,y)
		self.width = width
		self.height = height
	def move(self):
		self.goto(self.xcor()+self.dx , self.ycor())


