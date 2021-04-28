import numpy as np
from time import time

#Ordenamiento burbuja
def bubble(A):
    for i in range(len(A)-1):
        for j in range(len(A)-1):
            if A[j]>A[j+1]:
                aux=A[j]
                A[j]=A[j+1]
                A[j+1]=aux


#Ordenamiento por inserción
def insertion(A):
    
    for i in range(1, len(A)):
        key = A[i]
        j = i-1

        while j >= 0 and A[j] > key:
            A[j+1] = A[j]
            j -= 1

        A[j+1] = key


'''Hacemos uso de loadtxt de la librería numpy para poder cargar los datos
anteriormente guardados en un archivo de texto, y a través de un ciclo for recorremos
la matriz donde cada fila representa un arreglo a ordenar'''
n=0
m=0

#Tiempos de ejecución de Bubblesort
b=np.loadtxt("arreglo1000.txt")#Cargamos el archivo de texto con los arreglos generados previamente
for i in range(10):
    tiempo_inicio=time()
    bubble(b[i])
    tiempo_final=time()
    tiempo_ejecucion=tiempo_final-tiempo_inicio
    n+=tiempo_ejecucion
    print(tiempo_ejecucion)
print(n/10)#Promedio de todos los tiempos hallados en Bubble

print()


#Tiempos de ejecución de InsertSort
for j in range(10):
    tiempo_inicio1=time()
    insertion(b[j])
    tiempo_final1=time()
    tiempo_ejecucion1=tiempo_final1-tiempo_inicio1
    m+=tiempo_ejecucion1
    print(tiempo_ejecucion1)
print(m/10)#Promedio de los tiempos hallados en Insert

'''Una de las desventajas para poder hallar los tiempos y graficarlos es que se tiene que
ejecutar el generador de arreglos cada vez por cada tamaño, es decir que tendremos
que guardar 10 archivos de texto para este caso, es decir uno para el tamaño de 1000,
otro para 2000, etc; y como consecuencia tenemos que ejecutar los algoritmos de ordenamiento
para cada tamaño de arreglo, quizás sea posible hacerlo todo en una sola ejecución, pero
en mi caso aun no fue posible'''

#Todos los promedios fueron copiados y ploteados usando la librería matplotlib de python

#Conclusión: Al observar la gráfica notamos que los tiempos de Insert son mejores que los de Bubblesort por lo que podríamos afirmar que el método insert es más eficiente que Bubble


#ANALISIS Y DISEÑO DE ALGORITMOS
#ALUMNO: Jhon Ismael Flores Pacheco


