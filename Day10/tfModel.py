import tensorflow as tf    #type:ignore
from tensorflow.keras.datasets import mnist    #type:ignore


(X_train,y_train),(X_test,y_test)=mnist.load_data()


X_train = X_train / 255.0
X_test = X_test / 255.0

model = tf.keras.Sequential([tf.keras.layers.Flatten(input_shape=(28,28)),tf.keras.layers.Dense(128,activation="relu"),tf.keras.layers.Dense(10,activation="softmax")])


model.compile(optimizer="adam",loss="sparse_categorical_crossentropy",metrics=["accuracy"])

model.fit(X_train,y_train,epochs=5)

loss,accuracy = model.evaluate(X_test,y_test)


print("Accuracy:",accuracy)


####   OUTPUT   #####

# Epoch 1/5
# 1875/1875 ━━━━━━━━━━━━━━━━━━━━ 6s 3ms/step - accuracy: 0.9272 - loss: 0.2554     
# Epoch 2/5
# 1875/1875 ━━━━━━━━━━━━━━━━━━━━ 5s 3ms/step - accuracy: 0.9668 - loss: 0.1112   
# Epoch 3/5
# 1875/1875 ━━━━━━━━━━━━━━━━━━━━ 6s 3ms/step - accuracy: 0.9766 - loss: 0.0773   
# Epoch 4/5
# 1875/1875 ━━━━━━━━━━━━━━━━━━━━ 5s 3ms/step - accuracy: 0.9828 - loss: 0.0577   
# Epoch 5/5
# 1875/1875 ━━━━━━━━━━━━━━━━━━━━ 5s 3ms/step - accuracy: 0.9857 - loss: 0.0451  
# 313/313 ━━━━━━━━━━━━━━━━━━━━ 1s 2ms/step - accuracy: 0.9761 - loss: 0.0808   
# Accuracy: 0.9761000275611877