import unittest
import pandas as pd
import numpy as np
from src.analyzer import BookAnalyzer
from src.utils import load_and_validate_csv, create_author_summary

class TestBookAnalyzer(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Set up test data once for all test methods."""
        cls.test_data = pd.DataFrame({
            'title': ['Book1', 'Book2', 'Book3'],
            'authors': ['Author1', 'Author2', 'Author1'],
            'average_rating': [4.5, 3.8, 4.2],
            'isbn': ['123', '456', '789'],
            'language_code': ['eng', 'eng', 'spa'],
            'num_pages': [200, 300, 250],
            'ratings_count': [1000, 500, 750],
            'publication_date': ['2020-01-01', '2020-02-01', '2020-03-01']
        })
        cls.test_data.to_csv('test_books.csv', index=False)
        cls.analyzer = BookAnalyzer('test_books.csv')

    def test_get_language_distribution(self):
        """Test language distribution calculation."""
        dist = self.analyzer.get_language_distribution()
        self.assertEqual(dist['eng'], 2)
        self.assertEqual(dist['spa'], 1)

    def test_get_top_rated_books(self):
        """Test top rated books retrieval."""
        top_books = self.analyzer.get_top_rated_books(min_ratings=0)
        self.assertEqual(len(top_books), 3)
        self.assertEqual(top_books.iloc[0]['average_rating'], 4.5)

    def test_get_most_prolific_authors(self):
        """Test most prolific authors calculation."""
        top_authors = self.analyzer.get_most_prolific_authors()
        self.assertEqual(top_authors['Author1'], 2)
        self.assertEqual(top_authors['Author2'], 1)

    def test_recommend_books(self):
        """Test book recommendation system."""
        recommendations = self.analyzer.recommend_books('Author1', n_recommendations=1)
        self.assertEqual(len(recommendations), 1)
        self.assertEqual(recommendations.iloc[0]['authors'], 'Author2')

    def test_utils_create_author_summary(self):
        """Test author summary creation."""
        summary = create_author_summary(self.analyzer.df, 'Author1')
        self.assertEqual(summary['num_books'], 2)
        self.assertAlmostEqual(summary['avg_rating'], 4.35)

if __name__ == '__main__':
    unittest.main()