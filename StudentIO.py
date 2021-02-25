import shelve

def save_students(x):
    s = shelve.open('students.db')
    s['x']=x
    s.close()

def read_students(y,z): # El primer argumento que sea el nombre del archivo y en comillas (str)
    with shelve.open(y) as s:
        for j in s:
            for i in range(len(z)):
                print(f'Estudiante {i + 1}: {s[j][i]}')

def edit_students(yy,zz):
    with shelve.open(yy) as s:
        print("Qué estudiante se requiere cambiar? (1-5)")
        change = int(input()) - 1
        print("Qué se desea cambiar?\n1) Nombre\n2) Correo\n3) Contraseña")
        change_2 = int(input()) - 1
        zz[change].pop(change_2)
        print("Ingresar el dato correcto:")
        correct = str(input())
        zz[change].insert(change_2, correct)
        print(zz)

# def read_students(y,z): #ingresar los argumentos como string ''
#     with shelve.open(y, flag='r') as p:
#         #existing = p[z]
#
#     print('Existing: ', p[z])
#     try:
#         p[z] = 'new value'
#     except dbm.error as err:
#         print('ERROR: {}'.format(err))

    # p = shelve.open(y)
    # print (p[z])
    # p.close()