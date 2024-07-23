import tkinter as tk
from tkinter import messagebox
import random

# Configurações do jogo
LARGURA = 600  # largura da janela
ALTURA = 600   # altura da janela
TAMANHO_CELULA = 30  # tamanho da célula em pixels
COR_FUNDO = "#cccccc"
COR_CELULA = "#dddddd"
COR_BORDA = "#666666"
COR_BANDEIRA = "red"

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

# Função para revelar uma célula
def revelar_celula(campo, linhas, colunas, x, y):
    # Se a célula já foi revelada ou marcada com bandeira, não faz nada
    if campo[x][y].revealed or campo[x][y].flagged:
        return

    campo[x][y].revealed = True

    # Se clicar numa célula vazia, revela recursivamente as células adjacentes
    if campo[x][y].value == CELULA_OCULTA and campo[x][y].num_adjacent_mines == 0:
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if 0 <= x + dx < linhas and 0 <= y + dy < colunas:
                    revelar_celula(campo, linhas, colunas, x + dx, y + dy)

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

# Função para desenhar o campo na tela
def desenhar_campo():
    canvas.delete("all")  # Limpar o canvas antes de desenhar

    for i in range(len(campo)):
        for j in range(len(campo[0])):
            cor = COR_CELULA
            texto_cor = "black"

            if campo[i][j].revealed:
                cor = COR_FUNDO
                if campo[i][j].value == CELULA_MINA:
                    canvas.create_oval(j * TAMANHO_CELULA + TAMANHO_CELULA // 2 - 10, i * TAMANHO_CELULA + TAMANHO_CELULA // 2 - 10,
                                       j * TAMANHO_CELULA + TAMANHO_CELULA // 2 + 10, i * TAMANHO_CELULA + TAMANHO_CELULA // 2 + 10, fill="black")
                elif campo[i][j].num_adjacent_mines > 0:
                    texto = str(campo[i][j].num_adjacent_mines)
                    if campo[i][j].num_adjacent_mines == 1:
                        texto_cor = "#1976D2"  # Azul
                    elif campo[i][j].num_adjacent_mines == 2:
                        texto_cor = "#388E3C"  # Verde
                    elif campo[i][j].num_adjacent_mines == 3:
                        texto_cor = "#D32F2F"  # Vermelho
                    elif campo[i][j].num_adjacent_mines == 4:
                        texto_cor = "#7B1FA2"  # Roxo
                    elif campo[i][j].num_adjacent_mines == 5:
                        texto_cor = "#FF8C00"  # Laranja
                    elif campo[i][j].num_adjacent_mines == 6:
                        texto_cor = "#8B4513"  # Marrom
                    elif campo[i][j].num_adjacent_mines == 7:
                        texto_cor = "#FF00FF"  # Magenta
                    elif campo[i][j].num_adjacent_mines == 8:
                        texto_cor = "#00FFFF"  # Ciano
                    canvas.create_text(j * TAMANHO_CELULA + TAMANHO_CELULA // 2, i * TAMANHO_CELULA + TAMANHO_CELULA // 2,
                                       text=texto, font=("Helvetica", 12, "bold"), fill=texto_cor)
            canvas.create_rectangle(j * TAMANHO_CELULA, i * TAMANHO_CELULA,
                                    j * TAMANHO_CELULA + TAMANHO_CELULA, i * TAMANHO_CELULA + TAMANHO_CELULA,
                                    fill=cor, outline=COR_BORDA, width=1)
            if campo[i][j].flagged:
                canvas.create_line(j * TAMANHO_CELULA + TAMANHO_CELULA // 4, i * TAMANHO_CELULA + TAMANHO_CELULA // 4,
                                   j * TAMANHO_CELULA + 3 * TAMANHO_CELULA // 4, i * TAMANHO_CELULA + 3 * TAMANHO_CELULA // 4,
                                   fill=COR_BANDEIRA, width=2)
                canvas.create_line(j * TAMANHO_CELULA + TAMANHO_CELULA // 4, i * TAMANHO_CELULA + 3 * TAMANHO_CELULA // 4,
                                   j * TAMANHO_CELULA + 3 * TAMANHO_CELULA // 4, i * TAMANHO_CELULA + TAMANHO_CELULA // 4,
                                   fill=COR_BANDEIRA, width=2)

# Função para lidar com clique do mouse
def on_click(event):
    x = event.y // TAMANHO_CELULA
    y = event.x // TAMANHO_CELULA
    if event.num == 1:  # Clique esquerdo
        revelar_celula(campo, linhas, colunas, x, y)
    elif event.num == 3:  # Clique direito
        clicar_bandeira(campo, x, y)
    desenhar_campo()
    if verificar_vitoria(campo):
        messagebox.showinfo("Campo Minado", "Você ganhou!")
        root.destroy()
    elif verificar_derrota(campo):
        messagebox.showinfo("Campo Minado", "Você perdeu!")
        root.destroy()

# Inicialização do jogo
root = tk.Tk()
root.title("Campo Minado")

# Criação do canvas
canvas = tk.Canvas(root, width=LARGURA, height=ALTURA, bg=COR_FUNDO)
canvas.pack()

# Configuração do campo minado
linhas = ALTURA // TAMANHO_CELULA
colunas = LARGURA // TAMANHO_CELULA
campo = criar_campo(linhas, colunas, 40)  # Campo 20x20 com 40 minas

# Bind do clique do mouse
canvas.bind("<Button-1>", on_click)  # Clique esquerdo
canvas.bind("<Button-3>", on_click)  # Clique direito

# Desenhar o campo inicial
desenhar_campo()

# Executar o loop principal
root.mainloop()
