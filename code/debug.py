#This file won't actually influence our game instead it debugs tools; so it's here to give us info about what's going in the game but it's not going to influence the game itself, so you could ignore it entirely if you don't care about it
import pygame
pygame.init()
font = pygame.font.Font(None,30)

def debug(info,y= 10,x= 10):
    display_surface = pygame.display.get_surface()
    debug_surf = font.render(str(info),True,'White')
    debug_rect = debug_surf.get_rect(topleft = (x,y))
    pygame.draw.rect(display_surface,'Black',debug_rect)
    display_surface.blit(debug_surf,debug_rect)
