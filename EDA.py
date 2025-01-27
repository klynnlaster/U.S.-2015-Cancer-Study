import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression


# Load the dataset
data = pd.read_csv('cancer_reg_cleaned.csv')

# Inspect the data
print(data.info())
print(data.head())
data['state'] = data['geography'].str.split(',').str[-1].str.strip()

# Calculate the diagnosis rate per capita for each row
# Assuming 'incidencerate' is per 100,000 people and 'popest2015' is the population
data['diagnosis_rate_per_capita'] = (data['incidencerate'] / 100000) * data['popest2015']

# Group data by state and calculate total diagnosis rate and population
state_data = data.groupby('state').agg({
    'diagnosis_rate_per_capita': 'sum',  # Sum up diagnosis rates for all cities in a state
    'popest2015': 'sum'  # Sum up the population for each state
}).reset_index()

# Calculate overall diagnosis rate relative to the total state population
state_data['diagnosis_rate_relative'] = state_data['diagnosis_rate_per_capita'] / state_data['popest2015']

# Sort by the diagnosis rate relative to the population
state_data_sorted = state_data.sort_values(by='diagnosis_rate_relative', ascending=False)

# Display the top states with the highest rates
print(state_data_sorted.head())

#Kentucky is first with 22624, Delaware with 4683, New Hampshire with 6559, Pennsylvania 62921, and Connecticut with 17530.

region_mapping = {
    'Northeast': ['Connecticut', 'Maine', 'Massachusetts', 'New Hampshire', 'Rhode Island', 'Vermont', 'New Jersey', 'New York', 'Pennsylvania'],
    'Midwest': ['Illinois', 'Indiana', 'Iowa', 'Kansas', 'Michigan', 'Minnesota', 'Missouri', 'Nebraska', 'North Dakota', 'Ohio', 'South Dakota', 'Wisconsin'],
    'South': ['Alabama', 'Arkansas', 'Delaware', 'Florida', 'Georgia', 'Kentucky', 'Louisiana', 'Maryland', 'Mississippi', 'North Carolina', 'Oklahoma', 'South Carolina', 'Tennessee', 'Texas', 'Virginia', 'West Virginia', 'District of Columbia'],
    'West': ['Alaska', 'Arizona', 'California', 'Colorado', 'Hawaii', 'Idaho', 'Montana', 'Nevada', 'New Mexico', 'Oregon', 'Utah', 'Washington', 'Wyoming']
}

missing_states = [state for state in data['state'].unique() if not any(state in states for states in region_mapping.values())]
print("States not mapped to regions:", missing_states)

# Extract state abbreviation from geography
data['state'] = data['geography'].str.split(',').str[-1].str.strip()

# Assign regions based on state
data['region'] = data['state'].map(lambda x: next((region for region, states in region_mapping.items() if x in states), 'Unknown'))

# Calculate diagnosis rate per capita
data['diagnosis_rate_per_capita'] = (data['incidencerate'] / 100000) * data['popest2015']

# Group by region and calculate metrics
region_data = data.groupby('region').agg({
    'diagnosis_rate_per_capita': 'mean',  # Average diagnosis rate per capita
    'popest2015': 'sum',  # Total population for the region
    'target_deathrate': 'mean'  # Average death rate for the region
}).reset_index()

# Sort by diagnosis rate or other metrics
region_data_sorted = region_data.sort_values(by='diagnosis_rate_per_capita', ascending=False)

# Display the results
print(region_data_sorted)

print(data.columns)

columns_of_interest = ['medincome', 'povertypercent', 'incidencerate', 'target_deathrate']
subset = data[columns_of_interest]

# Check for missing values and drop rows with null values
subset = subset.dropna()

correlation_matrix = subset.corr()

print("Correlation Matrix:")
print(correlation_matrix)

sns.scatterplot(x='medincome', y='incidencerate', data=subset)
plt.title('Median Income vs. Cancer Diagnosis Rate')
plt.xlabel('Median Income')
plt.ylabel('Cancer Diagnosis Rate')
plt.show()

# Scatter plot: Poverty Levels vs. Cancer Death Rate
sns.scatterplot(x='povertypercent', y='target_deathrate', data=subset)
plt.title('Poverty Levels vs. Cancer Death Rate')
plt.xlabel('Poverty Levels (%)')
plt.ylabel('Cancer Death Rate')
plt.show()

sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Heatmap')
plt.show()


columns_of_interest2 = ['pctbachdeg25_over', 'incidencerate', 'target_deathrate']
subset2 = data[columns_of_interest2].dropna()

correlation_matrix = subset2.corr()
print(correlation_matrix)

sns.scatterplot(x='pctbachdeg25_over', y='incidencerate', data=subset2)
plt.title('Education Levels vs. Cancer Diagnosis Rate')
plt.xlabel('Percent with Bachelor’s Degrees')
plt.ylabel('Cancer Diagnosis Rate')
plt.show()

# Scatter plot: Percent with bachelor's degrees vs. cancer death rate
sns.scatterplot(x='pctbachdeg25_over', y='target_deathrate', data=subset2)
plt.title('Education Levels vs. Cancer Death Rate')
plt.xlabel('Percent with Bachelor’s Degrees')
plt.ylabel('Cancer Death Rate')
plt.show()

columns_of_interest3 = ['pctwhite', 'pctblack', 'pctasian', 'pctotherrace', 'incidencerate', 'target_deathrate']
subset3 = data[columns_of_interest3].dropna()

correlation_matrix = subset3.corr()
print(correlation_matrix)

# Scatter plot: Percent White vs. Cancer Diagnosis Rate
sns.scatterplot(x='pctwhite', y='incidencerate', data=subset3)
plt.title('Percent White vs. Cancer Diagnosis Rate')
plt.xlabel('Percent White')
plt.ylabel('Cancer Diagnosis Rate')
plt.show()

sns.scatterplot(x='pctblack', y='incidencerate', data=subset3)
plt.title('Percent Black vs. Cancer Diagnosis Rate')
plt.xlabel('Percent Black')
plt.ylabel('Cancer Diagnosis Rate')
plt.show()

sns.scatterplot(x='pctasian', y='incidencerate', data=subset3)
plt.title('Percent Asian vs. Cancer Diagnosis Rate')
plt.xlabel('Percent Asian')
plt.ylabel('Cancer Diagnosis Rate')
plt.show()

sns.scatterplot(x='pctotherrace', y='incidencerate', data=subset3)
plt.title('Percent OR vs. Cancer Diagnosis Rate')
plt.xlabel('Percent OR')
plt.ylabel('Cancer Diagnosis Rate')
plt.show()

# Scatter plot: Percent Black vs. Cancer Death Rate
sns.scatterplot(x='pctblack', y='target_deathrate', data=subset3)
plt.title('Percent Black vs. Cancer Death Rate')
plt.xlabel('Percent Black')
plt.ylabel('Cancer Death Rate')
plt.show()