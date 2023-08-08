import pygame

import random

from typing import Literal

# Utils

pygame.init()
#Parte 7 - Fonte
pygame.font.init()

pygame.mixer.init()

# CONSTS

WIN_POINTS = 3

# Funcs

def generate_random_number(min_value, max_value):
    return random.randint(min_value, max_value)


def random_hit_sound():

    PATH = "src/assets/hits/"

    hit_list = {
        1: "tom",
        2: "oof",
        3: "rodrigo_ai",
        4: "cavalo",
        5: "villager",
        6: "bamboo",
        7: "cartoon"
    }

    music_idx = generate_random_number(1, len(hit_list))

    final_path = PATH + hit_list[music_idx] + ".wav"

    return final_path


def play_sound(sound_path:str, overlay:bool):

    sound = pygame.mixer.Sound(sound_path)

    if overlay == True:

        if not pygame.mixer.get_busy():

            sound.play()


    else:

        sound.play()

#janela
display = pygame.display.set_mode((1280, 720))

#3 Parte - formas - player
#pos e forma em retangulo
# 0,0 pos esquerda superior
player1 = pygame.Rect(0, 0, 30, 150)
player1_velocidade = 1
player1_score =0

player2 = pygame.Rect(1250, 0, 30, 150)
player2_score =0

ball = pygame.Rect(600, 350, 15, 15)
ball_dir_x=1
ball_dir_y=1

#parte 7 - escrever texto na tela
font = pygame.font.Font(None, 50)
placar_player1 = font.render(str(player1_score), True, "white")
placar_player2 = font.render(str(player2_score), True, "white")

#loop do game
cena: Literal["menu", "jogo", "gameover", "win"] = "menu"

loop = True
while loop:

    if cena == "jogo":
        #Parte 2 - eventos
        for event in pygame.event.get():
            #evento do X de fechar
            if event.type == pygame.QUIT:
                loop = False

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_s:

                    player1_velocidade=1

                if event.key == pygame.K_w:

                    player1_velocidade=-1

        if player2_score >= WIN_POINTS:
            cena="gameover"

        if player1_score >= WIN_POINTS:

            cena="win"

        #parte 6 - colisão e mov bola
        if ball.colliderect(player1) or ball.colliderect(player2):
            ball_dir_x *= -1

            hit_sound = random_hit_sound()

            play_sound(hit_sound, False)

        if player1.y<=0:

            player1.y=0

        elif player1.y>=720-150:

            player1.y=720-150

        player1.y+=player1_velocidade

        if ball.x <=0:

            player2_score+=1
            placar_player2 = font.render(str(player2_score), True, "white")
            ball.x=600
            ball_dir_x*=-1

        elif ball.x >= 1280:
            player1_score += 1
            placar_player1 = font.render(str(player1_score), True, "white")
            ball.x = 600
            ball_dir_x *= -1

        if ball.y <=0:
            ball_dir_y *=-1
        elif ball.y >= 720-15:
            ball_dir_y*=-1

        ball.x+=ball_dir_x
        ball.y+=ball_dir_y

        player2.y=ball.y-75

        #fica preenchendo a tela
        display.fill((0,0,0))

        #3 - parte - formas
        pygame.draw.rect(display, "white", player1)
        pygame.draw.rect(display, "white", player2)
        pygame.draw.circle(display, "white", ball.center, 8)

        display.blit(placar_player1, (500, 50))
        display.blit(placar_player2, (780, 50))

    elif cena == "gameover":

        play_sound("src/assets/death.wav", True)

        for event in pygame.event.get():

            if event.type==pygame.QUIT:
                loop = False

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_RETURN:

                    player1_score=0
                    player2_score=0
                    placar_player1 = font.render(str(player1_score), True, "white")
                    placar_player2 = font.render(str(player2_score), True, "white")
                    ball.x = 640
                    ball.y = 320
                    player1.y=0
                    player2.y =0

                    cena="menu"

        display.fill((0,0,0))

        text_win = font.render("Game Over", True, "white")
        display.blit(text_win, [(520),260])

    elif cena == "menu":

        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                loop = False

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_RETURN:

                    cena="jogo"
                    start = pygame.mixer.Sound("src/assets/start.wav")
                    start.play()

                if event.key == pygame.K_q:

                    loop = False

        display.fill((0,0,0))
        text_win=font.render("Aperte Enter", True, "white")
        display.blit(text_win, [(520),260])
    
    elif cena == "win":

        if not pygame.mixer.get_busy():  # Check if no sound is currently playing
            victory_sound = pygame.mixer.Sound("src/assets/win.wav")
            victory_sound.play()

        for event in pygame.event.get():

            if event.type == pygame.QUIT:

                loop = False

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_RETURN:

                    cena = "jogo"
                    start = pygame.mixer.Sound("src/assets/start.wav")
                    start.play()

                if event.key == pygame.K_q:

                    loop = False

        display.fill((0,0,0))

        text_win = font.render("You Won. ENTER to play again", True, "white")
        display.blit(text_win, [(520),260])


    #atualizando a tela
    pygame.display.flip()
