def bubbleSort(x):
    
    # sortowanie
    for j in range(len(x)-1, 0, -1):
        for k in range(j):
            if x[k] > x[k+1]:
                temp = x[k]
                x[k] = x[k+1]
                x[k+1] = temp
