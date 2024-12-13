from nltk.sentiment.vader import SentimentIntensityAnalyzer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation
import nltk
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

nltk.download('vader_lexicon')

def perform_sentiment_analysis(df, text_column):
    """
    Perform sentiment analysis on the specified text column.
    """
    sia = SentimentIntensityAnalyzer()
    df['sentiment_score'] = df[text_column].apply(lambda x: sia.polarity_scores(x)['compound'])
    df['sentiment'] = pd.cut(df['sentiment_score'], bins=[-1, -0.05, 0.05, 1], labels=['negative', 'neutral', 'positive'])

    # Visualize sentiment distribution
    sns.countplot(data=df, x='sentiment')
    plt.title('Sentiment Distribution')
    plt.show()
    return df



def perform_topic_modeling(df, text_column):
    """
    Perform topic modeling on the specified text column.
    """
    vectorizer = CountVectorizer(stop_words='english', max_features=1000)
    X = vectorizer.fit_transform(df[text_column])

    lda = LatentDirichletAllocation(n_components=5, random_state=42)
    lda.fit(X)

    for idx, topic in enumerate(lda.components_):
        print(f"Topic {idx + 1}:")
        print([vectorizer.get_feature_names_out()[i] for i in topic.argsort()[-10:]])
