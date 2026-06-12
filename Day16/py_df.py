import pandas as pd

# Create Dictionary
data = {"Name": ["Gopika", "Anu", "Priya"],"Age": [22, 21, 23],"Department": ["CSE", "IT", "ECE"]}

# Convert Dictionary to DataFrame
df = pd.DataFrame(data)

# Display DataFrame
print("Pandas DataFrame:")
print(df)

####    OUTPUT    ####

# Pandas DataFrame:
#      Name  Age Department
# 0  Gopika   22        CSE
# 1     Anu   21         IT
# 2   Priya   23        ECE