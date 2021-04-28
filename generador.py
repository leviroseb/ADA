import random
import numpy as np

#########################  Generador de arreglos  ###########################

'''El generador de arreglos propuesto utiliza la librería numpy que permite
crear y leer arreglos a través de los comandos savetxt y loadtxt'''



#En este caso la función recibe 2 argumentos que representan el número de arreglos y el tamaño de cada arreglo
def generador(n,tam):
    global a
    a=np.random.randint(-tam,tam,(n,tam),dtype=np.int32)
    #creamos una matriz a de n filas y tam columnas, con valores entre tam y -tam, es decir, n arreglos de tamaño tam


generador(10,10000)
np.savetxt('arreglo10000.txt',a) #Guardamos la matriz en un archivo de texto
#print(a)

#ANALISIS Y DISEÑO DE ALGORITMOS
#ALUMNO: Jhon Ismael Flores Pacheco
