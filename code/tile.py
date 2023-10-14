# for now this file will be representing the rock/obstacle or "x" sign from the "settings.py" file
import pygame
from settings import *

class Tile(pygame.sprite.Sprite):
    def __init__(self,pos,groups,sprite_type,surface = pygame.Surface((TILESIZE,TILESIZE))): #The "pos" will allows us to know where we place the obstacle + the "group" argu,ment is the sprite group the obstacle should be part of.
        super().__init__(groups) #This line allows us to initiate the class above (so "pygame.sprite.sprite")
        self.sprite_type = sprite_type
        y_offset = HITBOX_OFFSET[sprite_type]
        self.image = surface # OLD LINE: 'self.image = pygame.image.load('../graphics/test/rock.png').convert_alpha()'; comment associated with old line:  One of the thing you'll always need for a sprite + We're importing a file for the image
        if sprite_type == 'object':
            # do an offset
            self.rect = self.image.get_rect(topleft = (pos[0],pos[1] - TILESIZE)) # we use this line if we have an offset
        else:
            self.rect = self.image.get_rect(topleft = pos) # One of the thing you'll always need for a sprite + the "pos" in this line code is the postion we'll get in "def __init__(self,pos,groups)"
        self.hitbox = self.rect.inflate(0,y_offset)
        
