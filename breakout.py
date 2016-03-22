from classes import *

import turtle	
canvas=getcanvas()
CANVAS_WIDTH = canvas.winfo_width()
CANVAS_HEIGHT = canvas.winfo_height()
def get_screen_width():
	global CANVAS_WIDTH
	return int(CANVAS_WIDTH/2-10)
def get_screen_height():
	global CANVAS_HEIGHT
	return int(CANVAS_HEIGHT/2-5)	
turtle.tracer(0)
screen =  turtle.getscreen()
turtle.ht()
bricklist = []

for i in range(0,20):
	for j in range(0,3):
		brick1 = Brick("red",i*30-300,j*25+200)
		bricklist.append(brick1)
ball = Ball(30, -200, -1, 1, 50 , "black")

while True:	
	ball.movement()
	get_screen_width()
	get_screen_height()
	if ((ball.ycor() + ball.radius) >= get_screen_height() + 50):
		ball.dy*= -1 
		
	if ((ball.ycor() + ball.radius) <= -get_screen_height() + 50):
		ball.dy *= -1 
		
	if ((ball.xcor() + ball.radius) >= get_screen_width() + 50):
		ball.dx *= -1 
		
	if ((ball.xcor() + ball.radius) <= -get_screen_width() + 50): 
		ball.dx *= -1 
	
	screen.update()	
