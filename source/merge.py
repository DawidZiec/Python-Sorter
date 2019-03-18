def mergeSort(arr): 
    if len(arr) >1: 
        mid = len(arr)//2 # Okreslenie srodka listy 
        L = arr[:mid] # Podzielenie listy na pol
        R = arr[mid:]
  
        mergeSort(L) # Sortowanie pierwszej polowki 
        mergeSort(R) # Sortowanie drugiej polowki
  
        i = j = k = 0
          
        # Kopiowanie danych z tymczsaowych list L[] i R[] 
        while i < len(L) and j < len(R): 
            if L[i] < R[j]: 
                arr[k] = L[i] 
                i+=1
            else: 
                arr[k] = R[j] 
                j+=1
            k+=1
          
        # Sprawdzanie, czy zaden element nie zostal bez przypisania
        while i < len(L): 
            arr[k] = L[i] 
            i+=1
            k+=1
          
        while j < len(R): 
            arr[k] = R[j] 
            j+=1
            k+=1