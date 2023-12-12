import json
import hashlib

chemin = r'C:\Users\rijar\Desktop\Ecole_Laplateforme\Projet\password\password\password.json'

def caractere_speciaux(mot_de_passe):
    caractere_special = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '+']
    for index in caractere_special:
        if index in mot_de_passe:
            return True
    return False

def saisir_mot_de_passe():
    passwords = []  # Liste pour stocker les mots de passe cryptés
    
    while True:
        new_mdp = input("Entrez un mot de passe : ")
        
        if len(new_mdp) < 8:
            print("Votre mot de passe doit contenir au moins huit caractères")
        # Autres conditions pour vérifier les majuscules, minuscules, chiffres et caractères spéciaux
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
            if caractere_speciaux(new_mdp) == False:
                print("Votre mot de passe doit contenir au moins un caractère spécial")
            else:
                h = hashlib.sha256(new_mdp.encode()).hexdigest()
                passwords.append(h)  # Ajouter le hachage à la liste des mots de passe
                
                print(f"Votre mot de passe '{new_mdp}' est valide")
                print("Cryptage du mot de passe...")
                print(f"Mot de passe crypté: \n{h}")
                
                sauvegarder_mots_de_passe(passwords)  # Enregistrer la liste mise à jour dans le fichier JSON
                break

def sauvegarder_mots_de_passe(passwords):
    with open(chemin, "w") as fichier:
        json.dump(passwords, fichier)
        print("Mots de passe cryptés enregistrés dans le fichier password.json")

def afficher_mots_de_passe():
    with open(chemin, "r") as fichier:
        print(f"Mots de passe cryptés : {json.load(fichier)}")

saisir_mot_de_passe()
afficher_mots_de_passe()
