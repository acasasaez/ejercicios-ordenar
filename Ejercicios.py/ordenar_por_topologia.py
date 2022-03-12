from argparse import _VersionAction
from mailbox import NoSuchMailboxError


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