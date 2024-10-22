import pymongo
import json
import os

mongodb_uri = 'mongodb://MYUSERNAME:MYPASSWORD@localhost:27018/?authSource=test'

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
        print("La collection existe déjà")

        if os.path.exists("historique.txt"):
            os.remove("historique.txt")

    # Get the informations about the shards - sharding
    print("### --- On recupere les informations sur les shards avec la commande sh.status() --- ###")
    informations_shards = client["admin"].command('listShards')
    for shard in informations_shards["shards"]:
        print(shard)

    print("### ---- On recupere les informations sur les collections --- ###")
    collections = bd.list_collection_names()
    for collection in collections:
        print(collection)

        
    def log_query_results(collection_name, action, query, results):
        with open("historique.txt", "a") as history_file:
            history_file.write(f"Table: {collection_name}\n")
            history_file.write(f"Action: {action}\n")
            history_file.write(f"Query: {json.dumps(query)}\n")
            if action == "update_many":
                history_file.write(f"Matched count: {results.matched_count}\n")
                history_file.write(f"Modified count: {results.modified_count}\n")
            else:
                for result in results:
                    print(result)
                    history_file.write(f"{json.dumps(result)}\n")
            print("")

    def execute_action(action, collection, query=None, update=None):
        if action == "Find":
            results = collection.find(query)
            log_query_results(collection.name, action, query, results)
        elif action == "update_many":
            results = collection.update_many(query, update)
            log_query_results(collection.name, action, query, update)
        else:
            print(f"Action {action} not recognized")

    # Example usage
    action = "Find"
    query = {"title": "The Catcher in the Rye - J.D. Salinger"}
    execute_action(action, books, query=query)

    action = "update_many"
    query = {"categories": {"$regex": "Java", "$options": "i"}}
    update = {"$inc": {"pageCount": 50}}
    execute_action(action, books, query=query, update=update)

    print("### --- Affichage de la collection books --- ###")
    books_entrees = books.find()
    for book in books_entrees:
        print(book)

    # print("### --- on va modifier les données  --- ###")
    # books.update_one({"title": "PFC Programmer's Reference Manual"}, {"$set": {"title": "The Catcher in the Rye - J.D. Salinger"}})
    print("### --- Read collection --- ###")
    query = {"title": "The Catcher in the Rye - J.D. Salinger"}
    
    books_entrees = books.find(query)

    query = {"categories": {"$regex": "Java", "$options": "i"}}
    update = {"$inc": {"pageCount": 50}}

    books_update = books.update_many(query, update)

except pymongo.errors.ConnectionFailure as e:
    print(e)
except Exception as e:
    print(e)
