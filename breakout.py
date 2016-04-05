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

bricklist = []
#made the bricks and appended them to the bricklist
for i in range(0,20):
	for j in range(0,3):
		brick1 = Brick("red",i*30-300,j*25+200)
		bricklist.append(brick1)


#made the ball and the skateboard
ball = Ball(30, -200, -1, 1, 5 , "black")
skateboard = Skateboard(1, 0 , -230)
turtle.hideturtle()

while True:
	#move the bakll and skateboard	
	skateboard.move()	
	ball.movement()
	get_screen_width()
	get_screen_height()
	
	#collision with borders
	if ((ball.ycor() + ball.radius) >= get_screen_height() + 50):
		ball.dy*= -1 
		
	if ((ball.ycor() + ball.radius) <= -get_screen_height() + 50):
		ball.dy *= -1 
		
	if ((ball.xcor() + ball.radius) >= get_screen_width() + 50):
		ball.dx *= -1 
		
	if ((ball.xcor() + ball.radius) <= -get_screen_width() + 50): 
		ball.dx *= -1 
	for brick1 in bricklist:
		#collision with bricks, 
'''
		if ((ball.ycor() - ball.radius) == (brick1.ycor() + 0.25)):
			bricklist.remove(brick1)
			print("hello")
			ball.dx = ball.dx*(-1)
			ball.dy = ball.dy*(-1)
		if ((ball.ycor() + ball.radius) == (brick1.ycor() - 0.25)):
			print("he")
			
		if ((ball.xcor() - ball.radius) == (brick1.xcor() + 2)):
			bricklist.remove(brick1)
			print("merts")
			ball.dx = ball.dx*(-1)
			ball.dy = ball.dy*(-1)
		if ((ball.xcor() + ball.radius) == (brick1.xcor() - 2)):
			print("bye")
'''
	ball_left = ball.xcor 

	

	screen.update()	
