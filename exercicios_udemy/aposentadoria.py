
VALOR_MIN = 1212.00
VALOR_MAX = 7087.22

idade = int(input('Sua idade: '))
tempo_serviço = int(input('Tempo de serviço: '))
ultimo_salario = float(input('Seu ultimo salario: '))

if idade >= 65 or tempo_serviço >= 30 or idade>=60 and tempo_serviço>= 25:
    
    print('Voce pode se aposentar')
    
    if tempo_serviço >= 20:
        aposentadoria = ultimo_salario * 0.8 
        if aposentadoria <VALOR_MIN:
            print(f'Sua aposentadoria sera: R${VALOR_MIN}')
        elif aposentadoria > VALOR_MAX:
            print(f'Sua aposentadoria sera: R${VALOR_MAX}')
        else:
            print(f'Sua aposentadoria sera: R${aposentadoria}')
    else:
        aposentadoria =ultimo_salario *0.6
        if aposentadoria <VALOR_MIN:
            print(f'Sua aposentadoria sera: R${VALOR_MIN}')
        elif aposentadoria > VALOR_MAX:
            print(f'Sua aposentadoria sera: R${VALOR_MAX}')
        else:
            print(f'Sua aposentadoria sera: R${aposentadoria}')
                 
else:
    print('Voce nao pode se aposentar')
