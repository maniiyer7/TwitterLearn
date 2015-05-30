import json
import requests
from collections import Counter



# This is a handy function to classify a list of texts in batch mode (much faster)
########################## classify_batch
def classify_batch(text_list, classifier_id):
    """
    Batch classify texts
    text_list -- list of texts to be classified
    classifier_id -- id of the MonkeyLearn classifier to be applied to the texts
    """
    MONKEYLEARN_CLASSIFIER_BASE_URL = 'https://api.monkeylearn.com/api/v1/categorizer/'
    MONKEYLEARN_EXTRACTOR_BASE_URL = 'https://api.monkeylearn.com/api/v1/extraction/'
    #named_entity_extractor = 'https://api.monkeylearn.com/v2/extractors/ex_isnnZRbS/extract/'
    #generic_topic_classifier = 'https://api.monkeylearn.com/v2/classifiers/cl_5icAVzKR/'
    MONKEYLEARN_TOKEN = 'a2a32cb39c6842565f6776d44f25a0ce4d949255'

    results = []
    
    step = 250
    for start in xrange(0, len(text_list), step):
        end = start + step

        data = {'text_list': text_list[start:end]}

        response = requests.post(
            'https://api.monkeylearn.com/api/v1/categorizer/' + classifier_id + '/classify_batch_text/',
            data=json.dumps(data),
            headers={
                'Authorization': 'Token {}'.format(MONKEYLEARN_TOKEN),
                'Content-Type': 'application/json'
        })
        
        try:
            results.extend(response.json()['result'])
        except:
            print response.text
            raise

    return results

########################## category_histogram
def category_histogram(texts, short_texts):
    """
    Return the ???
    
    texts -- 
    short_texts -- 
    """
    # Classify the bios and tweets with MonkeyLearn's news classifier.
    topics = classify_batch(texts, MONKEYLEARN_TOPIC_CLASSIFIER_ID)
    
    # The histogram will keep the counters of how many texts fall in
    # a given category.
    histogram = Counter()
    samples = {}

    for classification, text, short_text in zip(topics, texts, short_texts):

        # Join the parent and child category names in one string.
        category = classification[0]['label']
        probability = classification[0]['probability']
        
        if len(classification) > 1:
            category += '/' + classification[1]['label']
            probability *= classification[1]['probability']
        
        MIN_PROB = 0.0
        # Discard texts with a predicted topic with probability lower than a treshold
        if probability < MIN_PROB:
            continue
        
        # Increment the category counter.
        histogram[category] += 1
        
        # Store the texts by category
        samples.setdefault(category, []).append((short_text, text))
        
    return histogram, samples


