number_inicio = int(input('Início: '))
number_fim = int(input('Fim: '))

if number_fim > number_inicio:
    while number_fim > number_inicio:
        number_inicio += 1
        print(number_inicio)
else:
    while number_fim < number_inicio:
        number_inicio -= 1
        print(number_inicio)