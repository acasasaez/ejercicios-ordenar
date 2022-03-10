# ejercicios-ordenar
Ejercicio 1: Consistía en realizar un algoritmo que nos permitiese ordenar los elementos de una lista por dicotomía e insercción.


Ejercicio 2: Consistía en elaborar un algoritmo que nos permitiese ordenar n tareas.
Para este ejercicio hemos tomado una matriz en la que aparecieran los n números de las tareas y una vez comparados los números por filas y columnas devuelve mensajes que nos permiten saber el orden por filas y por columnas y con esto podemos saber el orden de las tareas.


Ejercicio 3: Consistía en realizarun algoritmo que nols permitiese ordenar un segmento determinado de una lista y que guardase el máximo del segmento.

Diagramas que representan nuestro programa

![ordenac_dicotomia](https://user-images.githubusercontent.com/91721826/157718454-b86b604d-fb49-4fb5-82a5-5f82d93ac4d1.jpg)

![ord_top](https://user-images.githubusercontent.com/91721826/157718464-8cee2a19-a76f-4fdd-9e6f-2796f2828937.jpg)


![ejespecif](https://user-images.githubusercontent.com/91721826/157718485-10db580e-a14f-4543-a633-3a5c8759a123.jpg)

Código: 

´´´Ejercicio 1:
Algoritmo ordenar: 
Entrada: 
    t:LISTA #Lista ennumerada
Variables:
    t2:LISTA #Lista que inicialmente está vacía
    lista_intermedia: LISTA #Lista inicialmente vacía 
    a = t[0]
Precondicion: 
    t!=NULO
Realizacion:
    añadir t[0] a t2
    Para i en rango contar(t):
        comparar t[i] con los t2[n]
            cuando t[i]< que algún t2[j]
                entonces 
                    añadir 0 a lista 
                    en t2[j+1:] sustituir t2[x] por t2[x-1]
                    t2[j]:t[i]
                
#Nuestro código debería añadir t[0] a t2. 
# Comparar cada elemento de t con los n elementos de t2.
# Cuando el elemento "a" a comparar sea menor a algún elemento "x" de t2 entonces  añadimos 0 al final de la lista y desde la posición "x"+1 hasta el final
#cada elemento toma el valor del anterior 
# #por último X toma el valor de "a"
Postcondicion: 
en t2 t2[i]<t[i+1]
Resusltado lista t1 ordenada #es decir t2
#Teniendo en cuenta que el ejercicio no está hecho a código no podremos ejecurtarlo sin embargo al final de nuestra función deberíamos acabar con un "if __name__ ==__main__:
#                                                                                                                                                               ordenar)" Así
#igual que en el ejercicio prueba podríamos hacer que se ejecutase en el main si lo desemaos 

    
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
def ordenar_segmento(Lista, e,b):
    segmento = Lista[e:b]
    for i in range (len(segmento)-1):
        while segmento[i] < segmento [i+1]:
            if segmento[i] < segmento [i+1]:
                a = segmento[i+1]
                segmento[i+1] = segmento[i]
                segmento[i+1] =a
            return segmento
    Lista[e:b] = segmento
    m=segmento[0]
    print (m)
    return Lista
    
if __name__=="__main__":
    ordenar_segmento ()
# Explicación de lo que debería hacer nuestra función : 
#Al pasarle por parámetro una lista y las posiciones entre las que queremos variarla esta debería intercambiar los elementos en este invetervaloo si el elemento en posisición i+1 es mayor que elelemento en posición i
#Como nuestra función debe ejecutar este proceso hasta que todos los elementos de posición i+1 sean inferiores al de posición i como resultado obtendríamos una lista ordenada con los  elementosz del segmento indicado de nuestra lista principal
#Por último, esta debe de sustituir el segmento de la lista principal (indicado por los parámetros) por nuestro nuevo segmento donde los elementos se encuentran en orden decreciente
#A continuación guarda en la variable m el máximo de nuestro segmento
#Como resultado imprime el elemento de mayor valor del segmento y devuelve la lista con el segmento ordenado 
