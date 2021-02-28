from mongoengine import *
from pymongo import MongoClient
import datetime


class Estudiante(Document):
    Nombre = StringField(required=True, max_length=100)
    Correo = StringField(required=True, max_length=100)
    Contrasena = StringField(required=True, max_length=50)
    Materias = StringField(required=True, max_length=300)
    Registro = DateField(default=datetime.date.today())


def read_estudiantes():
    client = MongoClient('localhost', 27017)
    db = client['IECA']
    coll = db['estudiante']
    for i in coll.find():
        print(i)
    # for a in Estudiante.objects:
    #     print(a.Nombre)
    #     print(a.Correo)
    #     print(a.Contrasena)
    #     print(a.Materias)
    #     print('------------------')


def edit_estudiante():
    client = MongoClient('localhost', 27017)
    db = client['IECA']
    coll = db['estudiante']
    print("Que alumno desea cambiar (escribir nombre): ")
    name = str(input())
    print("Que variable desea cambiar (escribir nombre de variable): ")
    var = str(input())
    print("Ingrese el/los nuevo(s) dato(s): ")
    new = str(input())

    coll.update_one({"Nombre": name}, {"$set": {var: new}})

def writeNew_estudiante():
    client = MongoClient('localhost', 27017)
    db = client['IECA']
    coll = db['estudiante']
    if coll.find().count()<=5:
        print('Cuantos alumnos se registran?: ')
        num = int(input())
        if num <= 5-coll.find().count():
            for i in range(num):
                print('Nombre del alumno: ')
                nom = str(input())
                print('Correo del alumno: ')
                corr = str(input())
                print('Contraseña del alumno: ')
                cont = str(input())
                print('Materias del alumno: ')
                matr = str(input())
                estudiante = Estudiante(
                    Nombre=nom,
                    Correo=corr,
                    Contrasena=cont,
                    Materias=matr
                )
                estudiante.save()


def clear_estudiantes():
    client = MongoClient('localhost', 27017)
    db = client['IECA']
    coll = db['estudiante']
    coll.delete_many({})

