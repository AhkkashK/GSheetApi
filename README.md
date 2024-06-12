# Google Sheet Api et Analyse N-Gram

## Description

Ce projet a pour but de me familiariser avec l'environnement GCP et l'api Google Sheet. Ainsi dans ce projet vous retrouverez
vous comment s'est fait la connection à l'api et le chargement des données dans un sheet. D'autre part j'ai fait une ngram et extrait des insights. 


## Installation

1. Cloner le dépôt :
   ```bash
   git clone https://github.com/votre-nom-utilisateur/nom-de-votre-depot.git
   cd nom-de-votre-depot
   ```
   Sinon vous pouvez simplement télécharger le code.


2. Créer un environnement virtuel** :
   ```bash
   python -m venv myvenv
   source myvenv/bin/activate  

Il faudra activer l'env virtuel en fonction de votre os.

  puis lancez cette commande : 
    
    pip install -r requirements.txt


## Création du projet GCP

1. Créez un projet sur Google Cloud Platform.
2. Activez l'API Google Sheets et l'API Google Drive dans votre projet.
3. Créez des identifiants pour un compte de service et téléchargez le fichier (le renommer :credentials.json) .


## Utilisation 


Vous trouverez un fichier main.py qui regroupe tout le code.

Explication des fonctions : 
 
connect_to_googlea_api : se connecte à l'api google sheet à l'aide de votre fichier credentials.json se trouvant dans votre projet.

clean_data : fait un nettoyage du texte pour faire une analyse nngram plus tard. Prend en entrée un string.

ngram_generator : génère des ngram en donnant en entrée un string et un int (qui est votre n).

ngram_analysis : retourne les ngram les plus fréquents à l'aide des deux fonctions précédentes. J'ai mis en commentaire les insights que j'ai pu trouvé.

df_to_sheet : charge une dataframe sur un fichier google sheet spécifique. Prend en entrée le workbook, le titre du sheet, les lignes et colonnes.

main : programme principal qui fera la connection à l'api, l'analyse ngram et le chargement des données. A noter que la variable sheet_id devra être modifier selon l'id de votre fichier google sheet.
   
