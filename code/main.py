import pygame, sys 
from settings import * #We're importing everything from settings + settings in this line referes to the "settings.py" file
from level import Level

class Game:
    def __init__(self): #The __init__ function is called every time an object is created from a class. The __init__ method lets the class initialize the object's attributes and serves no other purpose. It is only used within classes.

        # general setup
        pygame.init() #We are initiazing pygame
        self.screen = pygame.display.set_mode((WIDTH,HEIGTH)) #Creation of the display surface
        pygame.display.set_caption('Zelda Game') #This allows us to rename the game
        self.clock = pygame.time.Clock() #Creation of the clock
        #The above is the basic  set-up you need for pygames

        self.level = Level() #we're creating an instance of a level class in our main game

        # sound
        main_sound = pygame.mixer.Sound('../audio/main.ogg')
        main_sound.set_volume(0.5)
        main_sound.play(loops = -1)
        
    def run(self): #we'll be running our run(self) method and 2 things will be happening:
        while True: #This is going to be our event loop
            for event in pygame.event.get(): #component of the event loop
                if event.type == pygame.QUIT: #component of the event loop + this line allows us to check if we're closing the game
                    pygame.quit()#component of the event loop
                    sys.exit() #component of the event loop
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_m:
                        self.level.toggle_menu()
                    

                self.screen.fill(WATER_COLOR) #we're filling the screen with a black color
                self.level.run() #we're running the instance of the level class inside our loop + we're calling the "def_run(self)" method from the "level.py" file
                pygame.display.update() #We're updating the screen
                self.clock.tick(FPS)#we're controling the frame rate (i.e. FPS)
# What we do with the class above(i.e. "Class Game:") comes down to here:
if __name__ == '__main__': #This allows us to # 1st check if this is our main file
    game = Game() # Create an instance of the game class 
    game.run() # Call the method run of the game class

###My Notes
    # initiaze: to prepare a computer program or system to start working

    # stopped @ 6:45:25min



