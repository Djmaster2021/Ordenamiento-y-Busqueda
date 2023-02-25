import random
import heapq
import random
import os
from colorama import *

class Opera():

    def __init__(self):
        pass
        
    
    def mergesort(self, arr):
        if len(arr) <= 1:
            return arr
        else:
            mid = len(arr) // 2
            left = arr[:mid]
            right = arr[mid:]
            left_sorted = self.mergesort(left)
            right_sorted = self.mergesort(right)
            return self.merge(left_sorted, right_sorted)
    
    def merge(self,left , right):
        result = []
        i, j = 0, 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
            j += 1
        result += left[i:]
        result += right[j:]
        return result
    
    #(Ordenamiento Rapido tambien llamado quicksort )
    def quicksort(self, arr):
        if len(arr) <= 1:
            return arr
        else:
            pivot = arr[0]
            left = [x for x in arr[1:] if x <= pivot]
            right = [x for x in arr[1:] if x > pivot]
            return self.quicksort(left) + [pivot] + self.quicksort(right)

    def Limpiar(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def BucaLineal(self, Lista, Valor):
            for i in range(len(Lista)):
                if Lista[i] == Valor:
                    return i
            return -1

    def bubbleSort(self, arr):
        n = len(arr)
        for i in range(n):
            for j in range(0, n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]

    def BusquedaBinaria(self, lista, valor):

        izquierda = 0
        derecha = len(lista) - 1
        while izquierda <= derecha:
            medio = (izquierda + derecha) // 2
        if lista[medio] == valor:
                return medio
        elif lista[medio] > valor:
                derecha = medio - 1
        else:
                izquierda = medio + 1
                return -1
        
    def selection_sort(self, arr):
        n = len(arr)
        for i in range(n):
            # Encuentra el elemento más pequeño en el subarreglo restante
            MinIndex = i
            for j in range(i+1, n):
                if arr[j] < arr[MinIndex]:
                    MinIndex = j
                    
            # Intercambia el elemento más pequeño con el primer elemento sin ordenar
            arr[i], arr[MinIndex] = arr[MinIndex], arr[i]

    def InsertionSort(self, arr):
        n = len(arr)
        for i in range(1, n):
            key = arr[i]
            j = i-1
            # Mueve los elementos mayores que el valor clave hacia adelante
            while j >= 0 and key < arr[j]:
                arr[j+1] = arr[j]
                j -= 1
            arr[j+1] = key

    def ErrorMensaje(self):
        input("Valores Incorrectos - PRESIONA ENTER")
        self.Limpiar()

    def Input(self):
        input(Fore.GREEN + "Presiona Enter" + Fore.RESET)
        self.Limpiar()

    def EnterMenu(self):
        input(Fore.CYAN + "\nPRESIONA ENTER PARA MAS OPCIONES...\n" + Fore.RESET)
