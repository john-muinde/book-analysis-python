# Dependency Management Guide

## Quick Start

```bash
# Create environment and install dependencies
python setup_env.py
```

## Detailed Setup Process

### 1. Environment Setup

The `setup_env.py` script handles:

- Python version verification (3.8+ required)
- Virtual environment creation
- Pip upgrade
- Package installation
- Project structure setup
- Environment information logging

### 2. Dependencies Overview

#### Core Libraries

- **pandas** (>= 2.2.0)

  - Purpose: Data manipulation and analysis
  - Used for: Loading CSV, data cleaning, analysis
- **numpy** (>= 1.26.0)

  - Purpose: Numerical computations
  - Used for: Mathematical operations, array manipulations

#### Visualization

- **matplotlib** (>= 3.8.0)

  - Purpose: Basic plotting
  - Used for: Creating visualizations
- **seaborn** (>= 0.13.0)

  - Purpose: Statistical visualizations
  - Used for: Enhanced plotting, statistical graphics

#### Machine Learning

- **scikit-learn** (>= 1.4.0)

  - Purpose: Machine learning algorithms
  - Used for: Recommendation system, similarity calculations
- **scipy** (>= 1.12.0)

  - Purpose: Scientific computing
  - Used for: Statistical operations

#### Development Tools (Optional)

- **jupyter** (>= 1.0.0)

  - Purpose: Interactive development
  - Used for: Notebook interface
- **pytest** (>= 7.4.0)

  - Purpose: Testing
  - Used for: Unit tests
- **black** (>= 23.12.0)

  - Purpose: Code formatting
  - Used for: Maintaining code style

### 3. Installation Methods

#### Automatic Installation

```bash
python setup_env.py
```

#### Manual Installation

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# Unix/MacOS:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 4. Troubleshooting

#### Common Issues

1. **Python Version Conflicts**

   - Error: "Python 3.8 or higher is required"
   - Solution: Install Python 3.8+
2. **Package Installation Failures**

   ```bash
   # Try installing problematic package separately
   pip install package-name --no-deps
   # Then install dependencies
   pip install package-name --no-cache-dir
   ```
3. **Virtual Environment Issues**

   ```bash
   # Remove and recreate environment
   rm -rf venv
   python setup_env.py
   ```

### 5. Updating Dependencies

#### Checking for Updates

```bash
pip list --outdated
```

#### Safe Update Process

1. Create requirements.txt backup:

   ```bash
   cp requirements.txt requirements.backup
   ```
2. Update specific package:

   ```bash
   pip install --upgrade package-name
   ```
3. Generate new requirements:

   ```bash
   pip freeze > requirements.txt
   ```

### 6. Development Workflow

#### Setting Up Development Environment

1. Install development dependencies:

   ```bash
   pip install -r requirements.txt
   ```
2. Configure VS Code:

   - Select Python interpreter
   - Install recommended extensions

#### Code Quality Tools

- Use Black for formatting:

  ```bash
  black src/
  ```
- Run tests:

  ```bash
  pytest tests/
  ```

### 7. Environment Information

The setup script creates `environment_info.json` containing:

- Python version
- Platform information
- Installation date
- Installed packages and versions

### 8. GPU Support (Optional)

The setup script checks for GPU support which can accelerate certain computations if available.

### 9. Maintenance

#### Regular Updates

```bash
# Activate environment
source venv/bin/activate

# Update all packages
pip install --upgrade -r requirements.txt
```

#### Environment Backup

```bash
# Export environment
pip freeze > requirements_full.txt
```

### 10. Security Considerations

- Dependencies are version-locked for stability
- Regular updates recommended for security patches
- Use trusted package sources only
