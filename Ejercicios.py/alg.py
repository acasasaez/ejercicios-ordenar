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
