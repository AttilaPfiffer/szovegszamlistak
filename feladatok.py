import random
import math


"""Írd ki a képernyőre a lista elemeit
Írj metódust amely a paraméterében kapott lista elemeit kiírja a képernyőre"""
def kiiratas(szam_lista):
    for i in range(0, len(szam_lista), 1):
        print(f"{i}. eleme: {szam_lista[i]}")




"""1. Mennyi a pozitív számok összege? (Összegzés tétele)"""
def poz_osszeg(szam_lista):
    print("1. feladat")
    osszeg:int = 0
    for i in range(0, len(szam_lista), 1):
        if szam_lista[i] > 0:
            osszeg += szam_lista[i]
    return osszeg


"""2. Hány negatív szám van? (Megszámlálás tétele)"""
def hany_negativ(szam_lista):
    print("2. feladat")
    db:int = 0
    for i in range(0, len(szam_lista), 1):
        if szam_lista[i] < 0:
            db += 1
    return db

"""3. Hány nem egész szám van a számok között? (Megszámlálás tétele)"""
def nem_egesz(szam_lista):
    print("3. feladat")
    db: int = 0
    for i in range(0, len(szam_lista), 1):
        if round(szam_lista[i]) != szam_lista[i]:
            db += 1
    return db


"""4. Mennyi a hárommal osztható számok átlaga? (Összegzés tétele)"""
def harommal_oszthato(szam_lista):
    print("4. feladat")
    atlag: int = 0
    osztas: int = 0
    for i in range(0, len(szam_lista), 1):
        if szam_lista[i] % 3 == 0:
            osztas += szam_lista[i]
            atlag += 1
    return(osztas / atlag)

"""5. Mekkora a legnagyobb szám? (Maximum kiválasztás tétele)"""
def legnagyobb_szam(szam_lista):
    print("5. feladat")
    max: int = szam_lista[0]
    for i in range(0, len(szam_lista), 1):
        if szam_lista[i] > max:
            max = szam_lista[i]
    return max

"""6. Mekkora a legkisebb szám? (Maximum kiválasztás tétele)"""
def legkisebb_szam(szam_lista):
    print("6. feladat")
    min: int = szam_lista[0]
    for i in range(0, len(szam_lista), 1):
        if szam_lista[i] < min:
            min = szam_lista[i]
    return min

"""7. Mekkora a legkisebb és a legnagyobb szám különbsége? """
def legkisebb_legnagyobb(szam_lista):
    print("7. feladat")
    max: int = szam_lista[0]
    min: int = szam_lista[0]
    for i in range(0, len(szam_lista), 1):
        if szam_lista[i] < min:
            min = szam_lista[i]
        elif szam_lista[i] > max:
            max = szam_lista[i]
    return(max - min)