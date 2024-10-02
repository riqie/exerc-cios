
  # Usando algoritmos recursivos, escreva funções que:
# a. Calcule o produtório de um número m, n vezes.
# b. Calcule a potência n de um número k.
# c. Some os dígitos de um número inteiro não negativo.
# d. Calcule a média dos dígitos de um número inteiro não negativo.


# ======== A) e B) ======================================================================

def produtorio(m, n): 
    if n == 0:
        return 1
    return m * produtorio(m, n - 1)

def potencia(k, n):
    if n == 0:
        return 1
    return k * potencia(k, n - 1)

# ======== C) e D) ======================================================================

def somaDigitos(n):
    if n == 0:
        return 0
    return n % 10 + somaDigitos(n // 10) # A divisão por 10 serve para interagir apenas com o último número.

'''
Ex: somaDigitos(123)
    = 123 % 10   + somaDigitos(123 // 10)
    = 3          + somaDigitos(12)
    = 3 + 2      + somaDigitos(12 // 10)
    = 3 + 2      + somaDigitos(1)
    = 3 + 2 + 1  + somaDigitos(0 // 10)
    = 3 + 2 + 1  + somaDigitos(0)
                     return 0
    = 3 + 2 + 1
    = 6
'''
        

def quantidadeDigitos(n):
    if n == 0:
        return 0
    return 1 + quantidadeDigitos(n // 10)

def mediaDigitos(n):
    soma = somaDigitos(n)
    quantidade = quantidadeDigitos(n)
    if quantidade == 0: 
        return 0
    else: 
        return soma / quantidade 

# ========== Main ===============================================================

def main():
    print('\nBem Vindo! \nO programa irá realizar várias operações.')
    print('---')
    print('\nA) Calculo do Produtório \nB) Calculo da Potência \nC) Calculo da Soma dos Dígitos \nD) Calculo da Média dos Dígitos\n')

    print('\n---Calculo do Produtório---')
    try:
        m = int(input('Digite um número para m: '))
        n = int(input('Digite um número para n: '))
        print(f'O produtorio de {m} por {n} é igual a: {produtorio(m, n)}\n')
    except ValueError:
        print('Entrada inválida, use somente números inteiros positivos!')

    print('\n---Calculo da Potência---')
    try:
        k = int(input('Digite um número para k: '))
        n = int(input('Digite um número para n: '))
        print(f'A potência de {k} elevado a {n} é igual a: {potencia(k, n)}\n')
    except ValueError:
        print('Entrada inválida, use somente números inteiros positivos!')

    print('\n---Calculo da Soma dos Dígitos---')
    try:
        n = int(input('Digite um número n: '))
        print(f'A soma dos dígitos do número é: {somaDigitos(n)}\n')
    except ValueError:
        print('Entrada inválida, use somente números inteiros positivos!')

    print('\n---Calculo da Média dos Dígitos---')
    try:
        n = int(input('Digite um número n: '))
        print(f'A média dos dígitos do número é: {mediaDigitos(n)}\n')
    except ValueError:
        print('Entrada inválida, use somente números inteiros positivos!')

    print('Fim do programa!')

main()
