# organ-donation-management 🍀
Platform for ethical organ donation and transplantation management

## **Prérequis 🤬**
Avant de commencer, assurez-vous d'avoir les outils suivants installés sur votre machine :
- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)

---

## **Étapes pour exécuter le projet**

### **1. Cloner le projet 🚀**
Clonez ce dépôt depuis GitHub :

```bash
git clone https://github.com/sagnolkamdem/organ-donation-management.git

cd organ-donation-management
```

### **2. Lancer le projet ⚡️**

Nb: Veuillez lancer votre application Docker avant de lancer le projet

```bash
docker compose up --build
```

### **3. N'oubliez pas de profiter de la vie 😎**
Nb: Ouvrez votre navigateur et lancez: ```localhost:4200```

![sfdgs](https://github.com/user-attachments/assets/5bf22d6f-4dda-4132-abca-6f7d72549167)


1. GET Donations

    Description: Permet de récupérer les informations sur les dons existants.
    Objectif: Afficher la liste de tous les dons ou récupérer les détails d'un don spécifique.
    Cas d'usage:
        Voir tous les dons enregistrés dans le système.
        Filtrer les dons par critères (date, type, donneur, etc.).
        Consulter les détails d'un don particulier (ex. un don d'organe avec ses informations spécifiques).

2. POST Donations

    Description: Permet de créer un nouveau don dans le système.
    Objectif: Ajouter un don fait par un utilisateur ou un donneur au système.
    Cas d'usage:
        Enregistrer un nouveau don.
        Associer les informations pertinentes, telles que :
            Le type de don (organes, sang, argent, etc.).
            Les informations du donneur (nom, coordonnées, etc.).
            Les détails spécifiques au don (quantité, conditions, date, etc.).

3. PUT Donations

    Description: Permet de mettre à jour les informations existantes d'un don.
    Objectif: Modifier un don déjà enregistré pour corriger ou ajouter des informations.
    Cas d'usage:
        Mettre à jour les détails d'un don (par exemple, changer la date de collecte).
        Corriger des erreurs (ex. une quantité incorrecte).
        Ajouter des informations complémentaires après un don (statut ou suivi).

4. DELETE Donation

    Description: Permet de supprimer un don spécifique du système.
    Objectif: Supprimer un don qui n'est plus pertinent ou qui a été ajouté par erreur.
    Cas d'usage:
        Retirer un don annulé.
        Nettoyer les données obsolètes du système.
        Gestion des cas d'erreurs (ex. suppression d'un enregistrement dupliqué).


---

## **Les membres du groupe 🧑🏽‍🎓**
- Hind KHAYATI (frontend - Dockerfile)
- Amira FATHALLA (backend - Dockerfile)
- Sagnol Boutal KAMDEM DJOKO (BD - Docker-compose)


