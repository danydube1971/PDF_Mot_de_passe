# PDF_Mot_de_passe

Ce script permet de protéger un fichier PDF en le cryptant avec un mot de passe. 
Voici les étapes effectuées par le script :

1. Importation du module PyPDF2.
2. Demande à l'utilisateur d'entrer le nom du fichier PDF à protéger et le mot de passe à utiliser.
3. Ouverture du fichier PDF en mode lecture binaire ('rb') et création d'un objet PDFReader à l'aide de PyPDF2.
4. Vérification si le fichier PDF est déjà protégé par un mot de passe. Si c'est le cas, un message est imprimé à l'écran et le script s'arrête.
5. Création d'un objet PDFWriter à l'aide de PyPDF2 et copie de chaque page du PDF original.
6. Cryptage du PDF avec le mot de passe spécifié à l'aide de la méthode "encrypt" de l'objet PDFWriter.
7. Écriture du fichier PDF crypté sur le disque dur avec un nouveau nom de fichier qui commence par "secure_" pour indiquer qu'il est protégé.
8. Impression d'un message de confirmation à l'écran indiquant que le fichier PDF a été crypté avec succès avec le mot de passe spécifié.

Pour utiliser ce script, placez-le dans le même répertoire que le fichier PDF que vous voulez sécurisé.
Exécutez le script dans un terminal Linux avec la commande suivante :
**python3 "PDF_Mot_de_passe.py"**

Testé sous Linux Mint 21
