'''''
pilha e filas
pilha(stack) - LIFO - last in, fris out.
    Exemplo: pilha de livros que são adicionados um sobre e outro
fila (queue ) - FIFo - frist in, frist out
    Exemplo:  Uma fila de Banco ( Ou qualquer fia da vida 'real')
Filas podem ter o efeitos colaterais em desempenho, porque cada item alterado, todos os indices serão modificados
'''

'''livros = list()
livros.append('livro 1') #1
livros.append('livro 2') #2
livros.append('livro 3') #3
livros.append('livro 4') #4
livros.append('livro 5') #5

livro_removido = livros.pop()

print(livros, livro_removido)'''
from time import sleep
from collections import deque
fila = deque(maxlen=6)
fila = deque()

fila.append('Hedris Pereira')
fila.append('Janaina Pereira')
fila.append('Nunes Rocha')
fila.append('Henrique Rocha')
fila.append('José Silva')
fila.append('Marcos Da Silva')
print(f'Saiu: {fila.popleft()}')
print(f'Saiu: {fila.popleft()}')
print(f'Saiu: {fila.popleft()}')
print(f'Saiu: {fila.popleft()}')
print(f'Saiu: {fila.popleft()}')
print(f'Saiu: {fila.popleft()}')

for i in range(100):
    fila.append(i)
    sleep(1)
    print(fila)

