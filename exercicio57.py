NUMERO = 20
i = 0
soma_quadrados_pares = 0
soma_quadrados_impares = 0

while i<NUMERO:
    i = i +1 
    quadrado = i**2
    if quadrado % 2 == 0:
        soma_quadrados_pares += quadrado
    else:
        soma_quadrados_impares += quadrado
    print(f'Numero: {i}, Quadrado: {quadrado}')

print(f"A soma dos quadrados pares: {soma_quadrados_pares}\nA soma dos quadrados impares {soma_quadrados_impares}")
    

