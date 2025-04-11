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
df_clean = df.dropna(subset=['Geo Place Name', 'Data Value'])
median_pollution = df_clean.groupby('Geo Place Name')['Data Value'].median().sort_values(ascending=False).head(10)
print(median_pollution)
median_df = median_pollution.to_frame()

plt.figure(figsize=(6, 10))
sns.heatmap(median_df, annot=True, cmap='YlOrRd', linewidths=0.5)
plt.title("Top 10 Locations by Median Pollution Level")
plt.xlabel("Median Data Value")
plt.ylabel("Location")
plt.show()

#Objective 3: Analyze Pollution Trends Over Time
df['Start_Date'] = pd.to_datetime(df['Start_Date'], errors='coerce')
df_clean = df.dropna(subset=['Start_Date', 'Data Value'])
monthly_avg = df_clean.groupby(df_clean['Start_Date'].dt.to_period("M"))['Data Value'].mean()
monthly_avg.index = monthly_avg.index.to_timestamp()
print(monthly_avg)

plt.figure(figsize=(14, 6))
sns.lineplot(x=monthly_avg.index, y=monthly_avg.values, marker='o', linewidth=2.5, color='teal')

plt.title("Monthly Average Pollution Trend Over Time", fontsize=16, fontweight='bold')
plt.xlabel("Month", fontsize=12)
plt.ylabel("Average Pollution Level", fontsize=12)
plt.xticks(rotation=45)
plt.grid(True, linestyle='--', alpha=0.6)

plt.show()

#Objective 4: Detect Outliers in Air Quality Measurements
plt.figure(figsize=(8, 6))
sns.boxplot(x=df_clean['Data Value'], color='salmon', width=0.5, fliersize=6, linewidth=2)

plt.title("Detection of Outliers in Air Quality Measurements", fontsize=15, fontweight='bold')
plt.xlabel("Pollution Level (Data Value)", fontsize=12)
plt.grid(True, linestyle='--', alpha=0.5)
plt.show()

#Objective 5: Explore Variability of Pollutants by Location
variability = df_clean.groupby('Geo Place Name')['Data Value'].std().sort_values(ascending=False).head(10)

sns.barplot(x=variability.values, y=variability.index,color="r")
plt.title("Top 10 Locations with Highest Variability")
plt.xlabel("Standard Deviation")
plt.ylabel("Location")
plt.show()

#Objective 6: Detect Pollution Hotspots Using Standardized Scores
df_clean = df.dropna(subset=['Data Value', 'Name', 'Geo Place Name']).copy()
means = df_clean.groupby('Name')['Data Value'].transform('mean')
stds = df_clean.groupby('Name')['Data Value'].transform('std')
df_clean['Z_Score'] = (df_clean['Data Value'] - means) / stds
hotspots = df_clean[df_clean['Z_Score'] > 2]
top_hotspots = hotspots['Geo Place Name'].value_counts().nlargest(10)

sns.barplot(x=top_hotspots.values, y=top_hotspots.index, color='tomato')
plt.title("Top 10 Pollution Hotspots (Z-Score > 2)")
plt.xlabel("Number of High Pollution Events")
plt.ylabel("Location")
plt.tight_layout()
plt.show()

#Objective 7: Detect Sudden Pollution Spikes
df_sorted = df_clean.sort_values(by='Start_Date')
rolling_avg = df_sorted['Data Value'].rolling(window=30, min_periods=1).mean()
spikes = df_sorted[(df_sorted['Data Value'] - rolling_avg).abs() > 2 * df_sorted['Data Value'].std()]
print(rolling_avg)
plt.figure(figsize=(12, 6))
sns.lineplot(x=df_sorted['Start_Date'], y=df_sorted['Data Value'], label='Data Value')
sns.scatterplot(x=spikes['Start_Date'], y=spikes['Data Value'], color='red', label='Spike')
plt.xticks(rotation=70)
plt.title("Detected Pollution Spikes")
plt.xlabel("Date")
plt.ylabel("Data Value")
plt.legend()
plt.show()