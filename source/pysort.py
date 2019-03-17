# program implementujacy sortowanie listy, real thing
import random
import bubble
import quick

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

if metoda == '1':
    # wypisanie #1
    print(" ")
    print("Przed sortowaniem:")
    print(x)

    bubble.bubbleSort(x)

    # wypisanie #2
    print(" ")
    print("Po sortowaniu babelkowym rosnaco:")
    print(x)
    print(" ")
    print("Po sortowaniu babelkowym malejaco:")
    x.reverse();
    print(x)

#########################################################################
#############################  QUICKSORT  ###############################
#########################################################################

else:
    # wypisanie #1
    print(" ")
    print("Przed sortowaniem:")
    print(x)

    quick.quickSort(x, 0, len(x)-1)

    # wypisanie #2
    print(" ")
    print("Po sortowaniu szybkim rosnaco:")
    print(x)
    print(" ")
    print("Po sortowaniu szybkim malejaco:")
    x.reverse();
    print(x)

# probowanie gita commita z konsoli