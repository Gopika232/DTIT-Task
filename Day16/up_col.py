import pandas as pd


# Create DataFrame
data = {"Name": ["Gopika", "Anu", "Priya"],"Marks": [85, 90, 80]}

df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

# Update Column
df["Marks"] = df["Marks"] + 5

print("\nUpdated DataFrame:")
print(df)


####   OUTPUT   ####

# Original DataFrame:
#      Name  Marks
# 0  Gopika     85
# 1     Anu     90
# 2   Priya     80

# Updated DataFrame:
#      Name  Marks
# 0  Gopika     90
# 1     Anu     95
# 2   Priya     85