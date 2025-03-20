number_inicio = int(input('Início: '))
number_fim = int(input('Fim: '))

if number_fim > number_inicio:
    while number_inicio <= number_fim:
        print(number_inicio,end='... ')
        number_inicio += 1
else:
    while number_inicio >= number_fim:
        print(number_inicio,end='... ')
        number_inicio -= 1
print()