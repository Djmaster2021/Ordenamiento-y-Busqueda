import TDALista
import TDAPila
import TDACola
import Operaciones 
from colorama import *

paso =  True
limpiar = Operaciones.Opera()
limpiar.Limpiar()

if __name__ == "__main__":
        while paso:

            try:
                print(Fore.GREEN + "--------------------MENU--------------------" + Fore.RESET)
                print("1. Listas Estaticas")
                print("2. Pila Estaticas")
                print("3. Cola Estaticas")
                print("4. Cerra programa")

                
                opcion = int(input("-> "))

                if opcion == 1:
                    limpiar.Limpiar()
                    lista_Estatica = TDALista.Lista()
                elif opcion == 2:
                    limpiar.Limpiar()
                    pila_Estatica = TDAPila.Pila()
                elif opcion == 3:
                    limpiar.Limpiar()
                    cola_Estatica = TDACola.Cola()
                elif opcion == 4:
                    paso = False
            except:
                print("Valores incorrectos.")