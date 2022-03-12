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
Algoritmo ordenacion_topologica:
Entrada: 
    t: MATRIZ 
Precondicion:
    t != NULO 
Realizacion: 
    Para i en rango contar(t)-1: 
            para j en rango contar (t)-1:         #Nuestro código debe comparar cada elemento con los elementos adyacentes
               si t[i]< t[i+1]:                   #Una vez comparados los elementos nos indica cuál va antes de de las 2                                                
                    imprimir tarea i por fila va antes que tarea i+1 por fila
                si no:
                    imprimir tarea i+1 por fila va antes que tarea i por fila
                fin si 

                si t[i][j]< t[i][j+1]:
                    imprimir  tarea j por columna va antes que j por columna
                si no: 
                    imprimir tarea j+1 por columna va antes quej por columna 
                fin si 
Postcondicion:
Resultado #Como resultado la función nos imprime una serie de frases lógicas que nos permite tomar las n tareas y ordenarlas  
#Teniendo en cuenta que el ejercicio no está hecho a código no podremos ejecurtarlo sin embargo al final de nuestra función deberíamos acabar con un "if __name__ ==__main__:
#                                                                                                                                                               ordenar)" Así
#igual que en el ejercicio prueba podríamos hacer que se ejecutase en el main si lo desemaos 



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


