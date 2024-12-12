# Unemployment Analysis with Python

## Project Overview
This project analyzes unemployment trends in India using Python, focusing on unemployment rates across different states and years. The dataset includes various statistics related to unemployment in India.

---

## Features
- Data Cleaning and Preprocessing
- Missing Value Handling
- Data Visualization:
  - Unemployment Rate by Year (Line Plot)
  - State-wise Unemployment Comparison (Bar Plot)
- Exporting Cleaned Data to CSV

---

## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-repo/unemployment-analysis.git
   cd unemployment-analysis
   ```

2. **Create and Activate a Virtual Environment:**
   ```bash
   python -m venv myenv
   .\myenv\Scripts\Activate  # On Windows
   source myenv/bin/activate   # On Linux/Mac
   ```

3. **Install Required Libraries:**
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

1. **Place the Data Files:**
   Ensure the following CSV files are present in the project directory:
   - `Unemployment in India.csv`
   - `Unemployment_Rate_upto_11_2020.csv`

2. **Run the Script:**
   ```bash
   python analysis.py
   ```

3. **Expected Output:**
   - Summary Statistics
   - Cleaned Data Preview
   - Line Plot: Unemployment Rate by Year
   - Bar Plot: State-wise Unemployment Comparison
   - Exported Cleaned Data (`cleaned_unemployment_data.csv`)

---

## Libraries Used
- `pandas` - Data Manipulation
- `matplotlib` - Data Visualization
- `seaborn` - Statistical Data Visualization

---

## Project Structure
```
|-- analysis.py                # Main analysis script
|-- Unemployment in India.csv  # Dataset 1
|-- Unemployment_Rate_upto_11_2020.csv  # Dataset 2
|-- cleaned_unemployment_data.csv  # Exported Cleaned Data
|-- requirements.txt           # Dependencies
|-- README.md                  # Project Documentation
```
