# Write a Python file that uploads an image to your 
# Twitter account.  Make sure to use the 
# hashtags #UMSI-206 #Proj3 in the tweet.

# You will demo this live for grading.
import tweepy

# Unique code from Twitter
access_token = "459652384-jiGFor8jLLPGUnSutcEnr0dqQg576MEhEGIKkZVX"
access_token_secret = "T9sl2TZZvzjXXq0W2Vjhk6vneY69Onp1qRxY7ubWIKpO8"
consumer_key = "EwClIX1YYUr8GJt3EV8csg6gp"
consumer_secret = "F3EnfNJ8WGgTHlz01QF3uecTLCZ1VjU5JRExi31YWI0nvJLvDB"

# Boilerplate code here
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

# Allows us to Create Tweets, Delete Tweets, and Find Twitter Users
api = tweepy.API(auth)

# Posts an image with the required hashtags to personal Twitter account 
post_image_status = api.update_with_media('media/imwithher.jpg', status = "#UMSI206 #Proj3")

print("""No output necessary although you 
	can print out a success/failure message if you want to.""")