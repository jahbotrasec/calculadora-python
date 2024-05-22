while True:


    # usuário informar os números
    x = str(input('Informe o primeiro número:')).replace(',',',')
    y = str('Informe o segundo número:').replace(',',',')

    # converte para números decimais
    x = float(x)
    y = float(y)

    print('Informe a operação que deseja fazer:\n')
    print('"+" para somar.')
    print('"-" para subtrair.')
    print('"*" para multilicar')
    print('"/" paradividir')
    print('"%" para encontrar o resto da divisão')

    op = input('operação desejada')

match op:
    case '+':
        print(f'A soma é: {x + y}.')

    case '-':
        print(f'A subtração é: {x - y}.')

    case '*':
        print(f'A multiplicação é: {x * y}.')

    case '/':
        print(f'A divisão é: {x / y}.')

    case '/':
        print(f'A divisão é: {x / y}.')


        