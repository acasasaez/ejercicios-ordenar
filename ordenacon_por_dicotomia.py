#¿Cómo afrontar el ejercicio de ordenación por dicotomía?
#Según he entendido ordenar por dicotomía consiste en ordenar crecientemente una lista
#para esto haremos lo siguiente 
# # primero definiré el algoritmo mínimo

Algoritmo minimo:
Entrada: 
    t: LISTA 
Precondición: 
    t !=0
Realización:
    si 
        t[0] < t[n]
    entoncesº
        devolver t[0]
    si no si 
        t[0] > t[i]
    entonces
        comprobar t[i]<t[n]
        devolver t[i]
    fin si 
Postcondicion
Resultado: ENTERO 

