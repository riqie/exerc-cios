def verifica_positivos_negativos(lista):
    positivos = 0
    negativos = 0
    
    for x in lista:
        if x > 0:
            positivos += 1
        elif x < 0:
            negativos += 1
    
    return positivos == negativos

def verifica_todas_listas(w):
    if not w:
        return True
    
    primeira_lista = w[0]
    resto_listas = w[1:]
    
    if not verifica_positivos_negativos(primeira_lista):
        return False
    
    return verifica_todas_listas(resto_listas)

def main():
    print('\nO programa vai ler uma lista de listas, então ele dirá "True" caso o número de elementos positivos e de negativos forem iguais, observando para cada lista. Caso contrário ele dirá "False".')

    w = [[2, 4, -9, -1], [-3, 0, 7], [-8, 6]]
    resultado = verifica_todas_listas(w)
    print('\nResultado:', resultado)
    print('Fim do programa')

main()
