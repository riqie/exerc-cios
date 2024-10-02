'''
18. O número 3025 possui a interessante característica:
30 + 25 = 55
55 elevado a 2 = 3025
Faça um programa que procure todos os números de 4 algarismos que possuem essa
característica.
'''
def verificarCaracteristica():
    for i in range(1000, 10000):

        # Dividir o número em duas partes: os dois primeiros e os dois últimos dígitos
        parte1 = i // 100  
        parte2 = i % 100   

        soma = parte1 + parte2  

        if soma ** 2 == i:  
            print(f'O número {i} possui tal característica.\nVeja:\n{parte1, parte2}\n{soma} elevado a 2:\n{soma **2}\n')

def main():
    verificarCaracteristica()

main()
