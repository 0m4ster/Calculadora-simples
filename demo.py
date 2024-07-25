
n1 = 0 
n2 = 0
resultado = 0
soma = ''


while True:



    n1 = float(input('Digite um numero: '))
    soma = input('Escolha o operador: ')
    n2 = float(input('Escolha outro numero: '))

    if soma == '+':
        resultado = n1 + n2
        print(resultado)
        print("="*40)
    elif soma == '-':
        resultado = n1 - n2
        print(resultado)
        print("="*40)
    elif soma == '/':
        resultado = n1 / n2
        print(resultado)
        print("="*40)
    elif soma == '*':
        resultado = n1 * n2
        print(resultado) 
        print("="*40)
    else: print("Erro de calculo") 
    text = input('Deseja finalizar?')
    if  text == "sim":
        break 
   




