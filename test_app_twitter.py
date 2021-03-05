from webapp import app, conn, tw
import webapp.tw as tw
import twitter_text

UA_WOE_ID   = 23424976
KYIV_WOE_ID = 924938

# auth = tw.oauth.OAuth(app.config.get('ACCESS_TOKEN'), app.config.get('ACCESS_SECRET'), app.config.get('CONSUMER_KEY'), app.config.get('CONSUMER_SECRET'))
# twitter_api = tw.Twitter(auth=auth)
twitter_api = tw.oauth_login()

# 1.
# ua_trends = twitter_api.trends.place(_id = UA_WOE_ID)
# kyiv_trends = twitter_api.trends.place(_id = KYIV_WOE_ID)
# ua_trends_set = set([trend['name'] for trend in ua_trends[0]['trends']])
# kyiv_trends_set = set([trend['name'] for trend in kyiv_trends[0]['trends']])
# common_trends = ua_trends_set.intersection(kyiv_trends_set)
#
# print(ua_trends)
# print(kyiv_trends)
# print(common_trends)

# 2.
# response = tw.make_twitter_request(twitter_api.users.lookup, screen_name='TheSergeyS')
# print(response)

# 3.
# print(tw.get_user_profile(twitter_api, screen_names=['TheSergeyS', 'Fly4freepl', 'ladygaga']))

# 4.
friends_id, followers_ids = tw.get_friends_followers_ids(twitter_api,
                                                         screen_name='TheSergeyS')
users_profile = tw.get_user_profile(twitter_api,user_ids=friends_id)

print(friends_id)
print(followers_ids)
print(users_profile)

for key, value in users_profile.items():
    print(value)
