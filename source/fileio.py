import os

def loadFile(workfile):
    with open(workfile) as f:
        dane = f.read()
        return dane

def saveFile(nazwapliku, lista, kier):
    export = str(lista)
    with open(nazwapliku, 'a') as pp:
        #if os.path.isfile(nazwapliku) == True: // mialo testowac czy plik istnieje i dodwan \n jesli tak
            #pp.write("\n")                     // ale nie dziala dobrze
        pp.write(export)
        if kier == 'd':
            pp.write("\n")
            lista.reverse()
            export2 = str(lista)
            pp.write(export2)