import shelve
import StudentIO

estudiantes = [[], [], [], [], []]

for i in range(len(estudiantes)):
    print(f"Ingrese el nombre del {i + 1} estudiante: ")
    estudiantes[i].append(str(input()))
    print(f"Ingrese el correo del {i + 1} estudiante: ")
    estudiantes[i].append(str(input()))
    print(f"Ingrese la contraseña del {i + 1} estudiante: ")
    estudiantes[i].append(str(input()))

StudentIO.save_students(estudiantes)

StudentIO.read_students('students.db',estudiantes)

StudentIO.edit_students('students.db',estudiantes)



