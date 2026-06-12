import pandas as pd
from sklearn.preprocessing import OneHotEncoder    #type:ignore

# Dataset
data = {"Employee": ["A", "B", "C", "D"],"Department": ["IT", "HR", "Finance", "IT"]}

df = pd.DataFrame(data)
print("Original Data")
print(df)

# OneHot Encoding
encoder = OneHotEncoder()
encoded = encoder.fit_transform(df[["Department"]]).toarray()
encoded_df = pd.DataFrame(encoded,columns=encoder.get_feature_names_out(["Department"]))

# Combine Data
final_data = pd.concat([df, encoded_df],axis=1)

print("\nAfter OneHot Encoding")
print(final_data)

####   OUTPUT    ####

# Original Data
#   Employee Department
# 0        A         IT
# 1        B         HR
# 2        C    Finance
# 3        D         IT

# After OneHot Encoding
#   Employee Department  Department_Finance  Department_HR  Department_IT
# 0        A         IT                 0.0            0.0            1.0
# 1        B         HR                 0.0            1.0            0.0
# 2        C    Finance                 1.0            0.0            0.0
# 3        D         IT                 0.0            0.0            1.0