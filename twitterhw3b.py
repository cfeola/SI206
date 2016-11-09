# In this assignment you must do a Twitter search on any term
# of your choice.
# Deliverables:
# 1) Print each tweet
# 2) Print the average subjectivity of the results
# 3) Print the average polarity of the results

# Be prepared to change the search term during demo.

import tweepy
from textblob import TextBlob

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

# Searches for tweets related to the term "Barack Obama"
public_tweets = api.search('Barack Obama')

# Prints each tweet 
for tweet in public_tweets:
	print(tweet.text)

# Creates an empty list that will be used to stored the polarity value of each tweet
polarity_list = []

# Creates an empty list that will be used to stored the subjectivity value of each tweet
subjectivity_list = []

# Iterates through all of the tweets public tweets that are related to the term "Barack Obama"
for tweet in public_tweets:
	# Sentiment Analysis - Understand and Extracting Feelings from Data
	analysis = TextBlob(tweet.text)
	# We extract the first value - which represents polarity - from the sentiment analysis data for each tweet and append it to the list of polarity values 
	polarity_list.append(analysis.sentiment[0])
	# We extract the second value - which represents subjectivity - from the sentiment analysis data for each tweet and append it to the list of subjectivity values
	subjectivity_list.append(analysis.sentiment[1])

# We find the average polarity by finding the sum of all of the values in the polarity list and dividing that by the length of the list 
polarity = sum(polarity_list)/len(polarity_list)
# We find the average subjectivity by finding the sum of all of the values in the subjectivity list and dividing that by the length of the list
subjectivity = sum(subjectivity_list)/len(subjectivity_list)

print("Average subjectivity is", subjectivity)
print("Average polarity is", polarity)
