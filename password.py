#import random
#import secrets
import json
import hashlib

#nombres_caracteres = 8
#majuscule = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#minuscule = "abcdefghijklmnopqrstuvwxyz"
#chiffre = "0123456789"
caractere_special = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+']


def caractere_speciaux(mot_de_passe): # Vérifie si le mot de passe contient un caractère spécial
    global caractere_special # Permet d'utiliser la variable caractere_special qui est en dehors de la fonction
    for index in caractere_special: # Pour chaque caractère spécial dans la liste caractere_special 
        if index in mot_de_passe: # Si le caractère spécial est dans le mot de passe
            return True # Retourne True si le mot de passe contient un caractère spécial 
    return False # Retourne False si le mot de passe ne contient pas de caractère spécial

def mdp(new_mdp):
    while True:
        
        if len(new_mdp) < 8:
            print("Votre mot de passe doit contenir au moins huit caractères")
        
        elif new_mdp.islower(): # Si le mot de passe contient que des lettres minuscules # islower() est une fonction qui permet de vérifier si le mot de passe contient que des lettres minuscules
            print("Votre mot de passe contient que des lettres minuscules, il ne respecte pas les conditions")
        
        elif new_mdp.isupper():
            print("Votre mot de passe contient que des lettres majuscules, il ne respecte pas les conditions")
        
        elif new_mdp.isdigit():
            print("Votre mot de passe contient que des nombres, il ne respecte pas les conditions")
        
        elif new_mdp.isalpha():
            print("Votre mot de passe contient que des lettres, il ne respecte pas les conditions")
        
        elif caractere_speciaux(new_mdp) == False: # Si la fonction caractere_speciaux retourne False
            print("Votre mot de passe doit contenir au moins un caractère spécial !, @, #, $, %, ^, &, * ")
        
        else:
            h = hashlib.sha256(mot_de_passe.encode()).hexdigest()# Cryptage du mot de passe avec la fonction sha256 de la librairie hashlib # Conversion du mot de passe en hexadecimal # Stockage du mot de passe crypté dans la variable h
            with open("password.json", "a") as fichier: # Ouverture du fichier password.json en mode écriture
                json.dump(h, fichier) # Ecriture du mot de passe crypté dans le fichier password.json
                fichier.write("\n") # Ecriture d'un retour à la ligne dans le fichier password.json
            print(f"Votre mot de passe '{new_mdp}' est valide")
            print("Cryptage du mot de passe...")
            print(f"Mot de passe crypté: \n{h}")
            print("Mot de passe crypté enregistré dans le fichier password.json")

            return True
        
        new_mdp = input("écrire un mot de passe valide : ")

mot_de_passe = input("Votre mot de passe doit contenir: \n-au moins huit caractères \n-au moins une majuscule \n-au moins une minuscule \n-au moins un chiffre \n-au moins un caractère spécial(!, @, #, $, %, ^, &, *) \nEntrez un mot de passe : ")

mdp(mot_de_passe)  