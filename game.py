import pygame, os, sys, random

class Game:
	'''
	Initialization function that runs when the game is fired up
	images are loaded, the screen is initialized and text and fonts are set
	'''
	def __init__(self):
		print("Initializing variables")
		
		#load pygame and initialize the screen
		pygame = __import__(pygame)
		pygame.display.init()
		self.screen_width = 800
		self.screen_height = 600
		self.screen = pygame.display.set_mode([screen_width,screen_height])
		pygame.display.set_caption("Ball Game Baby!")
		
		
		#Colors and fonts
		self.COLOUR_TEXT = (255, 255, 255)

		pygame.font.init()
		game_over_font = pygame.font.Font("Signature of the Ancient.ttf", 48)
		game_over_message = game_over_font.render("Game Over Baby!", 1, self.COLOUR_TEXT)
		game_over_rectangle = game_over_message.get_rect(center = (int(self.screen_height/2),int(self.screen_width/2)))

	'''
	Game objectes are created here
	'''
	def create():
		
	'''
	Rendering process
	'''	
	def render():	
		print("rendering process running")

	'''
	Game objectes are updated here
	'''
	def update():
		print("update process running")


	
