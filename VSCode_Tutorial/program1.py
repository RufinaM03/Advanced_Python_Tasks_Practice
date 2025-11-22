from textblob import TextBlob
text = input("Enter a sentence: ")
blob = TextBlob(text)
print("Polarity:", blob.sentiment.polarity)
print("Subjectivity:", blob.sentiment.subjectivity)
if blob.sentiment.polarity > 0:
 print("Sentiment: Positive ")
elif blob.sentiment.polarity < 0:
 print("Sentiment: Negative")
else:
 print("Sentiment: Neutral ")