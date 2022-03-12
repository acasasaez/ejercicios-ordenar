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

    
