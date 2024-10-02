# Usando algoritmos recursivos, escreva funções que:
# a. Defina uma função que recebe como argumento um número natural n e
# devolva a lista dos n primeiros quadrados perfeitos.
# b. Defina uma função que recebe como argumento um número natural n e
# devolva a lista dos quadrados perfeitos até n, por ordem decrescente.

def quadradosPerfeitos(n):
    if n == 0:
        return []
    
    return quadradosPerfeitos(n-1) + [n*n]


def perfeitosDecrescente(n):
    decrescente = quadradosPerfeitos(n)

    return decrescente[::-1]  # Inverte a lista

def main():
    print('O programa fará uma lista dos quadrados perfeitos até o número n.\nEm seguida fará o mesmo procedimento, porém em ordem decrescente.')
    n = int(input('Digite um número natural positivo: '))
    print(quadradosPerfeitos(n))
    print(perfeitosDecrescente(n))  # Saída: [25, 16, 9, 4, 1]

main()
    
