import pygame, sys, os, random
from pygame.locals import *

# Code is ready for some major clean up. The idea is change it form python functional/procedural
# to python object oriented style code. That is task number 1. Task number 2 is to make the ball
# collectable grow the snake and  follow the head of the snake based on postion history.

#-------------------------------------------------------------------------------------------------
class Basketball:
	# Initialize the main variable
	def __init__(self):
		self.position = [int(screen_width/4),int(screen_height/4)]
		self.direction = D_right
		basket_ball = pygame.image.load('Basketball-clipart-2.png')
		basket_ball_mask = pygame.mask.from_surface(basket_ball, 50)
	
	
	def update_position (direction,D_right, D_left, D_down, D_up):
		if direction == D_up:
			self.position[1] -= 1
		elif direction == D_down:
			self.position[1] += 1
		elif direction == D_left:
			self.position[0] -= 1
		elif direction == D_right:
			self.position[0] += 1
		else:
			self.position += 0
		#return ball_position

#-------------------------------------------------------------------------------------------------
#load images and music
bball = pygame.image.load('Basketball-clipart-2.png')
tball = pygame.image.load('tennis-ball-hi.png')
pygame.mixer.init()
pygame.mixer.music.load('tetris-gameboy-02.mp3')

n =1

#create a mask for the images
bball_mask = pygame.mask.from_surface(bball, 50)
tball_mask = pygame.mask.from_surface(tball, 50)

#this is the location of the bball and tball
bball_rect = bball.get_rect()
tball_rect = tball.get_rect()
#rect -> (x,y,w,h) so positoin of nex is x-w

#Colors baby
COLOUR_TEXT = (255, 255, 255)

#Open a window on the screen ---------------------------------done
pygame.display.init()
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode([screen_width,screen_height])
pygame.display.set_caption("Ball Game Baby!")

#Direction related variables
D_up = 0
D_down = 1
D_right = 2
D_left = 3

direction = D_right
X = int(screen_width/4)
Y = int(screen_height/4)
ball_position = [int(screen_width/4),int(screen_height/4)]
tennis_position = [(random.randint(1, screen_width-2)),(random.randint(1, screen_height-2))]
last_position = [0,0]


#logic variables
quit_game = False
game_over = False

#Other game variables	---------------------------------done
pygame.font.init()
game_over_font = pygame.font.Font("Signature of the Ancient.ttf", 48)
game_over_message = game_over_font.render("Game Over Baby!", 1, COLOUR_TEXT)
game_over_rectangle = game_over_message.get_rect(center = (int(screen_height/2),int(screen_width/2)))

#Direction Variables
key_index = [K_UP,K_DOWN, K_LEFT, K_RIGHT,K_ESCAPE]
direction_index = [D_up, D_down, D_left, D_right]

#Game day funcitons -this function updates the direction of the ball
# It could be more suited to integrate this with the position update function
def boundcheck (ball_position, D_right, D_left, D_down, D_up, direction):
	if ball_position[0] < 0:
		direction = D_right
	elif ball_position[0] > screen_width:
		direction = D_left
	elif ball_position[1] < 0:
		direction = D_down
	elif ball_position[1] > screen_height:
		direction = D_up
	else:
		direction = direction
	return direction

def drawimage():
	screen.fill((0,0,0))
	screen.blit(bball,ball_position)
	bball_rect[0] = ball_position[0]
	bball_rect[1] = ball_position[1]
	tball_rect[0] = tennis_position[0]
	tball_rect[1] = tennis_position[1]
	screen.blit(tball, tennis_position)
	pygame.event.peek()
	return

def collectable(ball_position, tennis_position):
	offset = [tennis_position[0] - ball_position[0],tennis_position[1] - ball_position[1]]
	overlap = bball_mask.overlap(tball_mask, offset)
	if overlap:
		tennis_position = [(random.randint(1, screen_width-2)),(random.randint(1, screen_height-2))]
	return tennis_position

def update_position (direction, ball_position, D_right, D_left, D_down, D_up):
	if direction == D_up:
		ball_position[1] = ball_position[1] - 1
	elif direction == D_down:
		ball_position[1] = ball_position[1] + 1
	elif direction == D_left:
		ball_position[0] = ball_position[0] - 1
	elif direction == D_right:
		ball_position[0] = ball_position[0]+1
	else:
		ball_position = ball_position
	return ball_position

#Start the music track
pygame.mixer.music.play(-1,0.0)

while not quit_game:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
	#If the music stops, Dj bring it back!
	if not pygame.mixer.music.get_busy():
		pygame.mixer.music.play(-1,0.0)

	#Render - Draw ball on the screen
	drawimage()
	
	pressed_keys = pygame.key.get_pressed() 
	#Keyboard input
	if pressed_keys[pygame.K_ESCAPE] == 1:
		game_over = True
	elif pressed_keys[pygame.K_UP] == 1:
		direction = D_up
	elif pressed_keys[pygame.K_DOWN] == 1:
		direction = D_down
	elif pressed_keys[pygame.K_LEFT] == 1:
		direction = D_left
	elif pressed_keys[pygame.K_RIGHT] == 1:
		direction = D_right

	#Game logic
	last_positoin = ball_position
	if game_over:
		pygame.mixer.music.load('10-dreamtime.mp3')
		pygame.mixer.music.play(-1,0.0)
		screen.blit(game_over_message, game_over_rectangle)
	
	else:
		ball_position =update_position(direction, ball_position, D_right, D_left, D_down, D_up)
	
	#Out of bounds logic and collectable
	direction = boundcheck(ball_position,D_right,D_left,D_down,D_up,direction)
	tennis_position = collectable(ball_position, tennis_position)
	pygame.display.update()
	pygame.time.delay(1)

