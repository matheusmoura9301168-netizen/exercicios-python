# Jogo da cobra feito com Pygame.

import pygame
import random

def jogo():
    pygame.init()

    largura, altura = 800, 600
    tamanho_bloco = 10
    velocidade = 10

    branco = (255, 255, 255)
    preto = (0, 0, 0)
    vermelho = (213, 50, 80)
    verde = (0, 255, 0)
    azul = (54, 100, 230)
    amarelo = (255, 255, 0)

    tela = pygame.display.set_mode((largura, altura))
    pygame.display.set_caption("Jogo da Cobra")

    font = pygame.font.SysFont("bahnschrift", 25)
    Tempo = pygame.time.Clock()

    def M_p(pontos):
        valor = font.render("Pontuação: " + str(pontos), True, preto)
        tela.blit(valor, [10, 10])

    game_over = False
    game_close = False

    x = largura / 2
    y = altura / 2
    dx = 0
    dy = 0

    # DIREÇÃO INICIAL
    direcao = "parado"   # pode ser: esquerda, direita, cima, baixo

    lista_cobra = []
    comprimento_cobra = 1

    maca_x = round(random.randrange(0, largura - tamanho_bloco) / 20.0) * 20.0
    maca_y = round(random.randrange(0, altura - tamanho_bloco) / 20.0) * 20.0
    maca_x1 = round(random.randrange(0, largura - tamanho_bloco) / 20.0) * 20.0
    maca_y1 = round(random.randrange(0, altura - tamanho_bloco) / 20.0) * 20.0
    maca_x2 = round(random.randrange(0, largura - tamanho_bloco) / 20.0) * 20.0
    maca_y2 = round(random.randrange(0, altura - tamanho_bloco) / 20.0) * 20.0

    while not game_over:
        while game_close:
            tela.fill(azul)
            mensagem = font.render("Fim de jogo! C = continuar | Q = sair", True, vermelho)
            tela.blit(mensagem, [largura / 10, altura / 3])
            M_p(comprimento_cobra - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        jogo()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

            if event.type == pygame.KEYDOWN:

                # BLOQUEAR DIREÇÃO OPOSTA
                if event.key == pygame.K_a:   # esquerda
                    if direcao != "direita":
                        dx = -tamanho_bloco
                        dy = 0
                        direcao = "esquerda"

                elif event.key == pygame.K_d: # direita
                    if direcao != "esquerda":
                        dx = tamanho_bloco
                        dy = 0
                        direcao = "direita"

                elif event.key == pygame.K_w: # cima
                    if direcao != "baixo":
                        dy = -tamanho_bloco
                        dx = 0
                        direcao = "cima"

                elif event.key == pygame.K_s: # baixo
                    if direcao != "cima":
                        dy = tamanho_bloco
                        dx = 0
                        direcao = "baixo"

        x += dx
        y += dy
        tela.fill(azul)

        pygame.draw.rect(tela, vermelho, [maca_x, maca_y, tamanho_bloco, tamanho_bloco])
        pygame.draw.rect(tela, vermelho, [maca_x1, maca_y1, tamanho_bloco, tamanho_bloco])
        pygame.draw.rect(tela, vermelho, [maca_x2, maca_y2, tamanho_bloco, tamanho_bloco])

        cabeca = [x, y]
        lista_cobra.append(cabeca)
        if len(lista_cobra) > comprimento_cobra:
            del lista_cobra[0]

        for parte in lista_cobra[:-1]:
            if parte == cabeca:
                game_close = True

        for bloco in lista_cobra:
            pygame.draw.rect(tela, verde, [ bloco[0], bloco[1], tamanho_bloco, tamanho_bloco])


        M_p(comprimento_cobra - 1)
        pygame.display.update()


        if x == maca_x and y == maca_y:
            maca_x = round(random.randrange(0, largura - tamanho_bloco) / 20.0) * 20.0
            maca_y = round(random.randrange(0, altura - tamanho_bloco) / 20.0) * 20.0
            comprimento_cobra += 100


        if x == maca_x1 and y == maca_y1:
            maca_x1 = round(random.randrange(0, largura - tamanho_bloco) / 20.0) * 20.0
            maca_y1 = round(random.randrange(0, altura - tamanho_bloco) / 20.0) * 20.0
            comprimento_cobra += 200

        if x == maca_x2 and y == maca_y2:
            maca_x2 = round(random.randrange(0, largura - tamanho_bloco) / 20.0) * 20.0
            maca_y2 = round(random.randrange(0, altura - tamanho_bloco) / 20.0) * 20.0
            comprimento_cobra += 300


        if x >= largura or x < 0 or y >= altura or y < 0:
            game_close = True

        Tempo.tick(velocidade)

    pygame.quit()
    quit()


jogo()
