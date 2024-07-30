# Depot entrainement git

## On est là pour se faire des coups de pute !!
ohhh yeah

## **Création de Branche**

Dans une soucis d'uniformité de travail, voici les process.  
Nommage de branche:   
```Nom-de-Ticket_description-efficace-et-rapide-du changement```    
Depuis la branche main afin d'être à jour :   
```git pull```
```git checkout -b <nom_branche>```

Exemple de nom de commande:
```git checkout -b MG-2501_add-database-connexion```   

## **Commit sur branche de travail**
Depot standart   
```git add <fichier>```    
```git commit -m "Nom-de-Ticket_description-efficace-et-rapide-du changement"```   
d'où l'importance de bien choisir le nom de ticket/branche.   
```git push```    

## Depot complémentaire
Vous avez déjà un commit mais vous avez des changements à ajouter.    
```git add <fichier>```     
```git commit --amend```    
la console qui va s'ouvrir va vous permettre de changer le nom de commit si besoin.   
sinon vous sortez de la console avec ```:wq```   
```git push```   

## **Code review**

Sur l'interface de github    
Cliquer create merge request    
SUR code_review    
- Mettre le lien https de github avec la demande de merge    
- Une description du changement apporté dans le ticket. Le but est de facilité la review pour l'autre.   
NB: plus la review est propre et simple plus c'est facile pour l'autre de review.    
- un ```@back``` ou ```@front``` ou ```@nom_de_collègue``` afin d'interpeler les bonnes personnes.     
ATTENTION la review est devenue bloquante.    

## **Rebase avant de merge vers main**

Mettre à jour main.   
```git checkout main```   
```git pull```   
Puis mettre à jour votre branche.    
```git checkout <branche>```    
```git rebase main```   
Résoudre les conflits si besoin.   
```git push```  

Il se peut que vous ayez besoin de force le push à cause de votre MR si tel est le cas merce de saisir.    
```git push --force-with-lease``` 

# Process de RELEASE GIT sur staging :
Une fois la branch faite, le boulot fait et la demande de PR acceptée ...
clicker sur valider la merge sur le site de github
sur le terminal depot aive : sur la branch main ->
```git pull ```
(car le merge de github est fait fait seulement en distant donc il faut mettre à jour en local)
sur main saisir (pour créer les tags de version)
```tools/auto-tag <type> <api> ```
exemple : ```tools/auto minor graphq-api workspace-api```
pour créer des tags mineurs sur graphql et workspace
pour mettre à jour les tags en distant cette fois.
```git push --tags```
Contrôler la construction des images docker en allant sur github -> actions -> ça doit passer au vert !!
Ensuite faire le message sur release staging de slack avec un contenue de type
```Release de <nom de ticket>```
```-<api>v<numero de version>```
exemple :
```Release de  https://aive.atlassian.net/browse/PF-5682```
```-graphql-api-v101.5.0```
```-platform-app-v23.4.0```
On obtient les liens en copiant depuis jira le copy link to issue et pour les version depuis github dans actions ce qui doit être vert
Ensuite on passe au dépot slack
mettre à jour les versions dans le fichier pour les app concernées
fichier concerné k8s/staging/services/kustomization.yaml
dans la console (main) :
```kubectl diff -k k8s/staging/services```
Pour controler les différences et qu'il n'y ait pas autre chose que ce que tu veux
pour appliquer cette nouvelle version
```kubectl apply -k k8s/staging/services```
afin de controler que tout ce soit bien passé et que tes pods se sont bien relancés
```kubectl get pod```
Là tu controles que ceux que tu as refait ont une durée de vie cohérente et se soient bien lancés.
(presque optionnel) controler sur google : app.staging.aive.com que tout aille bien
si ça semble ok on peut passer à la suite
Sur le terminal en depot slack (main)
```git status```
```git add -u```
```git commit -m "<numero-ticket app-version app-version>"```
```git push```
exemple de commit :
```git commit -m "PF-5682 graphql-api-v101.5.0 platform-app-v23.4.0"```
slack (main) : (ouais juste au cas où)
```git pull ```
retour sur aive (main)
```git pull```
afin de mettre tout à jour (edited) 