import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
data1 = pd.read_csv(r"C:\Users\ASUS\Downloads\Air_Quality.csv") #read csv file 
df = pd.DataFrame(data1) 
print(df)

#Objective 1: Understand the Distribution of Air Quality Measurements

df_clean = df.dropna(subset=['Data Value'])

plt.figure(figsize=(10, 5))
sns.histplot(df_clean['Data Value'], kde=True, bins=20, color='lightcoral', edgecolor='black')
plt.title("Distribution of Air Quality Measurements")
plt.xlabel("Data Value")
plt.ylabel("Frequency")
plt.show()

#Objective 2: Analyze Pollution Levels by Location
# Clean data
df_clean = df.dropna(subset=['Geo Place Name', 'Data Value'])

# Compute median Data Value per location
median_pollution = df_clean.groupby('Geo Place Name')['Data Value'].median().sort_values(ascending=False).head(10)
print(median_pollution)
# Convert to DataFrame for heatmap
median_df = median_pollution.reset_index().pivot_table(index='Geo Place Name', values='Data Value')

# Plot heatmap
plt.figure(figsize=(6, 10))
sns.heatmap(median_df, annot=True, cmap='YlOrRd', linewidths=0.5)
plt.title("Top 10 Locations by Median Pollution Level")
plt.xlabel("Median Data Value")
plt.ylabel("Location")
plt.show()
