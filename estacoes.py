# Sistema que retorna as estações do ano

# Apresentação
print('\n\t\t\t -- Estações do Ano --\n')

# Entradas
mes = int(input('Informe o mês: '))
dia = int(input('Informe o dia: '))

# Processamento e saída

if mes in(1, 2, 3):
    print('Verão')
elif mes in(4, 5, 6):
    print('Outono')
elif mes in(7, 8, 9):
    print('Inverno')
elif mes in(10, 11, 12):
    print('Primavera')
else:
    print(f'Mês {mes} incorreto!')