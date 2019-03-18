# Kopcowanie drzewka pod indeksem i. 
# n to rozmiar kopca 
def heapify(arr, n, i): 
    largest = i # Najwieksza wartosc to korzen 
    l = 2 * i + 1     # lewo = 2*i + 1 
    r = 2 * i + 2     # prawo = 2*i + 2 
  
    # Sprawdzenie, czy lewa galaz istanieje i jest wieksza niz korzen 
    # 
    if l < n and arr[i] < arr[l]: 
        largest = l 
  
    # Sprawdzenie, czy prawa galaz isnieje i jest wieksza niz korzen 
    # 
    if r < n and arr[largest] < arr[r]: 
        largest = r 
  
    # Zmiana korzenia, jesli jest taka potrzeba 
    if largest != i: 
        arr[i],arr[largest] = arr[largest],arr[i] # zamiana 
  
        # Kopcowanie korzenia 
        heapify(arr, n, largest) 
  
# Glowna funkcja sortujaca 
def heapSort(arr): 
    n = len(arr) 
  
    # Tworzenie najwiekszego kopca
    for i in range(n, -1, -1): 
        heapify(arr, n, i) 
  
    # Pojedyncze wypakowywanie elementow
    for i in range(n-1, 0, -1): 
        arr[i], arr[0] = arr[0], arr[i] # zamiana 
        heapify(arr, i, 0) 