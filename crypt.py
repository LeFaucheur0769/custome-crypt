# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 11:05:55 2021

@author: Bruno Meslin
"""
# J'ouvre le fichier et sauvegarde les deux colonnes sous les noms "col1" pour 
# les lettres et "col2" pour le codage associé. Afin d'avoir accès à chaque lettre,
# je peux les utiliser comme un tableau ou une liste tel que col1[0] tapé dans
# la console donne 'a' par exemple.

import numpy as np
# Ouverture clé de codage
import csv
import re
col1 = []
col2 = []
with open("phython.csv", "r", newline='') as fichier_csv:
    fichierForRead = csv.reader(fichier_csv)
    hello = "hello world"


    for ligne in fichierForRead :
        col1.append(ligne[0])
        col2.append(ligne[1])
    fichier_csv.close ()

# print("Clé de codage et décodage:\n")
# print("Lettres :\n",col1)
# print("Symboles :\n",col2)

# Ouverture et affichage du texte à coder
texte = open("texte.txt", "r")
lignes = texte.readlines()
# print("\n Texte à coder :\n",lignes)


def crypter ():
    for i in range(len(hello)):
        for k in range(len(col1)):
            if col1[k] == hello[i]:
                crypt.append(col2[k])
            else:
                    None
    end = " ".join(crypt)
    print(end)
    return
uncrypt=[]
helloend = end.split()
def decrypt():
    for i in range(len(helloend)):
        for k in range(len(col2)):
            if col2[k] == helloend[i]:
                uncrypt.append(col1[k])
            else:
                    None
    enduncrypt = " ".join(uncrypt)

    print(enduncrypt)


crypt_or_decrypt = input("Pour crypter : c pour décrypter : d : ")
encore = True
while encore == True:
        if crypt_or_decrypt == "c":
            crypter()
            encore = False
        elif crypt_or_decrypt == "d":
            decrypt()
            encore = False


crypt=[]
if len(col1)== len(col2):
    None
else:
    print("Erreur, pas assez de caractères codés")
    StopIteration
end = ""

# end = re.sub(" ","",end)
    

crypter()
decrypt()
        






        

# col1 = ['h','H','o','l','e',' ','w','d','r']
# col2 = ['1','2','3','4','#','ty','?','q','pynje']
