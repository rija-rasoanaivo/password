#import secrets
import json
import hashlib
import random

#nombres_caracteres = 8

caractere_special = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+']
chemin = 'password.json'

def caractere_speciaux(mot_de_passe): # Vérifie si le mot de passe contient un caractère spécial
    global caractere_special # Permet d'utiliser la variable caractere_special qui est en dehors de la fonction
    for index in caractere_special: # Pour chaque caractère spécial dans la liste caractere_special 
        if index in mot_de_passe: # Si le caractère spécial est dans le mot de passe
            return True # Retourne True si le mot de passe contient un caractère spécial 
    return False # Retourne False si le mot de passe ne contient pas de caractère spécial

def mdp(new_mdp=None): # Fonction principale  
    global chemin
    
    while True: #On entre dans la boucle
        if new_mdp is None:
            new_mdp = input("Entrez votre mot de passe : ")

        if len(new_mdp) < 8:
            print("Votre mot de passe doit contenir au moins huit caractères")
        
        elif new_mdp.islower():
            print("Votre mot de passe contient que des lettres minuscules, il ne respecte pas les conditions")
        
        elif new_mdp.isupper():
            print("Votre mot de passe contient que des lettres majuscules, il ne respecte pas les conditions")
        
        elif new_mdp.isdigit():
            print("Votre mot de passe contient que des nombres, il ne respecte pas les conditions")
        
        elif new_mdp.isalpha():
            print("Votre mot de passe contient que des lettres, il ne respecte pas les conditions")
        
        elif not caractere_speciaux(new_mdp):
            print("Votre mot de passe doit contenir au moins un caractère spécial parmi !, @, #, $, %, ^, &, * ")
        
        else:
            nom_mot_de_passe = input("Entrez un nom pour ce mot de passe : ")  # Demander le nom du mot de passe
            
            h = hashlib.sha256(new_mdp.encode()).hexdigest()  # Calculer le hachage du mot de passe

            mot_de_passe_info = {"nom": nom_mot_de_passe, "mot_de_passe_hache": h}  # Stocker le nom et le hachage du mot de passe

            with open(chemin, "r") as fichier: # Ouverture du fichier password.json en mode lecture
                try:
                    liste = json.load(fichier) # Charger le contenu du fichier password.json dans la variable liste
                except json.decoder.JSONDecodeError: # json.decoder.JSONDecodeError est une exception qui est levée lorsque le décodage JSON échoue
                    liste = []
                           
            liste.append(mot_de_passe_info)  # Ajouter le mot de passe haché avec son nom dans la liste
            with open(chemin, "w") as fichier:
                json.dump(liste, fichier, indent=3) #indent=3 permet d'indenter le fichier json pour une meilleure lisibilité
            
            print("Votre mot de passe est valide")
            print("Cryptage du mot de passe...")
            print("Mot de passe haché enregistré dans le fichier password.json avec le nom associé")
            afficher_mdp()
            mdp_aleatoire()
            ajouter_autre_mdp() 
              
            return True
        new_mdp = input("Ecrire un mot de passe valide : ")
             
def afficher_mdp(): # Fonction qui permet d'afficher le mot de passe crypté
    reponse = input("Voulez-vous afficher le mot de passe crypté ? (Oui/Non) : ")
    if reponse == "Oui" or reponse == "oui" or reponse == "OUI" or reponse == "O" or reponse == "o":
        with open(chemin, "r") as fichier:
            print(fichier.read())
    else:
        print("Mot de passe crypté non affiché")

def ajouter_autre_mdp(): # Fonction qui permet d'ajouter un autre mot de passe
    reponse = input("Voulez-vous ajouter un autre mot de passe ? (Oui/Non) : ")
    if reponse == "Oui" or reponse == "oui" or reponse == "OUI" or reponse == "O" or reponse == "o":
        mdp()
    else:
        print("D'accord")

def mdp_aleatoire(): # Fonction qui permet de générer un mot de passe aléatoire
    majuscule = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    minuscule = "abcdefghijklmnopqrstuvwxyz"
    chiffre = "0123456789"
    caractere_special = "!@#$%^&*()_+"
    mot_de_passe = ""
    reponse = input("Voulez-vous générer un mot de passe aléatoire ? (Oui/Non) : ")
    if reponse == "Oui" or reponse == "oui" or reponse == "OUI" or reponse == "O" or reponse == "o":
        for i in range(15):
            mot_de_passe += random.choice(majuscule + minuscule + chiffre + caractere_special)
        print("Voici votre mot de passe aléatoire : ", mot_de_passe)
        
        nom_mot_de_passe = input("Entrez un nom pour ce mot de passe : ")
        
        h = hashlib.sha256(mot_de_passe.encode()).hexdigest() # Cryptage du mot de passe avec la fonction sha256 de la librairie hashlib # Conversion du mot de passe en hexadecimal # Stockage du mot de passe crypté dans la variable h
        
        mot_de_passe_info = {"nom": nom_mot_de_passe, "mot_de_passe_hache": h}
        
        with open(chemin, "r") as fichier:
            try:
                liste = json.load(fichier)
            except json.decoder.JSONDecodeError:
                liste = []
                        
        liste.append(mot_de_passe_info) # Ajout du mot de passe crypté dans la liste
        with open(chemin, "w") as fichier: # Ouverture du fichier password.json en mode ajout # Si le fichier n'existe pas, il sera créé automatiquement
            json.dump(liste, fichier, indent=3) # Ecriture du mot de passe crypté dans le fichier password.json
            
        return mot_de_passe
    else:
        print("D'accord")
        return reponse

mot_de_passe = input("Votre mot de passe doit contenir :\n- au moins huit caractères\n- au moins une majuscule\n- au moins une minuscule\n- au moins un chiffre\n- au moins un caractère spécial (!, @, #, $, %, ^, &, *)\nEntrez un mot de passe : ")

mdp(mot_de_passe)
