from unicodedata import name

def hola():
    lista=[1,2,3,4,5]
    segmento = lista[2:5]
    segmento[0] = 7
    lista[2:5] = segmento
    print (lista)

if __name__ == "__main__":
    hola()