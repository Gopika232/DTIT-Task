import pandas as pd

data = {'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
        'Age': [25, 30, 35, 40, 45],}
df = pd.DataFrame(data)
print("DataFrame:")
print(df)


#Specific Column print
print("\nName Column :")
print(df['Name'])

#add column
df['City'] = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix']
print(df)