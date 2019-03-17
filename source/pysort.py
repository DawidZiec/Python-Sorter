# program implementujacy sortowanie listy, real thing
import random

print(" ")
print('''Witaj w pythonowym sorterze!
Dzieki niemu mozesz dokonac sortowania wybrana metoda wpisanych przez Ciebie lub losowych liczb.
Pamietaj, aby zakonczyc dzialanie apliacji wczesniej, uzyj skrotu ctrl+Z i zatwierdz enterem''')
print(" ")

metoda = '0'
# wybor: metoda sortowania
while metoda != '1' and metoda != '2' and metoda != '3' and metoda != '4' and metoda != '5':
    print("Jakiego algorytmu sortowania chcesz uzyc?")
    print("1 - babelkowe, 2 - szybkie, 3 - kubelkowe, 4 - przez scalanie, 5 - kopcowe")
    metoda = input()

print(" ")

wybor = 'z'
# wybor: wlasne liczby, lub losowe
while wybor != 'w' and wybor != 'l':
    print("Czy chcesz wprowadzic wlasne liczby do posortowania, czy posortowac losowe?")
    print("w - wlasne, l - losowe")
    wybor = input()

print(" ")

if wybor == 'l':
    # wczytanie rozmiaru listy od uzytkownika
    print("Podaj rozmiar listy do posortowania:")
    rozmiar = int(input())
    x = []
    # losowe wypelnienie listy
    for i in range(rozmiar):
        x.append(random.randrange(1000))

if wybor == 'w':
    # uzytkownik wypelnia liste
    print("Wypisz liczby, oddzielajac je spacjami")
    x = [int(x) for x in input().split()]

#########################################################################
##########################  BUBBLE SORT  ################################
#########################################################################

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
print("Po sortowaniu:")
print(x)
print(" ")

#########################################################################
#############################  QUICKSORT  ###############################
#########################################################################
