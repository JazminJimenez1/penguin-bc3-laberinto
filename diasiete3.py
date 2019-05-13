#creamos un archivo nuevo
#uso de numeros aleatorios
#con la extension .py
#uso de numeros aleatorios
 
#importamos la libreria randint
from random import randint 
aleatorio=randint(0,20)       #creamos una variable
#y generamos un numero aleatorio entre 0 y 20
print(aleatorio)                #imprimimos el numero generado

#ejercicio
#escribir una funcioin sorteo() que reciba
#una lista de participantes, y elegir a uno
#de los participantes aleatorios, y
#retornar esa persona elegida
#DESAFIO: no volver retornar imprimir a la persona ya sorteada
 
from random import randint

def sorteo (lista_participantes):
    cant=len(lista_participantes)-1                           #utilizamos cant/len para saber la cantidad de personas que hay en la lista
    aleatorio=randint(0,cant) 
    return lista_participantes[aleatorio]                   #retornamos a la lista de participantes, y volvemos a sortear
participantes=["Dulce","Maria","Paula","Laura","Ana"]           
participante_ganador=sorteo(participantes)                  
print(participante_ganador)                                 #imprimimos al ganador
#DESAFIO


