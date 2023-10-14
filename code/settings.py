# game set up
# We have 2 sections here:
WIDTH = 1280 # this is part of the 1st section which includes the main (i.e. main.py file) game's variable + on this line we're defining the width of our game window (this would be flexible, so if the game window's width is too large for your window, you can make it smaller)
HEIGTH = 720 # this is part of the 1st section which includes the main (i.e. main.py file) game's variable + on this line we're defining the height of our game window (this would be flexible, so if the game window's height is too large for your window, you can make it smaller)
FPS = 60     # this is part of the 1st section which includes the main (i.e. main.py file) game's variable + you should keep the FPS number static
TILESIZE = 64# this is part of the 1st section which includes the main (i.e. main.py file) game's variable + you should keep the TILESIZE number static
HITBOX_OFFSET = {
    'player': -26,
    'object': -40,
    'grass': -10,
    'invisible': 0}
#The "WORLD_MAP" variable below is going to be the layout of our game
#In the "WORLD_MAP": "p" = player; "x"= rock/obsticle; "' '"= empty space
#The "WORLD_MAP" is a list containing a ton of individual list + isnide each list we have 1 string that could be either "x", "' '" or "p" and this we're going to translate into specific
##positions. E.g. the 1st 'x' in the list would be postion 0,0 because it's on the top left. The 'x' on the right of it will be position 64 (because our tile size is 64), 0 (because it's
### on the 1st row). The 1st 'p' on the world_map coordiante will be: x = 128 (as it's in the column with the index 2, so we do 2*64 to find the x axis) and y = 128 (as the p is in the list
#### with index 2 and we multiply 2*64 to find the y axis)
#####We got rid of our world map

#ui
BAR_HEIGHT = 20
HEALTH_BAR_WIDTH = 200
ENERGY_BAR_WIDTH = 140
ITEM_BOX_SIZE = 80
UI_FONT = '../graphics/font/joystix.ttf'
UI_FONT_SIZE = 18

# general colors
WATER_COLOR = '#71ddee'
UI_BG_COLOR = '#222222'
UI_BORDER_COLOR = '#111111'
TEXT_COLOR = '#EEEEEE'

# ui colors
HEALTH_COLOR = 'red'
ENERGY_COLOR = 'blue'
UI_BORDER_COLOR_ACTIVE = 'gold'

# upgrade menu
TEXT_COLOR_SELECTED = '#111111'
BAR_COLOR = '#EEEEEE'
BAR_COLOR_SELECTED = '#111111'
UPGRADE_BG_COLOR_SELECTED = '#EEEEEE'

# weapons
weapon_data = {
    'sword': {'cooldown': 100, 'damage': 15,'graphic':'../graphics/weapons/sword/full.png'},
    'lance': {'cooldown': 400, 'damage': 30,'graphic':'../graphics/weapons/lance/full.png'},
    'axe': {'cooldown': 300, 'damage': 20,'graphic':'../graphics/weapons/axe/full.png'},
    'rapier':{'cooldown': 50, 'damage': 8,'graphic':'../graphics/weapons/rapier/full.png'},
    'sai':{'cooldown': 80, 'damage': 10,'graphic':'../graphics/weapons/sai/full.png'}}

# magic
magic_data = {
    'flame': {'strength': 5,'cost': 20,'graphic':'../graphics/particles/flame/fire.png'},
    'heal': {'strength': 20,'cost': 10,'graphic':'../graphics/particles/heal/heal.png'}}
    
# enemy
monster_data = {
    'squid': {'health':100,'exp':100,'damage':20,'attack_type': 'slash', 'attack_sound':'../audio/attack/slash.wav', 'speed': 3, 'resistance': 3, 'attack_radius':80, 'notice_radius': 360},
    'raccoon': {'health': 300,'exp':250,'damage':40,'attack_type': 'claw', 'attack_sound':'../audio/attack/claw.wav','speed': 2, 'resistance': 3, 'attack_radius': 120, 'notice_radius': 400},
    'spirit': {'health':100,'exp':110,'damage':8,'attack_type': 'thunder', 'attack_sound':'../audio/attack/fireball.wav', 'speed': 4, 'resistance': 3, 'attack_radius': 60, 'notice_radius': 350},
    'bamboo': {'health': 70,'exp':120,'damage':6,'attack_type': 'leaf_attack','attack_sound':'../audio/attack/slash.wav', 'speed': 3, 'resistance': 3, 'attack_radius': 50, 'notice_radius':300}}

# ennemeies details:   
## health: how healthy the enemies are
## exp: how experienced the enemies give
## damage: how much damage they do to the player
## attack_type: is for the particle effect, so when the ennemy aatacks the player, a slash, claw, thunder or leaf_attack will be displaayed on the windown
## speed: speed of the ennemy
## resistance: the repulsion distance the ennemy will have to go through after being hit/pushed back  by player.
## attack_radius: radius around the ennemy, that if the player enter into, they'll be attacked
## notice_radius: a larger (larger than attack_radius) radius surrounding the ennemy. If the player is in that radius, the ennemy will just start moving towards the player. If the plkayer is outside the notice_radius, the ennemy won't do anythings.
