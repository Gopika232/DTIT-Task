import pandas as pd

from sklearn.model_selection import train_test_split   #type:ignore
from sklearn.preprocessing import LabelEncoder, OneHotEncoder     #type:ignore
from sklearn.tree import DecisionTreeClassifier     #type:ignore
from sklearn.metrics import accuracy_score      #type:ignore


data = pd.read_csv("data.csv")


# Example:
# Gender,Age,Salary,Purchased

X = data[['Age','Salary','Gender']]
y = data['Purchased']


# Split

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)

# Label Encoding

le = LabelEncoder()

X_train_le = X_train.copy()
X_test_le = X_test.copy()

X_train_le['Gender'] = le.fit_transform(X_train_le['Gender'])

X_test_le['Gender'] = le.transform(X_test_le['Gender'])

model = DecisionTreeClassifier()
model.fit(X_train_le,y_train)

pred = model.predict(X_test_le)
print("Label Encoding Accuracy:",accuracy_score(y_test,pred))



# One Hot Encoding

X_ohe = pd.get_dummies(X,columns=['Gender'])

X_train,X_test,y_train,y_test = train_test_split(X_ohe,y,test_size=0.2,random_state=42)
model.fit(X_train,y_train)

pred = model.predict(X_test)

print("One Hot Encoding Accuracy:",accuracy_score(y_test,pred))


#####      OUTPUT      #####
# Label Encoding Accuracy: 0.5
# One Hot Encoding Accuracy: 0.5