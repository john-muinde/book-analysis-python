import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_and_validate_csv(file_path):
    """
    Load CSV file and perform basic validation.
    
    Args:
        file_path (str): Path to the CSV file
        
    Returns:
        pd.DataFrame: Validated DataFrame
    """
    try:
        df = pd.read_csv(file_path)
        required_columns = [
            'title', 'authors', 'average_rating', 'isbn',
            'language_code', 'num_pages', 'ratings_count'
        ]
        
        missing_columns = [col for col in required_columns if col not in df.columns]
        if missing_columns:
            raise ValueError(f"Missing required columns: {missing_columns}")
            
        return df
    except FileNotFoundError:
        raise FileNotFoundError(f"Could not find CSV file at {file_path}")
    except pd.errors.EmptyDataError:
        raise ValueError("The CSV file is empty")

def plot_rating_distribution(df):
    """
    Plot the distribution of book ratings.
    
    Args:
        df (pd.DataFrame): DataFrame containing book data
    """
    plt.figure(figsize=(10, 6))
    sns.histplot(data=df, x='average_rating', bins=50)
    plt.title('Distribution of Book Ratings')
    plt.xlabel('Rating')
    plt.ylabel('Count')
    return plt

def create_author_summary(df, author_name):
    """
    Create a summary of an author's books.
    
    Args:
        df (pd.DataFrame): DataFrame containing book data
        author_name (str): Name of the author
        
    Returns:
        dict: Summary statistics for the author
    """
    author_df = df[df['authors'].str.contains(author_name, case=False, na=False)]
    
    if len(author_df) == 0:
        return None
        
    return {
        'num_books': len(author_df),
        'avg_rating': author_df['average_rating'].mean(),
        'total_ratings': author_df['ratings_count'].sum(),
        'avg_pages': author_df['num_pages'].mean(),
        'most_rated_book': author_df.loc[author_df['ratings_count'].idxmax(), 'title'],
        'highest_rated_book': author_df.loc[author_df['average_rating'].idxmax(), 'title']
    }

def format_book_recommendations(recommendations_df):
    """
    Format book recommendations for display.
    
    Args:
        recommendations_df (pd.DataFrame): DataFrame containing recommendations
        
    Returns:
        pd.DataFrame: Formatted recommendations
    """
    if len(recommendations_df) == 0:
        return pd.DataFrame()
        
    formatted_df = recommendations_df.copy()
    formatted_df['average_rating'] = formatted_df['average_rating'].round(2)
    formatted_df['ratings_count'] = formatted_df['ratings_count'].apply(lambda x: f"{x:,}")
    
    return formatted_df