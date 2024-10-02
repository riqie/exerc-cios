import pygame
import random

# Inicialização do Pygame
pygame.init()

# Configurações da janela
largura = 600  # largura da janela
altura = 600   # altura da janela
tamanho_celula = 30  # tamanho da célula em pixels
cor_fundo = (200, 200, 200)
cor_celula = (220, 220, 220)
cor_borda = (100, 100, 100)

# Definição das constantes para representar o estado de cada célula
CELULA_OCULTA = 0
CELULA_REVELADA = 1
CELULA_MINA = 2

# Classe para representar cada célula do campo
class Tile:
    def __init__(self):
        self.value = CELULA_OCULTA  # Estado inicial
        self.revealed = False       # Se a célula foi revelada
        self.flagged = False        # Se a célula está marcada com uma bandeira
        self.num_adjacent_mines = 0 # Número de minas adjacentes

# Função para criar um campo minado aleatório
def criar_campo(linhas, colunas, num_minas):
    campo = [[Tile() for _ in range(colunas)] for _ in range(linhas)]

    # Distribuir minas aleatoriamente
    for _ in range(num_minas):
        while True:
            x = random.randint(0, linhas - 1)
            y = random.randint(0, colunas - 1)
            if campo[x][y].value != CELULA_MINA:
                campo[x][y].value = CELULA_MINA
                break

    # Calcular número de minas adjacentes para cada célula
    for i in range(linhas):
        for j in range(colunas):
            if campo[i][j].value != CELULA_MINA:
                num_adjacentes = 0
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        if 0 <= i + dx < linhas and 0 <= j + dy < colunas:
                            if campo[i + dx][j + dy].value == CELULA_MINA:
                                num_adjacentes += 1
                campo[i][j].num_adjacent_mines = num_adjacentes

    return campo

# Função para desenhar o campo na tela
def desenhar_campo(screen, campo):
    for i in range(len(campo)):
        for j in range(len(campo[0])):
            cor = cor_celula
            if campo[i][j].revealed:
                cor = cor_fundo
                if campo[i][j].value == CELULA_MINA:
                    pygame.draw.circle(screen, (0, 0, 0), (j * tamanho_celula + tamanho_celula // 2, i * tamanho_celula + tamanho_celula // 2), tamanho_celula // 3)
                elif campo[i][j].num_adjacent_mines > 0:
                    fonte = pygame.font.Font(None, tamanho_celula // 2)
                    texto = fonte.render(str(campo[i][j].num_adjacent_mines), True, (0, 0, 0))
                    screen.blit(texto, (j * tamanho_celula + tamanho_celula // 3, i * tamanho_celula + tamanho_celula // 3))
            pygame.draw.rect(screen, cor, (j * tamanho_celula, i * tamanho_celula, tamanho_celula, tamanho_celula))
            pygame.draw.rect(screen, cor_borda, (j * tamanho_celula, i * tamanho_celula, tamanho_celula, tamanho_celula), 1)
            if campo[i][j].flagged:
                pygame.draw.line(screen, (255, 0, 0), (j * tamanho_celula + tamanho_celula // 4, i * tamanho_celula + tamanho_celula // 4), 
                                                (j * tamanho_celula + tamanho_celula * 3 // 4, i * tamanho_celula + tamanho_celula * 3 // 4), 2)
                pygame.draw.line(screen, (255, 0, 0), (j * tamanho_celula + tamanho_celula // 4, i * tamanho_celula + tamanho_celula * 3 // 4), 
                                                (j * tamanho_celula + tamanho_celula * 3 // 4, i * tamanho_celula + tamanho_celula // 4), 2)

# Função para clicar numa célula
def clicar_celula(campo, linhas, colunas, x, y):
    # Se a célula já foi revelada ou marcada com bandeira, não faz nada
    if campo[x][y].revealed or campo[x][y].flagged:
        return

    campo[x][y].revealed = True

    # Se clicar numa célula vazia, revela recursivamente as células adjacentes
    if campo[x][y].value == CELULA_OCULTA and campo[x][y].num_adjacent_mines == 0:
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if 0 <= x + dx < linhas and 0 <= y + dy < colunas:
                    clicar_celula(campo, linhas, colunas, x + dx, y + dy)

# Função para clicar com bandeira numa célula
def clicar_bandeira(campo, x, y):
    campo[x][y].flagged = not campo[x][y].flagged

# Função para verificar vitória
def verificar_vitoria(campo):
    for linha in campo:
        for tile in linha:
            if not tile.revealed and not tile.flagged:
                return False
            if tile.flagged and tile.value != CELULA_MINA:
                return False
    return True

# Função para verificar derrota
def verificar_derrota(campo):
    for linha in campo:
        for tile in linha:
            if tile.revealed and tile.value == CELULA_MINA:
                return True
    return False

# Função principal do jogo
def main():
    screen = pygame.display.set_mode((largura, altura))
    pygame.display.set_caption('Campo Minado')

    linhas = altura // tamanho_celula
    colunas = largura // tamanho_celula
    campo = criar_campo(linhas, colunas, 20)  # Campo 20x20 com 20 minas

    rodando = True
    while rodando:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                rodando = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Clique esquerdo
                    x = event.pos[1] // tamanho_celula
                    y = event.pos[0] // tamanho_celula
                    clicar_celula(campo, linhas, colunas, x, y)
                elif event.button == 3:  # Clique direito
                    x = event.pos[1] // tamanho_celula
                    y = event.pos[0] // tamanho_celula
                    clicar_bandeira(campo, x, y)

        # Verificar vitória e derrota
        if verificar_vitoria(campo):
            print("Você ganhou!")
            rodando = False
        elif verificar_derrota(campo):
            print("Você perdeu!")
            rodando = False

        # Desenhar o campo na tela
        screen.fill(cor_fundo)
        desenhar_campo(screen, campo)

        pygame.display.flip()

    pygame.quit()

if __name__ == '__main__':
    main()
