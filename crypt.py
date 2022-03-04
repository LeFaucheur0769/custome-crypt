# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 11:05:55 2021

@author: Bruno Meslin
"""
# J'ouvre le fichier et sauvegarde les deux colonnes sous les noms "col1" pour 
# les lettres et "col2" pour le codage associé. Afin d'avoir accès à chaque lettre,
# je peux les utiliser comme un tableau ou une liste tel que col1[0] tapé dans
# la console donne 'a' par exemple.

# Ouverture clé de codage
import csv
import re
fichier_csv = open("phython.csv", "r",encoding='utf-8-sig')
csv = csv.reader(fichier_csv, delimiter=";")


col1 = []
col2 = []
for ligne in csv :
    col1.append(ligne[0])
    col2.append(ligne[1])
fichier_csv.close ()

# print("Clé de codage et décodage:\n")
# print("Lettres :\n",col1)
# print("Symboles :\n",col2)

# Ouverture et affichage du texte à coder
# print("\n Texte à coder :\n",lignes)





crypt=[]
if len(col1)== len(col2):
    None
else:
    print("Erreur, pas assez de caractères codés")
    StopIteration
end = ""
def crypter ():
    hello = ""
    end = ""
    i = ""
    k = ""
    hello = input("Veuillez écrire votre texte à crypter : ")
    for i in range(len(hello)):
        for k in range(len(col1)):
            if col1[k] == hello[i]:
                crypt.append(col2[k])
            else:
                    None
    end = " ".join(crypt)
# end = re.sub(" ","",end)
    print(end)
    return end
uncrypt=[]
def decrypt():
    utilisateurInuot = input("veuillez écrire le texte à décrypter : ")
    utilisateurInuot = utilisateurInuot.split()
    for i in range(len(utilisateurInuot)):
        for k in range(len(col2)):
            if col2[k] == utilisateurInuot[i]:
                uncrypt.append(col1[k])
            else:
                    None
    enduncrypt = " ".join(uncrypt)

    print(enduncrypt)
cryptOrDecrypt = True
print(chr(27) + "[2J")
while cryptOrDecrypt == True :
    cryptDecrypt = input("pour crypter /c/, pour décrypter /d/ et /q/ pour quitter : ")
    if(cryptDecrypt == "c" or cryptDecrypt == "C"):
        end = ""
        crypt = []
        crypter()
    elif(cryptDecrypt == "d" or cryptDecrypt == "D"):
        uncrypt = []
        decrypt()
    elif(cryptDecrypt == "q" or cryptDecrypt == "Q"):
        cryptOrDecrypt = False
    else:
        print("Veuillez ecrire quelque chose de valide")

        






        

# col1 = ['h','H','o','l','e',' ','w','d','r']
# col2 = ['1','2','3','4','#','ty','?','q','pynje']
