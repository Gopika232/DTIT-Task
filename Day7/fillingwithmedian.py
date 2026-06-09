import pandas as pd

def fill_missing_values(df):

    for column in df.columns:
        df[column] = df[column].fillna(df[column].median())

    return df


data = {
    "Age":[20,25,None,30],
    "Marks":[80,None,90,95]
}

df = pd.DataFrame(data)

print(fill_missing_values(df))


####   OUTPUT  ####

#     Age  Marks
# 0  20.0   80.0
# 1  25.0   90.0
# 2  25.0   90.0
# 3  30.0   95.0