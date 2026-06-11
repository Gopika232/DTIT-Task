from sklearn.datasets import load_iris    #type:ignore
from sklearn.ensemble import RandomForestClassifier    #type:ignore
import joblib     #type:ignore
import time

data = load_iris()

X = data.data
y = data.target


print("Dataset Loaded")
print("Features:", X.shape[1])
print("\nOriginal Model")
original_model = RandomForestClassifier(n_estimators=200,random_state=42)

original_model.fit(X,y)


# Measure inference time
start = time.time()
prediction = original_model.predict([[5.1,3.5,1.4,0.2]])

end = time.time()

original_time = end-start

print("Prediction:",prediction)
print("Inference Time:",original_time,"seconds")

# Save original model
joblib.dump(original_model,"original_model.pkl")

print("\nOptimized Model")


optimized_model = RandomForestClassifier(
    # Reduced trees
    n_estimators=50,
    # Reduced depth
    max_depth=5,
    random_state=42)

optimized_model.fit(X,y)
start = time.time()
optimized_prediction = optimized_model.predict([[5.1,3.5,1.4,0.2]])
end = time.time()
optimized_time = end-start

print("Prediction:",optimized_prediction)
print("Inference Time:",optimized_time,"seconds")


# Save optimized model
joblib.dump(optimized_model,"optimized_model.pkl")

print("\nLoading Saved Model")

loaded_model = joblib.load("optimized_model.pkl")

result = loaded_model.predict([[6.1,2.8,4.7,1.2]])

print("Loaded Model Prediction:",result)

print("\nOptimization Result")

print("Original Time:",original_time)

print("Optimized Time:",optimized_time)

difference = (original_time - optimized_time)

print("Time Reduced:",difference,"seconds")

print("\nTechniques Used:")
print("1. Reduced number of Random Forest trees")
print("2. Limited tree depth")
print("3. Saved model using Joblib")
print("4. Faster loading without retraining")
print("5. Reduced computation during inference")



####     OUTPUT     ####

# Dataset Loaded
# Features: 4

# Original Model
# Prediction: [0]
# Inference Time: 0.006028890609741211 seconds

# Optimized Model
# Prediction: [0]
# Inference Time: 0.0010442733764648438 seconds

# Loading Saved Model
# Loaded Model Prediction: [1]

# Optimization Result
# Original Time: 0.006028890609741211
# Optimized Time: 0.0010442733764648438
# Time Reduced: 0.004984617233276367 seconds

# Techniques Used:
# 1. Reduced number of Random Forest trees
# 2. Limited tree depth
# 3. Saved model using Joblib
# 4. Faster loading without retraining
# 5. Reduced computation during inference