"""Programa que pede ao usuário 1 número inteiro
informa se este número é par ou ímpar
se não digitar inteiro exibe erro """

""" num = input("Digite um número: ")

if num.isdigit():
    num_int = int(num)    
    if (num_int%2) == 0:
        print(f"Numero {num} e par")
    else:
        print(f"Numero {num} e impar")
else:
    print("Digite um numero inteiro")"""

 

"""
Programa que exibe uma saudação de acordo com a hora do usuário,
recebe um horario e diz Bom dia, boa tarde ou boa noite"""

hora = int(input("Que horas são?\n"))

if hora >= 0 and hora <= 24:
    
    if (hora >= 0 and hora <= 11):
        print("Bom dia")
    elif (hora == 12 and hora <= 17):
        print("Boa tarde")
    elif (hora >=18 and hora <=23): 
        print("Boa noite")
else:
    print("Digite um horario válido")

""" Programa que pede o nome do usuário, se o nome tiver 4 letras ou menos
informe que o nome é curto, se tiver 5 e 6 normal e mais que 6 muito grande

nome = str(input("Qual seu nome\n"))

qtd_letra = int(len(nome))

if qtd_letra <= 4:
    print("Seu nome e curto")
elif qtd_letra == 5 or qtd_letra == 6:
    print("Seu nome e normal")
else:
    print("Seu nome e grande")
"""

   


    