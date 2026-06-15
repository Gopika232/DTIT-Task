import pandas as pd
import matplotlib.pyplot as plt  #type:ignore
import seaborn as sns     #type:ignore
from sklearn.datasets import load_iris    #type:ignore


# Load real-world dataset
iris = load_iris()

# Convert to DataFrame
df = pd.DataFrame(iris.data,columns=iris.feature_names)

# Add target column
df["species"] = iris.target_names[iris.target]


# -------------------------
# Exploratory Data Analysis
# -------------------------

# Display first rows
print("First 5 rows:")
print(df.head())


# Dataset structure
print("\nDataset Information:")
print(df.info())


# Shape of dataset
print("\nDataset Shape:")
print(df.shape)


# Statistical summary
print("\nStatistical Summary:")
print(df.describe())


# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())


# Count species
print("\nSpecies Count:")
print(df["species"].value_counts())


# -------------------------
# Visualization
# -------------------------

# 1. Distribution of sepal length
plt.figure(figsize=(6,4))
sns.histplot(df["sepal length (cm)"], kde=True)
plt.title("Sepal Length Distribution")
plt.xlabel("Sepal Length (cm)")
plt.show()


# 2. Distribution of petal length
plt.figure(figsize=(6,4))
sns.histplot(df["petal length (cm)"], kde=True)
plt.title("Petal Length Distribution")
plt.xlabel("Petal Length (cm)")
plt.show()


# 3. Species comparison
plt.figure(figsize=(6,4))
sns.countplot(x="species", data=df)
plt.title("Number of Flowers by Species")
plt.show()


# 4. Relationship between features
plt.figure(figsize=(6,4))
sns.scatterplot(x="sepal length (cm)",y="petal length (cm)",hue="species",data=df)
plt.title("Sepal Length vs Petal Length")
plt.show()



#####    OUTPUT   ####

# First 5 rows:
#    sepal length (cm)  sepal width (cm)  petal length (cm)  petal width (cm) species
# 0                5.1               3.5                1.4               0.2  setosa
# 1                4.9               3.0                1.4               0.2  setosa
# 2                4.7               3.2                1.3               0.2  setosa
# 3                4.6               3.1                1.5               0.2  setosa
# 4                5.0               3.6                1.4               0.2  setosa

# Dataset Information:
# RangeIndex: 150 entries, 0 to 149
# Data columns (total 5 columns):
#  #   Column             Non-Null Count  Dtype  
# ---  ------             --------------  -----  
#  0   sepal length (cm)  150 non-null    float64
#  1   sepal width (cm)   150 non-null    float64
#  2   petal length (cm)  150 non-null    float64
#  3   petal width (cm)   150 non-null    float64
#  4   species            150 non-null    object 
# dtypes: float64(4), object(1)
# memory usage: 6.0+ KB
# None

# Dataset Shape:
# (150, 5)

# Statistical Summary:
#        sepal length (cm)  sepal width (cm)  petal length (cm)  petal width (cm)
# count         150.000000        150.000000         150.000000        150.000000
# mean            5.843333          3.057333           3.758000          1.199333
# std             0.828066          0.435866           1.765298          0.762238
# min             4.300000          2.000000           1.000000          0.100000
# 25%             5.100000          2.800000           1.600000          0.300000
# 50%             5.800000          3.000000           4.350000          1.300000
# 75%             6.400000          3.300000           5.100000          1.800000
# max             7.900000          4.400000           6.900000          2.500000

# Missing Values:
# sepal length (cm)    0
# sepal width (cm)     0
# petal length (cm)    0
# petal width (cm)     0
# species              0
# dtype: int64

# Species Count:
# species
# setosa        50
# versicolor    50
# virginica     50
# Name: count, dtype: int64