import Operaciones
from colorama import *

init()

class Lista():

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
        print("               Lista                  ")
        print("--------------------------------------"+ Fore.RESET)
        print(Fore.LIGHTYELLOW_EX + "La lista es: " + str(self.articulos) + Fore.RESET)
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

        nuevoItem = input("Digite el Nuevo Item: ")

        Position = int(input("Diguite la posición: "))
        
        new_list_size = len(self.articulos) + 1
        insert_position = Position - 1
        new_element = nuevoItem
        new_list = [Position] * new_list_size

        for i in range(insert_position):
            new_list[i] = self.articulos[i]
        new_list[insert_position] = new_element

        for i in range(insert_position, new_list_size-1):
            new_list[i+1] = self.articulos[i]
        self.articulos = new_list

        print ("Item Agregdo")
        print (self.articulos)
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
        print (self.articulos)

        DeletItem=int(input("Selecciona la POSICION del Item a eliminar:  "))
        DeletItem -= 1
        self.articulos.pop(DeletItem)
        print("El item Fue Eliminada")

        print("Nueva Lista")
        print(self.articulos)
        self.opera.Input()

    #---------------------------------------------------------
    #ORDENAR
    def ordenar(self):
        print("Ordenar")
        self.articulos.sort()
        print("La Lista fue acomodada Correctamente ")
        #Imprime la lista Acomodada de menor a mayor
        print(self.articulos)
        self.opera.Input()

    #---------------------------------------------------------
    #DESORDENAR
    def desordenar(self):
        print("Desordena")
        #Revolver Items
        print("La Lista se desordeno ")
        import random
        random.shuffle(self.articulos)
        print(self.articulos)
        self.opera.Input()
