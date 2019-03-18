def bucketSort(x):
    largest = max(x)
    length = len(x)
    size = largest/length
 
    buckets = [[] for _ in range(length)] #tworzy kubelki rownej wielkosci i wypelnia je czesciami calej listy
    for i in range(length):               # w ich wlasnych zakresach
        j = int(x[i]/size)
        if j != length:
            buckets[j].append(x[i])
        else:
            buckets[length - 1].append(x[i])
 
    for i in range(length): # sortuje poszczugolne kubelki
        insertion_sort(buckets[i])
 
    wynik = [] # laczy posortowane kubelki w posortowana liste
    for i in range(length):
        wynik = wynik + buckets[i]
 
    return wynik
 
def insertion_sort(x): # insertion sort dla poszczegolnych kubelkow, nie ma tu rekurencji
    for i in range(1, len(x)):
        temp = x[i]
        j = i - 1
        while (j >= 0 and temp < x[j]):
            x[j + 1] = x[j]
            j = j - 1
        x[j + 1] = temp