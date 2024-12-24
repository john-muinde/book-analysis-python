import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from src.analyzer import BookAnalyzer
from src.utils import plot_rating_distribution, create_author_summary

def main():
    # Initialize our analyzer with the dataset
    analyzer = BookAnalyzer('data/books.csv')

    # 1. Basic Dataset Analysis
    print("Basic Statistics:")
    print(analyzer.get_basic_stats())
    input("\nPress Enter to continue...")  # Pause for user to read

    # 2. Language Distribution
    print("\nLanguage Distribution:")
    lang_dist = analyzer.get_language_distribution()
    plt.figure(figsize=(12, 6))
    lang_dist.head(10).plot(kind='bar')
    plt.title('Top 10 Languages in Dataset')
    plt.xlabel('Language Code')
    plt.ylabel('Number of Books')
    plt.tight_layout()
    plt.show()

    # 3. Top Rated Books
    print("\nTop Rated Books (with at least 1000 ratings):")
    top_books = analyzer.get_top_rated_books(min_ratings=1000)
    print(top_books)
    input("\nPress Enter to continue...")

    # 4. Most Prolific Authors
    print("\nAuthors with Most Books:")
    print(analyzer.get_most_prolific_authors())
    input("\nPress Enter to continue...")

    # 5. Author Performance Analysis
    authors = ['J.K. Rowling', 'John Grisham', 'James Patterson', 'Lee Child']
    plt.figure(figsize=(15, 8))

    for author in authors:
        perf = analyzer.analyze_author_performance(author)
        if not perf.empty:
            plt.plot(perf['publication_date'], perf['average_rating'], 
                    marker='o', label=author)

    plt.title('Author Ratings Over Time')
    plt.xlabel('Publication Date')
    plt.ylabel('Average Rating')
    plt.legend()
    plt.grid(True)
    plt.show()

    # 6. Top Rated Authors
    print("\nTop Rated Authors (minimum 3 books):")
    print(analyzer.get_top_authors_by_rating())
    input("\nPress Enter to continue...")

    # 7. Correlation Analysis
    plt.figure(figsize=(12, 5))
    plt.subplot(1, 2, 1)
    analyzer.plot_ratings_reviews_correlation()
    plt.subplot(1, 2, 2)
    analyzer.plot_pages_ratings_correlation()
    plt.tight_layout()
    plt.show()

    # 8. Book Recommendations
    print("\nBook Recommendations based on J.K. Rowling:")
    recommendations = analyzer.recommend_books('J.K. Rowling')
    print(recommendations)
    input("\nPress Enter to continue...")

    print("\nBook Recommendations based on 'The Hobbit':")
    recommendations = analyzer.recommend_books('The Hobbit', attribute='title')
    print(recommendations)

if __name__ == "__main__":
    main()