import tkinter as tk
from tkinter import messagebox

class Peca:
    def __init__(self, cor):
        self.cor = cor

    def movimento_valido(self, pos_inicio, pos_fim, tabuleiro):
        raise NotImplementedError("Este método deve ser sobrescrito nas subclasses")

class Rei(Peca):
    def movimento_valido(self, pos_inicio, pos_fim, tabuleiro):
        dx = abs(pos_inicio[0] - pos_fim[0])
        dy = abs(pos_inicio[1] - pos_fim[1])
        return dx <= 1 and dy <= 1

    def __str__(self):
        return "Kb" if self.cor == 'branca' else "Kp"

class Rainha(Peca):
    def movimento_valido(self, pos_inicio, pos_fim, tabuleiro):
        dx = abs(pos_inicio[0] - pos_fim[0])
        dy = abs(pos_inicio[1] - pos_fim[1])
        return dx == dy or dx == 0 or dy == 0

    def __str__(self):
        return "Qb" if self.cor == 'branca' else "Qp"

class Torre(Peca):
    def movimento_valido(self, pos_inicio, pos_fim, tabuleiro):
        dx = abs(pos_inicio[0] - pos_fim[0])
        dy = abs(pos_inicio[1] - pos_fim[1])
        return dx == 0 or dy == 0

    def __str__(self):
        return "Rb" if self.cor == 'branca' else "Rp"

class Bispo(Peca):
    def movimento_valido(self, pos_inicio, pos_fim, tabuleiro):
        dx = abs(pos_inicio[0] - pos_fim[0])
        dy = abs(pos_inicio[1] - pos_fim[1])
        return dx == dy

    def __str__(self):
        return "Bb" if self.cor == 'branca' else "Bp"

class Cavalo(Peca):
    def movimento_valido(self, pos_inicio, pos_fim, tabuleiro):
        dx = abs(pos_inicio[0] - pos_fim[0])
        dy = abs(pos_inicio[1] - pos_fim[1])
        return (dx == 2 and dy == 1) or (dx == 1 and dy == 2)

    def __str__(self):
        return "Nb" if self.cor == 'branca' else "Np"

class Peao(Peca):
    def movimento_valido(self, pos_inicio, pos_fim, tabuleiro):
        direcao = 1 if self.cor == 'branca' else -1
        linha_inicial = 1 if self.cor == 'branca' else 6
        if pos_inicio[1] == pos_fim[1]:  # Movimento vertical
            if pos_inicio[0] == linha_inicial:  # Posição inicial
                return (pos_fim[0] - pos_inicio[0] == direcao) or (pos_fim[0] - pos_inicio[0] == 2 * direcao)
            else:
                return pos_fim[0] - pos_inicio[0] == direcao
        elif abs(pos_inicio[1] - pos_fim[1]) == 1 and pos_fim[0] - pos_inicio[0] == direcao:  # Captura diagonal
            return isinstance(tabuleiro[pos_fim[0]][pos_fim[1]], Peca) and tabuleiro[pos_fim[0]][pos_fim[1]].cor != self.cor
        return False

    def __str__(self):
        return "Pb" if self.cor == 'branca' else "Pp"

class Tabuleiro:
    def __init__(self):
        self.tabuleiro = [[None for _ in range(8)] for _ in range(8)]
        self.configurar_posicoes_iniciais()

    def configurar_posicoes_iniciais(self):
        # Configurar peças brancas
        self.tabuleiro[0][0] = Torre('branca')
        self.tabuleiro[0][1] = Cavalo('branca')
        self.tabuleiro[0][2] = Bispo('branca')
        self.tabuleiro[0][3] = Rainha('branca')
        self.tabuleiro[0][4] = Rei('branca')
        self.tabuleiro[0][5] = Bispo('branca')
        self.tabuleiro[0][6] = Cavalo('branca')
        self.tabuleiro[0][7] = Torre('branca')
        for i in range(8):
            self.tabuleiro[1][i] = Peao('branca')
        
        # Configurar peças pretas
        self.tabuleiro[7][0] = Torre('preta')
        self.tabuleiro[7][1] = Cavalo('preta')
        self.tabuleiro[7][2] = Bispo('preto')
        self.tabuleiro[7][3] = Rainha('preta')
        self.tabuleiro[7][4] = Rei('preta')
        self.tabuleiro[7][5] = Bispo('preto')
        self.tabuleiro[7][6] = Cavalo('preto')
        self.tabuleiro[7][7] = Torre('preta')
        for i in range(8):
            self.tabuleiro[6][i] = Peao('preta')

    def imprimir_tabuleiro(self):
        letras_colunas = 'A B C D E F G H'.split()
        print('  ' + ' '.join(letras_colunas))
        for i, linha in enumerate(self.tabuleiro):
            print(8 - i, ' '.join([str(peca) if peca else '.' for peca in linha]), 8 - i)
        print('  ' + ' '.join(letras_colunas))

def alternar_turno(turno):
    return 'branca' if turno == 'preta' else 'preta'

def iniciar_jogo():
    tabuleiro = Tabuleiro()
    turno = 'branca'
    jogo_terminado = False

    def atualizar_tabuleiro():
        for i in range(8):
            for j in range(8):
                peca = tabuleiro.tabuleiro[i][j]
                texto = str(peca) if peca else ''
                botoes[i][j].config(text=texto)

    def ao_clicar(linha, coluna):
        nonlocal posicao_selecionada, turno
        if posicao_selecionada is None:
            posicao_selecionada = (linha, coluna)
        else:
            pos_fim = (linha, coluna)
            pos_inicio = posicao_selecionada
            posicao_selecionada = None
            peca = tabuleiro.tabuleiro[pos_inicio[0]][pos_inicio[1]]
            if peca and peca.cor == turno:
                if peca.movimento_valido(pos_inicio, pos_fim, tabuleiro.tabuleiro):
                    tabuleiro.tabuleiro[pos_fim[0]][pos_fim[1]] = peca
                    tabuleiro.tabuleiro[pos_inicio[0]][pos_inicio[1]] = None
                    turno = alternar_turno(turno)
                    atualizar_tabuleiro()
                else:
                    messagebox.showerror("Erro", "Movimento inválido")
            else:
                messagebox.showerror("Erro", "Selecione uma peça válida")

    janela = tk.Tk()
    janela.title("Jogo de Xadrez")
    botoes = [[None for _ in range(8)] for _ in range(8)]
    posicao_selecionada = None

    for i in range(8):
        for j in range(8):
            botao = tk.Button(janela, width=4, height=2, font=('Arial', 24),
                              command=lambda i=i, j=j: ao_clicar(i, j))
            botao.grid(row=i+1, column=j+1)
            botoes[i][j] = botao

    for i in range(8):
        tk.Label(janela, text=chr(65 + i), font=('Arial', 18)).grid(row=0, column=i+1)
        tk.Label(janela, text=str(8 - i), font=('Arial', 18)).grid(row=i+1, column=0)
        tk.Label(janela, text=str(8 - i), font=('Arial', 18)).grid(row=i+1, column=9)
        tk.Label(janela, text=chr(65 + i), font=('Arial', 18)).grid(row=9, column=i+1)

    atualizar_tabuleiro()
    janela.mainloop()

def main():
    while True:
        print("1. Iniciar Jogo")
        print("2. Sair")
        escolha = input("Digite sua escolha: ")

        if escolha == '1':
            iniciar_jogo()
        elif escolha == '2':
            break
        else:
            print("Escolha inválida")

if __name__ == "__main__":
    main()
