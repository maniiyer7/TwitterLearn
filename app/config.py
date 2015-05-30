import os
import pandas as pd
import numpy as np

##################################################### TWITTER SETTINGS
# Put here your credentials to consume Twitter API
TWITTER_APPLICATION_NAME = 'monkeylearnTest'
TWITTER_APPLICATION_URL = 'https://apps.twitter.com/app/8315586'

TWITTER_CONSUMER_KEY = 'zo7Fi6LMUKpas2yfYNMItyt1J'
TWITTER_CONSUMER_SECRET = 'kQEjYM4xUGBHFrIQQJXl6boPDBENOsZyQMLNrXT6CtfptAJUzC'
TWITTER_ACCESS_TOKEN_KEY = '89396620-PSWxWC84Czei6pDKzX24hpNivNizpzaXPCzksu2wh'
TWITTER_ACCESS_TOKEN_SECRET = 'PeS5S8EDMAWIDbWhQFPexTN6d1IMgMheGxKsOaGLG7e9m'

# This is the twitter user that we will be profiling using our news classifier.
#TWITTER_USER = 'raulgarreta'
TWITTER_USER = 'katyperry'


##################################################### MONKEYLEARN SETTINGS
# Put here your MonkeyLearn API token
# MONKEYLEARN_TOKEN = '7f67703b89cf1ca7cd022fa4ece971d080965617'
MONKEYLEARN_TOKEN = 'a2a32cb39c6842565f6776d44f25a0ce4d949255'

#if 'MONKEYLEARN_APIKEY' in os.environ:
#    MONKEYLEARN_TOKEN = 'token %s' % os.environ.get('MONKEYLEARN_APIKEY')
#else:
#    raise Exception("Monkeylearn token is required")


# This classifier is used to detect the tweet/bio's topics
MONKEYLEARN_TOPIC_CLASSIFIER_ID = 'cl_5icAVzKR'

# This extractor is used to extract keywords from tweets and bios
MONKEYLEARN_EXTRACTOR_ID = 'ex_y7BPYzNG'

