import mongo
from os import remove
from datetime import datetime


from codigosSensoresRasp import  codSenRasp

from Sensor import Sensor
from datosSensor import DatosSensor
import os
import serial
import time


interacciondb = mongo.MongoConexion("mongodb+srv://admin:luisskate13@cluster0.7einrmk.mongodb.net/test", "sistemaSensores", "DatosSensores")

class InterfaceDatosSensor():
    def __init__(self):
        self.listaS = Sensor()
        self.listaS.toObjects()
        self.lista = DatosSensor()
        self.lista.toObjects()


    def cls(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def nuevoSensor(self):

        listaSensor = Sensor()
        listaSensor.nombreSensor = input("Nombre del Sensor:")
        listaSensor.tipo = input("tipo de sensor:")
        cantPin = int(input("ingresa la cantidad de pines"))
        pines = list()
        i = 0
        while i != cantPin:
            p = input("pin:")
            pines.append(p)
            i = i + 1
        listaSensor.pines = str(pines)
        listaSensor.descr = input("descripcion:")

        return listaSensor

    def mostrarSensor(self, lista=None):
        self.cls()
        print("\n\n" + "-" * 10 + "Datos de Sensor" + "" * 10)
        if (lista == None):
            mylista = self.lista
        else:
            mylista = lista
        print("ID".ljust(5) +"\t\t" + 'nombre'.ljust(20)+ "\t\t" + 'Datos'.ljust(20)+'Fecha'.ljust(20)+''+'Info'.ljust(20)+'')
        i = 0




        for listaDatosSensor in mylista:
            print(str(i).ljust(5) + "\t\t" + listaDatosSensor.nombre+"\t\t" + str(listaDatosSensor.datos) +  listaDatosSensor.medida+ "\t\t"+listaDatosSensor.fecha+ "\t\t"+str(listaDatosSensor.detalles))
            i += 1




    def buscarSensor(self, code):
        mylista = [listaSensor for listaSensor in self.lista if listaSensor.datos == code]
        self.mostrarSensor(mylista)

    def getListaSensor(self):
        return self.lista

    def modificarSensor(self,listaS=None):
        self.cls()

        if (listaS == None):
            mylistaS = self.listaS
        else:
            mylistaS = listaS






        id = 0



        i=0
        for listaSensor in mylistaS:

           if listaSensor.dispositivo == "raspberry":
               codSen = codSenRasp()
               if listaSensor.tipo== "us":
                   codSen.ultrasonico(listaSensor.pines[0],listaSensor.pines[1])
               elif listaSensor.tipo == "Tem":
                   codSen.temperatura(listaSensor.pines[0])







           elif listaSensor.dispositivo == "arduinoUno":
               ser = serial.Serial('COM5', 9600)  # Reemplaza 'COM3' con el nombre del puerto serial del Arduino
               x=0
               cadena = ser.readline()
               nom = cadena.decode('utf-8').rstrip()
               dtails = []

               dtails.append(listaSensor.nombreSensor)
               dtails.append(listaSensor.descr)
               dtails.append(listaSensor.pines)
               dtails.append(listaSensor.tipo)
               dtails.append(listaSensor.dispositivo)

               # print(str(i).ljust( 5) + "\t\t" + listaSensor.nombreSensor + "\t\t" + listaSensor.tipo + "\t\t" + listaSensor.pines + "\t\t" + listaSensor.descr)

               cadena = ser.readline()
               dats = cadena.decode('utf-8').rstrip()

               cadena = ser.readline()
               medida = cadena.decode('utf-8').rstrip()

               now = datetime.now()

               listaDatosSensor = self.lista.getlist()[id]
               listaDatosSensor.nombre = str(nom)
               listaDatosSensor.datos = int(dats)
               listaDatosSensor.medida = medida
               listaDatosSensor.detalles = dtails

               listaDatosSensor.fecha = str(now)
               self.lista.modificar(id, listaDatosSensor)

               if (interacciondb.conect()):
                   interacciondb.insert_oneD(listaDatosSensor)
               self.lista.toJson(self.lista)

               id = id + 1
               return listaSensor
           # time.sleep(2)
        else:

            print("no se encontro un sensor en un dispositivo conectado")



    def eliminarSensor(self):
        id = input("Introduce ID:")
        id = int(id)
        print(self.lista.getMateria(id))
        self.lista.eliminar(self.lista.getMateria(id))

    def menuSensor(self):
        a = 10
        while a != 0:
            self.cls()
            print("\n\n" + "-" * 10 + "Menu Datos Sensor" + "-" * 10)
            print("1) leer datos\n2) Modificar datos Sensor\n3) Eliminar datos Sensor\n4) Mostrar datos Sensor\n0)salir")

            a = input("Selecciona una opción: ")
            if (a == '1'):
              """  p = self.nuevoSensor()
                self.lista.add(p)
                self.lista.toJson(self.lista)"""
              while True:
                time.sleep(5)

                self.mostrarSensor()
                self.modificarSensor()



            elif (a == '2'):
                self.mostrarSensor()
                self.modificarSensor()
                self.lista.toJson(self.lista)
            elif (a == '3'):
                self.mostrarSensor()
                self.eliminarSensor()
                self.lista.toJson(self.lista)

            elif (a == '4'):
                self.mostrarSensor()
            elif (a == '0'):
                break
            else:
                print("La opcion no es correcta vuelve a seleccionar da enter para continuar.....")
                input()