import os
from tkinter import W

from interfaceSensor import InterfaceSensor
from interfaceDatosArduino import InterfaceDatosSensor

class Main():
    def __init__(self):
        self.interfaceSensor = InterfaceSensor()
        self.interfaceDAtos  = InterfaceDatosSensor()



    def cls(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def menuPrincipal(self):
        a = 10
        while a != 0:
            self.cls()
            print("\n\n" + "-" * 60 + "Welcome" + "-" * 60)

            print(" Datos de sensores(1) \n menu sensores(2)\n salir(0)")

            a = input("Selecciona una opción: ")
            if (a.upper() == '1'):
                p = self.interfaceDAtos.menuSensor()
            elif (a.upper() == '2'):
                p = self.interfaceSensor.menuSensor()

            elif (a == '0'):
                break
            else:
                print("La opcion no es correcta vuelve a seleccionar da enter para continuar.....")
                input()


if __name__ == '__main__':

    ip = Main()
    ip.menuPrincipal()