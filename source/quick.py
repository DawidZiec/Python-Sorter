def partition(x, p, r): # dzieli liste na dwie rowne czesci, lewa mniejsza od punktu podzialu, prawa wieksza
    a = x[p] #obiera a
    i = p
    j = r # i, j - indeksy w liscie

    while True: # petla nieskonczona, wylazi z niej return
        while x[j] > a:
            j = j - 1
        while x[i] < a:
            i = i + 1
        if i < j: # gdy i < j zamieniamy je miejscami
            temp = x[i]
            x[i] = x[j]
            x[j] = temp
            i = i + 1
            j = j - 1
        else: # gdy i >= j zwracamy j jako podzial
            return j

def quickSort(x, p, r):

    if p < r:
        q = partition(x, p, r) # dzieli liste na dwie czesci, q to punkt podzialu
        quickSort(x, p, q)     # rekurencyjnie quickSort dla pierwszej czesci
        quickSort(x, q+1, r)   #rekurencyjnie quickSort dla drugiej czesci
