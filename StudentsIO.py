from mongoengine import *
from pymongo import MongoClient
import datetime


class Estudiante(Document):
    Nombre = StringField(required=True, max_length=100)
    Correo = StringField(required=True, max_length=100)
    Contrasena = StringField(required=True, max_length=50)
    Materias = StringField(required=True, max_length=300)
    Registro = DateField(default=datetime.date.today())


def deleteOne(nombre):
    client = MongoClient('localhost', 27017)
    db = client['IECA']
    coll = db['estudiante']
    coll.delete_one({ "Nombre": nombre })



def edit_estudiante(nome, nom,n, corr,cr, contra,cn, mtrs,mt): #nombre de busqueda, nombre para cambiar, casilla de nombre correo,casilla de correo, contraseña, casilla de contraseña, materias, casilla de materias
    client = MongoClient('localhost', 27017)
    db = client['IECA']
    coll = db['estudiante']

    if n == True:  #Nombre
        coll.update_one({"Nombre": nome}, {"$set": {"Nombre": nom}})
    if cr == True:  #Correo
        coll.update_one({"Nombre": nome}, {"$set": {"Correo": corr}})
    if cn == True:  #Contraseña
        coll.update_one({"Nombre": nome}, {"$set": {"Contrasena": contra}})
    if mt == True: #Materias
        coll.update_one({"Nombre": nome}, {"$set": {"Materias": mtrs}})


def writeNew_estudiante(nom, corr, cont, matr):
    client = MongoClient('localhost', 27017)
    db = client['IECA']
    coll = db['estudiante']
    estudiante = Estudiante(
        Nombre=nom,
        Correo=corr,
        Contrasena=cont,
        Materias=matr
    )
    estudiante.save()



def delete_All():
    client = MongoClient('localhost', 27017)
    db = client['IECA']
    coll = db['estudiante']
    coll.delete_many({})

