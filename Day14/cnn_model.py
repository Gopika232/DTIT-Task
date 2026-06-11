import tensorflow as tf    #type:ignore
from tensorflow.keras import layers, models    #type:ignore
import matplotlib.pyplot as plt    #type:ignore

# Load CIFAR-10 dataset
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.cifar10.load_data()

# Normalize pixel values
x_train = x_train / 255.0
x_test = x_test / 255.0

# Class names
classes = ["airplane","automobile","bird","cat","deer","dog","frog","horse","ship","truck"]

# CNN Model
model = models.Sequential([
    # First convolution block
    layers.Conv2D(32,(3,3),activation="relu",input_shape=(32,32,3)),
    layers.MaxPooling2D((2,2)),
    # Second convolution block
    layers.Conv2D(64,(3,3),activation="relu"),
    layers.MaxPooling2D((2,2)),
    # Third convolution block
    layers.Conv2D(64,(3,3),activation="relu"),
    # Convert feature maps
    layers.Flatten(),
    # Fully connected layers
    layers.Dense(64,activation="relu"),layers.Dense(10,activation="softmax")])

# Display model
model.summary()

# Compile
model.compile(optimizer="adam",loss="sparse_categorical_crossentropy",metrics=["accuracy"])

# Train
history = model.fit(x_train,y_train,epochs=10,batch_size=64,validation_data=(x_test,y_test))

# Evaluate
loss, accuracy = model.evaluate(x_test,y_test)
print("\nCNN Test Accuracy:")
print(accuracy*100)

# Prediction
predictions = model.predict(x_test)
index = 5
predicted_class = classes[predictions[index].argmax()]
actual_class = classes[y_test[index][0]]
print("\nPredicted:",predicted_class)
print("Actual:",actual_class)

# Show image
plt.imshow(x_test[index])
plt.title("Predicted: "+predicted_class)
plt.axis("off")
plt.show()


###  OUTPUT  ###

# CNN Test Accuracy:
# 71.64999842643738

# Predicted: frog
# Actual: frog