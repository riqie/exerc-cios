import random

# Função para criar um tabuleiro vazio
def criar_tabuleiro():
    return [[' ' for _ in range(10)] for _ in range(10)]

# Função para imprimir o tabuleiro com coordenadas
def imprimir_tabuleiro(tabuleiro):
    letras = 'ABCDEFGHIJ'
    print('  | 0 1 2 3 4 5 6 7 8 9')
    print('--+-------------------')
    for i in range(10):
        linha = f'{letras[i]} | {" ".join(tabuleiro[i])}'
        print(linha)

# Função para validar a posição do navio no tabuleiro
def validar_posicao(tabuleiro, linha, coluna, tamanho, direcao):
    if direcao == 'h':
        if coluna + tamanho > 10:
            return False
        for c in range(coluna, coluna + tamanho):
            if tabuleiro[linha][c] != ' ':
                return False
    elif direcao == 'v':
        if linha + tamanho > 10:
            return False
        for l in range(linha, linha + tamanho):
            if tabuleiro[l][coluna] != ' ':
                return False
    return True

# Função para posicionar os navios no tabuleiro
def posicionar_navios(tabuleiro):
    navios = {'Porta-aviões': 5, 'Encouraçado': 4, 'Contratorpedeiro': 3, 'Submarino': 3, 'Navio-patrulha': 2}
    letras = 'ABCDEFGHIJ'
    for navio, tamanho in navios.items():
        print(f'Posicione o {navio} ({tamanho} células)')
        for tentativa in range(5):  # permitir até 5 tentativas para posicionar cada navio
            try:
                imprimir_tabuleiro(tabuleiro)
                print(f'Informe a posição inicial (linha e coluna) e direção (h para horizontal, v para vertical) para o {navio}:')
                entrada = input().strip().upper()
                if len(entrada) < 3:
                    raise ValueError('Entrada inválida. Tente novamente.')
                coluna = int(entrada[1])
                linha = letras.index(entrada[0])
                direcao = entrada[2]
                
                if validar_posicao(tabuleiro, linha, coluna, tamanho, direcao):
                    if direcao == 'h':
                        for c in range(coluna, coluna + tamanho):
                            tabuleiro[linha][c] = 'O'
                    elif direcao == 'v':
                        for l in range(linha, linha + tamanho):
                            tabuleiro[l][coluna] = 'O'
                    break
                else:
                    raise ValueError('Posição inválida. Tente novamente.')
            except (ValueError, IndexError):
                print('Erro ao posicionar o navio. Tente novamente.')

# Função para gerar o tabuleiro aleatório do computador
def gerar_tabuleiro_computador():
    tabuleiro = criar_tabuleiro()
    navios = {'Porta-aviões': 5, 'Encouraçado': 4, 'Contratorpedeiro': 3, 'Submarino': 3, 'Navio-patrulha': 2}
    letras = 'ABCDEFGHIJ'
    for navio, tamanho in navios.items():
        while True:
            linha = random.randint(0, 9)
            coluna = random.randint(0, 9)
            direcao = random.choice(['h', 'v'])
            if validar_posicao(tabuleiro, linha, coluna, tamanho, direcao):
                if direcao == 'h':
                    for c in range(coluna, coluna + tamanho):
                        tabuleiro[linha][c] = 'O'
                elif direcao == 'v':
                    for l in range(linha, linha + tamanho):
                        tabuleiro[l][coluna] = 'O'
                break
    return tabuleiro

# Função para verificar se todos os navios foram destruídos
def todos_navios_destruidos(tabuleiro):
    for linha in tabuleiro:
        if 'O' in linha:
            return False
    return True

# Função para o turno do jogador
def turno_jogador(tabuleiro_computador):
    letras = 'ABCDEFGHIJ'
    while True:
        try:
            imprimir_tabuleiro(tabuleiro_computador)
            print('Informe a coordenada para atacar (ex: A0):')
            entrada = input().strip().upper()
            if len(entrada) < 2:
                raise ValueError('Entrada inválida. Tente novamente.')
            coluna = int(entrada[1])
            linha = letras.index(entrada[0])
            if tabuleiro_computador[linha][coluna] == 'O':
                print('Você acertou um navio!')
                tabuleiro_computador[linha][coluna] = 'X'
                if todos_navios_destruidos(tabuleiro_computador):
                    return True
            else:
                print('Você errou o ataque.')
                if todos_navios_destruidos(tabuleiro_computador):
                    return True
            return False
        except (ValueError, IndexError):
            print('Coordenada inválida. Tente novamente.')

# Função para o turno do computador
def turno_computador(tabuleiro_jogador):
    letras = 'ABCDEFGHIJ'
    while True:
        linha = random.randint(0, 9)
        coluna = random.randint(0, 9)
        if tabuleiro_jogador[linha][coluna] == 'O':
            print(f'O computador acertou um navio na coordenada {letras[linha]}{coluna}!')
            tabuleiro_jogador[linha][coluna] = 'X'
            if todos_navios_destruidos(tabuleiro_jogador):
                return True
        else:
            print(f'O computador errou o ataque na coordenada {letras[linha]}{coluna}.')
            if todos_navios_destruidos(tabuleiro_jogador):
                return True
        return False

# Função principal que controla o jogo
def jogar_batalha_naval():
    print('Bem-vindo ao Jogo de Batalha Naval!')
    
    # Tabuleiro do jogador
    tabuleiro_jogador = criar_tabuleiro()
    posicionar_navios(tabuleiro_jogador)
    
    # Tabuleiro do computador
    tabuleiro_computador = gerar_tabuleiro_computador()
    
    # Início do jogo
    print('Pressione Enter para começar a batalha contra o computador...')
    input()
    
    while True:
        # Turno do jogador
        jogador_venceu = turno_jogador(tabuleiro_computador)
        if jogador_venceu:
            imprimir_tabuleiro(tabuleiro_computador)
            print('Parabéns! Você venceu!')
            break
        
        # Turno do computador
        computador_venceu = turno_computador(tabuleiro_jogador)
        if computador_venceu:
            imprimir_tabuleiro(tabuleiro_jogador)
            print('O computador venceu. Tente novamente!')
            break

# Iniciar o jogo
jogar_batalha_naval()
