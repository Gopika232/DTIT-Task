import pandas as pd
import numpy as np

from sklearn.preprocessing import StandardScaler, MinMaxScaler   #type:ignore
from sklearn.preprocessing import LabelEncoder, OneHotEncoder  #type:ignore


# Load dataset
data = pd.read_csv("dataset.csv")

print("Original Data")
print(data)

# Check missing values
print("\nMissing Values")
print(data.isnull().sum())


# Handling missing values
# Numerical columns -> mean
data['Age'] = data['Age'].fillna(data['Age'].mean())
data['Salary'] = data['Salary'].fillna(data['Salary'].mean())


# Categorical column -> mode
data['Department'] = data['Department'].fillna(data['Department'].mode()[0])
print("\nAfter Missing Value Handling")
print(data)


# Label Encoding
encoder = LabelEncoder()
data['Department_Label'] = encoder.fit_transform(data['Department'])
print("\nLabel Encoding")
print(data)


# One Hot Encoding
one_hot = pd.get_dummies(data,columns=['Department'])
print("\nOne Hot Encoding")
print(one_hot)


# Feature Scaling
scaler = StandardScaler()
scaled = scaler.fit_transform(data[['Age','Salary','Experience']])
scaled_data = pd.DataFrame(scaled,columns=['Age','Salary','Experience'])
print("\nScaled Data")
print(scaled_data)


# Feature Engineering
data['Salary_Per_Experience'] = (data['Salary'] / data['Experience'])

print("\nNew Feature Added")
print(data)


#####               OUTPUT               #####


# Original Data
#     Name   Age   Salary Department  Experience
# 0    Anu  25.0  35000.0         IT           2
# 1   Bala  30.0  50000.0         HR           5
# 2  Cathy   NaN  45000.0    Finance           4
# 3  David  28.0      NaN         IT           3
# 4   Esha  35.0  70000.0        NaN           8
# 5  Frank  40.0  90000.0         HR          10
# 6   Gopi  26.0  40000.0         IT           2
# 7   Hari   NaN  55000.0    Finance           6
# 8   Isha  32.0  65000.0         IT           7
# 9   John  29.0  48000.0         HR           4

# Missing Values
# Name          0
# Age           2
# Salary        1
# Department    1
# Experience    0
# dtype: int64

# After Missing Value Handling
#     Name     Age        Salary Department  Experience
# 0    Anu  25.000  35000.000000         IT           2
# 1   Bala  30.000  50000.000000         HR           5
# 2  Cathy  30.625  45000.000000    Finance           4
# 3  David  28.000  55333.333333         IT           3
# 4   Esha  35.000  70000.000000         IT           8
# 5  Frank  40.000  90000.000000         HR          10
# 6   Gopi  26.000  40000.000000         IT           2
# 7   Hari  30.625  55000.000000    Finance           6
# 8   Isha  32.000  65000.000000         IT           7
# 9   John  29.000  48000.000000         HR           4

# Label Encoding
#     Name     Age        Salary Department  Experience  Department_Label
# 0    Anu  25.000  35000.000000         IT           2                 2
# 1   Bala  30.000  50000.000000         HR           5                 1
# 2  Cathy  30.625  45000.000000    Finance           4                 0
# 3  David  28.000  55333.333333         IT           3                 2
# 4   Esha  35.000  70000.000000         IT           8                 2
# 5  Frank  40.000  90000.000000         HR          10                 1
# 6   Gopi  26.000  40000.000000         IT           2                 2
# 7   Hari  30.625  55000.000000    Finance           6                 0
# 8   Isha  32.000  65000.000000         IT           7                 2
# 9   John  29.000  48000.000000         HR           4                 1

# One Hot Encoding
#     Name     Age        Salary  Experience  Department_Label  Department_Finance  Department_HR  Department_IT
# 0    Anu  25.000  35000.000000           2                 2               False          False           True
# 1   Bala  30.000  50000.000000           5                 1               False           True          False
# 2  Cathy  30.625  45000.000000           4                 0                True          False          False
# 3  David  28.000  55333.333333           3                 2               False          False           True
# 4   Esha  35.000  70000.000000           8                 2               False          False           True
# 5  Frank  40.000  90000.000000          10                 1               False           True          False
# 6   Gopi  26.000  40000.000000           2                 2               False          False           True
# 7   Hari  30.625  55000.000000           6                 0                True          False          False
# 8   Isha  32.000  65000.000000           7                 2               False          False           True
# 9   John  29.000  48000.000000           4                 1               False           True          False

# Scaled Data
#         Age    Salary  Experience
# 0 -1.356801 -1.326965   -1.236051
# 1 -0.150756 -0.348056   -0.039873
# 2  0.000000 -0.674359   -0.438599
# 3 -0.633174  0.000000   -0.837325
# 4  1.055290  0.957155    1.156306
# 5  2.261335  2.262367    1.953758
# 6 -1.115592 -1.000662   -1.236051
# 7  0.000000 -0.021754    0.358854
# 8  0.331662  0.630852    0.757580
# 9 -0.391965 -0.478578   -0.438599

# New Feature Added
#     Name     Age        Salary Department  Experience  Department_Label  Salary_Per_Experience
# 0    Anu  25.000  35000.000000         IT           2                 2           17500.000000
# 1   Bala  30.000  50000.000000         HR           5                 1           10000.000000
# 2  Cathy  30.625  45000.000000    Finance           4                 0           11250.000000
# 3  David  28.000  55333.333333         IT           3                 2           18444.444444
# 4   Esha  35.000  70000.000000         IT           8                 2            8750.000000
# 5  Frank  40.000  90000.000000         HR          10                 1            9000.000000
# 6   Gopi  26.000  40000.000000         IT           2                 2           20000.000000
# 7   Hari  30.625  55000.000000    Finance           6                 0            9166.666667
# 8   Isha  32.000  65000.000000         IT           7                 2            9285.714286
# 9   John  29.000  48000.000000         HR           4                 1           12000.000000