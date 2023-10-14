import pygame
from settings import *
from tile import Tile
from player import Player
from debug import debug
from support import *
from random import choice, randint
from weapon import Weapon
from ui import UI
from enemy import Enemy
from particles import AnimationPlayer
from magic import MagicPlayer
from upgrade import Upgrade

class Level: #There is no inheritence
    def __init__(self): #We will create below the 2 sprite groups

        # Get the display surface
        self.display_surface = pygame.display.get_surface() # This will get us thge display surface anywhere in the code
        self.game_paused = False
        
        # sprite group setup
        self.visible_sprites = YSortCameraGroup() # we want to change this visible class to a custom made group (this will be the 'YSortCamerGroup' class below)
        self.obstacle_sprites = pygame.sprite.Group()

        # attack sprites
        self.current_attack = None
        self.attack_sprites = pygame.sprite.Group()
        self.attackable_sprites = pygame.sprite.Group()

        #Sprite Setup
        self.create_map()#we're just calling the method below (i.e. "def create_map"

        # user interface
        self.ui = UI()
        self.upgrade = Upgrade(self.player)

        # particles
        self.animation_player = AnimationPlayer()
        self.magic_player = MagicPlayer(self.animation_player)
        
    def create_map(self): #"def" is called a method + In this method we'll nest couple of photos
        #!!! LINES PRECEDED BY #W were old lines that was part of 'def create_map'!!!
        #W for row_index,row in enumerate(WORLD_MAP): #For each row we need to know the index because that'll be the number we'll multiply with the tile size to get the y position that's why we'll be using the enumnerate method to know the index a row is on
            #W for col_index, col in enumerate(row):
                #The 2 above lines is going to sipher/browse through every item, every single 'x', ' ', or 'p' inside the WORLD_MAP and give us the x and y positions

                #W x = col_index * TILESIZE
                #W y = row_index * TILESIZE
        #def create_map( mehtod allowed us to transform the WORLD_MAP into positions
                #W if col == 'x': # if the column = x then we want to create a rock
                    #W Tile((x,y),[self.visible_sprites,self.obstacle_sprites]) #for the above condition to materialize itself we have to import the Tile from the tile.py document as shown at the beginning of this program + This line code is prettu much the result we want to see (apparition of a tile) when the  above if condition is met
                    # The above line is Tile((pos),groups)
                    # NB: The Tile (from the 'Tile((x,y),[self.visible_sprites, self.obstacle_sprites])' line) should be in 2 different groups: visible spriyes and obstacle sprite. Eventhough you won't be able to see the
                    ## difference, later on the player's behavior will be affected when facing the obstacle sprite
                #W if col == 'p': # this line means if the column = 'p', then we want to place a player
                    #W self.player = Player((x,y),[self.visible_sprites],self.obstacle_sprites) # we want to create the player
                                                                        ## We put 'Player((x,y),[self.visible_sprites]) ' in 'self.player' because we'll be using 'self.player' quite a bit + we're placing the
                                                                        ### player isndide group 'self.obstacle_sprites' just for the collisions
        layouts = { # layout creation
            'boundary': import_csv_layout('../map/map_FloorBlocks.csv'),
            'grass': import_csv_layout('../map/map_Grass.csv'),
            'object': import_csv_layout('../map/map_LargeObjects.csv'), # "Objects CSV FILE WAS NOT IN THE MAP FOLDER, SO JUST USED THE 'largeObject' file
            'entities': import_csv_layout('../map/map_Entities.csv')
        }
        graphics = {
            'grass': import_folder('../graphics/Grass'),
            'objects': import_folder('../graphics/objects') # 'objects' is the name of the related objects with the the LargeObjects csv file in the graphics folder
        }
        
        for style,layout in layouts.items():
            for row_index,row in enumerate(layout):
                for col_index, col in enumerate(row):
                    if col != '-1':
                        x = col_index * TILESIZE
                        y = row_index * TILESIZE
                        if style == 'boundary':
                            Tile((x,y),[self.obstacle_sprites],'invisible')
                        if style == 'grass':
                            #Create grass tile:
                            random_grass_image = choice(graphics['grass'])
                            Tile((x,y),
                                 [self.visible_sprites,self.obstacle_sprites,self.attackable_sprites],
                                 'grass',
                                 random_grass_image)
                        if style == 'object':
                            surf = graphics['objects'][int(col)]
                            Tile((x,y),[self.visible_sprites,self.obstacle_sprites],'object',surf)
                        if style == 'entities':
                            if col == '394':
                                self.player = Player(
                                    (x,y),
                                    [self.visible_sprites],
                                    self.obstacle_sprites,
                                    self.create_attack,
                                    self.destroy_attack,
                                    self.create_magic)# the lines in 'self.player' places the player in the middle of the map
                                    
                            else:
                                if col == '390': monster_name = 'bamboo'
                                elif col == '391': monster_name = 'spirit'
                                elif col == '392': monster_name = 'raccoon'
                                else: monster_name = 'squid'
                                Enemy(monster_name,
                                      (x,y),
                                      [self.visible_sprites,self.attackable_sprites],
                                      self.obstacle_sprites,
                                      self.damage_player,
                                      self.trigger_death_particles,
                                      self.add_exp)
    
    def create_attack(self):
        self.current_attack = Weapon(self.player,[self.visible_sprites,self.attack_sprites])

    def create_magic(self,style,strength,cost):
        if style == 'heal':
            self.magic_player.heal(self.player,strength,cost,[self.visible_sprites])
                                   
        if style == 'flame':
            self.magic_player.flame(self.player,cost,[self.visible_sprites,self.attack_sprites])
        
    def destroy_attack(self):
        if self.current_attack:
            self.current_attack.kill()
        self.current_attack = None

    def player_attack_logic(self):
        if self.attack_sprites:
            for attack_sprite in self.attack_sprites:
                collision_sprites = pygame.sprite.spritecollide(attack_sprite,self.attackable_sprites,False)
                if collision_sprites:
                    for target_sprite in collision_sprites:
                        if target_sprite.sprite_type == 'grass':
                            pos = target_sprite.rect.center
                            offset = pygame.math.Vector2(0,75)
                            for leaf in range(randint(3,6)):
                                self.animation_player.create_grass_particles(pos - offset,[self.visible_sprites])
                            target_sprite.kill()
                        else:
                            target_sprite.get_damage(self.player,attack_sprite.sprite_type)

    def damage_player(self,amount,attack_type):
        if self.player.vulnerable:
            self.player.health -= amount
            self.player.vulnerable = False
            self.player.hurt_time = pygame.time.get_ticks()
            self.animation_player.create_particles(attack_type,self.player.rect.center,[self.visible_sprites])

    def trigger_death_particles(self,pos,particle_type):
        
        self.animation_player.create_particles(particle_type,pos,self.visible_sprites)

    def add_exp(self,amount):
        
        self.player.exp += amount
        
    def toggle_menu(self):

        self.game_paused =  not self.game_paused
        
    def run(self): #in the method class we're crearing another method called run which doesn't need any argument beside self
        self.visible_sprites.custom_draw(self.player)# The previous 'draw(self.display_surface)' line would enable the system to draw all sprites in visible_sprites (i.e. generate  images of sprites). + by adding 'player' in 'self.visible_sprites_custom_draw(self.player)', now we can access the player & get the player position
        self.ui.display(self.player)
        
        if self.game_paused:
            self.upgrade.display()
        else:
            self.visible_sprites.update()
            self.visible_sprites.enemy_update(self.player)
            self.player_attack_logic()   
        
class YSortCameraGroup(pygame.sprite.Group): # This sprite group is going to fucntion as a camera + the 'YSort' means that we're going to sort the sprute by the coordinate, that way we're going to give the player and tile some  overlap
    def __init__(self):

        # general setup
        super().__init__()
        self.display_surface = pygame.display.get_surface()
        self.half_width = self.display_surface.get_size()[0] // 2 # this code allows us to define the distance we want from the left + we divide by 2 so we can get an integer
        self.half_height = self.display_surface.get_size()[1] // 2 # this code allows us to define the distance we want from the top + we divide by 2 so we can get an integer
        self.offset = pygame.math.Vector2()# the values inside 'Vector2()' parenthesis vont decider de l'emplacement du jeux, donc ils peuvent faire en sorte que le map du jeux soit plus a droite/gauche en haut/bas

        #creating the floor
        self.floor_surf = pygame.image.load('../graphics/tilemap/ground.png').convert()
        self.floor_rect = self.floor_surf.get_rect(topleft = (0,0))
        
    def custom_draw(self,player): # by adding 'player' after 'self', now we can access the player & get the player position

        # getting the offset
        self.offset.x = player.rect.centerx - self.half_width
        self.offset.y = player.rect.centery - self.half_height

        #drawing the floor
        floor_offset_pos = self.floor_rect.topleft - self.offset
        self.display_surface.blit(self.floor_surf,floor_offset_pos)
        
        #for sprite in self.sprites():
        for sprite in sorted(self.sprites(),key = lambda sprite: sprite.rect.centery):# the 1st argument 'self.sprite' is a list of what we want to sort + the 'key' is by what kind of metric are we going to sort the sprite
            offset_pos = sprite.rect.topleft - self.offset
            self.display_surface.blit(sprite.image,offset_pos)

    def enemy_update(self,player):
        enemy_sprites = [sprite for sprite in self.sprites() if hasattr(sprite,'sprite_type') and sprite.sprite_type == 'enemy']
        for enemy in enemy_sprites:
            enemy.enemy_update(player)
            
