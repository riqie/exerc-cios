# Escreva uma função recursiva que demonstre solução da Torre de Hanoi para n
# discos, indicados pelo usuário.

def torre_hanoi(n, origem, destino, auxiliar):
    '''
    n = número de discos. OBS: o número está em ordem decrescente. Ex: caso entre com 3 discos, o disco menor está em último, o médio em segundo e o maior em primeiro.
    '''

    if n == 1:
        print(f"Mova o disco 1 de {origem} para {destino}")
        return
    
    torre_hanoi(n - 1, origem, auxiliar, destino)
    print(f"Mova o disco {n} de {origem} para {destino}")
    torre_hanoi(n - 1, auxiliar, destino, origem)

def main():
    print('O programa realizará a solução da Torre de Hanoi. ')
    try:
        n = int(input("Digite o número de discos: "))
        if n <= 0:
            raise ValueError("O número de discos deve ser um inteiro positivo.")
        torre_hanoi(n, 'A', 'C', 'B')

    except ValueError:
        print('Entrada inválida. Por favor, entre com um número inteiro positivo.')

main()
