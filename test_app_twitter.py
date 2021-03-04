from webapp import app, conn, tw

UA_WOE_ID   = 23424976
KYIV_WOE_ID = 924938

auth = tw.oauth.OAuth(app.config.get('ACCESS_TOKEN'), app.config.get('ACCESS_SECRET'), app.config.get('CONSUMER_KEY'), app.config.get('CONSUMER_SECRET'))
twitter_api = tw.Twitter(auth=auth)

ua_trends = twitter_api.trends.place(_id = UA_WOE_ID)
kyiv_trends = twitter_api.trends.place(_id = KYIV_WOE_ID)



print(ua_trends)
print(kyiv_trends)

ua_trends_set = set([trend['name'] for trend in ua_trends[0]['trends']])
kyiv_trends_set = set([trend['name'] for trend in kyiv_trends[0]['trends']])

common_trends = ua_trends_set.intersection(kyiv_trends_set)

print(common_trends)
