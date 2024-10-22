import pymongo
import json
import queries  # Assumed this is a custom module you have
mongodb_uri = 'mongodb://MYUSERNAME:MYPASSWORD@localhost:27018/?authSource=test'

# jeu de données books.json

cur_query = []

try:
    client = pymongo.MongoClient(mongodb_uri)

    with open("books.json") as f:
        file_data = json.load(f)

    bd = client["bd"]
    books = bd.get_collection("books")

    # Insertion des données
    if "books" not in bd.list_collection_names():
        insertion_books = books.insert_many(file_data)
        cur_query.append({"Insertion": insertion_books.inserted_ids})
    else:
        print("La collection existe déjà")
        cur_query.append("La collection books existe déjà")

    # Get the informations about the shards - sharding
    print("### --- On récupère les informations sur les shards avec la commande sh.status() --- ###")
    informations_shards = client["admin"].command('listShards')
    cur_query.append({"Shards Info": informations_shards})

    for shard in informations_shards["shards"]:
        print(shard)

    print("### ---- On récupère les informations sur les collections --- ###")
    collections = bd.list_collection_names()
    cur_query.append({"Collections": collections})
    for collection in collections:
        print(collection)

    print("### --- Affichage de la collection books --- ###")
    books_entries = list(books.find())  # Convert cursor to list to store results
    cur_query.append({"Books": books_entries})
    for book in books_entries:
        print(book)

    # Lecture d'une collection spécifique
    print("### --- Read collection --- ###")
    books_entries = list(books.find({"title": "The Catcher in the Rye - J.D. Salinger"}))  # Convert to list
    cur_query.append({"Filtered Books": books_entries})
    for book in books_entries:
        print(book)

except pymongo.errors.ConnectionFailure as e:
    print(f"Erreur de connexion: {e}")
    cur_query.append({"ConnectionFailure": str(e)})
except Exception as e:
    print(f"Erreur: {e}")
    cur_query.append({"Exception": str(e)})

# Enregistrement de l'historique des requêtes dans le fichier
with open("historique.txt", "w") as historique:
    for entry in cur_query:
        historique.write(str(entry) + "\n")

print("Historique des requêtes enregistré dans historique.txt")
