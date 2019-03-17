def bubbleSort(x):
    # wypisanie #1
    print(" ")
    print("Przed sortowaniem:")
    print(x)

    # sortowanie
    for j in range(len(x)-1, 0, -1):
        for k in range(j):
            if x[k] > x[k+1]:
                temp = x[k]
                x[k] = x[k+1]
                x[k+1] = temp

    # wypisanie #2
    print(" ")
    print("Po sortowaniu babelkowym:")
    print(x)
    print(" ")