

##################################################### Classify Using MonkeyLearn

# Classify the expanded bios of the followed users using MonkeyLearn, return the historgram
descriptions_histogram, descriptions_categorized = category_histogram(expanded_descriptions, descriptions_english)

# Print the catogories sorted by most frequent
for topic, count in descriptions_histogram.most_common():
    print count, topic


# Classify the expanded tweets using MonkeyLearn, return the historgram
tweets_histogram, tweets_categorized = category_histogram(expanded_tweets, tweets_english)

# Print the catogories sorted by most frequent
for topic, count in tweets_histogram.most_common():
    print count, topic






##################################################### Plot the most popular topics

import matplotlib.pyplot as plt

# Add the two histograms (bios and tweets) to a total histogram
total_histogram = tweets_histogram + descriptions_histogram

# Get the top N categories by frequency
max_categories = 6
top_categories, values = zip(*total_histogram.most_common(max_categories))

# Plot the distribution of the top categories with a pie chart
plt.figure(1, figsize=(5,5))
ax = plt.axes([0.1, 0.1, 0.8, 0.8])

plt.pie(
    values,
    labels=top_categories,
    shadow=True,
    colors = [
        (0.86, 0.37, 0.34), (0.86, 0.76, 0.34), (0.57, 0.86, 0.34), (0.34, 0.86, 0.50),
        (0.34, 0.83, 0.86), (0.34, 0.44, 0.86), (0.63, 0.34, 0.86), (0.86, 0.34, 0.70),
    ],
    radius=20,
    autopct='%1.f%%',
)

plt.axis('equal')
plt.show()


##################################################### Get the keywords of each category with MonkeyLearn API

joined_texts = {}

for category in tweets_categorized:
    if category not in top_categories:
        continue
    
    expanded = 0
    joined_texts[category] = u' '.join(map(lambda t: t[expanded], tweets_categorized[category]))


keywords = dict(zip(joined_texts.keys(), extract_keywords(joined_texts.values(), 20)))

for cat, kw in keywords.iteritems():
    top_relevant = map(
        lambda x: x.get('keyword'),
        sorted(kw, key=lambda x: float(x.get('relevance')), reverse=True)
    )
    
    print u"{}: {}".format(cat, u", ".join(top_relevant))




##################################### Word Cloud

def plot_wordcloud(wordcloud):
    return 0


