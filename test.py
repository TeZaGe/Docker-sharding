import pymongo
import json
mongodb_uri = 'mongodb://MYUSERNAME:MYPASSWORD@localhost:27018/?authSource=test'

# jeu de données books.json


try:
    client = pymongo.MongoClient(mongodb_uri)

    with open("books.json") as f:
        file_data = json.load(f)



    bd = client["bd"]
    books = bd.get_collection("books")

    # Insertion des données
    if "books" not in bd.list_collection_names():
        books.insert_many(file_data)
    else:
        print("La collection existe déja ")


 # Get the informations about the shards - sharding
    print("### --- On recupere les informations sur les shards avec la commande sh.status() --- ###")
    informations_shards = client["admin"].command('listShards')
    for shard in informations_shards["shards"]:
        print(shard)
        
    print("### ---- On recupere les informations sur les collections --- ###")
    collections = bd.list_collection_names()
    for collection in collections:
        print(collection)

    print("### --- Affichage de la collection books --- ###")
    books_entrees = books.find()
    for book in books_entrees:
        print(book)


    # print("### --- on va modifier les données  --- ###")
    # books.update_one({"title": "PFC Programmer's Reference Manual"}, {"$set": {"title": "The Catcher in the Rye - J.D. Salinger"}})
    print("### --- Read collection --- ###")
    books_entrees = books.find({"title": "The Catcher in the Rye - J.D. Salinger"})
    for book in books_entrees:
        print(book)

except pymongo.errors.ConnectionFailure as e:
    print(e)
except Exception as e:
    print(e)





