import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def calculate_and_describe_column_length(df, column_name):
    """
    Add a column for text lengths and return basic statistics.
    """
    length_column = f"{column_name}_length"
    df[length_column] = df[column_name].str.len()
    stats = df[length_column].describe()
    return df, stats, length_column

def plot_distribution(df, column, title, xlabel, ylabel, bins=20, color='blue'):
    """
    Plot the distribution of a numerical column.
    """
    plt.figure(figsize=(8, 5))
    sns.histplot(df[column], kde=True, bins=bins, color=color)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()

def count_values(df, column):
    """
    Count the occurrences of each value in a column.
    """
    return df[column].value_counts()

def plot_top_values(value_counts, column_name, top_n=10, color='teal'):
    """
    Plot the top N values in a column.
    """
    plt.figure(figsize=(10, 6))
    # value_counts.head(top_n).plot(kind='bar', color=color)
    plt.title(f"Top {top_n} {column_name} by Count")
    plt.xlabel(column_name.capitalize())
    plt.ylabel("Count")
    plt.xticks(rotation=45)
    plt.show()



def plot_time_series(df, date_column, title, xlabel, ylabel):
    """
    Plot the number of occurrences over time.
    """
    time_series = df[date_column].value_counts().sort_index()
    plt.figure(figsize=(12, 6))
    time_series.plot()
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.show()