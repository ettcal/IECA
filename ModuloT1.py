def validacion(x,y):
    # Condicionales donde se compara la deción del usuario y la elección aleatoria de la PC para saber si se empata, pierde o gana
    if x == y:
        print('\nEmpate!')
    elif x == 'Piedra' and y == 'Papel':
        print('\nPerdiste!')
    elif x == 'Piedra' and y == 'Tijera':
        print('\nGanaste!')
    elif x == 'Papel' and y == 'Tijera':
        print('\nPerdiste!')
    elif x == 'Papel' and y == 'Piedra':
        print('\nGanaste!')
    elif x == 'Tijera' and y == 'Piedra':
        print('\nPerdiste!')
    elif x == 'Tijera' and y == 'Papel':
        print('\nGanaste!')
    else:
        print('\nSelección no válida!')