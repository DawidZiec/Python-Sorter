def bucketSort(alist):
    largest = max(alist)
    length = len(alist)
    size = largest/length
 
    buckets = [[] for _ in range(length)] #tworzy kubelki rownej wielkosci i wypelnia je czesciami calej listy
    for i in range(length):               # w ich wlasnych zakresach
        j = int(alist[i]/size)
        if j != length:
            buckets[j].append(alist[i])
        else:
            buckets[length - 1].append(alist[i])
 
    for i in range(length): # sortuje poszczugolne kubelki
        insertion_sort(buckets[i])
 
    result = [] # laczy posortowane kubelki w posortowana liste
    for i in range(length):
        result = result + buckets[i]
 
    return result
 
def insertion_sort(alist): # insertion sort dla poszczegolnych kubelkow, nie ma tu rekurencji
    for i in range(1, len(alist)):
        temp = alist[i]
        j = i - 1
        while (j >= 0 and temp < alist[j]):
            alist[j + 1] = alist[j]
            j = j - 1
        alist[j + 1] = temp