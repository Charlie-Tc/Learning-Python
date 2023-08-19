import pygame
import random
import math
from pygame import mixer

# pygame: Es un módulo diseñado para la creación de videojuegos y aplicaciones multimedia interactiva.

# initializing game
pygame.init()

# screen size
pantalla = pygame.display.set_mode((800, 600))

# title and icon
pygame.display.set_caption('Invasión Espacial')
icon = pygame.image.load('3.1 ovni.png')
pygame.display.set_icon(icon)
fondo = pygame.image.load('10.1 Fondo.jpg')

# music
mixer.music.load('16.3 MusicaFondo.mp3')
mixer.music.set_volume(0.7)
mixer.music.play(-1)

# game player
image_player = pygame.image.load('4.1 cohete.png')
position_player_x = 368
position_player_y = 500
change_player_x = 0

# game enemy
image_enemy = []
position_enemy_x = []
position_enemy_y = []
change_enemy_x = []
change_enemy_y = []
enemy_quantity = 7

for e in range(enemy_quantity):
    image_enemy.append(pygame.image.load('8.1 enemigo.png'))
    position_enemy_x.append(random.randint(0, 736))
    position_enemy_y.append(random.randint(50, 200))
    change_enemy_x.append(0.3)
    change_enemy_y.append(50)

# game bullet
image_bullet = pygame.image.load('11.1 bala.png')
position_bullet_x = 0
position_bullet_y = 500
change_bullet_x = 0
change_bullet_y = 3
bullet_visible = False

# score
score = 0
fon_t = pygame.font.Font('freesansbold.ttf', 32)
text_x = 10
text_y = 10

# font end
font_end = pygame.font.Font('freesansbold.ttf', 40)

# function font
def display_score(x, y):
    text = fon_t.render(f'Score: {score}', True, (255, 255, 255))
    pantalla.blit(text, (x, y))

# function font 2
def text_end():
    text2 = font_end.render('JUEGO TERMINADO', True, (255, 255, 255))
    pantalla.blit(text2, (200, 200))



# function of player
def player(x, y):
    pantalla.blit(image_player, (x, y))

# function of enemy
def enemy(x, y, ene):
    pantalla.blit(image_enemy[ene], (x, y))

# function of enemy
def shoot_bullets(x, y):
    global bullet_visible
    bullet_visible = True
    pantalla.blit(image_bullet, (x + 16, y + 10))

# collision detected function
def collision(x_1, y_1, x_2, y_2):
    distance = math.sqrt(math.pow(x_1 - x_2, 2) + math.pow(y_2 - y_1, 2))
    if distance <= 27:
        return True
    else:
        return False


ejecuta = True
while ejecuta:

    # RGB
    pantalla.blit(fondo, (0,0))

    # event close
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            ejecuta = False

        # Key press event
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                change_player_x = -1
            if evento.key == pygame.K_RIGHT:
                change_player_x = 1
            if evento.key == pygame.K_SPACE:
                sound_bullet = mixer.Sound('16.1 disparo.mp3')
                sound_bullet.play()
                if not bullet_visible:
                    position_bullet_x = position_player_x
                    shoot_bullets(position_player_x, position_bullet_y)

        # Key release event
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_UP or evento.key == pygame.K_DOWN:
                change_player_x = 0
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                change_player_x = 0

    # change position
    position_player_x += change_player_x

    # keep within borders - players
    if position_player_x <= 0:
        position_player_x = 0
    elif position_player_x >= 736:
        position_player_x = 736

    # change position
    for e in range(enemy_quantity):

        # end of game
        if position_enemy_y[e] > 250:
            for k in range(enemy_quantity):
                position_enemy_y[k] = 1000
            text_end()
            break

        position_enemy_x[e] += change_enemy_x[e]


        # keep within borders - enemy
        if position_enemy_x[e] <= 0:
            change_enemy_x[e] = 0.4
            position_enemy_y[e] += change_enemy_y[e]
        elif position_enemy_x[e] >= 736:
            change_enemy_x[e] = -0.4
            position_enemy_y[e] += change_enemy_y[e]

        # collision
        collition = collision(position_enemy_x[e], position_enemy_y[e], position_bullet_x, position_bullet_y)
        if collition:
            sound_collision = mixer.Sound('16.2 Golpe.mp3')
            sound_collision.play()
            position_bullet_y = 500
            bullet_visible = False
            score += 1
            position_enemy_x[e] = random.randint(0, 736)
            position_enemy_y[e] = random.randint(50, 200)
        # calling the enemy function
        enemy(position_enemy_x[e], position_enemy_y[e], e)

    # keep within borders - bullet
    if position_bullet_y <= -64:
        position_bullet_y = 500
        bullet_visible = False
    if bullet_visible:
        shoot_bullets(position_bullet_x, position_bullet_y)
        position_bullet_y -= change_bullet_y



    # calling the player function
    player(position_player_x, position_player_y)

    # calling the display_score function
    display_score(text_x, text_y)

    # update
    pygame.display.update()