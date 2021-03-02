import twitter

# Variables that contains the user credentials to access Twitter API
ACCESS_TOKEN    = ""
ACCESS_SECRET   = ""
CONSUMER_KEY    = ""
CONSUMER_SECRET = ""

UA_WOE_ID   = 23424976
KYIV_WOE_ID = 924938

auth = twitter.oauth.OAuth(ACCESS_TOKEN, ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)
twitter_api = twitter.Twitter(auth=auth)

ua_trends = twitter_api.trends.place(_id = UA_WOE_ID)
kyiv_trends = twitter_api.trends.place(_id = KYIV_WOE_ID)



print(ua_trends)
print(kyiv_trends)

ua_trends_set = set([trend['name'] for trend in ua_trends[0]['trends']])
kyiv_trends_set = set([trend['name'] for trend in kyiv_trends[0]['trends']])

common_trends = ua_trends_set.intersection(kyiv_trends_set)

print(common_trends)