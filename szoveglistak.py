"""Hány Alma/alma van a listában"""
def kisalma_nagyalma(szoveg_lista):
    print("1. feladat")
    db: int = 0
    for i in range(0, len(szoveg_lista), 1):
        if szoveg_lista[i] == "Alma" or szoveg_lista[i] == "alma":
            db += 1
    return db
"""Hány Sz betűvel kezdődő szöveg van a listában?"""
def sz_betu(szoveg_lista):
    print("2. feladat")
    db: int = 0
    for i in range(0, len(szoveg_lista), 1):
        if szoveg_lista[i][0: 2] == "Sz":
            db += 1
    return db
"""Melyik a leghosszabb szó? Mekkora a hossza? Hányadik helyen áll a listában?"""
def leghosszabb(szoveg_lista):
    print("3. feladat")
    max: str = 0
    for i in range(0, len(szoveg_lista), 1):
        