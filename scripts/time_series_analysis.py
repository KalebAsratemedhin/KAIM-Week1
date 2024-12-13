import matplotlib.pyplot as plt
import seaborn as sns

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
