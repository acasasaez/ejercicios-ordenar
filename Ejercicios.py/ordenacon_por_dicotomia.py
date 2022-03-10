
def ordenar(a):
    nuevalista = [a[0]]
    for i in range (len(a)-1):
        if a[i] >nuevalista[0]:
            nuevalista.append(a[i])
        else:
            nuevalista[i+1] = nuevalista[i]
            nuevalista[0]=a[i]
        print (nuevalista)

ordenar ([1,5,8,3,7])