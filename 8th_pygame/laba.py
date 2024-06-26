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