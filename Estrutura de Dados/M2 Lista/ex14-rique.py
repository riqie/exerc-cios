'''
14. Escreva um algoritmo que receba valores em um vetor e imprima “ORDENADO” se o
vetor estiver em ordem crescente. Qual é a complexidade deste seu algoritmo?
'''

def verificarVetor(vetor):
    for i in range(len(vetor)):
        if not(vetor[0:] <= vetor[1:]):
            return
        else:
            return print('ORDENADO')

def main():
    vetor = [1,2,3,4,5] # ordenado
    vetor = [9,8,7,6,5]
    vetor = [0,1,1,1,2] # ordenado
    verificarVetor(vetor)

main()

'''
o algoritmo possui ordem de grandeza O(n), isto pois,
além das execuções simples, a execução do loop executa 'n' vezes,
isso faz com que a ordem de grandeza mais importante seja O(N)
'''
 