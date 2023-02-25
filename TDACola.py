import Operaciones
import heapq
from colorama import *
import random

init()

class Cola():

    #Variables a declarar
    articulos = ["Ipads","Telesvisores","Celulares"]
    historial = []

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
        print("----------------Cola------------------")
        print("--------------------------------------" + Fore.RESET)
        print(Fore.BLUE + "1)  Ingresar                 ") 
        print("2)  Sacar                    ")
        print("3)  Recorrido                ")
        print("4)  Ordenar                  ")
        print("5)  Desordenar               ")
        print("6)  Historial de Salidas     ")
        print("7)  Regresar a la Fila       " + Fore.RESET)

        print(Fore.YELLOW + "-------------------------------------------")
        print("-------------Busqueda Tipos----------------")  
        print("-------------------------------------------" + Fore.RESET)
        print(Fore.BLUE + "8)  Busqueda Secuencial      ")
        print("9)  Busqueda Lineal")
        print("10) Busqueda Binaria" + Fore.RESET)

        print(Fore.YELLOW + "--------------------------------------")
        print("-------Ordenamientos Iterativos-------")
        print("--------------------------------------" + Fore.RESET)   
        print(Fore.BLUE + "11) Burbuja       ")
        print("12) Selección")
        print("13) Insercción" + Fore.RESET)

        print(Fore.YELLOW + "--------------------------------------")
        print("--------Ordenamiento Recursivo--------")
        print("--------------------------------------" + Fore.RESET)
        print(Fore.BLUE + "14) ordenamiento rápido")
        print("15) ordenamiento por mezcla")
        print("16) Regresar al Menu Principal" + Fore.RESET)
        print()

        opcion = int(input(Fore.YELLOW + "Seleccione Una Operación: --> " + Fore.RESET))

        if opcion == 1:
            self.opera.Limpiar()
            self.ingresar()
        elif opcion == 2:
            self.opera.Limpiar()
            self.sacar()
        elif opcion == 3:
            self.opera.Limpiar()
            self.recorrido()
        elif opcion == 4:
            self.opera.Limpiar()
            self.ordenar()
        elif opcion == 5:
            self.opera.Limpiar()
            self.desordenar()
        elif opcion == 6:
            self.opera.Limpiar()
            self.historialS()
        elif opcion == 7:
            self.opera.Limpiar()
            self.regresarC()
        elif opcion == 8:
            self.opera.Limpiar()
            self.busquedaSecuencial()
        elif opcion == 9:
            self.opera.Limpiar()
            self.busquedaLineal()
        elif opcion == 10:
            self.opera.Limpiar()
            self.busquedaBinaria()
        elif opcion == 11:
            self.opera.Limpiar()
            self.ordenamientoBorbuja()
        elif opcion == 12:
            self.opera.Limpiar()
            self.seleccionar()
        elif opcion == 13:
            self.opera.Limpiar()
            self.ordenamientoInsercion()
        elif opcion == 14:
            self.opera.Limpiar()
            self.ordenamientoRapido()
        elif opcion == 15:
            self.opera.Limpiar()
            self.ordenamientoMezcaldo()
        elif opcion == 16:
            self.opera.Limpiar()
            self.paso = False
        else:
            print(Fore.RED + "El valor no se encuantra en el menu" + Fore.RESET)        

    #---------------------------------------------------------
    #INGRESAR DATOS A COLA
    def ingresar(self):
        print("Ingresar")
        print("Inserte el Nombre")
        Persona = input("--> ")
        self.articulos.append(Persona)
        print(self.articulos)
        self.opera.Input()


    #---------------------------------------------------------
    #SACAR DATOS DE COLAS
    def sacar(self):
        print("Sacar")
        print("Se agrego nuevo historial")
        self.historial.append(self.articulos.pop(0))
        print(self.articulos)
        self.opera.Input()
        

    #---------------------------------------------------------
    #RECORRIDO
    def recorrido(self):
        print("Recorrido")
        for elemento in self.articulos: 
            print(elemento)
        self.opera.Input()
          

    #---------------------------------------------------------
    #HISTORIAL DE SALIDAS COLA
    def historialS(self):
        print("Historial de Salida")
        print ("Resultados del Historial")
        print(self.historial)
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
        print("Ordenar ")
        nombre = sorted(self.articulos, key=lambda x: x)
        self.articulos.clear()
        self.articulos = nombre
        print(self.articulos)
        self.opera.Input()


    #---------------------------------------------------------
    #DESORDENAR
    def desordenar(self):
        print("Desordenar ")
        random.shuffle(self.articulos)
        print(self.articulos)
        self.opera.Input()
        
    
    #---------------------------------------------------------
    #REGRESAR A LA COLA
    def regresarC(self):
        print("Regresar a la Fila")
        self.articulos.append(self.historial.pop(0))
        print(self.articulos)
        self.opera.Input()

        
    #---------------------------------------------------------
    #BUSQUEDA SECUECIAL
    def busquedaSecuencial(self):
        print("Busqueda Secuencial  ")
        BuscaNum=input("Seleccione el elemento a buscar:  ")
        search_item = BuscaNum
        if search_item in self.articulos:
            print(f'{search_item} se encuentra en la lista.')
            print("\n")
        else: print("No se encontro Persona ")
        self.opera.Input()

        
    #---------------------------------------------------------
    #BUSQUEDA LINEAL
    def busquedaLineal(self):
        print("Busqueda Lineal ")
        PersoneBusca = input("Inserte el Nombre")
        indice = self.opera.BucaLineal(self.articulos, PersoneBusca)

        if indice != -1:
            print( PersoneBusca + f" se encuentra en la posición {indice} de la lista.")
        else:
            print(PersoneBusca + "no se encuentra en la lista.")
        self.opera.Input()
            

    #---------------------------------------------------------
    #BUSQUEDA BINARIA
    def busquedaBinaria(self):
        BusqBin = (input("Inserte el nombre de la persona que desea Buscar: "))
        indice = self.opera.BucaLineal(self.articulos, BusqBin)

        print("Busqueda Binaria")
        if indice != -1:
            print(BusqBin +f" se encuentra en la posición {indice} de la lista.")
        else:
            print(BusqBin+" no se encuentra en la lista.")
        self.opera.Input()
            

    #---------------------------------------------------------
    #ORDENAMIENTO BORBUJA
    def ordenamientoBorbuja(self):
        self.opera.bubbleSort(self.articulos)
        print("Lista ordenada:")
        for i in range(len(self.articulos)):
            print(self.articulos[i])
        self.opera.Input()

            
    #---------------------------------------------------------
    #SELECCIONAR Y ORDENAR
    def seleccionar(self):
        self.opera.selection_sort(self.articulos)
        print("Lista ordenada:")
        for i in range(len(self.articulos)):
            print(self.articulos[i])
        self.opera.Input()

           
    #---------------------------------------------------------
    #ORDENAMIENTO INTERACTIVO POR INSERCION
    def ordenamientoInsercion(self):
        self.opera.InsertionSort(self.articulos)
        print("Lista ordenada:")
        for i in range(len(self.articulos)):
            print(self.articulos[i]) 
        self.opera.Input()


    #---------------------------------------------------------
    #ORDENAMIENTO RAPIDO
    def ordenamientoRapido(self):
        print("Ordenamiento Rapido")
        self.opera.quicksort(self.articulos)
        print(self.articulos)
        self.opera.Input()
        
        
    #---------------------------------------------------------
    #ORDENAMIENTO POR MEZCLA
    def ordenamientoMezcaldo(self):
        print("Ordenamiento Por Mezcla")
        self.opera.mergesort(self.articulos)
        print(self.articulos)
        self.opera.Input()