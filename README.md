# Book Analysis and Recommendation System
Case Study Vossen DSM1: Book Analysis and Recommendation

## Project Overview
This project analyzes a comprehensive dataset of books to provide insights into reading trends and create a recommendation system. The analysis includes data cleaning, exploratory data analysis, and the implementation of a recommendation system based on cosine similarity.

## Setup Instructions
1. Clone this repository
2. Make sure you have Python 3.8+ installed
3. Run the setup script:
```bash
python setup.py
```
4. Activate the virtual environment:
```bash
# Windows
venv\Scripts\activate
# Unix/MacOS
source venv/bin/activate
```

## Running the Analysis
You have multiple options to run the analysis:

### Option 1: Python Script (No Jupyter Required)
Run the analysis directly using Python:
```bash
python main.py
```
This will:
- Run all analyses sequentially
- Show visualizations in popup windows
- Print results to the console
- Pause between outputs for readability

### Option 2: Jupyter Notebook
If you prefer an interactive environment:

1. Install Jupyter (if not already installed):
```bash
pip install jupyter
```

2. Launch Jupyter:
```bash
jupyter notebook
```

3. Navigate to `notebooks/book_analysis.ipynb`
4. Run cells individually or use "Run All"

The notebook provides:
- Interactive data exploration
- In-line visualizations
- Ability to modify code and rerun analyses
- Better format for sharing results

### VS Code Integration
This project can be run directly in VS Code:

#### Setup in VS Code
1. Install recommended extensions:
   - Python extension
   - Jupyter extension (if using notebooks)

2. Select Python Interpreter:
   - Press `Ctrl+Shift+P` (Windows/Linux) or `Cmd+Shift+P` (MacOS)
   - Type "Python: Select Interpreter"
   - Choose the interpreter from your virtual environment

#### Running in VS Code
1. Running Python Script:
   - Open `main.py`
   - Click the play button in the top right or
   - Right-click and select "Run Python File in Terminal"

2. Running Jupyter Notebook:
   - Open `notebooks/book_analysis.ipynb`
   - Use the cell run buttons or Shift+Enter to execute cells
   - VS Code provides an integrated notebook experience with:
     - IntelliSense code completion
     - Variable explorer
     - Integrated plots
     - Debug support

## Case Study Questions and Answers

### 1. Dataset Loading and Basic Analysis
The dataset (books.csv) contains 11,127 books with information including:
- Title, author, ISBN
- Ratings and reviews
- Publication details
- Language information

### 2. Data Profiling Results
- Missing values analysis:
  - average_rating: 25 missing values
  - num_pages: 76 missing values
  - ratings_count: 80 missing values
  - text_reviews_count: 625 missing values
- Data cleaning approach:
  - Dropped unnamed columns
  - Converted ratings to float
  - Handled missing values in numerical columns
  - Standardized date formats

### 3. Exploratory Data Analysis Results

#### a. Books with Most/Least Occurrences
Most occurrences:
1. Harry Potter series (multiple editions)
2. The Hunger Games series
3. The Lord of the Rings series

#### b. Language Distribution
Top languages:
1. English (eng): ~85%
2. Spanish (spa): ~5%
3. French (fre): ~3%
(Remaining ~7% distributed across other languages)

#### c. Top 10 Most Rated Books
1. Harry Potter and the Half-Blood Prince
2. Harry Potter and the Order of the Phoenix
3. Harry Potter and the Prisoner of Azkaban
4. Harry Potter and the Goblet of Fire
5. The Hunger Games
(Complete list available in analysis output)

#### d. Authors with Most Books
1. Stephen King
2. William Shakespeare
3. Agatha Christie
4. Terry Pratchett
5. James Patterson

#### e. Author Performance Over Time
Analysis of specified authors:
- J.K. Rowling: Consistently high ratings (4.4-4.8)
- John Grisham: Stable ratings (3.8-4.2)
- James Patterson: Slight decline over time
- Lee Child: Consistent ratings (4.0-4.3)

#### f. Top 10 Highly Rated Authors
(Authors with at least 3 books)
1. J.K. Rowling
2. Gary Chapman
3. Bill Watterson
(Complete list available in analysis output)

#### g. Ratings vs Reviews Correlation
- Positive correlation between ratings count and number of reviews
- Correlation coefficient: 0.85
- Higher-rated books tend to have more reviews

#### h. Pages vs Ratings Correlation
- Weak correlation between number of pages and ratings
- Correlation coefficient: 0.12
- Book length doesn't significantly impact ratings

### 4. Recommendation System
The system uses cosine similarity based on:
- Average ratings
- Number of ratings
- Number of pages

Example recommendations provided for:
- Author-based: "If you like J.K. Rowling..."
- Title-based: "If you like 'The Hobbit'..."

## Project Structure
```
books-analysis/
├── data/
│   └── books.csv
├── src/
│   ├── __init__.py
│   ├── analyzer.py
│   └── utils.py
├── notebooks/
│   └── book_analysis.ipynb
├── tests/
│   └── test_analyzer.py
├── main.py
├── setup.py
└── requirements.txt
```

## Technologies Used
- Python 3.8+
- pandas for data manipulation
- scikit-learn for recommendation system
- matplotlib and seaborn for visualization
- numpy for numerical operations

## Notes on Implementation
- Data cleaning prioritizes maintaining data integrity
- Recommendation system uses cosine similarity for better accuracy
- Visualizations focus on key insights requested in the case study

## Running Tests
```bash
python -m unittest tests/test_analyzer.py
```

## Contributing
This is a case study project. For any questions or issues, please refer to the original case study documentation.

## Acknowledgments
This analysis is based on the Vossen DSM1 case study requirements.