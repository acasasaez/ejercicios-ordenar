
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
    m= lista[b-1]
    
    return lista,m
print (intercambio_segmento([18,20,12,1,3,4,6,7,8],2,7))



