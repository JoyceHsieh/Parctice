# import library
import pygame
import random
import sys
import easy_gui as g


# settings windows
# Initialization
pygame.init()
 # Window title
pygame.display.set_caption('Puzzle game')
 # Window size
s = pygame.display.set_mode((1500, 720))


#Numbering the blocks
imgMap = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8]
]

winMap =  [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8]
]


#Define click swap function

def clickImage(x, y, map):
    if y - 1 >= 0 and map[y - 1][x] == 8:
        map[y][x], map[y - 1][x] = map[y - 1][x], map[y][x]
    elif y + 1 <= 2 and map[y + 1][x] == 8:
        map[y][x], map[y + 1][x] = map[y + 1][x], map[y][x]
    elif x - 1 >= 0 and map[y][x - 1] == 8:
        map[y][x], map[y][x - 1] = map[y][x - 1], map[y][x]
    elif x + 1 <= 2 and map[y][x + 1] == 8:
        map[y][x], map[y][x + 1] = map[y][x + 1], map[y][x]

#Define the function of scrambled blocks

def randomImage(map):
    for i in range(1000):
        x = random.randint(0, 2)
        y = random.randint(0, 2)
        clickImage(x, y, map)

#Loading game picture
img = pygame.image.load('./Disney_castle.jpg')

#Break the game picture into pieces
randomImage(imgMap)


# Set window background color and original image display
s.fill((25,35,45))  
s.blit(img, (800, 0))


#Block the picture
for y in range(3):
    for x in range(3):
        i = imgMap[y][x]
        if i == 8:      #8No need to place pictures
            continue
        dx = (i % 3) * 239            #Game block image size setting
        dy = (int(i / 3)) * 240
        s.blit(img, (x * 239, y * 240), (dx, dy, 239, 240))

#Mouse click event
for event in pygame.event.get():
    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
    elif event.type == pygame.MOUSEBUTTONDOWN:      
        if pygame.mouse.get_pressed() == (1, 0, 0):     
            mousex, mousey = pygame.mouse.get_pos()     
            if mousex<719 and mousey <720:      
                x=int(mousex/239)       
                y=int(mousey/240)
                clickImage(x,y,imgMap)
                if imgMap == winMap:
                    g.msgbox("Congratulations on completing the puzzle!")