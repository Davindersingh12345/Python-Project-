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
