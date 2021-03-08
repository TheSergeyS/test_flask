from pymongo import MongoClient
import webapp.tw as tw
import twitter_text
import pprint

twitter_api = tw.oauth_login()
client = MongoClient('127.0.0.1', 3979)

# 1.
# db = client.test_db
# post = {"author": "Mike", "text": "My first blog post!"}
# posts = db.posts
# post_id = posts.insert_one(post).inserted_id
# print(post_id)

# 2.
# db = client.tw_data
# users = db.users
#
# friends_id, followers_ids = tw.get_friends_followers_ids(twitter_api, screen_name='TheSergeyS')
# users_profile = tw.get_user_profile(twitter_api,user_ids=friends_id)
#
# for key, value in users_profile.items():
#     user_id = users.insert_one(value).inserted_id
#     print(user_id)

# 3.
db = client.tw_data
users = db.users

# pprint.pprint(users.find_one())
# pprint.pprint((users.find_one({'name': 'дїїїїїїїдько'})))
# print(users.count_documents({}))

# for user in users.find():
#     print("name: {0}, id: {1}".format(user['name'], user['id']))

# for user in users.find({"id": {"$in": [42980370, 2813067186]}}):
#     print("name: {0}, id: {1}".format(user['name'], user['id']))

for user in users.find({"followers_count": {"$gte": 1000000}}):
    print("name: {0}, id: {1}, followers: {2}".format(user['name'], user['id'], user['followers_count']))
    print(user)
