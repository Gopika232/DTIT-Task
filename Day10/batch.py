import pandas as pd
import joblib #type:ignore


model = joblib.load("model.pkl")

data = pd.read_csv("data.csv")

data["prediction"] = model.predict(data[["sepal_length","sepal_width","petal_length","petal_width"]])
print(data)