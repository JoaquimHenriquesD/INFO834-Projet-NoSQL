from pymongo import MongoClient
import time
import sys

# Connects to default host and port
client = MongoClient()

# Set the database France and collection communes
db = client.France
communes = db.communes

def search_commune(name):
    """
    Print the searched commune, and the time it took to retrieve the data.
    :param: (name) String
    :return: void
    """
    tic = time.perf_counter()
    commune = communes.find_one({"nom_commune" : name})
    toc = time.perf_counter()
    print(commune)
    print(f"Document found in {toc - tic:0.4f} seconds")

if __name__ == "__main__":
    search_commune(sys.argv[1])
