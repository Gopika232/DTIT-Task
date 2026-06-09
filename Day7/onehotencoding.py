import pandas as pd
from sklearn.preprocessing import OneHotEncoder #type:ignore


df = pd.DataFrame({"Department": ["AI","Python","Data Science","AI"]})


encoder = OneHotEncoder(sparse_output=False)

encoded = encoder.fit_transform(df[["Department"]])

encoded_df = pd.DataFrame(encoded,columns=encoder.get_feature_names_out(["Department"]))

print(encoded_df)


####    OUTPUT   ####
#    Department_AI  Department_Data Science  Department_Python
# 0            1.0                      0.0                0.0
# 1            0.0                      0.0                1.0
# 2            0.0                      1.0                0.0
# 3            1.0                      0.0                0.0