"""
import time
import random
import pygame
game_over = True
run  = True
level_up_image = pygame.image.load("level_up1.jpg") # в этом строке кода я создал  цикл для отоброжения игра окончена , создал счетчик для коинов и счетчик для левеле при достижении определенного числа коинов  
counter_for_coin = 0
current_level = 1
pygame.init()
win = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Hello world")
visible_police = True
visible_police1 = True 
image_of_car = pygame.image.load("unnamed.png")
image_of_coin = pygame.image.load("frota.png")
image_of_coin = pygame.transform.scale(image_of_coin, (50, 50))
image_of_road = pygame.image.load("road.png")
image_of_road = pygame.transform.scale(image_of_road, (800, 600)) # тут я создал все картинки которые нужны в этой игре кратинка машины картинка полицейского картинка коинов картинка игра окончена 
image_of_car = pygame.transform.scale(image_of_car, (50, 50))
image_of_polices = pygame.image.load("police.png")
image_of_polices = pygame.transform.scale(image_of_polices,(50,50))
image_of_game_over = pygame.image.load("ty_gde_prava_kupil.jpg")
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
# опции для первого enemy 
image_of_polices = pygame.image.load("police.png")
image_of_polices = pygame.transform.scale(image_of_polices,(50,50))
# опции для второго enemy
image_of_polices1 = pygame.image.load("police.png")
image_of_polices1 = pygame.transform.scale(image_of_polices1,(50,50))

# опции для бонус коина
bonus_coin = pygame.image.load("100tenge-round.png")
bonus_coin = pygame.transform.scale(bonus_coin , (50,50))
x_for_bonus_coin = random.randint(105,600)
y_for_bonus_coin = random.randint(0,600)

def spawn_bonus_coin():
    global x_for_bonus_coin , y_for_bonus_coin
    x_for_bonus_coin = random.randint(105,600)# мы тут спанвим бонусные коины 
    y_for_bonus_coin = 0
def move_bonus_coin():
    global y_for_bonus_coin
    y_for_bonus_coin += velocity_of_a_coin
def check_collision_with_bonus():
    car_rect = pygame.Rect(x,y,image_of_car.get_width(),image_of_car.get_height())
    bonus_coin_rect  = pygame.Rect(x_for_bonus_coin,y_for_bonus_coin, bonus_coin.get_width(),bonus_coin.get_height())# тут проверяем столкновение бонус коинов с машиной 
    if car_rect.colliderect(bonus_coin_rect):
        global counter_for_coin , current_level, velocity_of_a_car, velocity_of_a_police
        counter_for_coin += 10
        if counter_for_coin >= 100:
            velocity_of_a_police += 1
            current_level +=1
            win.blit(level_up_image,((win.get_width() - level_up_image.get_width())//2,(win.get_height() - level_up_image.get_height())//2))
            pygame.display.update()
            pygame.time.delay(5000)
            counter_for_coin  = 0
        spawn_bonus_coin()
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
        spawn_coin()
x_for_police = random.randint(105,600) # функция для движения полицейской машины как enemey я взял полицейскую машину 
y_for_police  = random.randint(0,600)

x_for_police1 = random.randint(105,600)
y_for_police1 = random.randint(0,600)


# в целом это опция для первого enemy 
def spawn_police():
    global x_for_police, y_for_police
    x_for_police = random.randint(105,600) # функция которая спавнит enemy полицейскую машину 
    y_for_police  = 0
def move_police():
    global y_for_police, velocity_of_a_police, visible_police
    y_for_police += velocity_of_a_police # функция которая двишгает полицейскую машину
    if y_for_police > win.get_height():  # Если полицейская машина ушла за пределы экрана
        visible_police = False



start_time = time.time()
start_time_for_bonus_coin = time.time()# выдаем начально время чтобы спавнить опции по интервалу 
start_time_for_police_spawn = time.time()
start_time_for_police_spawn1 = time.time()




# тут я устанавливаю опции для второго enemy такие как спавн енеми и его движение 
def spawn_police1():
    global x_for_police1,y_for_police1 
    x_for_police1  = random.randint(110,600)
    y_for_police1 =  0
def move_police1():
    global y_for_police1 , velocity_of_a_police , vsisible_police1
    y_for_police1 += velocity_of_a_police
    if y_for_police > win.get_height():
        visible_police1 =  False

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

    current_time = time.time()  # выдаю время потом в цикле если разница между временами будет 4 секунд я спавню новые коины чтоюы интервал был 4 секунд  
    current_time_for_police_spawn = time.time()
     #тут получается я даю секундомер на 2 секунды если прошло то появляется первый (enemy)  , потом выдаю start time for polcie spawn -> current time for polcie spawn чтобы обновлять время 
    if current_time_for_police_spawn - start_time_for_police_spawn   >= 2:
        spawn_police()
        start_time_for_police_spawn  = current_time_for_police_spawn
    if current_time_for_police_spawn -  start_time_for_police_spawn1 >= 3:
        spawn_police1()
        start_time_for_police_spawn1 = current_time_for_police_spawn 
    
    if current_time - start_time >= 4: # тут получается если прошло 4 секунды то появляется новый коин 
        spawn_coin()
        start_time = current_time
    if current_time - start_time_for_bonus_coin >= 30:
        spawn_bonus_coin()
        start_time_for_bonus_coin = current_time 

    move_coin()
    move_bonus_coin()
    win.blit(image_of_coin, (x_for_coin, y_for_coin))
    win.blit(bonus_coin,(x_for_bonus_coin,y_for_bonus_coin))
    win.blit(image_of_polices,(x_for_police,y_for_police))
    win.blit(image_of_polices1, (x_for_police1,y_for_police1))
    move_police()
    move_police1()
    check_collision()
    check_collision_with_bonus()
    text_surface = font.render(f"Your score:{counter_for_coin}", None , (255,0,0))
    level_surface  = font.render(f"Your current level:{current_level}",None,(255,0,0))  # пишу счетчик коинов и левел через ttf формат  
    win.blit(text_surface,(0,0))
    win.blit(level_surface,(win.get_width() - level_surface.get_width(),0))
    car_rect = pygame.Rect(x,y,image_of_car.get_width(),image_of_car.get_height())
    police_rect = pygame.Rect(x_for_police, y_for_police,image_of_polices.get_width(),image_of_polices.get_height())
    police_rect1 =  pygame.Rect(x_for_police1,y_for_police1,image_of_polices1.get_width() , image_of_polices1.get_height())
    if car_rect.colliderect(police_rect):
        win.blit(image_of_game_over, (0, 0)) # проверяю столкновение машины с enemy (полицейская машина)
        pygame.mixer.music.load(list_of_muics[1])
        pygame.mixer.music.play()
        pygame.display.update()
        pygame.time.delay(3000)
        run = False
    if car_rect.colliderect(police_rect1):
        win.blit(image_of_game_over,(0,0))# проверяею столкновение с enemy->2
        pygame.mixer.music.load(list_of_muics[1])
        pygame.mixer.music.play()
        pygame.display.update()
        pygame.time.delay(3000)
        run = False 
    pygame.display.update()
pygame.quit()
"""


"""
from random import randrange as rnd 
import pygame
pygame.init()

counter = 0 
sc = pygame.display.set_mode((1200,800))
WIDTH = 1200
HEIGHT = 800
pygame.display.set_caption("Arckanoid new version")
FPS= 60
#icon 
icon = pygame.image.load("icon.png")
pygame.display.set_icon(icon)
# Настройки тележки 
paddle_color = pygame.Color('darkorange')
paddle_w = 330
paddle_h = 35
paddle_speed  = 15
paddle  = pygame.Rect(WIDTH//2 - paddle_w // 2,HEIGHT - paddle_h - 10,paddle_w,paddle_h)
general_shrink_interval = 10
last_shrink_time = pygame.time.get_ticks() / 1000
# настройка для фонта 
font  = pygame.font.Font(None,36)
changing_pictures  =  [("1.jpg"),("2.jpg"),("3.jpg"),("4.jpg")]
current_background  = pygame.image.load(changing_pictures[0])
current_background = pygame.transform.scale(current_background,(1200,800))
# настройка кирпичей 
block_list = [pygame.Rect(10+120*i,10+70*j,100,50) for i in range(10) for j in range(4)] # устанавливаю лист блоков 4 ряда по 10 штук 
color_list = [(rnd(30,256),rnd(30,256),rnd(30,256)) for i in range(10) for j in range(4)]# устанавливаю цвет для всех вот этих вот блоков 
ball_radius = 20  # опции  мяча радиус его и так далее 
ball_speed = 6
ball_rect  =  int(ball_radius*2**0.5) # a  = 2aqrt(R) тут  получается прямоугольник расположен внутри круга и по формуле a ^2 / 4 + a^2 / 4  = R^2 здесь находим сторону прямоугольника a
ball  = pygame.Rect(rnd(ball_rect,WIDTH - ball_rect),HEIGHT // 2, ball_rect,ball_rect)
dx, dy = 1, -1 # Даю дайрекшн для мяча 
clock = pygame.time.Clock()
winn = pygame.image.load("winning.jpg")  # устанавливаю задний фон выигрыша проигрыша 
gameover = pygame.image.load("game_over.png")
gameover = pygame.transform.scale(gameover,(1200,800))
winn = pygame.transform.scale(winn,(1200,800))

# Создание не ломающихся блоков
unbreakable_block_list = [pygame.Rect(120+400*i, 300, 100, 50) for i in range(3)]# создаю не ломающиеся блоки их штук три и цвета у них черные 

# Создание бонусных блоков
bonus_block_list = [] # создание бонус кирпичей цветом золота 
bonus_block_color = pygame.Color('gold')
last_golden_block_time = pygame.time.get_ticks() / 1000 # устанавливаю таймер для рандлмного появления золотых кирпичей 
# pause option 


paused = False

def detect_collision(dx, dy, ball, rect):
    if dx > 0:# значит что удар попал с левой сторона  потому что с левой по правой x увеличивается 
        delta_x = ball.right - rect.left
    else:
        delta_x = rect.right - ball.left # удар попал с правой стороны 
    if dy > 0:
        delta_y = ball.bottom - rect.top  # если удар был с верхней стороны к кирпичу 
    else:
        delta_y = rect.bottom - ball.top# если удар был с нижней стороны 

    if abs(delta_x - delta_y) < 10: # если их значение одинаковые мо модуля это значи что оно попало в угол кирпчиа тогда он по х и по у идет обратно 
        dx, dy = -dx, -dy
    elif delta_x > delta_y: # это озночает что мы поаали в огоризонтальную сторону и будем менять положение по корлинату у 
        dy = -dy
    elif delta_y > delta_x: # это значит что мячь попал в вертикальную часть где дельта у больше чем дельта х то мы меняем ешго дирекшн по х 
        dx = -dx


    return dx, dy

def handle_bonus_collision():
    """Обработка столкновений с бонусными блоками"""
    global counter
    hit_bonus = ball.collidelist(bonus_block_list)
    if hit_bonus != -1:
        i = 0
        # Проигрываем звук золотого блока
        pygame.mixer.music.load("for_gold_block.wav")
        pygame.mixer.music.play()

        # Удаляем бонусный блок из списка
        bonus_block_list.pop(hit_bonus)

        # Добавляем эффекты бонуса
        # Например, изменяем цвет падла на золотой
        global paddle_speed
        paddle_speed += 2 # когда пяч попадает в золотой кирпич это дает ему advantage как увелечение его скорости 
        paddle_color = pygame.Color('gold')
        # Ускоряем паддл на 10 секунд
        pygame.time.set_timer(pygame.USEREVENT + 2, 10000) # эта функция для того чтобы поставить таймер для какого то события , события можем написать как USEREVENT + 1 || USEREVENT + 2

        # Увеличиваем шарик на 10 секунд
        global ball_rect,ball_radius
        ball_rect += 15
        ball_radius += 15  # Увеличиваем радиус шарика
        # Устанавливаем таймер для возврата падла и шарика к исходным значениям
        pygame.time.set_timer(pygame.USEREVENT + 1, 10000) # тут устанавливаем таймер на 10 секунд 
        counter += 1
        i+=1

# Обработка событий для возврата падла и шарика к исходным значениям после истечения времени бонуса
def handle_bonus_effects():
    for event in pygame.event.get():
        if event.type == pygame.USEREVENT + 1: # а тут если 10 секунд прошло для события USEREVENT + 1 то возварщаем все опции к заводским настройкам
            # Возвращаем паддл к исходной скорости
            global paddle_speed
            paddle_speed //= 1.5
            # Возвращаем радиус шарика к исходному значению
            global ball_rect,ball,radius 
            ball_rect -= 15
            ball_radius -= 15
            global last_shrink_time
            last_shrink_time = pygame.time.get_ticks() // 1000
        elif event.type == pygame.USEREVENT + 2: # тут если  прошло таймер для события USEREVENT+2 то устанавливаем ему прежний цвет 
            # Устанавливаем цвет падла обратно
            global paddle_color
            paddle_color = pygame.Color('darkorange')

run = True

while run:
    sc.blit(current_background,(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # запускаю основной цикл игры 
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                paused = not paused
            elif paused and event.key == pygame.K_r:  # Опция рестарта
                # Reset all game variables to their initial values
                counter = 0
                block_list = [pygame.Rect(10+120*i,10+70*j,100,50) for i in range(10) for j in range(4)]
                color_list = [(rnd(30,256),rnd(30,256),rnd(30,256)) for i in range(10) for j in range(4)]
                ball = pygame.Rect(rnd(ball_rect,WIDTH - ball_rect),HEIGHT // 2, ball_rect,ball_rect)
                dx, dy = 1, -1
                paddle = pygame.Rect(WIDTH//2 - paddle_w // 2,HEIGHT - paddle_h - 10,paddle_w,paddle_h)
                paddle_speed = 15
                paddle_color = pygame.Color('darkorange')
                last_shrink_time = pygame.time.get_ticks() / 1000
                ball_speed = 6
                last_golden_block_time = pygame.time.get_ticks() / 1000
                bonus_block_list = []
                paused = False  # Ensure the game is unpaused after restart

            elif paused and event.key == pygame.K_c:  # Опция продолжения
                paused = False 

    if paused:
        # Отрисовка меню паузы
        pause_rect = pygame.Rect(WIDTH // 4, HEIGHT // 4, WIDTH // 2, HEIGHT // 2)
        pygame.draw.rect(sc, (128, 128, 0), pause_rect)
        pygame.draw.rect(sc, (128, 0, 0), pause_rect, 3)  # Обводка для прямоугольника

        # Отображение текста
        text_continue = font.render("Press 'C' to Continue", True, (255, 255, 255))
        text_restart = font.render("Press 'R' to Restart", True, (255, 255, 255)) # в этом разеделе получается мы просто ставим условие если оно в паузе то рисуем три кнопки опции менью паузы
        text_game_over = font.render("WELCOME TO PAUSE MENU", True ,(255,255,255))
        sc.blit(text_game_over,(460,250))
        sc.blit(text_continue, (pause_rect.centerx - text_continue.get_width() // 2, pause_rect.centery - 50))
        sc.blit(text_restart, (pause_rect.centerx - text_restart.get_width() // 2, pause_rect.centery + 50))

        pygame.display.flip() 
        continue # если код в паузе то пропускаем остальной код по continue 
    # если код не в паузе  то работает остальной код 
    keys_for_option_of_color = pygame.key.get_pressed()
    if keys_for_option_of_color[pygame.K_g]:
        paddle_color = (0,255,0)
    if keys_for_option_of_color[pygame.K_r]:
        paddle_color = (255,0,0)
    if keys_for_option_of_color[pygame.K_b]:
        paddle_color = (0,0,0)
    if keys_for_option_of_color[pygame.K_y]:
        paddle_color = (0,255,255)
    key_for_changing_backrground = pygame.key.get_pressed()
    if key_for_changing_backrground[pygame.K_1]:
        current_background  = pygame.image.load(changing_pictures[0])
        current_background  = pygame.transform.scale(current_background,(1200,800))
    if key_for_changing_backrground[pygame.K_2]:
        current_background  = pygame.image.load(changing_pictures[1])
        current_background  = pygame.transform.scale(current_background,(1200,800))
    if key_for_changing_backrground[pygame.K_3]:
        current_background  = pygame.image.load(changing_pictures[2])
        current_background  = pygame.transform.scale(current_background,(1200,800))
    if key_for_changing_backrground[pygame.K_4]:
        current_background  = pygame.image.load(changing_pictures[3])
        current_background  = pygame.transform.scale(current_background,(1200,800))
    # Обработка столкновений с бонусными блоками
    handle_bonus_collision() # вызываем функцию для столкновения с бонусными кирпичами 

    # Появление золотого бонусного блока каждые 10 секунд
    current_time = pygame.time.get_ticks() / 1000
    if current_time - last_golden_block_time >= 20:
        last_golden_block_time = current_time
        # Удаляем предыдущий золотой блок, если он есть
        if bonus_block_list: # если мы не смогли разрушить этот блок за 10 секунд то появляется новый кирпич 
            bonus_block_list.pop(0)
        # Создаем новый золотой блок в случайном месте
        new_bonus_block = pygame.Rect(rnd(0, WIDTH - 100), rnd(0, HEIGHT - 50), 100, 50) # даем ему координату появления рандомно и с одникаовыми размерами как обычные блоки 
        bonus_block_list.append(new_bonus_block) # добавляем эти рандомные кирпии в спсико получается мы только добавляем только один кирпичь 


    # Отображение не ломающихся блоков
    for block in unbreakable_block_list:
        pygame.draw.rect(sc, pygame.Color('black'), block) # тут мы отоброжаем не ломающиеся блоки их штук три 

    # Отображение бонусных блоков
    for block in bonus_block_list:
        pygame.draw.rect(sc, bonus_block_color, block) #тут мы рисуем бонусные кирпчичи 

    [pygame.draw.rect(sc,color_list[color],block) for color,block in enumerate (block_list)]
    pygame.draw.rect(sc,paddle_color,paddle) # тут основыне элементы игры такие как мяч паддл жане лист кирпичей 
    pygame.draw.circle(sc,pygame.Color('white'),ball.center,ball_radius)

    ball.x += ball_speed * dx # движения мяча по коорлдинатам у и  х 
    ball.y += ball_speed * dy
    if ball.centerx < ball_radius or ball.centerx > WIDTH - ball_radius:
        dx  = -dx # если  координата мяча по х и у становится меншье радиуса это и есть когда выходит за рамки левого края , и когда его координаты по х и у больше значения A (A ->  Ширина экрана - радиус шарика)
    if ball.centery < ball_radius: # это для верхней стены если координата становиться меньше радиуса а верхняя точка всегда уменшается то мы делаем его дайрекшн обратным 
        dy = -dy
    if ball.colliderect(paddle) and dy > 0: # тут я фиксирую столкновения мяча с паддлом  второй кондишн для того чтобы узнать мячь движется вниз или нет ? если да то мы вызываем функцию 
        dx,dy = detect_collision(dx,dy,ball,paddle)
    if ball.bottom > HEIGHT:
        sc.blit(gameover,(0,0))# тут если его нижняя часть больше высоты экрана то это значит что он вышел за нижние пределы то показываем картинку гейм овер 
        text_surface = font.render(f"YOUR SCORE:{counter}", None , (0,255,255))
        sc.blit(text_surface,(WIDTH  - text_surface.get_width(),0))
        pygame.display.update()# устанавливаем таймер на 3 секунды чтобы стояла картинка гейм овер ровно на 3 секунды 
        pygame.time.delay(3000)
        run  = False
    hit = ball.collidelist(block_list)
    if hit != -1:
        hit_rect  = block_list.pop(hit) #мы проверяем если произошла столконовение то мы удаляем этот кирпич и удалаеям его цвет и музыка появляется 
        hit_color  = color_list.pop(hit)
        dx,dy = detect_collision(dx,dy,ball,hit_rect)
        pygame.mixer.music.load("catch1.mp3")
        pygame.mixer.music.play()  
        counter += 1
    # Обработка столкновения с не ломающимися блоками
    hit_unbreakable = ball.collidelist(unbreakable_block_list)
    if hit_unbreakable != -1: # тут когда мы сталкиваемся с неломающиемися кирпичами то мы просто меняем его дирекшн без удаления блока 
        dx, dy = detect_collision(dx, dy, ball, unbreakable_block_list[hit_unbreakable])
        pygame.mixer.music.load("erro.mp3")
        pygame.mixer.music.play()
        counter -= 1
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] and paddle.left > 0 : # обычные настройки для того чтобы паддл не вышел за пределы окна 
        paddle.left -= paddle_speed
    if key[pygame.K_RIGHT] and paddle.right  < WIDTH :
        paddle.right += paddle_speed
    if not block_list:
        sc.blit(winn,(0,0))# если очко равняется -> 40 это значит что мы добили все кирпичи то выходит картинка вы выиграли и стоитт 3 секунды 
        text_surface = font.render(f"YOUR SCORE:{counter}", None , (0,255,255))
        sc.blit(text_surface,(WIDTH - text_surface.get_width(),0))
        pygame.display.update()
        pygame.time.delay(3000)
        run = False
    handle_bonus_effects() # вызываем функцию чтобы ее работа стала доступной в нашем главном цикле 
    current_time = pygame.time.get_ticks() / 1000

    if current_time - last_shrink_time >= general_shrink_interval: # если разница во времени равна 10 секундам то мы уменьшаем размеры кирпичей 
        ball_speed += 2
        paddle.width -= 10
        last_shrink_time = current_time
             # тут просто увелечиваем эту переменную чтобы каждые 10 секунд размер уменьшался в 2 раза
    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()
"""





"""
import pygame
import math

pygame.init()

font = pygame.font.Font("Samson.ttf", 24)
text_surface = font.render("Welcome to paint application!!!", None, (0, 0, 0))
win = pygame.display.set_mode((1200, 800)) # основные настройки  такие как текст 
pygame.display.set_caption("Paint application")

run = True
size_of_a_brush = 15
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255) # опции цветов какие цветы существуют для рисования 
GREEN = (0, 255, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
PURPLE = (255, 0, 255)
DARKBLUE = (0, 0, 128)
drawing = False
current_color = RED
shape = 'circle'
win.fill((255, 255, 255))
paint_icon = pygame.image.load("paint.png")# устонавливаю иконку для приложения 
pygame.display.set_icon(paint_icon)
rectangle_size = 15

#Define the shapes
shapes = ['circle', 'rectangle', 'right_triangle', 'equilateral_triangle', 'square', 'rhombus']# это у нас список фигур которые доступны для рисования 



def draw_color_buttons():
   button_width = 50
   button_height = 50# тут я рисую кнопки для опции цветов 50 на 50 квадратики 
   button_margin = 10# это у нас пространство между каждыми блоками 
   colors = [BLACK, RED, GREEN, BLUE, YELLOW, PURPLE, DARKBLUE] # создал список цветов которые доступные 
   x = 10
   y = 10
   for color in colors:
      pygame.draw.rect(win, color, (x, y, button_width, button_height)) #  рисую квадратики для опции цветов 
      y += button_height + button_margin# у меня получается все квадратики идут по вертикали менятся только положение по у  каждый раз каждый новый блок расположен внизу предедущего 


def draw_shape_buttons():
   button_width = 50# создаю уже опцию для фигур которые доступны для использования в нашем примере это треугольник правельный , квадрат , равнобедренный треугольник , ромб 
   button_height = 50
   button_margin = 10
   x = win.get_width() - button_width - 10 # устанавливая эти опции в правом верхнем углу 10 см от угла по вертикали 
   y = 10
   #enumerate() - это встроенная функция Python, которая принимает итерируемый объект (в данном случае, список shapes) и возвращает объект-перечислитель, который генерирует пары значений (индекс, элемент) для каждого элемента в списке. В данном случае, enumerate(shapes) будет генерировать пары (i, shape), где i - это индекс элемента в списке, а shape - это сам элемент.
   for i, shape in enumerate(shapes): # в этом коде получается он  дает для каждой фигуры индекс например для первой фигуры 1 для второй 2 и так далее 
      pygame.draw.rect(win, BLACK, (x, y, button_width, button_height))
      shape_text = font.render(str(i + 1), True, WHITE)# вторая булевая опция отвечает за сглаживание текста 
      shape_text_rect = shape_text.get_rect(center=(x + button_width / 2, y + button_height / 2))# тут мы получается для отображения чисел берем середину блока 
      win.blit(shape_text, shape_text_rect)# тут мы отображаем эти числа 
      y += button_height + button_margin# спускаемя по оси у на 10 см 


def handle_color_buttons_click(pos):
     button_width = 50  # устнаваливаем нажимаем ли мы на границе блоков для цветов  (проверяем мышка расположена ли в блоках)
     button_height = 50
     button_margin = 10
     colors = [BLACK, RED, GREEN, BLUE, YELLOW, PURPLE, DARKBLUE]
     x = 10
     y = 10
     for color in colors:
         if x <= pos[0] <= x + button_width and y <= pos[1] <= y + button_height: # если позиция кнопка мыши по оси х между (x -> x это 10 ) и между границей правого блока 
             return color # вернем цвет 
         y += button_height + button_margin
     return None # если кнопка не входит за гарницы точек тот ничего не рисуем 


def handle_shape_buttons_click(pos):# тут мы проверяемс позицию мыши находится ли между блоками для фигур
     button_width = 50
     button_height = 50 # еще раз напоминаем размеры блоков 
     button_margin = 10
     x = win.get_width() - button_width - 10
     y = 10
     for i, _ in enumerate(shapes):
         if x <= pos[0] <= x + button_width and y <= pos[1] <= y + button_height:  # также проверяе находится ля  позиця мыши по координату x между левым углом и правым углом если находится то рисуем 
             return shapes[i]# вернем блок номерами shapes[0], shapes[1], shapes[2], shapes[3], shapes[3]
         y += button_height + button_margin# ось у снижаем на 10 см 
     return None# если не нажимается ни одна кнопка то ничего не возваращаем 

def draw_right_triangle(pos, color, size):
     pygame.draw.polygon(win, color, [(pos[0], pos[1] + size), (pos[0] + size, pos[1] + size), (pos[0] + size, pos[1])])# 


def draw_equilateral_triangle(pos, color, size):
     height = int(math.sqrt(3) / 2 * size)
     half_base = size // 2
     pygame.draw.polygon(win, color, [(pos[0], pos[1] + height), (pos[0] + half_base, pos[1]), (pos[0] + size, pos[1] + height)])

def draw_square(pos, color, size):
     pygame.draw.rect(win, color, (pos[0], pos[1], size, size))

def draw_rhombus(pos, color, size):
     pygame.draw.polygon(win, color, [(pos[0], pos[1] + size // 2), (pos[0] + size // 2, pos[1]), (pos[0] + size, pos[1] + size // 2), (pos[0] + size // 2, pos[1] + size)])


while run:
     for event in pygame.event.get():# обычная кнопка 
         if event.type == pygame.QUIT:
             run = False
         elif event.type == pygame.MOUSEBUTTONDOWN:# если кнопка мыши нажимается 
             if event.button == 1:# если кнопка мыши нажимаем на левую кнопку 
                 drawing = True # булевую данную drawing -> True 
             else:
                 # Handle color selection button clicks
                 new_color = handle_color_buttons_click(pygame.mouse.get_pos())
                 if new_color:
                     current_color = new_color
                 # Handle shape selection button clicks
                 selected_shape = handle_shape_buttons_click(pygame.mouse.get_pos())
                 if selected_shape:
                     shape = selected_shape
         elif event.type == pygame.MOUSEBUTTONUP:
             if event.button == 1:# если отпустиили кнопку мыши то не рисуем через булевую данную 
                 drawing = False
         elif event.type == pygame.KEYDOWN:# проверяем данные кнопки 
             if event.key == pygame.K_c:# это я добавил не нажимая кнопку мыши если кнопка с то круг и так далее это как альтернатива 
                 shape = 'circle'
             elif event.key == pygame.K_q:
                 shape = 'rectangle'
             elif event.key == pygame.K_r:# тут я выбираю цветы 
                 current_color = RED
             elif event.key == pygame.K_g:
                 current_color = GREEN
             elif event.key == pygame.K_b:
                 current_color = BLUE
             elif event.key == pygame.K_w:
                 current_color = WHITE
             elif event.key == pygame.K_p:
                 current_color = PURPLE
             elif event.key == pygame.K_d:
                 current_color = DARKBLUE
             elif event.key == pygame.K_y:
                 current_color = YELLOW
             elif event.key == pygame.K_n:
                 win.fill((255, 255, 255))
             elif event.key == pygame.K_1:# если я выбираю кнопки 1 2 3 4 5 то меняем размер рисования 
                 size_of_a_brush = 15
                 rectangle_size = 15
             elif event.key == pygame.K_2:
                 size_of_a_brush = 20
                 rectangle_size = 20
             elif event.key == pygame.K_3:
                 size_of_a_brush = 30
                 rectangle_size = 30
             elif event.key == pygame.K_4:
                 size_of_a_brush = 40
                 rectangle_size = 40
             elif event.key == pygame.K_5:
                 size_of_a_brush = 50
                 rectangle_size  = 50

     if drawing:
         if shape == 'circle':
             pos = pygame.mouse.get_pos()
             pygame.draw.circle(win, current_color, pos, size_of_a_brush)# если мы рисуем и если круг то  берем позицию мышки и рисуем круг 
         elif shape == 'rectangle':
             rect_pos = pygame.mouse.get_pos()# мы берем позицию от мыши х и у и рисуем 
             pygame.draw.rect(win, current_color, (rect_pos[0] - 20, rect_pos[1] - 20, rectangle_size + 10, rectangle_size)) # добавил для него новые размеры чтобы он отличался от квадрата 
         elif shape == 'right_triangle':
            pos = pygame.mouse.get_pos()# если правельный треугольник то рисуем  это 
            draw_right_triangle(pos, current_color, size_of_a_brush * 2)
         elif shape == 'equilateral_triangle': # если треугольник равносторонии то рисуем его 
             pos = pygame.mouse.get_pos()
             draw_equilateral_triangle(pos, current_color, size_of_a_brush * 2)
         elif shape == 'square':# если квадрат то квадрат 
             pos = pygame.mouse.get_pos()
             draw_square(pos, current_color, size_of_a_brush * 2)
         elif shape == 'rhombus':
             pos = pygame.mouse.get_pos()
             draw_rhombus(pos, current_color, size_of_a_brush * 2)

     win.blit(text_surface, (430, 0))
     draw_color_buttons()
     draw_shape_buttons()
     pygame.display.update()
pygame.quit()
"""