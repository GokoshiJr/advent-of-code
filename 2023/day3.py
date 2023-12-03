import sys
D = open(sys.argv[1]).read().strip()

def encontrar_adyacentes(matriz, fila, columna):
    adyacentes = []
    for i in range(fila-1, fila+2):
        for j in range(columna-1, columna+2):
            if 0 <= i < len(matriz) and 0 <= j < len(matriz[0]) and (i, j) != (fila, columna): adyacentes.append(matriz[i][j])
    return adyacentes
  
matrix = []
for line in D.split('\n'): matrix.append([char for char in line])
ok = False
numbers = []
number = ''

for fila in range(len(matrix)):
    for col in range(len(matrix[0])):        
        for e in encontrar_adyacentes(matrix, fila, col):
            if (not e.isdigit()) and (e != '.') and (matrix[fila][col] != '.') and (matrix[fila][col].isdigit()): ok = True                
        if matrix[fila][col].isdigit(): number += matrix[fila][col]
        else: 
            if ok: numbers.append((number))
            number = ''
            ok = False
         
print(sum([int(x) for x in numbers if x != '']))
