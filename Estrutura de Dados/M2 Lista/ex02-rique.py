'''
O método de lista 'reverse' inverte os elementos da lista. Defina uma função chamada
'reverse' que inverte os elementos no argumento de lista (sem usar o método reverse).
Tente tornar essa função a mais eficiente possível e indique sua complexidade
computacional usando a notação big-O.
'''

def reverse(example_list): # criamos uma função e passamos como parametro uma lista exemplo
    
    left = 0 # contador que aumenta
    right = len(example_list) - 1 # contador que diminui
    
    while left < right:
        temp = example_list[left] 
        example_list[left] = example_list[right]
        example_list[right] = temp
        left += 1
        right -= 1
        print(example_list)
    
    '''
    primeiro forçamos a entrada no while, então criamos uma variavel temporária
    para realizarmos as substituições. tempo recebe o primeiro número,
    o primeiro numero recebe o último e o ultimo recebe temp. Com isso: left incrementa 1 e right decrementa 1,
    assim fazendo com que a lista seja mudada por completo.
    OBS: caso a lista seja impar, o elemento do meio nao precisa ser alterado.
    '''
    
    return example_list

def main():
    print('\nThe program will flip the list manually')
    mylist = [0,1, 2, 3, 4, 5,6,7,8,9]
    print(f'\nOriginal List: {mylist}')

    reverse(mylist)
    print(f'\nNew List: {mylist}\n\nEnd of program. Thank you!')

main()


