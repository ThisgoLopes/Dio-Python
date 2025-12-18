"""Exercício Aula 47
    1. Digitar nome
    2. Digitar idade
    3. Se nome e idade digitados:
        Exibir: 
        a. Nome
        b. Nome invertido
        c. Seu nome contém (ou não) espaços
        d. Quantas letras tem o nome
        e. Primeira letra
        f. Ultima letra
    Se nada for digitado imprima uma mensagem de erro
"""
nome = input("Digite seu nome: ")
idade = input("Digite sua idade: ")

verifica_nome = (len(nome))
verifica_idade = len(idade)
nome_invertido = nome[-1:-verifica_nome:-1]

if verifica_idade <= 1 or verifica_idade == 0 or  verifica_nome < 2:
        print("Você deixou campos vazios")
else:
    print(f"Seu nome e: {nome}")
    print(f"Seu nome invertido fica: {nome[::-1]}")
    print(f"Seu nome possui: {len(nome)} letras")
    if " " in nome:
        print("Seu nome possui espaço")
    else:
        print("Seu nome não possui espaço")
    print(f"A primeira letra do seu nome e: {nome[0]}")
    print(f"A ultima letra do seu nome e: {nome[-1]}")


    
    
    

    
    

    

