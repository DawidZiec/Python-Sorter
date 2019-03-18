# Kopcowanie drzewka pod indeksem i. 
# n to rozmiar kopca 
def heapify(x, n, i): 
    largest = i # Najwieksza wartosc to korzen 
    l = 2 * i + 1     # lewo = 2*i + 1 
    r = 2 * i + 2     # prawo = 2*i + 2 
  
    # Sprawdzenie, czy lewa galaz istanieje i jest wieksza niz korzen 
    # 
    if l < n and x[i] < x[l]: 
        largest = l 
  
    # Sprawdzenie, czy prawa galaz isnieje i jest wieksza niz korzen 
    # 
    if r < n and x[largest] < x[r]: 
        largest = r 
  
    # Zmiana korzenia, jesli jest taka potrzeba 
    if largest != i: 
        x[i],x[largest] = x[largest],x[i] # zamiana 
  
        # Kopcowanie korzenia 
        heapify(x, n, largest) 
  
# Glowna funkcja sortujaca 
def heapSort(x): 
    n = len(x) 
  
    # Tworzenie najwiekszego kopca
    for i in range(n, -1, -1): 
        heapify(x, n, i) 
  
    # Pojedyncze wypakowywanie elementow
    for i in range(n-1, 0, -1): 
        x[i], x[0] = x[0], x[i] # zamiana 
        heapify(x, i, 0) 