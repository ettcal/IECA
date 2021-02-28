from mongoengine import *
from pymongo import MongoClient
import  datetime
from Tarea_4_StudentsIO import Estudiante, read_estudiantes, edit_estudiante, writeNew_estudiante,clear_estudiantes

connect('IECA', host = 'localhost', port = 27017)

print('Cuantos alumnos se registran?: ')
num=int(input())

for i in range(num):
    print('Nombre del alumno: ')
    nom=str(input())
    print('Correo del alumno: ')
    corr = str(input())
    print('Contraseña del alumno: ')
    cont = str(input())
    print('Materias del alumno: ')
    matr = str(input())
    estudiante = Estudiante(
        Nombre = nom,
        Correo = corr,
        Contrasena = cont,
        Materias = matr
    )
    estudiante.save()

read_estudiantes()
edit_estudiante()
writeNew_estudiante()
clear_estudiantes()

print("Hecho por: Etienne Calderón Romero")
