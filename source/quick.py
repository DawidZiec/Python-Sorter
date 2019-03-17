def partition(lista, p, r): # dzieli liste na dwie rowne czesci, lewa mniejsza od punktu podzialu, prawa wieksza
    a = lista[p] #obiera a
    i = p
    j = r # i, j - indeksy w liscie

    while True: # petla nieskonczona, wylazi z niej return
        while lista[j] > a:
            j = j - 1
        while lista[i] < a:
            i = i + 1
        if i < j: # gdy i < j zamieniamy je miejscami
            temp = lista[i]
            lista[i] = lista[j]
            lista[j] = temp
            i = i + 1
            j = j - 1
        else: # gdy i >= j zwracamy j jako podzial
            return j

def quickSort(lista, p, r):

    if p < r:
        q = partition(lista, p, r) # dzieli liste na dwie czesci, q to punkt podzialu
        quickSort(lista, p, q)     # rekurencyjnie quickSort dla pierwszej czesci
        quickSort(lista, q+1, r)   #rekurencyjnie quickSort dla drugiej czesci

