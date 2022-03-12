
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


j