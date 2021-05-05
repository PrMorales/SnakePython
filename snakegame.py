import pygame
import random

pygame.init()


azul = (56, 61, 96)

laranja = (205, 102, 0)

verde = (0, 255, 0)

amarelo = (241, 221, 136)


dimensoes = (600, 600)

# VALORES INICIAIS #

x = 300
y = 300

d = 20

lista_cobra = [[x, y]]

dx = 0
dy = 0

x_comida = round(random.randrange(0, 600 - d) / 20) * 20
y_comida = round(random.randrange(0, 600 - d) / 20) * 20

fonte = pygame.font.SysFont('hack', 35)


tela = pygame.display.set_mode((dimensoes))
pygame.display.set_caption('snake')

tela.fill(azul)

clock = pygame.time.Clock()


def desenha_cobra(lista_cobra):
    tela.fill(azul)
    for unidade in lista_cobra:
        pygame.draw.rect(tela, laranja, [unidade[0], unidade[1], d, d])


# movimentação no eixo x e y - delta
def mover_cobra(dx, dy, lista_cobra):

    # comando para teclas da seta #
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                dx = -d
                dy = 0
            elif event.key == pygame.K_RIGHT:
                dx = d
                dy = 0
            elif event.key == pygame.K_UP:
                dx = 0
                dy = -d
            elif event.key == pygame.K_DOWN:
                dx = 0
                dy = d

    x_novo = lista_cobra[-1][0] + dx
    y_novo = lista_cobra[-1][1] + dy

    lista_cobra.append([x_novo, y_novo])

    del lista_cobra[0]

    return dx, dy, lista_cobra


def verifica_comida(dx, dy, x_comida, y_comida, lista_cobra):

    head = lista_cobra[-1]

    x_novo = head[0] + dx
    y_novo = head[1] + dy

    if head[0] == x_comida and head[1] == y_comida:
        lista_cobra.append([x_novo, y_novo])
        x_comida = round(random.randrange(0, 600 - d) / 20) * 20
        y_comida = round(random.randrange(0, 600 - d) / 20) * 20
        pygame.mixer.init()
        pygame.mixer.music.load('bite_potato_chip.mp3')
        pygame.mixer.music.play()

    pygame.draw.rect(tela, verde, [x_comida, y_comida, d, d])

    return x_comida, y_comida, lista_cobra


def verifica_parede(lista_cobra):
    head = lista_cobra[-1]
    x = head[0]
    y = head[1]

    if x not in range(600) or y not in range(600):
        mensagem = fonte.render('GAME OVER!!', True, amarelo)
        tela.blit(mensagem, [200, 300])
       # raise Exception

    #def atravessar_paredes(lista_cobra):
        #head = lista_cobra[-1]
        #if head[0] == dimensoes[0]:
            #lista_cobra[-1] = [0, head[1]]
        #elif head[0] < 0:
            #lista_cobra[-1] = [dimensoes[0], head[1]]
        #elif head[1] == dimensoes[1]:
            #lista_cobra[-1] = [head[0], 0]
        #elif head[1] < 0:
            #lista_cobra[-1] = [head[0], dimensoes[1]]
        #return lista_cobra#


def verifica_mordeu_cobra(lista_cobra):
    head = lista_cobra[-1]
    corpo = lista_cobra.copy()
    del corpo[-1]
    for x, y in corpo:
        if x == head[0] and y == head[1]:
            raise Exception


def atualizar_pontos(lista_cobra):
    pts = str(len(lista_cobra))
    escore = fonte.render('Pontuação: ' + pts, True, amarelo)
    tela.blit(escore, [0, 0])


while True:
    pygame.display.update()
    desenha_cobra(lista_cobra)
    dx, dy, lista_cobra = mover_cobra(dx, dy, lista_cobra)
    x_comida, y_comida, lista_cobra = verifica_comida(dx, dy, x_comida, y_comida, lista_cobra)
    print(lista_cobra)
    verifica_parede(lista_cobra)
    verifica_mordeu_cobra(lista_cobra)
    atualizar_pontos(lista_cobra)


    clock.tick(5)