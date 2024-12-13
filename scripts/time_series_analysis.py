import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def analyze_publication_frequency(df, date_column):
    """
    Analyze publication frequency over time.
    """
    daily_counts = df.groupby(df[date_column].dt.date).size()
    daily_counts.plot(title='Publication Frequency Over Time', figsize=(10, 6))
    plt.xlabel('Date')
    plt.ylabel('Number of Articles')
    plt.show()

def analyze_publication_times(df, date_column):
    """
    Analyze distribution of publication times.
    """
    df['hour'] = df[date_column].dt.hour
    sns.histplot(df['hour'], bins=24, kde=True)
    plt.title('Distribution of Publication Times')
    plt.xlabel('Hour of Day')
    plt.show()

def analyze_publishers(df, publisher_column):
    """
    Analyze publishers and their contribution.
    """
    publisher_counts = df[publisher_column].value_counts()

    df['publisher_domain'] = df[publisher_column].str.extract(r'@([a-zA-Z0-9.-]+)')
    domain_counts = df['publisher_domain'].value_counts()

    publisher_counts.head(10).plot(kind='bar', title='Top 10 Publishers')
    domain_counts.head(10).plot(kind='bar', title='Top 10 Publishers by email')

    plt.ylabel('Number of Articles')
    plt.show()
