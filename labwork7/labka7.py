#1)
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





#2)
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

#3)
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