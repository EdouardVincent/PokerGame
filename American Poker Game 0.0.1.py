#American Poker Game
#auction = no-limit
#players = 4
#antes
#2 cards

import pygame
from pygame.locals import*
import time
import random
import sys

RED = 255, 0, 0
WHITE = 255, 255, 255

pygame.init()

fond = pygame.font.Font('freesansbold.ttf', 18)
fond2 = pygame.font.Font('freesansbold.ttf', 22)
one_h_image = pygame.image.load('C:\Poker Images\OIP (0).png')
two_h_image = pygame.image.load('C:\Poker Images\OIP (1).png')
three_h_image = pygame.image.load('C:\Poker Images\OIP (2).png')
four_h_image = pygame.image.load('C:\Poker Images\OIP (3).png')
five_h_image = pygame.image.load('C:\Poker Images\OIP (4).png')
six_h_image = pygame.image.load('C:\Poker Images\OIP (5).png')
seven_h_image = pygame.image.load('C:\Poker Images\OIP (6).png')
height_h_image = pygame.image.load('C:\Poker Images\OIP (7).png')
nine_h_image = pygame.image.load('C:\Poker Images\OIP (8).png')
ten_h_image = pygame.image.load('C:\Poker Images\OIP (9).png')
jake_h_image = pygame.image.load('C:\Poker Images\OIP (10).png')
queen_h_image = pygame.image.load('C:\Poker Images\OIP (11).png')
king_h_image = pygame.image.load('C:\Poker Images\OIP (12).png')

one_c_image = pygame.image.load('C:\Poker Images\OIP (13).png')
two_c_image = pygame.image.load('C:\Poker Images\OIP (14).png')
three_c_image = pygame.image.load('C:\Poker Images\OIP (15).png')
four_c_image = pygame.image.load('C:\Poker Images\OIP (16).png')
five_c_image = pygame.image.load('C:\Poker Images\OIP (17).png')
six_c_image = pygame.image.load('C:\Poker Images\OIP (18).png')
seven_c_image = pygame.image.load('C:\Poker Images\OIP (19).png')
height_c_image = pygame.image.load('C:\Poker Images\OIP (20).png')
nine_c_image = pygame.image.load('C:\Poker Images\OIP (21).png')
ten_c_image = pygame.image.load('C:\Poker Images\OIP (22).png')
jake_c_image = pygame.image.load('C:\Poker Images\OIP (23).png')
queen_c_image = pygame.image.load('C:\Poker Images\OIP (24).png')
king_c_image = pygame.image.load('C:\Poker Images\OIP (25).png')

one_t_image = pygame.image.load('C:\Poker Images\OIP (26).png')
two_t_image = pygame.image.load('C:\Poker Images\OIP (27).png')
three_t_image = pygame.image.load('C:\Poker Images\OIP (28).png')
four_t_image = pygame.image.load('C:\Poker Images\OIP (29).png')
five_t_image = pygame.image.load('C:\Poker Images\OIP (30).png')
six_t_image = pygame.image.load('C:\Poker Images\OIP (31).png')
seven_t_image = pygame.image.load('C:\Poker Images\OIP (32).png')
height_t_image = pygame.image.load('C:\Poker Images\OIP (33).png')
nine_t_image = pygame.image.load('C:\Poker Images\OIP (34).png')
ten_t_image = pygame.image.load('C:\Poker Images\OIP (35).png')
jake_t_image = pygame.image.load('C:\Poker Images\OIP (36).png')
queen_t_image = pygame.image.load('C:\Poker Images\OIP (37).png')
king_t_image = pygame.image.load('C:\Poker Images\OIP (38).png')

one_p_image = pygame.image.load('C:\Poker Images\OIP (39).png')
two_p_image = pygame.image.load('C:\Poker Images\OIP (40).png')
three_p_image = pygame.image.load('C:\Poker Images\OIP (41).png')
four_p_image = pygame.image.load('C:\Poker Images\OIP (42).png')
five_p_image = pygame.image.load('C:\Poker Images\OIP (43).png')
six_p_image = pygame.image.load('C:\Poker Images\OIP (44).png')
seven_p_image = pygame.image.load('C:\Poker Images\OIP (45).png')
height_p_image = pygame.image.load('C:\Poker Images\OIP (46).png')
nine_p_image = pygame.image.load('C:\Poker Images\OIP (47).png')
ten_p_image = pygame.image.load('C:\Poker Images\OIP (48).png')
jake_p_image = pygame.image.load('C:\Poker Images\OIP (49).png')
queen_p_image = pygame.image.load('C:\Poker Images\OIP (50).png')
king_p_image = pygame.image.load('C:\Poker Images\OIP (51).png')

cards_back_image = pygame.image.load('C:\Poker Images\OIP (52).jpg')
cards_back_on_the_side_image = pygame.image.load('C:\Poker Images\OIP (54).png')
bg = pygame.image.load('C:\Poker Images\OIP (53).png')

poker_chip_image = pygame.image.load('C:\Poker Images\OIP (55).png')

window = pygame.display.set_mode((1000,800))

pygame.display.set_caption('American Poker Game')

pygame.display.set_icon(cards_back_image)

game = 1

flop_display = 0
turn_display = 0
river_display = 0

player1_turn = 1
player2_turn = 0
player3_turn = 0
player4_turn = 0

#c = clover, trèfle
#p = peak, pic
#t = tile, carreau
#h = heart, coeur

package = ['1c','2c','3c','4c','5c','6c','7c','8c','9c','10c','Jc','Qc','Kc','1p','2p','3p','4p','5p','6p','7p','8p','9p','10p','Jp','Qp','Kp','1t','2t','3t','4t','5t','6t','7t','8t','9t','10t','Jt','Qt','Kt','1h','2h','3h','4h','5h','6h','7h','8h','9h','10h','Jh','Qh','Kh']

player1_package = []
player2_package = []
player3_package = []
player4_package = []

player1_money = 1000
player2_money = 1000
player3_money = 1000
player4_money = 1000

player1_card1 = ''
player1_card2 = ''

flop_card1 = ''
flop_card2 = ''
flop_card3 = ''

turn_card = ''

river_card = ''

flop = []
turn = []
river = []

indice_random_card = 0
random_card = 0

player1_lose = 0
player2_lose = 0
player3_lose = 0
player4_lose = 0

class Card () :
    def __init__ (self) :
        self.image = None
        self.x = 0
        self.y = 0
        self.velocity = 1

    def display (self) :
        window.blit(self.image,(self.x, self.y))

    def moove_right (self) :
        self.x+=self.velocity

    def moove_up (self) :
        self.y-=self.velocity

class Chip () :
    def __init__ (self) :
        self.image = poker_chip_image
        self.x = 0
        self.y = 0
        self.velocity = 0.5

    def display (self) :
        window.blit(self.image,(self.x, self.y))

    def moove_right (self) :
        self.x+=self.velocity

    def moove_left (self) :
        self.x-=self.velocity

    def moove_up (self) :
        self.y-=self.velocity

    def moove_down (self) :
        self.y+=self.velocity
    


indice_random_card = random.randint(0,len(package))
random_card = (package[indice_random_card-1])
player1_package.append(random_card)
package.remove(package [indice_random_card-1])

indice_random_card = random.randint(0,len(package))
random_card = (package[indice_random_card-1])
player2_package.append(random_card)
package.remove(package [indice_random_card-1])

indice_random_card = random.randint(0,len(package)-1)
random_card = (package[indice_random_card])
player3_package.append(random_card)
package.remove(package [indice_random_card])

indice_random_card = random.randint(0,len(package))
random_card = (package[indice_random_card-1])
player4_package.append(random_card)
package.remove(package [indice_random_card-1])

indice_random_card = random.randint(0,len(package))
random_card = (package[indice_random_card-1])
player1_package.append(random_card)
package.remove(package [indice_random_card-1])

indice_random_card = random.randint(0,len(package))
random_card = (package[indice_random_card-1])
player2_package.append(random_card)
package.remove(package [indice_random_card-1])

indice_random_card = random.randint(0,len(package))
random_card = (package[indice_random_card-1])
player3_package.append(random_card)
package.remove(package [indice_random_card-1])

indice_random_card = random.randint(0,len(package))
random_card = (package[indice_random_card-1])
player4_package.append(random_card)
package.remove(package [indice_random_card-1])



for x in range (0,3) :
    indice_random_card = random.randint(0,len(package))
    random_card = (package[indice_random_card-1])
    flop.append(random_card)
    package.remove(package [indice_random_card-1])
    

indice_random_card = random.randint(0,len(package))
random_card = (package[indice_random_card-1])
turn.append(random_card)
package.remove(package [indice_random_card-1])


indice_random_card = random.randint(0,len(package))
random_card = (package[indice_random_card-1])
river.append(random_card)
package.remove(package [indice_random_card-1])



one_h = Card()
one_h.image = one_h_image

two_h = Card()
two_h.image = two_h_image

three_h = Card()
three_h.image = three_h_image

four_h = Card()
four_h.image = four_h_image

five_h = Card()
five_h.image = five_h_image

six_h = Card()
six_h.image = six_h_image

seven_h = Card()
seven_h.image = seven_h_image

height_h = Card()
height_h.image = height_h_image

nine_h = Card()
nine_h.image = nine_h_image

ten_h = Card()
ten_h.image = ten_h_image

jake_h = Card()
jake_h.image = jake_h_image

queen_h = Card()
queen_h.image = queen_h_image

king_h = Card()
king_h.image = king_h_image

one_c = Card()
one_c.image = one_c_image

two_c = Card()
two_c.image = two_c_image

three_c = Card()
three_c.image = three_c_image

four_c = Card()
four_c.image = four_c_image

five_c = Card()
five_c.image = five_c_image

six_c = Card()
six_c.image = six_c_image

seven_c = Card()
seven_c.image = seven_c_image

height_c = Card()
height_c.image = height_c_image

nine_c = Card()
nine_c.image = nine_c_image

ten_c = Card()
ten_c.image = ten_c_image

jake_c = Card()
jake_c.image = jake_c_image

queen_c = Card()
queen_c.image = queen_c_image

king_c = Card()
king_c.image = king_c_image

one_p = Card()
one_p.image = one_p_image

two_p = Card()
two_p.image = two_p_image

three_p = Card()
three_p.image = three_p_image

four_p = Card()
four_p.image = four_p_image

five_p = Card()
five_p.image = five_p_image

six_p = Card()
six_p.image = six_p_image

seven_p = Card()
seven_p.image = seven_p_image

height_p = Card()
height_p.image = height_p_image

nine_p = Card()
nine_p.image = nine_p_image

ten_p = Card()
ten_p.image = ten_p_image

jake_p = Card()
jake_p.image = jake_p_image

queen_p = Card()
queen_p.image = queen_p_image

king_p = Card()
king_p.image = king_p_image

one_t = Card()
one_t.image = one_t_image

two_t = Card()
two_t.image = two_t_image

three_t = Card()
three_t.image = three_t_image

four_t = Card()
four_t.image = four_t_image

five_t = Card()
five_t.image = five_t_image

six_t = Card()
six_t.image = six_t_image

seven_t = Card()
seven_t.image = seven_t_image

height_t = Card()
height_t.image = height_t_image

nine_t = Card()
nine_t.image = nine_t_image

ten_t = Card()
ten_t.image = ten_t_image

jake_t = Card()
jake_t.image = jake_t_image

queen_t = Card()
queen_t.image = queen_t_image

king_t = Card()
king_t.image = king_t_image

cards_back1 = Card()
cards_back1.image = cards_back_image

cards_back1.x = 387.5
cards_back1.y = 0

cards_back2 = Card()
cards_back2.image = cards_back_image

cards_back2.x = 512.5
cards_back2.y = 0

cards_back_on_the_side1 = Card()
cards_back_on_the_side1.image = cards_back_on_the_side_image

cards_back_on_the_side1.x = 0
cards_back_on_the_side1.y = 325

cards_back_on_the_side2 = Card()
cards_back_on_the_side2.image = cards_back_on_the_side_image

cards_back_on_the_side2.x = 0
cards_back_on_the_side2.y = 450

cards_back_on_the_side3 = Card()
cards_back_on_the_side3.image = cards_back_on_the_side_image

cards_back_on_the_side3.x = 893
cards_back_on_the_side3.y = 325

cards_back_on_the_side4 = Card()
cards_back_on_the_side4.image = cards_back_on_the_side_image

cards_back_on_the_side4.x = 893
cards_back_on_the_side4.y = 450

cards_package = Card()
cards_package.image = cards_back_image

cards_package.x = 0
cards_package.y = 625

chip_player1 = Chip()
chip_player2 = Chip()
chip_player3 = Chip()
chip_player4 = Chip()

chip_player1.x = 600
chip_player1.y = 720

chip_player2.x = 30
chip_player2.y = 537.5

chip_player3.x = 325
chip_player3.y = 30

chip_player4.x = 923
chip_player4.y = 265

if '1c' == player1_package[0] :
    player1_card1 = one_c

if '2c' == player1_package[0] :
    player1_card1 = two_c

if '3c' == player1_package[0] :
    player1_card1 = three_c

if '4c' == player1_package[0] :
    player1_card1 = four_c

if '5c' == player1_package[0] :
    player1_card1 = five_c

if '6c' == player1_package[0] :
    player1_card1 = six_c

if '7c' == player1_package[0] :
    player1_card1 = seven_c
    
if '8c' == player1_package[0] :
    player1_card1 =height_c

if '9c' == player1_package[0] :
    player1_card1 = nine_c

if '10c' == player1_package[0] :
    player1_card1 = ten_c

if 'Jc' == player1_package[0] :
    player1_card1 = jake_c

if 'Qc' == player1_package[0] :
    player1_card1 = queen_c

if 'Kc' == player1_package[0] :
    player1_card1 = king_c

if '1p' == player1_package[0] :
    player1_card1 = one_p

if '2p' == player1_package[0] :
    player1_card1 = two_p

if '3p' == player1_package[0] :
    player1_card1 = three_p

if '4p' == player1_package[0] :
    player1_card1 = four_p

if '5p' == player1_package[0] :
    player1_card1 = five_p

if '6p' == player1_package[0] :
    player1_card1 = six_p

if '7p' == player1_package[0] :
    player1_card1 = seven_p
    
if '8p' == player1_package[0] :
    player1_card1 = height_p

if '9p' == player1_package[0] :
    player1_card1 = nine_p

if '10p' == player1_package[0] :
    player1_card1 = ten_p

if 'Jp' == player1_package[0] :
    player1_card1 = jake_p

if 'Qp' == player1_package[0] :
    player1_card1 = queen_p

if 'Kp' == player1_package[0] :
    player1_card1 = king_p

if '1t' == player1_package[0] :
    player1_card1 = one_t

if '2t' == player1_package[0] :
    player1_card1 = two_t

if '3t' == player1_package[0] :
    player1_card1 = three_t

if '4t' == player1_package[0] :
    player1_card1 = four_t

if '5t' == player1_package[0] :
    player1_card1 = five_t

if '6t' == player1_package[0] :
    player1_card1 = six_t

if '7t' == player1_package[0] :
    player1_card1 = seven_t
    
if '8t' == player1_package[0] :
    player1_card1 =height_t

if '9t' == player1_package[0] :
    player1_card1 = nine_t

if '10t' == player1_package[0] :
    player1_card1 = ten_t

if 'Jt' == player1_package[0] :
    player1_card1 = jake_t

if 'Qt' == player1_package[0] :
    player1_card1 = queen_t

if 'Kt' == player1_package[0] :
    player1_card1 = king_t

if '1h' == player1_package[0] :
    player1_card1 = one_h

if '2h' == player1_package[0] :
    player1_card1 = two_h

if '3h' == player1_package[0] :
    player1_card1 = three_h

if '4h' == player1_package[0] :
    player1_card1 = four_h

if '5h' == player1_package[0] :
    player1_card1 = five_h

if '6h' == player1_package[0] :
    player1_card1 = six_h

if '7h' == player1_package[0] :
    player1_card1 = seven_h
    
if '8h' == player1_package[0] :
    player1_card1 =height_h

if '9h' == player1_package[0] :
    player1_card1 = nine_h

if '10h' == player1_package[0] :
    player1_card1 = ten_h

if 'Jh' == player1_package[0] :
    player1_card1 = jake_h

if 'Qh' == player1_package[0] :
    player1_card1 = queen_h

if 'Kh' == player1_package[0] :
    player1_card1 = king_h




if '1c' == player1_package[1] :
    player1_card2 = one_c

if '2c' == player1_package[1] :
    player1_card2 = two_c

if '3c' == player1_package[1] :
    player1_card2 = three_c

if '4c' == player1_package[1] :
    player1_card2 = four_c

if '5c' == player1_package[1] :
    player1_card2 = five_c

if '6c' == player1_package[1] :
    player1_card2 = six_c

if '7c' == player1_package[1] :
    player1_card2 = seven_c
    
if '8c' == player1_package[1] :
    player1_card2 =height_c

if '9c' == player1_package[1]:
    player1_card2 = nine_c

if '10c' == player1_package[1] :
    player1_card2 = ten_c

if 'Jc' == player1_package[1] :
    player1_card2 = jake_c

if 'Qc' == player1_package[1] :
    player1_card2 = queen_c

if 'Kc' == player1_package[1] :
    player1_card2 = king_c

if '1p' == player1_package[1] :
    player1_card2 = one_p

if '2p' == player1_package[1] :
    player1_card2 = two_p

if '3p' == player1_package[1] :
    player1_card2 = three_p

if '4p' == player1_package[1] :
    player1_card2 = four_p

if '5p' == player1_package[1] :
    player1_card2 = five_p

if '6p' == player1_package[1] :
    player1_card2 = six_p

if '7p' == player1_package[1] :
    player1_card2 = seven_p
    
if '8p' == player1_package[1] :
    player1_card2 = height_p

if '9p' == player1_package[1] :
    player1_card2 = nine_p

if '10p' == player1_package[1] :
    player1_card2 = ten_p

if 'Jp' == player1_package[1] :
    player1_card2 = jake_p

if 'Qp' == player1_package[1] :
    player1_card2 = queen_p

if 'Kp' == player1_package[1] :
    player1_card2 = king_p

if '1t' == player1_package[1] :
    player1_card2 = one_t

if '2t' == player1_package[1] :
    player1_card2 = two_t

if '3t' == player1_package[1] :
    player1_card2 = three_t

if '4t' == player1_package[1] :
    player1_card2 = four_t

if '5t' == player1_package[1] :
    player1_card2 = five_t

if '6t' == player1_package[1] :
    player1_card2 = six_t

if '7t' == player1_package[1] :
    player1_card2 = seven_t
    
if '8t' == player1_package[1] :
    player1_card2 = height_t

if '9t' == player1_package[1] :
    player1_card2 = nine_t

if '1t' == player1_package[1] :
    player1_card2 = ten_t

if 'Jt' == player1_package[1] :
    player1_card2 = jake_t

if 'Qt' == player1_package[1] :
    player1_card2 = queen_t

if 'Kt' == player1_package[1] :
    player1_card2 = king_t

if '1h' == player1_package[1] :
    player1_card2 = one_h

if '2h' == player1_package[1] :
    player1_card2 = two_h

if '3h' == player1_package[1] :
    player1_card2 = three_h

if '4h' == player1_package[1] :
    player1_card2 = four_h

if '5h' == player1_package[1] :
    player1_card2 = five_h

if '6h' == player1_package[1] :
    player1_card2 = six_h

if '7h' == player1_package[1] :
    player1_card2 = seven_h
    
if '8h' == player1_package[1] :
    player1_card2 =height_h

if '9h' == player1_package[1] :
    player1_card2 = nine_h

if '10h' == player1_package[1] :
    player1_card2 = ten_h

if 'Jh' == player1_package[1] :
    player1_card2 = jake_h

if 'Qh' == player1_package[1] :
    player1_card2 = queen_h

if 'Kh' == player1_package[1] :
    player1_card2 = king_h


####



if '1c' == flop[0] :
    flop_card1 = one_c

if '2c' == flop[0] :
    flop_card1 = two_c

if '3c' == flop[0] :
    flop_card1 = three_c

if '4c' == flop[0] :
    flop_card1 = four_c

if '5c' == flop[0] :
    flop_card1 = five_c

if '6c' == flop[0] :
    flop_card1 = six_c

if '7c' == flop[0] :
    flop_card1 = seven_c
    
if '8c' == flop[0] :
    flop_card1 =height_c

if '9c' == flop[0] :
    flop_card1 = nine_c

if '10c' == flop[0] :
    flop_card1 = ten_c

if 'Jc' == flop[0] :
    flop_card1 = jake_c

if 'Qc' == flop[0] :
    flop_card1 = queen_c

if 'Kc' == flop[0] :
    flop_card1 = king_c

if '1p' == flop[0] :
    flop_card1 = one_p

if '2p' == flop[0] :
    flop_card1 = two_p

if '3p' == flop[0] :
    flop_card1 = three_p

if '4p' == flop[0] :
    flop_card1 = four_p

if '5p' == flop[0] :
    flop_card1 = five_p

if '6p' == flop[0] :
    flop_card1 = six_p

if '7p' == flop[0] :
    flop_card1 = seven_p
    
if '8p' == flop[0] :
    flop_card1 = height_p

if '9p' == flop[0] :
    flop_card1 = nine_p

if '10p' == flop[0] :
    flop_card1 = ten_p

if 'Jp' == flop[0] :
    flop_card1 = jake_p

if 'Qp' == flop[0] :
    flop_card1 = queen_p

if 'Kp' == flop[0] :
    flop_card1 = king_p

if '1t' == flop[0] :
    flop_card1 = one_t

if '2t' == flop[0] :
    flop_card1 = two_t

if '3t' == flop[0] :
    flop_card1 = three_t

if '4t' == flop[0] :
    flop_card1 = four_t

if '5t' == flop[0] :
    flop_card1 = five_t

if '6t' == flop[0] :
    flop_card1 = six_t

if '7t' == flop[0] :
    flop_card1 = seven_t
    
if '8t' == flop[0] :
    flop_card1 = height_t

if '9t' == flop[0] :
    flop_card1 = nine_t

if '10t' == flop[0] :
    flop_card1 = ten_t

if 'Jt' == flop[0] :
    flop_card1 = jake_t

if 'Qt' == flop[0] :
    flop_card1 = queen_t

if 'Kt' == flop[0] :
    flop_card1 = king_t

if '1h' == flop[0] :
    flop_card1 = one_h

if '2h' == flop[0] :
    flop_card1 = two_h

if '3h' == flop[0] :
    flop_card1 = three_h

if '4h' == flop[0] :
    flop_card1 = four_h

if '5h' == flop[0] :
    flop_card1 = five_h

if '6h' == flop[0] :
    flop_card1 = six_h

if '7h' == flop[0] :
    flop_card1 = seven_h
    
if '8h' == flop[0] :
    flop_card1 =height_h

if '9h' == flop[0] :
    flop_card1 = nine_h

if '10h' == flop[0] :
    flop_card1 = ten_h

if 'Jh' == flop[0] :
    flop_card1 = jake_h

if 'Qh' == flop[0] :
    flop_card1 = queen_h

if 'Kh' == flop[0] :
    flop_card1 = king_h




if '1c' == flop[1] :
    flop_card2 = one_c

if '2c' == flop[1] :
    flop_card2 = two_c

if '3c' == flop[1] :
    flop_card2 = three_c

if '4c' == flop[1] :
    flop_card2 = four_c

if '5c' == flop[1] :
    flop_card2 = five_c

if '6c' == flop[1] :
    flop_card2 = six_c

if '7c' == flop[1] :
    flop_card2 = seven_c
    
if '8c' == flop[1] :
    flop_card2 = height_c

if '9c' == flop[1] :
    flop_card2 = nine_c

if '10c' == flop[1] :
    flop_card2 = ten_c

if 'Jc' == flop[1] :
    flop_card2 = jake_c

if 'Qc' == flop[1] :
    flop_card2 = queen_c

if 'Kc' == flop[1] :
    flop_card2 = king_c

if '1p' == flop[1] :
    flop_card2 = one_p

if '2p' == flop[1] :
    flop_card2 = two_p

if '3p' == flop[1] :
    flop_card2 = three_p

if '4p' == flop[1] :
    flop_card2 = four_p

if '5p' == flop[1] :
    flop_card2 = five_p

if '6p' == flop[1] :
    flop_card2 = six_p

if '7p' == flop[1] :
    flop_card2 = seven_p
    
if '8p' == flop[1] :
    flop_card2 = height_p

if '9p' == flop[1] :
    flop_card2 = nine_p

if '10p' == flop[1] :
    flop_card2 = ten_p

if 'Jp' == flop[1] :
    flop_card2 = jake_p

if 'Qp' == flop[1] :
    flop_card2 = queen_p

if 'Kp' == flop[1] :
    flop_card2 = king_p

if '1t' == flop[1] :
    flop_card2 = one_t

if '2t' == flop[1] :
    flop_card2 = two_t

if '3t' == flop[1] :
    flop_card2 = three_t

if '4t' == flop[1] :
    flop_card2 = four_t

if '5t' == flop[1] :
    flop_card2 = five_t

if '6t' == flop[1] :
    flop_card2 = six_t

if '7t' == flop[1] :
    flop_card2 = seven_t
    
if '8t' == flop[1] :
    flop_card2 = height_t

if '9t' == flop[1] :
    flop_card2 = nine_t

if '10t' == flop[1] :
    flop_card2 = ten_t

if 'Jt' == flop[1] :
    flop_card2 = jake_t

if 'Qt' == flop[1] :
    flop_card2 = queen_t

if 'Kt' == flop[1] :
    flop_card2 = king_t

if '1h' == flop[1] :
    flop_card2 = one_h

if '2h' == flop[1] :
    flop_card2 = two_h

if '3h' == flop[1] :
    flop_card2 = three_h

if '4h' == flop[1] :
    flop_card2 = four_h

if '5h' == flop[1] :
    flop_card2 = five_h

if '6h' == flop[1] :
    flop_card2 = six_h

if '7h' == flop[1] :
    flop_card2 = seven_h
    
if '8h' == flop[1] :
    flop_card2 = height_h

if '9h' == flop[1] :
    flop_card2 = nine_h

if '10h' == flop[1] :
    flop_card2 = ten_h

if 'Jh' == flop[1] :
    flop_card2 = jake_h

if 'Qh' == flop[1] :
    flop_card2 = queen_h

if 'Kh' == flop[1] :
    flop_card2 = king_h





if '1c' == flop[2] :
    flop_card3 = one_c

if '2c' == flop[2] :
    flop_card3 = two_c

if '3c' == flop[2] :
    flop_card3 = three_c

if '4c' == flop[2] :
    flop_card3 = four_c

if '5c' == flop[2] :
    flop_card3 = five_c

if '6c' == flop[2] :
    flop_card3 = six_c

if '7c' == flop[2] :
    flop_card3 = seven_c
    
if '8c' == flop[2] :
    flop_card3 = height_c

if '9c' == flop[2] :
    flop_card3 = nine_c

if '10c' == flop[2] :
    flop_card3 = ten_c

if 'Jc' == flop[2] :
    flop_card3 = jake_c

if 'Qc' == flop[2] :
    flop_card3 = queen_c

if 'Kc' == flop[2] :
    flop_card3 = king_c

if '1p' == flop[2] :
    flop_card3 = one_p

if '2p' == flop[2] :
    flop_card3 = two_p

if '3p' == flop[2] :
    flop_card3 = three_p

if '4p' == flop[2] :
    flop_card3 = four_p

if '5p' == flop[2] :
    flop_card3 = five_p

if '6p' == flop[2] :
    flop_card3 = six_p

if '7p' == flop[2] :
    flop_card3 = seven_p
    
if '8p' == flop[2] :
    flop_card3 = height_p

if '9p' == flop[2] :
    flop_card3 = nine_p

if '10p' == flop[2] :
    flop_card3 = ten_p

if 'Jp' == flop[2] :
    flop_card3 = jake_p

if 'Qp' == flop[2] :
    flop_card3 = queen_p

if 'Kp' == flop[2] :
    flop_card3 = king_p

if '1t' == flop[2] :
    flop_card3 = one_t

if '2t' == flop[2] :
    flop_card3 = two_t

if '3t' == flop[2] :
    flop_card3 = three_t

if '4t' == flop[2] :
    flop_card3 = four_t

if '5t' == flop[2] :
    flop_card3 = five_t

if '6t' == flop[2] :
    flop_card3 = six_t

if '7t' == flop[2] :
    flop_card3 = seven_t
    
if '8t' == flop[2] :
    flop_card3 = height_t

if '9t' == flop[2] :
    flop_card3 = nine_t

if '10t' == flop[2] :
    flop_card3 = ten_t

if 'Jt' == flop[2] :
    flop_card3 = jake_t

if 'Qt' == flop[2] :
    flop_card3 = queen_t

if 'Kt' == flop[2] :
    flop_card3 = king_t

if '1h' == flop[2] :
    flop_card3 = one_h

if '2h' == flop[2] :
    flop_card3 = two_h

if '3h' == flop[2] :
    flop_card3 = three_h

if '4h' == flop[2] :
    flop_card3 = four_h

if '5h' == flop[2] :
    flop_card3 = five_h

if '6h' == flop[2] :
    flop_card3 = six_h

if '7h' == flop[2] :
    flop_card3 = seven_h
    
if '8h' == flop[2] :
    flop_card3 = height_h

if '9h' == flop[2] :
    flop_card3 = nine_h

if '10h' == flop[2] :
    flop_card3 = ten_h

if 'Jh' == flop[2] :
    flop_card3 = jake_h

if 'Qh' == flop[2] :
    flop_card3 = queen_h

if 'Kh' == flop[2] :
    flop_card3 = king_h





if '1c' == turn[0] :
    turn_card = one_c

if '2c' == turn[0] :
    turn_card = two_c

if '3c' == turn[0] :
    turn_card = three_c

if '4c' == turn[0] :
    turn_card = four_c

if '5c' == turn[0] :
    turn_card = five_c

if '6c' == turn[0] :
    turn_card = six_c

if '7c' == turn[0] :
    turn_card = seven_c
    
if '8c' == turn[0] :
    turn_card =height_c

if '9c' == turn[0] :
    turn_card = nine_c

if '10c' == turn[0] :
    turn_card = ten_c

if 'Jc' == turn[0] :
    turn_card = jake_c

if 'Qc' == turn[0] :
    turn_card = queen_c

if 'Kc' == turn[0] :
    turn_card = king_c

if '1p' == turn[0] :
    turn_card = one_p

if '2p' == turn[0] :
    turn_card = two_p

if '3p' == turn[0] :
    turn_card = three_p

if '4p' == turn[0] :
    turn_card = four_p

if '5p' == turn[0] :
    turn_card = five_p

if '6p' == turn[0] :
    turn_card = six_p

if '7p' == turn[0] :
    turn_card = seven_p
    
if '8p' == turn[0] :
    turn_card = height_p

if '9p' == turn[0] :
    turn_card = nine_p

if '10p' == turn[0] :
    turn_card = ten_p

if 'Jp' == turn[0] :
    turn_card = jake_p

if 'Qp' == turn[0] :
    turn_card = queen_p

if 'Kp' == turn[0] :
    turn_card = king_p

if '1t' == turn[0] :
    turn_card = one_t

if '2t' == turn[0] :
    turn_card = two_t

if '3t' == turn[0] :
    turn_card = three_t

if '4t' == turn[0] :
    turn_card = four_t

if '5t' == turn[0] :
    turn_card = five_t

if '6t' == turn[0] :
    turn_card = six_t

if '7t' == turn[0] :
    turn_card = seven_t
    
if '8t' == turn[0] :
    turn_card = height_t

if '9t' == turn[0] :
    turn_card = nine_t

if '10t' == turn[0] :
    turn_card = ten_t

if 'Jt' == turn[0] :
    turn_card = jake_t

if 'Qt' == turn[0] :
    turn_card = queen_t

if 'Kt' == turn[0] :
    turn_card = king_t

if '1h' == turn[0] :
    turn_card = one_h

if '2h' == turn[0] :
    turn_card = two_h

if '3h' == turn[0] :
    turn_card = three_h

if '4h' == turn[0] :
    turn_card = four_h

if '5h' == turn[0] :
    turn_card = five_h

if '6h' == turn[0] :
    turn_card = six_h

if '7h' == turn[0] :
    turn_card = seven_h
    
if '8h' == turn[0] :
    turn_card =height_h

if '9h' == turn[0] :
    turn_card = nine_h

if '10h' == turn[0] :
    turn_card = ten_h

if 'Jh' == turn[0] :
    turn_card = jake_h

if 'Qh' == turn[0] :
    turn_card = queen_h

if 'Kh' == turn[0] :
    turn_card = king_h




if '1c' == river[0] :
    river_card = one_c

if '2c' == river[0] :
    river_card = two_c

if '3c' == river[0] :
    river_card = three_c

if '4c' == river[0] :
    river_card = four_c

if '5c' == river[0] :
    river_card = five_c

if '6c' == river[0] :
    river_card = six_c

if '7c' == river[0] :
    river_card = seven_c
    
if '8c' == river[0] :
    river_card =height_c

if '9c' == river[0] :
    river_card = nine_c

if '10c' == river[0] :
    river_card = ten_c

if 'Jc' == river[0] :
    river_card = jake_c

if 'Qc' == river[0] :
    river_card = queen_c

if 'Kc' == river[0] :
    river_card = king_c

if '1p' == river[0] :
    river_card = one_p

if '2p' == river[0] :
    river_card = two_p

if '3p' == river[0] :
    river_card = three_p

if '4p' == river[0] :
    river_card = four_p

if '5p' == river[0] :
    river_card = five_p

if '6p' == river[0] :
    river_card = six_p

if '7p' == river[0] :
    river_card = seven_p
    
if '8p' == river[0] :
    river_card = height_p

if '9p' == river[0] :
    river_card = nine_p

if '10p' == river[0] :
    river_card = ten_p

if 'Jp' == river[0] :
    river_card = jake_p

if 'Qp' == river[0] :
    river_card = queen_p

if 'Kp' == river[0] :
    river_card = king_p

if '1t' == river[0] :
    river_card = one_t

if '2t' == river[0] :
    river_card = two_t

if '3t' == river[0] :
    river_card = three_t

if '4t' == river[0] :
    river_card = four_t

if '5t' == river[0] :
    river_card = five_t

if '6t' == river[0] :
    river_card = six_t

if '7t' == river[0] :
    river_card = seven_t
    
if '8t' == river[0] :
    river_card = height_t

if '9t' == river[0] :
    river_card = nine_t

if '10t' == river[0] :
    river_card = ten_t

if 'Jt' == river[0] :
    river_card = jake_t

if 'Qt' == river[0] :
    river_card = queen_t

if 'Kt' == river[0] :
    river_card = king_t

if '1h' == river[0] :
    river_card = one_h

if '2h' == river[0] :
    river_card = two_h

if '3h' == river[0] :
    river_card = three_h

if '4h' == river[0] :
    river_card = four_h

if '5h' == river[0] :
    river_card = five_h

if '6h' == river[0] :
    river_card = six_h

if '7h' == river[0] :
    river_card = seven_h
    
if '8h' == river[0] :
    river_card =height_h

if '9h' == river[0] :
    river_card = nine_h

if '10h' == river[0] :
    river_card = ten_h

if 'Jh' == river[0] :
    river_card = jake_h

if 'Qh' == river[0] :
    river_card = queen_h

if 'Kh' == river[0] :
    river_card = king_h


flop_card1.x = 0
flop_card1.y = 625

flop_card2.x = 0
flop_card2.y = 625

flop_card3.x = 0
flop_card3.y = 625

turn_card.x = 0
turn_card.y = 625

river_card.x = 0
river_card.y = 625

player1_card1.x = 387.5
player1_card1.y = 690

player1_card2.x = 512.5
player1_card2.y = 690

while game :

    for event in pygame.event.get() :
        if event.type == QUIT :
            pygame.quit()
            sys.exit()

        if event.type == KEYDOWN :
            if event.key == K_ESCAPE :
                pygame.quit()
                sys.exit()

            if event.key == K_b and player1_turn == 1 :
                if flop_display == 0 :
                    player1_money-= 20

            if event.key == K_a and player1_turn == 1 :
                pygame.quit()
                sys.exit()

            if event.key == K_c and player1_turn == 1 :
                if flop_display == 0 :
                    pass

    if player1_turn == 1 :
        if player1_money == 980 :
            chip_player1.moove_up()

            if chip_player1.y <= 550 :
                player1_turn = 0
                player2_turn = 1
                time.sleep(0.75)
                
    if player2_turn == 1 and player1_turn == 0 :
        if flop_display == 0 :
            chip_player2.moove_right()

            if chip_player2.x >= 200 :
                player2_money -= 20
                player2_turn = 0
                player3_turn = 1
                time.sleep(0.75)
        
    if player3_turn == 1 and player2_turn == 0 :
        if flop_display == 0 :
            chip_player3.moove_down()

            if chip_player3.y >= 200 :
                player3_money -= 20
                player3_turn = 0
                player4_turn = 1
                time.sleep(0.75)

        

    if player4_turn == 1 and player3_turn == 0 :
        if flop_display == 0 :
            chip_player4.moove_left()

            if chip_player4.x <= 753  :
                player4_money -= 20
                player4_turn = 0
                flop_display = 1
                time.sleep(0.75)

    if flop_display == 1 :

        if flop_card1.y <= 375 :
            flop_card1.velocity = 0
            flop_card2.velocity = 0
            flop_card3.velocity = 0
            
            if flop_card2.x <= 350 :
                flop_card2.x += 1  

            if flop_card3.x <= 450 :
                flop_card3.x += 1

            if flop_card3.x >= 450 :
                player1_turn = 1
        
        flop_card1.moove_right()
        flop_card1.moove_up()

        flop_card2.moove_right()
        flop_card2.moove_up()

        flop_card3.moove_right()
        flop_card3.moove_up()


    if turn_display == 1 :
        turn_card.moove_right()
        turn_card.moove_up()

        if turn_card.y <= 375 : 
            turn_card.velocity = 0

            if turn_card.x <= 550 :
                turn_card.x +=1

    if river_display == 1 :
        river_card.moove_right()
        river_card.moove_up()

        if river_card.y <= 375 : 
            river_card.velocity = 0

            if river_card.x <= 650 :
                river_card.x +=1
        
        
    money_player1Surf = fond.render('Your money : %s' % player1_money, True, RED)
    money_player2Surf = fond.render('Player s 2 money : %s' % player2_money, True, RED)
    money_player3Surf = fond.render('Player s 3 money : %s' % player3_money, True, RED)
    money_player4Surf = fond.render('Player s 4 money : %s' % player4_money, True, RED)

    player1winSurf = fond2.render('You won !', True, RED)
    player2winSurf = fond2.render('Player 2 has won !', True, RED)
    player3winSurf = fond2.render('Player 3 has won !', True, RED)
    player4winSurf = fond2.render('Player 4 has won !', True, RED)

    player1loseSurf = fond2.render('You lose !', True, RED)
    player2loseSurf = fond2.render('Player 2 just losed !', True, RED)
    player3loseSurf = fond2.render('Player 3 just losed !', True, RED)
    player4loseSurf = fond2.render('Player 4 just losed !', True, RED)

    player1auctionSurf = fond2.render('You have put 20 on the table', True, RED)
    player2auctionSurf = fond2.render('Player 2 has put 20 on the table', True, RED)
    player3auctionSurf = fond2.render('Player 3 has put 20 on the table', True, RED)
    player4auctionSurf = fond2.render('Player 4 has put 20 on the table', True, RED)

    betSurf = fond2.render('Bet : B', True, WHITE)
    foldSurf = fond2.render('Fold, Abandon : A', True, WHITE)
    followSurf = fond2.render('Follow : F', True, WHITE)
    checkSurf = fond2.render('Check : C',True, WHITE)
    leaveSurf = fond2.render('Leave : Escape',True, WHITE)

    YourTurnSurf = fond2.render('Your Turn !', True, RED)

    window.blit(bg,(0,0))

    if flop_display == 1 :
        flop_card1.display()
        flop_card2.display()
        flop_card3.display()

    if turn_display == 1 :
        flop_card1.display()
        flop_card2.display()
        flop_card3.display()
        turn_card.display()

    if river_display == 1 :
        flop_card1.display()
        flop_card2.display()
        flop_card3.display()
        turn_card.display()
        river_card.display()

    cards_package.display()
    cards_back1.display()
    cards_back2.display()
    cards_back_on_the_side1.display()
    cards_back_on_the_side2.display()
    cards_back_on_the_side3.display()
    cards_back_on_the_side4.display()
    player1_card1.display()
    player1_card2.display()
    window.blit(money_player1Surf,(180,700))
    window.blit(money_player2Surf,(0,200))
    window.blit(money_player3Surf,(600,100))
    window.blit(money_player4Surf,(780,600))
    
    if player1_turn == 1 :
        window.blit(YourTurnSurf,(425,600))
        window.blit(betSurf,(0,0))
        window.blit(foldSurf,(0,22))
        window.blit(followSurf,(0,44))
        window.blit(checkSurf,(0,66))
        window.blit(leaveSurf,(0,88))

    
    chip_player1.display()
    chip_player2.display()
    chip_player3.display()
    chip_player4.display()
        
    pygame.display.flip()
