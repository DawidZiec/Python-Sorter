def loadFile(workfile):
    with open(workfile) as f:
        dane = f.read()
        return dane