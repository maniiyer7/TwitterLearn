import tweepy
import re
import datetime
from random import shuffle

def get_friends_descriptions(api, twitter_account, max_users=100):
    """
    Return the bios of the people that a user follows
    
    api -- the tweetpy API object
    twitter_account -- the Twitter handle of the user
    max_users -- the maximum amount of users to return
    """
    
    user_ids = api.friends_ids(twitter_account)
    shuffle(user_ids)
    
    following = []
    for start in xrange(0, min(max_users, len(user_ids)), 100):
        end = start + 100
        following.extend(api.lookup_users(user_ids[start:end]))
    
    descriptions = []
    for user in following:
        description = re.sub(r'(https?://\S+)', '', user.description)

        # Only descriptions with at least ten words.
        if len(re.split(r'[^0-9A-Za-z]+', description)) > 10:
            descriptions.append(description.strip('#').strip('@'))
    
    return descriptions


def get_tweets(api, twitter_user, tweet_type='timeline', max_tweets=200, min_words=5):
    """
    Return the ???
    
    api -- ??????the tweetpy API object
    twitter_user -- 
    tweet_type --
    max_tweets -- 
    min_words -- 
    """
    tweets = []
    
    full_tweets = []
    step = 200  # Maximum value is 200.
    for start in xrange(0, max_tweets, step):
        end = start + step
        
        # Maximum of `step` tweets, or the remaining to reach max_tweets.
        count = min(step, max_tweets - start)

        kwargs = {'count': count}
        if full_tweets:
            last_id = full_tweets[-1].id
            kwargs['max_id'] = last_id - 1

        if tweet_type == 'timeline':
            current = api.user_timeline(twitter_user, **kwargs)
        else:
            current = api.favorites(twitter_user, **kwargs)
        
        full_tweets.extend(current)
    
    for tweet in full_tweets:
        text = re.sub(r'(https?://\S+)', '', tweet.text)
        
        score = tweet.favorite_count + tweet.retweet_count
        if tweet.in_reply_to_status_id_str:
            score -= 15

        # Only tweets with at least five words.
        if len(re.split(r'[^0-9A-Za-z]+', text)) > min_words:
            tweets.append((text, score))
            
    return tweets

