from pymongo import MongoClient

# Connects to default host and port
client = MongoClient()

# Set the database France and collection communes
db = client.Mailing
lists = db.lists

mailing_list = lists.find_one()

res = []
for user in mailing_list["users"]:
    res.append(db.users.find_one({"_id" : user}))
print(res)
