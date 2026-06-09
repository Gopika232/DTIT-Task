import pandas as pd


# Load dataset
df = pd.read_csv("real_world_data.csv")

print("Before Cleaning:")
print(df)

# Before Cleaning:
#     Employee_ID     Name   Age Department   Salary  Experience        City Performance
# 0           101     Arun  25.0         IT  45000.0           2     Chennai        Good
# 1           102    Divya  28.0         HR  52000.0           5  Coimbatore   Excellent
# 2           103  Karthik  30.0    Finance  60000.0           7     Madurai        Good
# 3           104    Meena  26.0         IT      NaN           3     Chennai     Average
# 4           105     Ravi  35.0  Marketing  75000.0          10       Salem   Excellent
# 5           106    Sneha  24.0         HR  40000.0           1     Vellore        Good
# 6           107     Ajay  29.0    Finance  58000.0           6      Trichy     Average
# 7           108    Priya  31.0         IT  65000.0           8     Chennai   Excellent
# 8           109    Rahul  27.0  Marketing  50000.0           4     Madurai        Good
# 9           110      Anu  23.0         HR  38000.0           1       Salem     Average
# 10          110      Anu  23.0         HR  38000.0           1       Salem     Average
# 11          111    Vijay   NaN         IT  70000.0           9  Coimbatore   Excellent
# 12          112    Latha  33.0    Finance  62000.0           8      Trichy        Good
# 13          113    Manoj  28.0        NaN  55000.0           5     Chennai     Average
# 14          114     Sara  26.0  Marketing  48000.0           3     Vellore        Good

# Remove duplicates
df = df.drop_duplicates()


# Handle missing values
for col in df.columns:

    if df[col].dtype == "object":
        df[col].fillna(df[col].mode()[0],inplace=True)

    else:
        df[col].fillna(df[col].mean(),inplace=True)


print("\nAfter Cleaning:")
print(df)


# After Cleaning:
#     Employee_ID     Name        Age Department        Salary  Experience        City Performance
# 0           101     Arun  25.000000         IT  45000.000000           2     Chennai        Good
# 1           102    Divya  28.000000         HR  52000.000000           5  Coimbatore   Excellent
# 2           103  Karthik  30.000000    Finance  60000.000000           7     Madurai        Good
# 3           104    Meena  26.000000         IT  55230.769231           3     Chennai     Average
# 4           105     Ravi  35.000000  Marketing  75000.000000          10       Salem   Excellent
# 5           106    Sneha  24.000000         HR  40000.000000           1     Vellore        Good
# 6           107     Ajay  29.000000    Finance  58000.000000           6      Trichy     Average
# 7           108    Priya  31.000000         IT  65000.000000           8     Chennai   Excellent
# 8           109    Rahul  27.000000  Marketing  50000.000000           4     Madurai        Good
# 9           110      Anu  23.000000         HR  38000.000000           1       Salem     Average
# 11          111    Vijay  28.076923         IT  70000.000000           9  Coimbatore   Excellent
# 12          112    Latha  33.000000    Finance  62000.000000           8      Trichy        Good
# 13          113    Manoj  28.000000         IT  55000.000000           5     Chennai     Average
# 14          114     Sara  26.000000  Marketing  48000.000000           3     Vellore        Good

# Save cleaned file

df.to_csv("cleaned_data.csv",index=False)

print("\nCleaned dataset saved")