#Level up this game
import pygame
import random
from pygame import mixer
  
# Starting the mixer
mixer.init()
  

surf_color = (0, 142, 204)
color = (0, 0, 0)

# Object class
class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, height, width):
		super().__init__()

		self.image = pygame.Surface([width, height])
		self.image.fill(surf_color)
		pygame.draw.rect(self.image,color,pygame.Rect(0, 0, width, height))
		self.rect = self.image.get_rect()
# Add a sprite


# Add one enemy 
# set the random position

		
		#load the fonts  
		
		
		# Render the text in new surface  
		
		
		# Loading the song
		
		
		# Setting the volume
		
		
		# Start playing the song
		