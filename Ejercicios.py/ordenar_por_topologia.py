#Para esta tarea emplearé de nuevo el pseudocódigo:
from re import A


Algoritmo ordenar_topología:
#EN primer lugar describimos las variables con las que trabajaremos
Lista_1: LISTA #Lista que contiene las n tareas a realizar
Lista_2:LISTA  #Lista a los que pasarán los elementos que no tienen precedente
Lista_3:LISTA #Lista de restricciones que nos indica cómo ordenar determinados elementos , viene dada como una lista de tuplas
Lista_4:LISTA #Lista ordenada

#Por otro lado describimos los pasos a seguir por el programa para poder ordenar, topológicamente, nuestra lista de n tareas
Mientras Lista_1 no esté vacía:
    Añadir los elementos sin precedente a Lista_2
    Eliminar de Lista_1 los eeemntos añadidos a Lista_2
    Eliminar de Lista_3 los elementos ((x,y)) cuya x se encuentre en Lista_2 
    Añadir los elementos de lista_2 a Lista_4 

    Si 
    existe (x,y) y (x1,y1) tales que x==y1 y y==x1:
    entonces
    ERROR: Se produce un ciclo que nos impide realizar la ordenación 

    si no 
        devolver Lista_4 
#Como resultado obtenemos una lista que nos ofrece 1 de las posibles soluciones para ordenar nuestra lista de tareas.
