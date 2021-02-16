import re

#---Datos de entrada---
correo="enn.calderon@hotmail.com"
telefono="(473)1220-542"
curp="CARE981101HGTLMT01"
rfc="CARE9601013A1"

#---Patrones asignados
patron_correo="([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)"
patron_telefono="[0-9]{10}"
patron_curp="[a-z]{4}[0-9]{6}[a-z]{6}[0-9]{2}"
patron_rfc="[a-z]{4}[0-9]{7}[a-z]{1}[0-9]{1}"

#---Líneas de código para quitar paréntesis, espacios y guiones del dato de teléfono
telefono=telefono.replace('(', '')
telefono=telefono.replace(')', '')
telefono=telefono.replace(' ', '')
telefono=telefono.replace('-', '')

#---Condicionales para impresión---
if re.fullmatch(patron_correo,correo):
    print("\nEl correo es valido")
else:
    print("\nEl correo NO es valido")
if re.match(patron_telefono,telefono):
    print("El número de teléfono es valido")
else:
    print("El número de teléfono NO es valido")
if re.fullmatch(patron_curp,curp,re.I):
    print("La CURP es valida")
else:
    print("La CURP NO es valida")
if re.fullmatch(patron_rfc,rfc,re.I):
    print("El RFC es valido")
else:
    print("El RFC NO es valido")

print("\n\nHecho por Etienne Calderón Romero")

