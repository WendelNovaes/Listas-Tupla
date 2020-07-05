lista = ['Cachorro', 'Gato', 'Passarinho', 'Peixe', 'Ornitorrinco']
lista_numeros = [1, 2, 3, 4, 5]

# Exibindo valores das da lista
cont = 0
for i in lista:
    cont += 1
    print(f'{cont}-{i}')

soma = sum(lista_numeros)
menor = min(lista_numeros)
maior = max(lista_numeros)

print(f'\nTotal de animais: {cont}')
print(f'\nSoma total da lista: {soma}')
print(f'Menor número da lista: {menor}')
print(f'Maior número da lista: {maior}')

print('\nRegistros da lista\n')
if 'Cachorro' in lista:
    print('Existe o registro Cachorro na lista!\n')

idLista = int(input('Informe o registro que deseja remover da lista: '))
lista.pop(idLista)
print(lista)




    
    
      