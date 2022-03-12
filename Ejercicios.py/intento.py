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
