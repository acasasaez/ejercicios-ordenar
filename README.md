# ejercicios-ordenar
Para epresentar mi tarea he realizado un repositorio en github, dejo aquí la dirección URL: https://github.com/acasasaez/ejercicios-ordenar.git


Ejercicio 1: Consistía en realizar un algoritmo que nos permitiese ordenar los elementos de una lista por dicotomía e insercción. De modo que nuestra lista se divide en 2; en una vamos añadiendo los elementos por orden y la otra va disminuyendo a medida que pasamos los mínimos de una lista a otra.


Ejercicio 2: Consistía en elaborar un algoritmo que nos permitiese ordenar n tareas.
Este ejercicio lo he realizado en pseudocódigo porque me estaba dando error al pasarlo a código.


Ejercicio 3: Consistía en realizarun algoritmo que nos permitiese ordenar un segmento determinado de una lista y que guardase el máximo del segmento.

Diagramas que representan nuestros programas

Ejercicio 1:
![ordenar por dicotomia de birn](https://user-images.githubusercontent.com/91721826/158067681-3ae836f1-0ec5-4c62-af16-8352417f4028.jpg)



Ejercicio 2:

![diagraba topologia bien](https://user-images.githubusercontent.com/91721826/158067694-d4652356-cc77-4aee-82b3-334a501dcdb3.jpg)



Ejercicio3: 

![último ejercicio segmento bien](https://user-images.githubusercontent.com/91721826/158069161-46f16439-733e-4876-9871-253ee7fc25e9.jpg)


Código: 

```
Ejercicio 1:
def ordenar_dicotomia(lista):
    lista_ordenada = []
    while len(lista)>0:
        min= lista[0]
        for i in range (len(lista)):
            if lista [i]< min:
                a=lista[i]
                min = a
        lista_ordenada.append(min)
        lista.remove(min)
                    
    return lista_ordenada

if __name__ == "__main__":
    ordenar_dicotomia()

    
Ejercicio 2: 
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



Ejercicio 3:
def intercambio_segmento(lista,e,b):
    segmento = lista[e:b]
    if b> len(lista) or e> b:
        return "ERROR"

    intercambios = True
    while intercambios:
        intercambios = False
        for i in range (len(segmento) -1):
            if segmento[i]>segmento[i+1]:
                a = segmento[i+1]
                segmento[i+1] = segmento[i]
                segmento [i] =a
                intercambios = True
    lista[e:b]=segmento
    return lista

if __name__ == "__main__":
    intercambio_segmento()


