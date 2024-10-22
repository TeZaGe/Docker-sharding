
# Docker-Sharding

## Création d'un réseau de serveurs MongoDB sur Docker 
- 2 routeurs
- 3 serveurs principaux (principal_a, principal_b, principal_c)
- Chaque serveur principal possède 3 serveurs secondaires (réplicas)

## Fonctionnement du projet

### Démarrer les services Docker

```bash
docker-compose up -d
```

### Lancer le script Python 

```bash
python3 script.py # ou simplement exécuter le fichier script.py
```

### Exécuter le script de test pour réaliser les requêtes sur la bd

```bash
python3 test.py # ou simplement exécuter le fichier test.py
```

## Quelques précisions 

L'erreur suivante :
```bash
MongoServerError[AlreadyInitialized]: already initialized
```
ne bloque pas l'utilisation du réseau. Cela signifie simplement que le fichier `script.py` a déjà été exécuté auparavant.

De même, l'erreur suivante :
```bash
MongoServerError[Location51003]: User "MYUSERNAME@test" already exists
```
n'est pas bloquante et n'empêche pas le bon fonctionnement du projet.
