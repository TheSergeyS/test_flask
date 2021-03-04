from pymongo import MongoClient

client = MongoClient('127.0.0.1', 3979)
db = client.test_db

post = {"author": "Mike", "text": "My first blog post!"}
posts = db.posts
post_id = posts.insert_one(post).inserted_id
print(post_id)

# net:
#   bindIp: 127.0.0.1
#   port: 3979