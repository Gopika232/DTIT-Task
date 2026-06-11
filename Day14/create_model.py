
import tensorflow as tf  #type:ignore
import numpy as np

model = tf.keras.Sequential([
    tf.keras.layers.Input(shape=(4,)),
    tf.keras.layers.Dense(128,activation="relu"),
    tf.keras.layers.Dense(64,activation="relu"),
    tf.keras.layers.Dense(1,activation="sigmoid")])
model.compile(optimizer="adam",loss="binary_crossentropy",metrics=["accuracy"])

# Convert list to numpy array
X = np.array([[5.1,3.5,1.4,0.2],[6.2,3.4,5.4,2.3],[5.9,3.0,4.2,1.5],[4.9,3.1,1.5,0.1]])
y = np.array([0,1,1,0])
model.fit(X,y,epochs=5)
model.export("model")
print("Model saved successfully")

