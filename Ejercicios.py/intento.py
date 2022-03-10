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
    

ordenar_segmento ([5,3,2,7],1,4)
# Explicación de lo que debería hacer nuestra función : 
#Al pasarle por parámetro una lista y las posiciones entre las que queremos variarla esta debería intercambiar los elementos en este invetervaloo si el elemento en posisición i+1 es mayor que elelemento en posición i
#Como nuestra función debe ejecutar este proceso hasta que todos los elementos de posición i+1 sean inferiores al de posición i como resultado obtendríam os una lista ordenada 
