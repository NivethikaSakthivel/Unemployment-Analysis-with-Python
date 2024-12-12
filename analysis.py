import pandas as pd
import matplotlib
matplotlib.use('Agg')  # Use a non-GUI backend
import matplotlib.pyplot as plt
import seaborn as sns

def load_data(file_path):
    try:
        data = pd.read_csv(file_path)
        print(f"Data from {file_path} loaded successfully!")
        return data
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        exit()

# Load datasets
file_paths = ['Unemployment in India.csv', 'Unemployment_Rate_upto_11_2020.csv']

dataframes = [load_data(fp) for fp in file_paths]

data = pd.concat(dataframes, ignore_index=True)

# Display dataset information
print("\nDataset Information:\n")
data.info()

# Preview the data
print("\nData Preview:\n")
print(data.head())

# Handle missing values
if data.isnull().sum().any():
    print("\nHandling missing values...")
    data.dropna(inplace=True)

# Clean column names by stripping whitespace
data.columns = data.columns.str.strip()

# Extract year from Date and clean column names
data['Year'] = pd.to_datetime(data['Date'], errors='coerce').dt.year

data.rename(columns={
    'Estimated Unemployment Rate (%)': 'Unemployment Rate',
    'Region': 'State'
}, inplace=True)

# Summary statistics
print("\nSummary Statistics:\n")
print(data.describe())

# Visualization: Unemployment Rate by Year
plt.figure(figsize=(10, 6))
sns.lineplot(x='Year', y='Unemployment Rate', data=data, marker='o')
plt.title('Unemployment Rate by Year')
plt.xlabel('Year')
plt.ylabel('Unemployment Rate (%)')
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()

# Visualization: State-wise Unemployment Comparison
plt.figure(figsize=(12, 8))
sns.barplot(x='State', y='Unemployment Rate', data=data)
plt.title('State-wise Unemployment Rate')
plt.xticks(rotation=90)
plt.show()

# Save cleaned data (optional)
data.to_csv('cleaned_unemployment_data.csv', index=False)
print("\nCleaned data saved successfully!")