"""
import pygame
import time
import math


pygame.init()


window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))

clock_image = pygame.image.load("mainclock.png")
clock_image = pygame.transform.scale(clock_image,(800,600))


right_hand_image = pygame.image.load("rightarm.png")
right_hand_image = pygame.transform.scale(right_hand_image, (int(right_hand_image.get_width() * 0.6), int(right_hand_image.get_height() * 0.6)))  # Уменьшение размера правой руки

left_hand_image = pygame.image.load("leftarm.png")
left_hand_image = pygame.transform.scale(left_hand_image, (int(left_hand_image.get_width() * 0.6), int(left_hand_image.get_height() * 0.6)))  # Уменьшение размера левой руки


clock_width, clock_height = clock_image.get_size()
right_hand_width, right_hand_height = right_hand_image.get_size()
left_hand_width, left_hand_height = left_hand_image.get_size()


clock_center_x = window_width // 2
clock_center_y = window_height // 2

start_angle = 90

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    
    current_time = time.localtime()
    seconds = current_time.tm_sec

    
    angle = start_angle - seconds * (360 / 60)
    angle_rad = math.radians(angle)

  
    rotated_left_hand = pygame.transform.rotate(left_hand_image, angle)

    
    left_hand_position_x = clock_center_x - rotated_left_hand.get_width() // 2
    left_hand_position_y = clock_center_y - rotated_left_hand.get_height() // 2
    window.blit(clock_image, (0, 0))

   
    window.blit(right_hand_image, (clock_center_x - right_hand_width // 2, clock_center_y - right_hand_height // 2))

    window.blit(rotated_left_hand, (left_hand_position_x, left_hand_position_y))

    pygame.display.flip()



pygame.quit()
"""
"""
import pygame

pygame.init()
x = 50
y = 50
width = 100
vel = 5
win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Gametoooooo")
Run = True

while Run:
    pygame.time.delay(20)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
    if keys[pygame.K_RIGHT] and x < 500 - width:
        x += vel
    if keys[pygame.K_UP] and y > vel:
        y -= vel
    if keys[pygame.K_DOWN] and y < 500 - width:
        y += vel

    win.fill((255, 255, 255))  # Перемещение этой строки вверх для очистки экрана перед рисованием
    pygame.draw.circle(win, (255, 255, 0), (x, y), 5, width)
    pygame.display.update()

pygame.quit()
"""

"""
import pygame
pygame.init()

win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("First Game")

x = 30
y = 30
radius = 25
vel = 5

run = True

while run:
    pygame.time.delay(5)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT] and x >  radius:  
        x -= vel

    if keys[pygame.K_RIGHT] and x < 500  - radius:  
        x += vel

    if keys[pygame.K_UP] and y > radius:  
        y -= vel

    if keys[pygame.K_DOWN] and y < 500 - radius:
        y += vel

    win.fill((255, 255, 255))
    pygame.draw.circle(win, (255, 0, 0), (x, y), radius)
    pygame.display.update()

pygame.quit()
"""

"""
import pygame
pygame.init()

screen = pygame.display.set_mode((50,50))

x ,y = screen.get_size()
pygame.display.quit()

print(x,y)
"""


"""
import pygame
pygame.init()
win = pygame.display.set_mode((500,500))
pygame.display.set_caption("Un resizable window")

running = True

while running :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()
"""


"""
import pygame
pygame.init()
win = pygame.display.set_mode((500,500), pygame.RESIZABLE)

pygame.display.set_caption("Resizable window")

running = True
while running :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runnning = False
pygame.quit()
"""



"""
import pygame
pygame.init()
win = pygame.display.set_mode((500,500))

pygame.display.set_caption("Hello world")
color  = (255,0,0)

win.fill(color)
pygame.display.flip()

"""

"""
import pygame
pygame.init()

win = pygame.display.set_mode((500,500))
pygame.display.set_caption("Eroor")
color = (255,255,255)

win.fill(color)
pygame.display.flip()
"""

"""
import pygame
pygame.init()
win = pygame.display.set_mode((160,900))
pygame.display.set_caption("Hello world")
color  = "red"
run = True
while run:
    
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
        run  = False

  win.fill(color)
  pygame.display.flip()


  if (color == "red"):
      color = "green"
  else:
      color = "red"


pygame.quit()
"""

"""
import pygame
pygame.init()

win = pygame.display.set_mode((500,500))
pygame.display.set_caption("Hello world")
icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)
"""



"""

import pygame
import datetime
pygame.init()
current_date = datetime.datetime.now()

SECONDS  = current_date.second
MINUTE = current_date.minute
win = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Mickey clock")

image = pygame.image.load("mainclock.png")
right_hand_image = pygame.image.load("rightarm.png")
left_hand_image = pygame.image.load("leftarm.png")

right_hand_image = pygame.transform.scale(right_hand_image, (int(right_hand_image.get_width() * 0.6), int(right_hand_image.get_height() * 0.6)))
left_hand_image = pygame.transform.scale(left_hand_image, (int(left_hand_image.get_width() * 0.6), int(left_hand_image.get_height() * 0.6)))

image = pygame.transform.scale(image, (800, 600))
image_width, image_height = image.get_size()

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    current_time = datetime.datetime.now()
    second_angle  =  90 - current_time.second * 6
    minute_angle = 90 - current_time.minute * 6 
    rotated_image_left  =  pygame.transform.rotate(left_hand_image , second_angle)
    rotated_image_right  = pygame.transform.rotate(right_hand_image, minute_angle)
    

    win.fill((255, 255, 255))
    win.blit(image, (0, 0))

    right_hand_x = (image_width - right_hand_image.get_width()) //2 
    right_hand_y = (image_height - right_hand_image.get_height()) //2 
    left_hand_x = (image_width - left_hand_image.get_width()) //2
    left_hand_y = (image_height - left_hand_image.get_height()) // 2
    rotated_image_x = (image_width - rotated_image_left.get_width()) // 2
    rotated_image_y  = (image_height - rotated_image_left.get_height()) // 2
    rotated_image_x1 = (image_width - rotated_image_right.get_width()) // 2
    rotated_image_y1 = (image_height - rotated_image_right.get_height())  // 2

    win.blit(rotated_image_right, (rotated_image_x1, rotated_image_y1))

    win.blit(rotated_image_left,(rotated_image_x,rotated_image_y))

    pygame.display.update()

pygame.quit()
"""

"""
import pygame
pygame.init()
win  = pygame.display.set_mode((500,500))
color = (255,255,0)
pygame.draw.rect(win,color,(0,0,60,60))
pygame.display.flip()
"""


"""
import pygame
pygame.init()
win = pygame.display.set_mode((500,500))
pygame.display.set_caption("Hello world")
image1 = pygame.image.load("mainclock.png")
win.blit(image1,(0,0))
win.blit(image1,(10,10))
pygame.display.flip()
"""


"""
import pygame
pygame.init()
win  = pygame.display.set_mode((500,500))]
pygame.display.set_caption("Hello world")
"""
"""
import pygame
pygame.init()

win = pygame.display.set_mode((500,500))
pygame.display.set_caption("Hello world")
square  = pygame.Surface((50,100))
square.fill((255,0,0))

run  =True
while run:
    win.blit(square, (0,0))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
pygame.quit()
"""

"""
import pygame
pygame.init()

win = pygame.display.set_mode((500,500))
pygame.display.set_caption("Hello world")
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.draw.circle(win,(255,0,0),(25,25),25)
    pygame.display.update()
    pygame.display.flip()
pygame.quit()
"""
"""
import pygame
pygame.init()

win  = pygame.display.set_mode((500,500))
pygame.display.set_caption("Music player")
white  = (255,255,255)
green = (0 , 255, 0 )
blue  = (0,0,255)
red = (255,0,0)
black = (0,0,0)
x = 400
y = 400

display_surface  = pygame.display.set_mode((x,y))
pygame.display.set_caption("Drawing")
display_surface.fill(white)

running   = True
while running :
    for event  in  pygame.event.get():
        if event.type == pygame.QUIT:
            running =  False
    pygame.draw.polygon(win,green , [(5,6), (30,39), (40,41), (25,25), (10,80)])
pygame.quit()
"""

"""
import pygame
pygame.init()
voice = 0.0
win = pygame.display.set_mode((800,600))
pygame.display.set_caption("MP4 music player")
image = pygame.image.load("musicplayer.png")
image_of_display = pygame.image.load("mp4.png")
image_of_display = pygame.transform.scale(image_of_display,(800,600))
pygame.display.set_icon(image)
list_of_musics= ["Егор Крид - Таро (feat. Тenderlybae & Егорик)", "23116-kairat-nurtas-ft-zangar-nurtas-meili"]
cur0rent_index = 0
pygame.mixer.music.load(list_of_musics[current_index])
pygame.mixer.music.play()
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run  = False
    keys  = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT] and current_index != len(list_of_musics):
        current_index += 1
        pygame.mixer.music.load(list_of_musics[current_index])
        pygame.mixer.music.play()
        if keys[pygame.K_SPACE]:
            pygame.mixer.music.pause()
        if keys[pygame.K_RETURN]:
            pygame.mixer.music.unpause()
        if keys[pygame.K_UP]:
            voice += 1
            pygame.mixer.music.set_volume(voice)
        if keys[pygame.K_DOWN]:
            voice = -1
            pygame.mixer.music.set_volume(voice)
            
    if keys[pygame.K_LEFT] and current_index != -1:
        current_index -= 1
        pygame.mixer.music.load(list_of_musics[current_index])
        pygame.mixer.music.play()
        if keys[pygame.K_SPACE]:
            pygame.mixer.music.pause()
        if keys[pygame.K_RETURN]:
            pygame.mixer.music.unpause()
        if keys[pygame.K_UP]:
            voice += 1
            pygame.mixer.music.set_volume(voice)
        if keys[pygame.K_DOWN]:
            voice = -1
            pygame.mixer.music.set_volume(voice)
        
        
        
    win.blit(image_of_display,(0,0))
    pygame.display.update()
pygame.quit()

"""

"""
import pygame

pygame.init()
voice = 0.5
win = pygame.display.set_mode((800, 600))
pygame.display.set_caption("MP4 music player")
image = pygame.image.load("musicplayer.png")
image_of_display = pygame.image.load("mp4.png")
image_of_display = pygame.transform.scale(image_of_display, (800, 600))
pygame.display.set_icon(image)
list_of_musics = ["23116-kairat-nurtas-ft-zangar-nurtas-meili.mp3", "Диета кз & Жоламан Абуталип - Чё там карындас - 2 2019-[muzmir.kz].mp3", "kazak_kobyzy.mp3"]
current_index = 0
pygame.mixer.music.load(list_of_musics[current_index])
pygame.mixer.music.play()
print(len(list_of_musics))

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT] and current_index < len(list_of_musics)-1:                          
        current_index += 1
        pygame.mixer.music.load(list_of_musics[current_index])
        pygame.mixer.music.play()

    if keys[pygame.K_LEFT] and current_index > 0:
        current_index -= 1
        pygame.mixer.music.load(list_of_musics[current_index])
        pygame.mixer.music.play()

    if keys[pygame.K_SPACE]: 
        if pygame.mixer.music.get_busy():
            pygame.mixer.music.pause()
        else:
            pygame.mixer.music.unpause()

    if keys[pygame.K_UP] and voice < 1.0:
        voice += 0.1
        pygame.mixer.music.set_volume(voice)

    if keys[pygame.K_DOWN] and voice >= 0.0:
        voice -= 0.1
        pygame.mixer.music.set_volume(voice)

    win.blit(image_of_display, (0, 0))
    pygame.display.update()

pygame.quit()
"""


"""
import pygame
pygame.init()

win = pygame.display.set_mode((500,500))
pygame.display.set_caption("First Game")

x = 0
y = 0
width = 40
height = 60
vel = 5

run = True

while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT] and x > vel:  # Making sure the top left position of our character is greater than our vel so we never move off the screen.
        x -= vel

    if keys[pygame.K_RIGHT] and x < 500 - width:  # Making sure the top right corner of our character is less than the screen width - its width 
        x += vel

    if keys[pygame.K_UP] and y >= vel:  # Same principles apply for the y coordinate
        y -= vel

    if keys[pygame.K_DOWN] and y < 500 - height:
        y += vel

    
    win.fill((0,0,0))
    pygame.draw.rect(win, (255,0,0), (x, y, width, height))   
    pygame.display.update() 
    
pygame.quit()
"""



"""
import pygame
from pygame.locals import *
pygame.init()

win = pygame.display.set_mode((500,500))
pygame.display.set_caption("Hello world")

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    win.fill((0,0,0))
    pygame.draw.line(win,(255,0,0),(0,0),(100,0),10)
    pygame.display.update()
pygame.quit()

"""



"""
import pygame
from pygame.locals import *

pygame.init()
vel = 5
win = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Hello World")
image_of_road = pygame.image.load("road.png")
image_of_road = pygame.transform.scale(image_of_road,(800,600))
image_of_car = pygame.image.load("unnamed.png")
image_of_car = pygame.transform.scale(image_of_car, (100, 100))
width_of_car, height_of_car = image_of_car.get_size()
image_of_coin = pygame.image.load("coin.png")
image_of_coin = pygame.transform.scale(image_of_coin,(50,50))
x = 105
FPS = 100
clock = pygame.time.Clock()
run = True



class Coin:
    def __init__(self):
        self.x = random.randint
while run:
    pygame.time.delay(3)
    #clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > 105:
        x -= vel
    if keys[pygame.K_RIGHT] and x < 800 - 200:
        x += vel
    win.blit(image_of_road,(0,0))
    win.blit(image_of_car, (x, win.get_height() - height_of_car))
    pygame.display.update()

pygame.quit()
"""


"""
import pygame
from pygame.locals import *
import random

pygame.init()
vel = 5
win = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Hello World")
image_of_road = pygame.image.load("road.png")
image_of_road = pygame.transform.scale(image_of_road, (800, 600))
image_of_car = pygame.image.load("unnamed.png")
image_of_car = pygame.transform.scale(image_of_car, (100, 100))
image_of_coin = pygame.image.load("coin.png")
image_of_coin = pygame.transform.scale(image_of_coin, (50, 50))
width_of_car, height_of_car = image_of_car.get_size()
x = 105
coin_x = random.randint(110, win.get_width() - 200)
coin_y = -image_of_coin.get_height()
coin_speed = 3
coin_visible = True
FPS = 60
clock = pygame.time.Clock()
run = True

def move_coin():
    global coin_x, coin_y, coin_visible
    coin_y += coin_speed
    if coin_y > win.get_height():
        coin_visible = False
        reset_coin()

def reset_coin():
    global coin_x, coin_y, coin_visible
    coin_x = random.randint(110, win.get_width() - 200)
    coin_y = -image_of_coin.get_height()
    coin_visible = True

while run:
    clock.tick(FPS)
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > 105:
        x -= vel
    if keys[pygame.K_RIGHT] and x < 800 - 200:
        x += vel

    move_coin()

    win.blit(image_of_road, (0, 0))
    win.blit(image_of_car, (x, win.get_height() - height_of_car))

    if coin_visible:
        win.blit(image_of_coin, (coin_x, coin_y))

    pygame.display.update()

pygame.quit()
"""








"""
import pygame
from pygame.locals import *
import random

pygame.init()
vel = 5
win = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Hello world")
image_of_road = pygame.image.load("road.png")
image_of_road = pygame.transform.scale(image_of_road, (800, 600))
image_of_car = pygame.image.load("unnamed.png")
image_of_car = pygame.transform.scale(image_of_car, (100, 100))
image_of_coin = pygame.image.load("coin.png")
image_of_coin = pygame.transform.scale(image_of_coin, (30, 30))
width_of_car, height_of_car = image_of_car.get_size()
x = 105
coin_x = random.randint(110, win.get_width())
coin_y = -image_of_coin.get_height()
coin_speed = 3
coin_visible = True
coins_collected = 0  
font = pygame.font.SysFont(None, 36)  
FPS = 60
clock = pygame.time.Clock()
run = True

def move_coin():
    global coin_x, coin_y, coin_visible
    coin_y += coin_speed
    if coin_y > win.get_height():
        coin_visible = False
        reset_coin()

def reset_coin():
    global coin_x, coin_y, coin_visible
    coin_x = random.randint(110, win.get_width() - 200)
    coin_y = -image_of_coin.get_height()
    coin_visible = True

def check_collision(rect1, rect2):
    return rect1.colliderect(rect2)

while run:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > 105:
        x -= vel
    if keys[pygame.K_RIGHT] and x < 800 - 200:
        x += vel

    move_coin()
    car_rect = pygame.Rect(x, win.get_height() - height_of_car, width_of_car, height_of_car)
    coin_rect = pygame.Rect(coin_x, coin_y, image_of_coin.get_width(), image_of_coin.get_height())

    if check_collision(car_rect, coin_rect):
        if coin_visible:
            coins_collected += 1
        coin_visible = False

    win.blit(image_of_road, (0, 0))
    win.blit(image_of_car, (x, win.get_height() - height_of_car))

    if coin_visible:
        win.blit(image_of_coin, (coin_x, coin_y))
    
 
    counter_text = font.render("YOUR SCORE PALUAN : " + str(coins_collected), True, (255, 0, 0))
    win.blit(counter_text, (10, 10))

    pygame.display.update()

pygame.quit()
"""


"""
import time
import random
import pygame
game_over = True
run  = True
level_up_image = pygame.image.load("level_up1.jpg") # в этом строке кода я создал  цикл для отоброжения игра окончена , создал счетчик для коинов и счетчик для левеле при достижении определенного числа коинов  
counter_for_coin=0
current_level = 1
pygame.init()
win = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Hello world")
visible_police = True
image_of_car = pygame.image.load("unnamed.png")
image_of_coin = pygame.image.load("frota.png")
image_of_coin = pygame.transform.scale(image_of_coin, (50, 50))
image_of_road = pygame.image.load("road.png")
image_of_road = pygame.transform.scale(image_of_road, (800, 600)) # тут я создал все картинки которые нужны в этой игре кратинка машины картинка полицейского картинка коинов картинка игра окончена 
image_of_car = pygame.transform.scale(image_of_car, (100, 100))
image_of_polices = pygame.image.load("police.png")
image_of_polices = pygame.transform.scale(image_of_polices,(100,100))
image_of_polices1 = pygame.image.load("police.png")
image_of_polices1 = pygame.transform.scale(image_of_polices,(100,100))
image_of_polices2 = pygame.image.load("police.png")
image_of_polices2 = pygame.transform.scale(image_of_polices,(100,100))
image_of_game_over = pygame.image.load("game_over.png")
image_of_game_over = pygame.transform.scale(image_of_game_over,(800,600))
list_of_muics = ["Mortal Kombat - Reptile Theme.mp3","4dbecaef6977b43.mp3"]
pygame.mixer.music.load(list_of_muics[0])
pygame.mixer.music.play()
music_or_not = True 
velocity_of_a_car = 2
velocity_of_a_coin = 2 # тут я для каждому обьекты дал скорость 
velocity_of_a_police = 3
x = 105
y = win.get_height() - image_of_car.get_height() 

x_for_coin = random.randint(105, 600)
y_for_coin = random.randint(0,600)# это для рандомного появления коинов 
font  = pygame.font.Font("c.ttf",24)


def spawn_coin():
    global x_for_coin, y_for_coin
    x_for_coin = random.randint(105, 600) # функция которая спавнит коины 
    y_for_coin = 0

def move_coin():
    global y_for_coin
    y_for_coin += velocity_of_a_coin # функция которая дает движение коину 
def check_collision():
    car_rect = pygame.Rect(x,y,image_of_car.get_width(),image_of_car.get_height())
    coin_rect  = pygame.Rect(x_for_coin,y_for_coin,image_of_coin.get_width(),image_of_coin.get_height()) # функция которая проверяет столкновение с коином и с машиной 
    if car_rect.colliderect(coin_rect):
        global counter_for_coin,current_level,velocity_of_a_car , velocity_of_a_police
        counter_for_coin += 5
        if counter_for_coin >= 100:
            velocity_of_a_police += 1
            current_level += 1
            win.blit(level_up_image,((win.get_width() - level_up_image.get_width())//2,(win.get_height() - level_up_image.get_height())//2))
            pygame.display.update()
            pygame.time.delay(5000)
            counter_for_coin = 0
            
        counter_for_coin += 5
        spawn_coin()
x_for_police = random.randint(105,600) # функция для движения полицейской машины как enemey я взял полицейскую машину 
y_for_police  = random.randint(0,600)

def spawn_police():
    global x_for_police, y_for_police,x_for_police1, y_for_police1,x_for_police2,y_for_police2
    x_for_police = random.randint(105,600) # функция которая спавнит enemy полицейскую машину 
    y_for_police  = 0
def move_police():
    global y_for_police, y_for_police1,y_for_police2
    y_for_police += velocity_of_a_police # функция которая двишгает полицейскую машину
    if y_for_police > win.get_height():  # Если полицейская машина ушла за пределы экрана
        visible_police = False
start_time = time.time()
pygame.time.delay(100)
start_time_for_police_spawn = time.time()

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
 
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > 105:
        x -= velocity_of_a_car
    if keys[pygame.K_RIGHT] and x < 800 - 200: #  подключаю кнопки от которых будет двигаться наша машина 
        x += velocity_of_a_car
    if keys[pygame.K_UP] and y > 0:
        y -= velocity_of_a_car
    if keys[pygame.K_DOWN] and y < win.get_height() - image_of_car.get_height():
        y += velocity_of_a_car

    win.blit(image_of_road, (0, 0))
    win.blit(image_of_car, (x, y))

    current_time = time.time()  # выдаю время потом в цикле если разница между временами будет 5 секунд я спавню новые коины чтоюы интервал был 5 секунд  
    current_time_for_police_spawn = time.time()

    if current_time_for_police_spawn - start_time_for_police_spawn   >= 2:
        spawn_police()
        start_time_for_police_spawn  = current_time_for_police_spawn
    
    if current_time - start_time >= 4:
        spawn_coin()
        start_time = current_time

    move_coin()
    win.blit(image_of_coin, (x_for_coin, y_for_coin))
    win.blit(image_of_polices,(x_for_police,y_for_police))
    move_police()
    check_collision()
    text_surface = font.render(f"Your score:{counter_for_coin}", None , (255,0,0))
    level_surface  = font.render(f"Your current level:{current_level}",None,(255,0,0))  # пишу счетчик коинов и левел через ttf формат  
    win.blit(text_surface,(0,0))
    win.blit(level_surface,(win.get_width() - level_surface.get_width(),0))
    car_rect = pygame.Rect(x,y,image_of_car.get_width(),image_of_car.get_height())
    police_rect = pygame.Rect(x_for_police, y_for_police,image_of_polices.get_width(),image_of_polices.get_height())
    if car_rect.colliderect(police_rect):
        win.blit(image_of_game_over, (0, 0)) # проверяю столкновение машины с enemy (полицейская машина)
        pygame.mixer.music.load(list_of_muics[1])
        pygame.mixer.music.play()
        pygame.display.update()
        pygame.time.delay(3000)
        run = False
    pygame.display.update()
pygame.quit()

"""





"""
import pygame 
import random
pygame.init()

W, H = 1200, 800
FPS = 60

screen = pygame.display.set_mode((W, H), pygame.RESIZABLE)
clock = pygame.time.Clock()
done = False
bg = (0, 0, 0)

#paddle
paddleW = 150
paddleH = 25
paddleSpeed = 20
paddle = pygame.Rect(W // 2 - paddleW // 2, H - paddleH - 30, paddleW, paddleH)


#Ball
ballRadius = 20
ballSpeed = 6
ball_rect = int(ballRadius * 2 ** 0.5)
ball = pygame.Rect(random.randrange(ball_rect, W - ball_rect), H // 2, ball_rect, ball_rect)
dx, dy = 1, -1

#Game score
game_score = 0
game_score_fonts = pygame.font.SysFont('comicsansms', 40)
game_score_text = game_score_fonts.render(f'Your game score is: {game_score}', True, (0, 0, 0))
game_score_rect = game_score_text.get_rect()
game_score_rect.center = (210, 20)

#Catching sound
collision_sound = pygame.mixer.Sound('audio/catch.mp3')

def detect_collision(dx, dy, ball, rect):
    if dx > 0:
        delta_x = ball.right - rect.left
    else:
        delta_x = rect.right - ball.left
    if dy > 0:
        delta_y = ball.bottom - rect.top
    else:
        delta_y = rect.bottom - ball.top

    if abs(delta_x - delta_y) < 10:
        dx, dy = -dx, -dy
    if delta_x > delta_y:
        dy = -dy
    elif delta_y > delta_x:
        dx = -dx
    return dx, dy


#block settings
block_list = [pygame.Rect(10 + 120 * i, 50 + 70 * j,
        100, 50) for i in range(10) for j in range (4)]
color_list = [(random.randrange(0, 255), 
    random.randrange(0, 255),  random.randrange(0, 255))
              for i in range(10) for j in range(4)] 
print(block_list)
#Game over Screen
losefont = pygame.font.SysFont('comicsansms', 40)
losetext = losefont.render('Game Over', True, (255, 255, 255))
losetextRect = losetext.get_rect()
losetextRect.center = (W // 2, H // 2)

#Win Screen
winfont = pygame.font.SysFont('comicsansms', 40)
wintext = losefont.render('You win yay', True, (0, 0, 0))
wintextRect = wintext.get_rect()
wintextRect.center = (W // 2, H // 2)


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(bg)
    
    # print(next(enumerate(block_list)))
    
    [pygame.draw.rect(screen, color_list[color], block)
     for color, block in enumerate (block_list)] #drawing blocks
    pygame.draw.rect(screen, pygame.Color(255, 255, 255), paddle)
    pygame.draw.circle(screen, pygame.Color(255, 0, 0), ball.center, ballRadius)
    # print(next(enumerate (block_list)))

    #Ball movement
    ball.x += ballSpeed * dx
    ball.y += ballSpeed * dy

    #Collision left 
    if ball.centerx < ballRadius or ball.centerx > W - ballRadius:
        dx = -dx
    #Collision top
    if ball.centery < ballRadius + 50: 
        dy = -dy
    #Collision with paddle
    if ball.colliderect(paddle) and dy > 0:
        dx, dy = detect_collision(dx, dy, ball, paddle)

    #Collision blocks
    hitIndex = ball.collidelist(block_list)

    if hitIndex != -1:
        hitRect = block_list.pop(hitIndex)
        hitColor = color_list.pop(hitIndex)
        dx, dy = detect_collision(dx, dy, ball, hitRect)
        game_score += 1
        collision_sound.play()
        
    #Game score
    game_score_text = game_score_fonts.render(f'Your game score is: {game_score}', True, (255, 255, 255))
    screen.blit(game_score_text, game_score_rect)
    
    #Win/lose screens
    if ball.bottom > H:
        screen.fill((0, 0, 0))
        screen.blit(losetext, losetextRect)
    elif not len(block_list):
        screen.fill((255,255, 255))
        screen.blit(wintext, wintextRect)
    # print(pygame.K_LEFT)
    #Paddle Control
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] and paddle.left > 0:
        paddle.left -= paddleSpeed
    if key[pygame.K_RIGHT] and paddle.right < W:
        paddle.right += paddleSpeed


    pygame.display.flip()
    clock.tick(FPS)

"""
"""
import pygame 
import random
pygame.init()

W, H = 800, 600
FPS = 60

screen = pygame.display.set_mode((W, H), pygame.RESIZABLE)
clock = pygame.time.Clock()
done = False
bg = (255, 192, 203)

paddleW = 200
paddleH = 25
paddleSpeed = 20
paddle = pygame.Rect(W // 2 - paddleW // 2, H - paddleH - 30, paddleW, paddleH)


#Ball
ballRadius = 20
ballSpeed = 6
ball_rect = int(ballRadius * 2 ** 0.5)
ball = pygame.Rect(random.randrange(ball_rect, W - ball_rect), H // 2, ball_rect, ball_rect)
dx, dy = 1, -1


#Game over
font = pygame.font.SysFont('comicsansms', 40)
text = font.render('Game Over', True, (255, 255, 255))
textRect = text.get_rect()
textRect.center = (W // 2, H // 2)
current_time  = 0 
def increase_speed_with_a_time():
    


while not done:
    current_time += 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(bg)
    
    pygame.draw.rect(screen, pygame.Color(234, 250, 177), paddle)
    pygame.draw.circle(screen, pygame.Color(250, 241, 157), ball.center, ballRadius)
    
    
    #Paddle Control
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] and paddle.left > 0:
        paddle.left -= paddleSpeed
    if key[pygame.K_RIGHT] and paddle.right < W:
        paddle.right += paddleSpeed


    #Ball movement
    ball.x += ballSpeed * dx
    ball.y += ballSpeed * dy

    # #Collision left 
    if ball.centerx < ballRadius or ball.centerx > W - ballRadius:
        dx = -dx
    #Collision TOP
    if ball.centery < ballRadius + 50: 
        dy = -dy
    #Collision with paddle
    if ball.colliderect(paddle) and dy > 0:
        dy = -dy
    if ball.y > H or ball.x > W:
        screen.fill((0, 0, 0))
        screen.blit(text, textRect)
    if current_time

    pygame.display.update()
    clock.tick(FPS)
"""

"""
import pygame
pygame.init()
white = (255,255,255)
black = (0,0,0)
win = pygame.display.set_mode((800,600))
pygame.display.set_caption("Hello world")
rectangle_image = pygame.image.load("rectangle1.png")
rectangle_image = pygame.transform.scale(rectangle_image,(80, 80))
circle_image = pygame.image.load("circle.png")
circle_image = pygame.transform.scale(circle_image, (80, 80))
run = True
drawing = True
current_tool = None

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # Левая кнопка мыши нажата
                mouse_pos = pygame.mouse.get_pos()
                if mouse_pos[0] < 80 and mouse_pos[1] < 80:  # Проверка клика на картинке прямоугольника
                    current_tool = "rectangle"
                elif 80 < mouse_pos[0] < 160 and mouse_pos[1] < 80:  # Проверка клика на картинке окружности
                    current_tool = "circle"

    if drawing:
        mouse_pos = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed()[0]:  # Левая кнопка мыши нажата
            if current_tool == "rectangle":
                pygame.draw.circle(win, black, mouse_pos, 5)
            elif current_tool == "circle":
                pygame.draw.circle(win, black, mouse_pos, 40)
    else:
        if pygame.mouse.get_pressed()[0]:  # Левая кнопка мыши нажата
            if current_tool == "rectangle":
                pygame.draw.circle(win, white, mouse_pos, 10)
            elif current_tool == "circle":                pygame.draw.circle(win, white, mouse_pos, 40)
    win.fill((255,255,255))
    rectangle_image = pygame.image.load("rectangle1.png")
    rectangle_image = pygame.transform.scale(rectangle_image,(80, 80))
    circle_image = pygame.image.load("circle.png")
    circle_image = pygame.transform.scale(circle_image, (80, 80))

pygame.quit()
"""
\


"""
import pygame
pygame.init()

w = 800
h = 600
sc = pygame.display.set_mode((w,h))
pygame.display.set_caption("Mouse")

WHITE  = (255,255,255)
BLUE = (0,0,255)
GREEN = (0,255,0)
RED = (255,0,0)

FPS = 60
clock = pygame.time.Clock()

run = True
while run :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print("Нажата кнопка : ", event.button)
pygame.quit()
"""


"""
import pygame
pygame.init()
win = pygame.display.set_mode((800,600))
pygame.display.set_caption("Paint application")
rectangle_image = pygame.image.load("rectangle1.png")
rectangle_image = pygame.transform.scale(rectangle_image,(80, 80))
circle_image = pygame.image.load("circle.png")
circle_image = pygame.transform.scale(circle_image, (80, 80))
run = True
drawing = False # пока ничего не рисуем и опция дроуинг фолс 
black = (0,0,0)
while run :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                drawing  = True
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                drawing  = False
    
    win.fill((255,255,255))
    win.blit(rectangle_image, (0,0))
    win.blit(circle_image, (80,0))
    pygame.draw.line(win, (200,200,200), (0,90),(800,90),4)
    if drawing:
        pos = pygame.mouse.get_pos()
        pygame.draw.circle(win,black,pos,5)
    pygame.display.update()
pygame.quit()
"""



"""
import pygame 
import random

pygame.init()

W, H = 1200, 800
FPS = 60

screen = pygame.display.set_mode((W, H), pygame.RESIZABLE)
clock = pygame.time.Clock()
done = False
bg = (0, 0, 0)

# Paddle
paddleW = 150
paddleH = 25
paddleSpeed = 20
paddle = pygame.Rect(W // 2 - paddleW // 2, H - paddleH - 30, paddleW, paddleH)

# Ball
ballRadius = 20
ballSpeed = 6  # Initial ball speed
ball_rect = int(ballRadius * 2 ** 0.5)
ball = pygame.Rect(random.randrange(ball_rect, W - ball_rect), H // 2, ball_rect, ball_rect)
dx, dy = 1, -1

# Game score
game_score = 0
game_score_fonts = pygame.font.SysFont('comicsansms', 40)
game_score_text = game_score_fonts.render(f'Your game score is: {game_score}', True, (0, 0, 0))
game_score_rect = game_score_text.get_rect()
game_score_rect.center = (210, 20)



# Time tracking for increasing ball speed
last_speed_increase = pygame.time.get_ticks() / 1000  # in seconds
speed_increase_interval = 10  # increase speed every 10 seconds


last_shrink_time = pygame.time.get_ticks() / 1000  
shrink_interval = 10  
shrink_amount = 10  

def detect_collision(dx, dy, ball, rect):
    if dx > 0:
        delta_x = ball.right - rect.left
    else:
        delta_x = rect.right - ball.left
    if dy > 0:
        delta_y = ball.bottom - rect.top
    else:
        delta_y = rect.bottom - ball.top

    if abs(delta_x - delta_y) < 10:
        dx, dy = -dx, -dy
    if delta_x > delta_y:
        dy = -dy
    elif delta_y > delta_x:
        dx = -dx
    return dx, dy

# Block settings
block_list = [pygame.Rect(10 + 120 * i, 50 + 70 * j, 100, 50) for i in range(10) for j in range(4)]
color_list = [(random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255)) for _ in range(40)]


# Game over Screen
losefont = pygame.font.SysFont('comicsansms', 40)
losetext = losefont.render('Game Over', True, (255, 255, 255))
losetextRect = losetext.get_rect()
losetextRect.center = (W // 2, H // 2)

# Win Screen
winfont = pygame.font.SysFont('comicsansms', 40)
wintext = losefont.render('You win yay', True, (0, 0, 0))
wintextRect = wintext.get_rect()
wintextRect.center = (W // 2, H // 2)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(bg)
    
    [pygame.draw.rect(screen, color_list[color], block) for color, block in enumerate(block_list)] #drawing blocks
    pygame.draw.rect(screen, pygame.Color(255, 255, 255), paddle)
    pygame.draw.circle(screen, pygame.Color(255, 0, 0), ball.center, ballRadius)

    ball.x += ballSpeed * dx
    ball.y += ballSpeed * dy

    if ball.centerx < ballRadius or ball.centerx > W - ballRadius:
        dx = -dx

    if ball.centery < ballRadius + 50: 
        dy = -dy

    if ball.colliderect(paddle) and dy > 0:
        dx, dy = detect_collision(dx, dy, ball, paddle)

    hitIndex = ball.collidelist(block_list)

    if hitIndex != -1:
        hitRect = block_list.pop(hitIndex)
        hitColor = color_list.pop(hitIndex)
        dx, dy = detect_collision(dx, dy, ball, hitRect)
        game_score += 1
        

    game_score_text = game_score_fonts.render(f'Your game score is: {game_score}', True, (255, 255, 255))
    screen.blit(game_score_text, game_score_rect)

    if ball.bottom > H:
        screen.fill((0, 0, 0))
        screen.blit(losetext, losetextRect)
    elif not len(block_list):
        screen.fill((255,255, 255))
        screen.blit(wintext, wintextRect)

    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] and paddle.left > 0:
        paddle.left -= paddleSpeed
    if key[pygame.K_RIGHT] and paddle.right < W:
        paddle.right += paddleSpeed

   
    current_time = pygame.time.get_ticks() / 1000  
    if current_time - last_speed_increase >= speed_increase_interval:
        ballSpeed += 1  
        last_speed_increase = current_time

    
    if current_time - last_shrink_time >= shrink_interval:
        paddle.width -= shrink_amount
        last_shrink_time = current_time

    pygame.display.flip()
    clock.tick(FPS)
"""

"""
import pygame

#functions
def erase():
    rect_pos = pygame.mouse.get_pos()
    rect_width = 30
    rect_height = 30
    pygame.draw.rect(monitor, white, (rect_pos, (rect_width, rect_height)))

def cirlce():
    circle_pos = pygame.mouse.get_pos()
    circle_radius = 30
    pygame.draw.circle(monitor, color, circle_pos, circle_radius)

def rectangle():
    rect_pos = pygame.mouse.get_pos()
    rect_width = 50
    rect_height = 50
    pygame.draw.rect(monitor, color, (rect_pos, (rect_width, rect_height)))

#Функция считывает передвижение кисти, без нее линия будет обрывчитывой, а с ней прямая и аккуратная
def roundline(canvas, color, start, end, radius=1) :
    Xaxis = end[0] - start[0]
    Yaxis = end[1] - start[1]
    dist = max(abs(Xaxis), abs(Yaxis))
    for i in range(dist) :
        x = int(start[0] + float(i) / dist * Xaxis)
        y = int(start[1] + float(i) / dist * Yaxis)
        pygame.draw.circle(canvas, color, (x, y), radius)
    
pygame.init()

monitor = pygame.display.set_mode((800,600))
pygame.display.set_caption("Paint")


#Colors
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
white = (255,255,255)
black = (0,0,0)
yellow = (255,255,0)
light_blue = (0,255,255)
pink = (255,0,255)

#Начальные значания или константы
color = red
last_pos = (0,0)
mouse_down = False
monitor.fill(white)
pygame.display.update()
radius = 5


#FPS
clock = pygame.time.Clock()
check = True

while check:
    action = pygame.event.wait()
    
    #Exit
    if action.type == pygame.QUIT:
        check = False
        pygame.quit()
        
    #Keybord
    if action.type == pygame.KEYDOWN:
        #Переключение цветов
        if action.key == pygame.K_r:
            color = red
            radius = 5
        elif action.key == pygame.K_b:
            color = blue
            radius = 5
        elif action.key == pygame.K_g:
            color = green
            radius = 5
            
        #Erase1
        if action.key == pygame.K_e:
            erase()
        
        #Erase2
        if action.key == pygame.K_w:
            color = white
            radius = 20
        
        #Rectange 
        if action.key == pygame.K_p:
            rectangle()
            
        #Circle
        if action.key == pygame.K_c:
            cirlce()
            
   
    if action.type == pygame.MOUSEBUTTONDOWN:
        pygame.draw.circle(monitor, color, action.pos, 5)
        mouse_down = True
    
    
    if action.type == pygame.MOUSEBUTTONUP:
        mouse_down = False
    
    
    if action.type == pygame.MOUSEMOTION:
        if mouse_down:
            pygame.draw.circle(monitor,color,action.pos,radius)
            roundline(monitor,color,action.pos,last_pos,radius)
        last_pos = action.pos
        
    pygame.display.update()
    clock.tick(60)

"""



import pygame
pygame.init()
font  = pygame.font.Font("Samson.ttf",24)
text_surface   = font.render("Welcome to paint application!!!",None,(0,255,255))
win = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Paint application")
run = True
size_of_a_brush = 15
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255,0,0)
YELLOW  =  (255,255,0)
PURPLE  = (255,0,255)
CYAN  = (0,255,255)
ORANGE = (255,165,0)
PINK = (255,192,203)
DARKBLUE = (0,0,128)
drawing = False
current_color = RED  
shape = 'circle'
win.fill((255, 255, 255))
paint_icon = pygame.image.load("paint.png")
pygame.display.set_icon(paint_icon)
rectangle_size = 15
while run:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1: # проверяю нажат ли кнопка мышки 1- левая кнопка 2 0 колесико 3 - правая кнопка 4 - покруть колесиком вверх 5 - покрутить колесиком вниз
                drawing = True
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1: #  если кнопка не нажата то даю к переменную драуинг фолсе 
                drawing = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_c: # тут я проверяю кргу или рестангл
                shape = 'circle'
            elif event.key == pygame.K_q:
                shape = 'rectangle'
            elif event.key == pygame.K_v:
                current_color = BLACK # тут получается я проверяю цвета
            elif event.key == pygame.K_r:
                current_color = RED
            elif event.key == pygame.K_g:
                current_color = GREEN
            elif event.key == pygame.K_b:
                current_color = BLUE
            elif event.key == pygame.K_w:
                current_color  = WHITE # то функция как  эрейзер работает даю просто белый цвет
            elif event.key == pygame.K_p:
                current_color = PURPLE
            elif event.key == pygame.K_d:
                current_color = DARKBLUE
            elif event.key == pygame.K_y:
                current_color = YELLOW
            elif event.key == pygame.K_n:
                win.fill((255,255,255))# принажатии этой кнопки мы полностью создаем новую сраницу
            elif event.key  == pygame.K_1:
                size_of_a_brush = 15
            elif event.key == pygame.K_2:
                size_of_a_brush = 20
            elif event.key == pygame.K_3:
                size_of_a_brush = 30
            elif event.key == pygame.K_4:
                size_of_a_brush = 40
            elif event.key == pygame.K_5:
                size_of_a_brush = 50
            

    if drawing:
        if shape == 'circle': # тут я рисую круг либо ректангл
            pos = pygame.mouse.get_pos()
            pygame.draw.circle(win, current_color, pos, size_of_a_brush)
        elif shape == 'rectangle':
            rect_pos = pygame.mouse.get_pos()
            pygame.draw.rect(win, current_color, (rect_pos[0] - 20, rect_pos[1] - 20, size_of_a_brush*2, size_of_a_brush*2))
    win.blit(text_surface,(0,0))

    pygame.display.update()
pygame.quit()





"""
import pygame.font
import pygame
splash_screen = pygame.image.load("zastavka.png")
splash_screen = pygame.transform.scale(splash_screen,(800,600))

game_over_png = pygame.image.load("game_over1.png")
game_over_png = pygame.transform.scale(game_over_png, (800, 600))
FPS = 60
clock = pygame.time.Clock()
score = 0
pygame.init()
dx, dy = 1, -1
pygame.font.init()
win = pygame.display.set_mode((800, 600))
pygame.display.set_caption("ARCKANOID")
run = True
list_of_musics = ["neon-gaming-128925.mp3", "0961f580f9e00da.mp3"] #  создаю лист музыки  
pygame.mixer.music.load(list_of_musics[0])
pygame.mixer.music.play()

platform_width, platform_height = 100, 20
platform_rect = pygame.Rect(win.get_width() // 2 - platform_width // 2,
                            win.get_height() - 40,
                            platform_width,
                            platform_height)
    
font = pygame.font.Font("Samson.ttf", 24)
platform_speed = 10
platform_color = (0, 255, 0)
platform_shrink_interval = 10  # Интервал уменьшения платформы в секундах
last_shrink_time = pygame.time.get_ticks() / 1000  # Последнее время уменьшения платформы в секундах
win_game_png = pygame.image.load("you_win.jpg")
win_game_png = pygame.transform.scale(win_game_png,(800,600))
ball_speed_interval = 10
last_speed_time = pygame.time.get_ticks() / 1000

# шариктын опциясы 
ball_radius = 20
ball_x = win.get_width() // 2
ball_y = win.get_height() // 2
ball_speed_x = 5
ball_speed_y = -5
ball_color = (255, 0, 0)
ball_rect = pygame.Rect(ball_x - ball_radius, ball_y - ball_radius, ball_radius * 2, ball_radius * 2)

# кирпичьтын опциясы 
brick_width, brick_height = 65, 65
brick_color = (0, 0, 255)
bricks = []

for i in range(2):
    for j in range(10):
        brick_rect = pygame.Rect(j * (brick_width + 10) + 25,i * (brick_height + 10) + 5, brick_width, brick_height)
        bricks.append(brick_rect)  # Добавление свойства неразрушимости к каждому кирпичу

# Переменная для отслеживания количества разрушенных кирпичей
destroyed_bricks = 0

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Движение платформы
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and platform_rect.x > 0:
        platform_rect.x -= platform_speed
    if keys[pygame.K_RIGHT] and platform_rect.x < win.get_width() - platform_width:
        platform_rect.x += platform_speed

    # Отскок мяча от платформы
    if ball_rect.colliderect(platform_rect):
        ball_speed_y = -ball_speed_y

    # Отскок мяча от верхней границы
    if ball_y - ball_radius <= 0:
        ball_speed_y = -ball_speed_y

    # Отскок мяча от правой и левых границ
    if ball_x - ball_radius <= 0 or ball_x + ball_radius >= win.get_width():
        ball_speed_x = -ball_speed_x

    # Проверка столкновения мяча с кирпичами
    for brick in bricks:
        if ball_rect.colliderect(brick):
                bricks.remove(brick)
                destroyed_bricks += 1  # Увеличение счетчика разрушенных кирпичей
                if destroyed_bricks % 5 == 0:  # Если разрушено кратное 5 количество кирпичей
                    platform_width += 10  # Увеличение ширины платформы на 10 пикселей
                    platform_rect.width = platform_width
                ball_speed_y = -ball_speed_y
                score += 1

    # Проверка уменьшения размера платформы
    current_time = pygame.time.get_ticks() / 1000  # Текущее время в секундах
    if current_time - last_shrink_time >= platform_shrink_interval:
        platform_width -= 10  # Уменьшение ширины платформы на 10 пикселей
        platform_rect.width = platform_width
        last_shrink_time = current_time
        

    # Проверка увеличения скорости мяча каждые 10 секунд
    current_time = pygame.time.get_ticks() / 1000  # Текущее время в секундах
    if current_time - last_speed_time >= ball_speed_interval:
        if ball_speed_y > 0:  # Если мяч движется вниз
            ball_speed_y += 3  # Увеличение скорости мяча вниз
        elif ball_speed_y < 0:  # Если мяч движется вверх
            ball_speed_y -= 3  # Увеличение скорости мяча вверх
        last_speed_time = current_time

    # Движение мяча
    ball_rect.x += ball_speed_x * dx
    ball_rect.y += ball_speed_y * dy
    ball_x = ball_rect.x 
    ball_y = ball_rect.y 

    
    win.fill((0, 0, 0))  
    text_surface = font.render(f"Your current score: {score}", True, (0, 255, 255))
    win.blit(text_surface, (10, 10))

    pygame.draw.rect(win, platform_color, platform_rect)
    pygame.draw.circle(win, ball_color, (ball_x, ball_y), ball_radius)
    for brick in bricks:
        pygame.draw.rect(win, brick_color, brick)

    if score == 20 :
        win.blit(win_game_png,(0,0))
        pygame.display.update()
        pygame.time.delay(3000)
        run = False
    if ball_y > win.get_height() - ball_radius:
        win.blit(game_over_png, (0, 0))
        pygame.mixer.music.load(list_of_musics[1])
        pygame.mixer.music.play()
        pygame.display.update()
        pygame.time.delay(3000)
        run = False

    pygame.display.update()
    clock.tick(FPS)
    
pygame.quit()

"""
