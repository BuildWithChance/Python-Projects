# Import required libraries 
import pandas as pd                   # For data manipulation and analysis
import matplotlib.pyplot as plt       # For creating visualizations 
import seaborn as sns                 # For advanced statisical visualizations 

# Load the dataset 
# The dataset contains information about employees, including their attrition status.
# Make sure the file path matches your local setup.
file_path = 'data/employee_hr_data.csv'   # Adjust the file path if needed 
data = pd.read_csv(file_path)

# Step 1: Explore the dataset
# Preview the first few rows to understand the data structure and column names.
print("Dataset preview:")
print(data.head())

# Get a summary of the dataset, including column data types and non-null values.
# This helps us identify potential data cleaning tasks (e.g., missing values).
print("\nDataset Info:")
data.info()

# Check for missing values to identify any columns that might need cleaning.
print("\nMissing Values:")
print(data.isnull().sum())

# Generate basic descriptive statistics for numeric columns.
# This helps us understand key metrics like mean, min, max, and standard deviation. 
print("\nDescriptive Statistics:")
print(data.describe())

# Display unique values in each column to understand the range of data (e.g., departments, job roles).
# This can help identify categories for grouping and analysis.
print("\nUnique Values Per Column:")
for col in data.columns:
    print(f"{col}: {data[col].unique()}")
    
# Step 2: Clean the data (optional, adjust as needed)
# Cleaning ensures data quality, which is critical for accurate analysis.
# Example: Dropping rows with missing values (if they are minimal).
# Uncomment the line below if the dataset contains significant missing rows:
# data = data.dropna()


# Example: Filling missing values in a specific column with a placeholder value.
# This is useful for categorical data where we don’t want to lose rows entirely.
# Uncomment and adjust as necessary:
# data['ColumnName'].fillna('Unknown', inplace=True)


# Step 3: Perform basic analysis
# Count of employees who stayed vs. left to understand overall attrition trends.
# This is the most basic and critical metric for retention analysis.
attrition_count = data['Attrition'].value_counts()
print("\nAttrition Counts:")
print(attrition_count)


# Attrition percentage by department helps identify which departments have the highest turnover rates.
# Normalizing the counts to percentages provides better context than raw counts.
attrition_by_department = data.groupby('Department')['Attrition'].value_counts(normalize=True) * 100
print("n\Attrition by Department (%):") 
print(attrition_by_department)


# Calculate average tenure (YearsAtCompany) for employees who left vs. stayed.
# This helps us determine if shorter-tenured employees are more likely to leave. 
tenure_stats = data.groupby('Attrition')['YearsAtCompany'].mean()
print("\nAverage Tenure by Attrition:")
print(tenure_stats)


# Step 4: Create visualizations
# Visualizations make it easier to spot trends and patterns in the data.


# Bar chart: Overall attrition count
# This provides a quick overview of the proportion of employees who stayed vs. left.
sns.countplot(data=data, x='Attrition')
plt.title('Employee Attrition Count')
plt.show()    

# Bar chart: Attrition by department
# This highlights which departments experience the most attrition.
sns.countplot(data=data, x='Department', hue='Attrition')
plt.title('Attrition by Department')
plt.show()

# Box plot: Tenure vs. attrition
# Box plots are ideal for showing distributions and identifying outliers.
# This helps us see if employees who leave tend to have shorter tenures.
sns.boxplot(data=data, x='Attrition', y='YearsAtCompany')
plt.title('Years at Company by Attrition')
plt.show()

# Step 5: Generate insights
# Use the outputs and visualizations to draw conclusions and answer specific questions:
# - Which departments are at the highest risk for attrition?
# - Are employees with shorter tenures more likely to leave?
# - Are there patterns related to age, job role, or other factors?
