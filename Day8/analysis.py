import pandas as pd

# Load dataset
df = pd.read_csv("real_world_data.csv")


# Display first 5 rows
print("First 5 Rows:")
print(df.head())


# First 5 Rows:
#    Employee_ID     Name   Age Department   Salary  Experience        City Performance
# 0          101     Arun  25.0         IT  45000.0           2     Chennai        Good
# 1          102    Divya  28.0         HR  52000.0           5  Coimbatore   Excellent
# 2          103  Karthik  30.0    Finance  60000.0           7     Madurai        Good
# 3          104    Meena  26.0         IT      NaN           3     Chennai     Average
# 4          105     Ravi  35.0  Marketing  75000.0          10       Salem   Excellent

# Dataset shape
print("\nShape:")
print(df.shape)

# Shape:
# (15, 8)


# Column names
print("\nColumns:")
print(df.columns)

# Columns:
# Index(['Employee_ID', 'Name', 'Age', 'Department', 'Salary', 'Experience',
#        'City', 'Performance'],
#       dtype='object')

# Data types
print("\nData Types:")
print(df.dtypes)

# Data Types:
# Employee_ID      int64
# Name            object
# Age            float64
# Department      object
# Salary         float64
# Experience       int64
# City            object
# Performance     object
# dtype: object


# Statistics
print("\nStatistics:")
print(df.describe())


# Statistics:
#        Employee_ID        Age        Salary  Experience
# count    15.000000  14.000000     14.000000   15.000000
# mean    107.666667  27.714286  54000.000000    4.866667
# std       4.082483   3.625308  11701.413458    3.044120
# min     101.000000  23.000000  38000.000000    1.000000
# 25%     104.500000  25.250000  45750.000000    2.500000
# 50%     108.000000  27.500000  53500.000000    5.000000
# 75%     110.500000  29.750000  61500.000000    7.500000
# max     114.000000  35.000000  75000.000000   10.000000

# Missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Missing Values:
# Employee_ID    0
# Name           0
# Age            1
# Department     1
# Salary         1
# Experience     0
# City           0
# Performance    0
# dtype: int64


# Duplicate records
print("\nDuplicate Count:")
print(df.duplicated().sum())

# Duplicate Count:
# 1


# Find patterns
print("\nUnique Values:")
for col in df.columns:
    print(col, df[col].unique())


# Unique Values:
# Employee_ID [101 102 103 104 105 106 107 108 109 110 111 112 113 114]
# Name ['Arun' 'Divya' 'Karthik' 'Meena' 'Ravi' 'Sneha' 'Ajay' 'Priya' 'Rahul'
#  'Anu' 'Vijay' 'Latha' 'Manoj' 'Sara']
# Age [25. 28. 30. 26. 35. 24. 29. 31. 27. 23. nan 33.]
# Department ['IT' 'HR' 'Finance' 'Marketing' nan]
# Salary [45000. 52000. 60000.    nan 75000. 40000. 58000. 65000. 50000. 38000.
#  70000. 62000. 55000. 48000.]
# Experience [ 2  5  7  3 10  1  6  8  4  9]
# City ['Chennai' 'Coimbatore' 'Madurai' 'Salem' 'Vellore' 'Trichy']
# Performance ['Good' 'Excellent' 'Average']