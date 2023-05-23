"""Calculadora com while"""
while True:
    numero_1= input('Digite um numero ')
    numero_2= input('Digite outro numero ')
    operador= input('Digite o operador (+-/*): ')


    numeros_validos=None  #aqui foi estabelecido uma flag 'bandeira' no nosso codigo.
    num_1_float= 0
    num_2_float= 0

    try:
        num_1_float=float(numero_1)
        num_2_float=float(numero_2)
        numeros_validos=True
    except:
        numeros_validos=None

        if numeros_validos is None:
            print('Um ou ambos os numeros digitados são invalidos.')
            continue # essa expressão serve para retornar a linha 10 e digitar o numero novamente , se ela nao existisse e como vimos none fosse Falso iria direto para a parte de sair ao inves de trazer um numero.

            operadores_permitidos= '+-/*'
            if operador not in operadores_permitidos:
                print('Operador Invalido')
                continue

            if len (operador)>1:
                print('Digite apenas um operador')
                continue

    print('Realizando sua conta confica o resultado a baixo.')
    if operador == '+':
        print(f'{num_1_float}+{num_2_float}=',num_1_float+num_2_float )
    elif operador== '-':
        print(f'{num_1_float}+{num_2_float}=',num_1_float-num_2_float)    
    elif operador== '/':
        print(f'{num_1_float}+{num_2_float}=',num_1_float/num_2_float)   
    elif operador== '-':
        print(f'{num_1_float}+{num_2_float}=',num_1_float*num_2_float)   
            
    else:
        print('Nao deveria estar aqui')                


    sair= input ( 'Quer sair?, Digite [s]im: ').lower().startswith('s')
    if sair is True:
        break
