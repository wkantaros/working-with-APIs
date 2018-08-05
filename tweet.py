import tweepy

auth = tweepy.OAuthHandler('AkOSJqXjLm3c8vviIevD1Ia2Y', 'rDaYCDoyRTqUDIA4lMS1xhUBWJafdtvHJWsTwM5PF1A5eOnIr4')
auth.set_access_token('906920594591154177-UaUQVYg2VJAM2bLdfdQaeq5ssJj7Oow', 'QKoSwWNKQiLFJFkbZEhnRGs4An1TKJN01QhmrbbnVOVkM')

api = tweepy.API(auth)

public_tweets = api.user_timeline('realDonaldTrump', '5')
for tweet in public_tweets:
    if('RT' not in tweet.text[0: 3]):
        print(tweet.text)
