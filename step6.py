# -*- coding: utf-8 -*-
"""step6.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1oZcFQoiS2imk54V_Zt7KBPTNVzadgQ2W
"""

# 5. Predicting New Tweets
new_tweet = "Forest fire near La Ronge Sask. Canada"

# Preprocess the new tweet
processed_tweet = preprocess_text(new_tweet)
tweet_vector = get_document_vector(processed_tweet, model)

# Add additional features for the new tweet
text_length = len(new_tweet)
num_hashtags = new_tweet.count('#')
sentiment = TextBlob(new_tweet).sentiment.polarity
new_tweet_combined = np.hstack((tweet_vector, [text_length, num_hashtags, sentiment]))

# Make the prediction
prediction = classifier.predict([new_tweet_combined])[0]

# Print the prediction
if prediction == 1:
    print(f"Tweet: '{new_tweet}' is predicted as a real disaster.")
else:
    print(f"Tweet: '{new_tweet}' is predicted as a fake disaster.")