
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import tensorflow as tf  #type:ignore
converter = tf.lite.TFLiteConverter.from_saved_model("model")

converter.optimizations = [tf.lite.Optimize.DEFAULT]

tflite_model = converter.convert()

with open("optimized_model.tflite","wb") as f:
    f.write(tflite_model)

print("Model optimized successfully")