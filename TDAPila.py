import Operaciones
from colorama import *
import random

init()

class Pila():

    #Variables a declarar
    articulos = ["Ipads","Telesvisores","Celulares"]
    numeros = [1,2,3,4,5]

    opera = Operaciones.Opera()
    paso = True

    def __init__(self):
        while self.paso:
            try:
                self.menu()
            except:
                self.opera.ErrorMensaje()
        
    def menu(self):

        print(Fore.GREEN + "--------------------------------------")
        print("               Pila                  ")
        print("--------------------------------------"+ Fore.RESET)
        print(Fore.LIGHTYELLOW_EX + "La pila de articulos es: " + str(self.articulos) + Fore.RESET)
        print(Fore.LIGHTYELLOW_EX + "La pila de numeros es: " + str(self.numeros) + Fore.RESET)
        print()
        print(Fore.CYAN + "1) Insertar     ")
        print("2) Recorrer     ")
        print("3) Buscar       ")
        print("4) Eliminnar    ")
        print("5) Ordenar      ")
        print("6) Desordenar   ")
        print("7) Cerrar el programa" + Fore.RESET)
        print()

        opcion = int(input(Fore.YELLOW + "Seleccione Una Operación: --> " + Fore.RESET))

        if opcion == 1:
            self.opera.Limpiar()
            self.insertar()
        elif opcion == 2:
            self.opera.Limpiar()
            self.recorrido()
        elif opcion == 3:
            self.opera.Limpiar()
            self.buscar()
        elif opcion == 4:
            self.opera.Limpiar()
            self.eliminar()
        elif opcion == 5:
            self.opera.Limpiar()
            self.ordenar()
        elif opcion == 6:
            self.opera.Limpiar()
            self.desordenar()
        elif opcion == 7:
            self.paso = False

    #---------------------------------------------------------
    #INSERTAR
    def insertar(self):
        print("Insertar")
        NueElemento = input("inserte el nuevo elemento:  ")
        self.articulos.append(NueElemento)
        print(self.articulos)
        self.opera.Input()

    #---------------------------------------------------------
    #RECORRIDO
    def recorrido(self):
        print ("Recorrido de Items")
        #Imprime cada uno de los elementos de la Lista
        for elemento in self.articulos:
            print("#",elemento)
        self.opera.Input()

    #---------------------------------------------------------
    #BUSCAR
    def buscar(self):
        print("Busca")
        Busqueda = input("ingrese el Item que desea buscar: ")
        search_item = Busqueda
        if search_item in self.articulos:
            print(f'{search_item} si se encuentra en la lista.')
        else:
            print(f'{search_item} no se encuentra en la lista.')
        self.opera.Input()

    #---------------------------------------------------------
    #ELIMINAR
    def eliminar(self): 
        print("Eliminar")
        n = self.articulos.pop()
        print(f"Sacando el elemento {n}")
        print(self.articulos)
        self.opera.Input()

    #---------------------------------------------------------
    #ORDENAR
    def ordenar(self):
        print("Ordenar - SOLO PILA NUMERICA")
        band = False
        while band == False:
            band = True
            for i in range(len(self.numeros)-1):
                if self.numeros[i] > self.numeros[i + 1]:
                    aux = self.numeros[i]
                    self.numeros[i] = self.numeros[i+1]
                    self.numeros[i+1] = aux
                    band = False
        print("self.numeros ordenada")
        print(self.numeros)
        self.opera.Input()
    #---------------------------------------------------------
    #DESORDENAR
    def desordenar(self):
        print("Desordena - SOLO PILA NUMERICA")
        print("Pila numerica desordenada:")
        random.shuffle(self.numeros)
        print(self.numeros)
        self.opera.Input()