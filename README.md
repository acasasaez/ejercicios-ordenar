# ejercicios-ordenar
Para epresentar mi tarea he realizado un repositorio en github, dejo aquí la dirección URL: https://github.com/acasasaez/ejercicios-ordenar.git


Ejercicio 1: Consistía en realizar un algoritmo que nos permitiese ordenar los elementos de una lista por dicotomía e insercción.


Ejercicio 2: Consistía en elaborar un algoritmo que nos permitiese ordenar n tareas.
Para este ejercicio hemos tomado una matriz en la que aparecieran los n números de las tareas y una vez comparados los números por filas y columnas devuelve mensajes que nos permiten saber el orden por filas y por columnas y con esto podemos saber el orden de las tareas.


Ejercicio 3: Consistía en realizarun algoritmo que nols permitiese ordenar un segmento determinado de una lista y que guardase el máximo del segmento.

Diagramas que representan nuestros programas

Ejercicio 1:

![ordenac_dicotomia](https://user-images.githubusercontent.com/91721826/157718454-b86b604d-fb49-4fb5-82a5-5f82d93ac4d1.jpg)

Ejercicio 2:

![ord_top](https://user-images.githubusercontent.com/91721826/157718464-8cee2a19-a76f-4fdd-9e6f-2796f2828937.jpg)

Ejercicio3: 

![ejespecif](https://user-images.githubusercontent.com/91721826/157718485-10db580e-a14f-4543-a633-3a5c8759a123.jpg)

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


