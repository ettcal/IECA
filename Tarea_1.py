#Módulos utilizados
from random import randint
from ModuloT1 import validacion

#Impresión en pantalla de las opciones disponibles
print('Selecciona un número\n'
      '1) Piedra\n'
      '2) Papel\n'
      '3) Tijera')

opciones = ['Piedra', 'Papel', 'Tijera']

seleccion = opciones[int(input())-1]     # Se resta 1 al número que se eligió para que quede en el rango de 0 a 2

eleccionPC=opciones[randint(0,2)]     # El str seleccionado aleatoriamente se queda guardado en una variable

print('\nTu elección: ',seleccion)
print('Elección de la PC: ',eleccionPC)


validacion(seleccion, eleccionPC)

print('\nRealizado por Etienne Calderón Romero')