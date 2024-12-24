import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.metrics.pairwise import cosine_similarity
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

class BookAnalyzer:
    """A class for analyzing book data and making recommendations."""
    
    def __init__(self, csv_path):
        """Initialize BookAnalyzer with a CSV file path."""
        self.df = pd.read_csv(csv_path)
        self._clean_data()
    
    def _clean_data(self):
        """Clean the dataset by handling missing values and data types."""
        # Convert ratings to float
        self.df['average_rating'] = pd.to_numeric(self.df['average_rating'], errors='coerce')
        
        # Convert num_pages to numeric, removing any leading/trailing spaces
        self.df['num_pages'] = pd.to_numeric(self.df['  num_pages'].str.strip(), errors='coerce')
        
        # Drop unnamed columns and empty rows
        self.df = self.df.drop(columns=[col for col in self.df.columns if 'Unnamed' in col])
        self.df = self.df.dropna(subset=['title', 'authors', 'average_rating'])
        
        # Convert dates to datetime
        self.df['publication_date'] = pd.to_datetime(self.df['publication_date'], errors='coerce')
    
    def get_basic_stats(self):
        """Get basic statistics about the dataset."""
        stats = {
            'Total Books': len(self.df),
            'Unique Authors': len(self.df['authors'].unique()),
            'Average Rating': round(self.df['average_rating'].mean(), 2),
            'Average Pages': int(self.df['num_pages'].mean()),
            'Most Common Languages': self.df['language_code'].value_counts().head(3).to_dict(),
            'Date Range': f"{self.df['publication_date'].min().year} to {self.df['publication_date'].max().year}",
            'Total Ratings': self.df['ratings_count'].sum(),
            'Average Ratings per Book': int(self.df['ratings_count'].mean())
        }
        return stats
    
    def get_language_distribution(self):
        """Get distribution of books across languages."""
        return self.df['language_code'].value_counts()
    
    def get_top_rated_books(self, min_ratings=1000):
        """Get top 10 most rated books with minimum ratings threshold."""
        mask = self.df['ratings_count'] >= min_ratings
        return (self.df[mask]
                .sort_values('average_rating', ascending=False)
                .head(10)[['title', 'authors', 'average_rating', 'ratings_count']])
    
    def get_most_prolific_authors(self):
        """Get authors with most books."""
        return self.df['authors'].value_counts().head(10)
    
    def analyze_author_performance(self, author_name):
        """Analyze performance of a specific author over time."""
        author_df = self.df[self.df['authors'].str.contains(author_name, case=False, na=False)]
        return author_df.sort_values('publication_date')[
            ['title', 'publication_date', 'average_rating', 'ratings_count']
        ]
    
    def get_top_authors_by_rating(self, min_books=3):
        """Get top authors by average rating with minimum books threshold."""
        author_stats = (self.df.groupby('authors')
                       .agg({
                           'average_rating': 'mean',
                           'title': 'count'
                       })
                       .reset_index())
        
        mask = author_stats['title'] >= min_books
        return (author_stats[mask]
                .sort_values('average_rating', ascending=False)
                .head(10))
    
    def plot_ratings_reviews_correlation(self):
        """Plot correlation between ratings and review counts."""
        plt.figure(figsize=(10, 6))
        plt.scatter(self.df['ratings_count'], 
                   self.df['average_rating'],
                   alpha=0.5)
        plt.xlabel('Number of Ratings')
        plt.ylabel('Average Rating')
        plt.title('Correlation between Ratings Count and Average Rating')
        plt.xscale('log')
        return plt
    
    def plot_pages_ratings_correlation(self):
        """Plot correlation between number of pages and ratings."""
        plt.figure(figsize=(10, 6))
        plt.scatter(self.df['num_pages'],
                   self.df['average_rating'],
                   alpha=0.5)
        plt.xlabel('Number of Pages')
        plt.ylabel('Average Rating')
        plt.title('Correlation between Number of Pages and Average Rating')
        return plt
    
    def recommend_books(self, query_value, attribute='authors', n_recommendations=5):
        """
        Recommend books based on similarity to a query value.
        
        Parameters:
        - query_value: Value to base recommendations on (e.g., author name)
        - attribute: Attribute to query on ('authors', 'title', etc.)
        - n_recommendations: Number of recommendations to return
        """
        # Find books matching the query
        query_books = self.df[self.df[attribute].str.contains(query_value, case=False, na=False)]
        
        if len(query_books) == 0:
            return pd.DataFrame()
        
        # Create feature matrix
        features = ['average_rating', 'ratings_count', 'num_pages']
        feature_matrix = self.df[features].fillna(0)
        
        # Standardize features
        scaler = StandardScaler()
        scaled_features = scaler.fit_transform(feature_matrix)
        
        # Calculate similarity
        similarities = cosine_similarity(scaled_features)
        
        # Get indices of query books
        query_indices = query_books.index
        
        # Calculate average similarity to query books
        avg_similarities = similarities[query_indices].mean(axis=0)
        
        # Get indices of most similar books
        similar_indices = avg_similarities.argsort()[::-1]
        
        # Filter out books by the same author/attribute
        recommendations = []
        for idx in similar_indices:
            if len(recommendations) >= n_recommendations:
                break
            if self.df.iloc[idx][attribute] not in query_books[attribute].values:
                recommendations.append(idx)
        
        return self.df.iloc[recommendations][['title', 'authors', 'average_rating', 'ratings_count']]