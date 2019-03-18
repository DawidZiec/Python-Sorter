def mergeSort(x): 
    if len(x) >1: 
        middle = len(x)//2 # Okreslenie srodka listy 
        left = x[:middle] # Podzielenie listy na pol
        right = x[middle:]
  
        mergeSort(left) # Sortowanie pierwszej polowki 
        mergeSort(right) # Sortowanie drugiej polowki
  
        i = j = k = 0
          
        # Kopiowanie danych z tymczsaowych list left[] i right[] 
        while i < len(left) and j < len(right): 
            if left[i] < right[j]: 
                x[k] = left[i] 
                i+=1
            else: 
                x[k] = right[j] 
                j+=1
            k+=1
          
        # Sprawdzanie, czy zaden element nie zostal bez przypisania
        while i < len(left): 
            x[k] = left[i] 
            i+=1
            k+=1
          
        while j < len(right): 
            x[k] = right[j] 
            j+=1
            k+=1