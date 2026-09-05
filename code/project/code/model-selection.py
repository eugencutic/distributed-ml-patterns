import os
import shutil

import tensorflow as tf
import tensorflow_datasets as tfds
from tensorflow import keras

# # Scaling MNIST data from (0, 255] to (0., 1.]
# def scale(image, label):
#   image = tf.cast(image, tf.float32)
#   image /= 255
#   return image, label

# best_model_path = ""
# best_accuracy = 0
# for i in range(1, 4):
#   model_path = "trained_model/saved_model_versions/" + str(i)
#   model = keras.models.load_model(model_path)
#   datasets, _ = tfds.load(name='fashion_mnist', with_info=True, as_supervised=True)
#   ds = datasets['test'].map(scale).cache().shuffle(10000).batch(64)
#   _, accuracy = model.evaluate(ds)
#   if accuracy > best_accuracy:
#     best_accuracy = accuracy
#     best_model_path = model_path

# destination = "trained_model/saved_model_versions/4"
# if os.path.exists(destination):
#   shutil.rmtree(destination)

# shutil.copytree(best_model_path, destination)
# print("Best model with accuracy %f is copied to %s" % (best_accuracy, destination))

def scale(image, label):
  image = tf.cast(image, tf.float32)
  image = image / 255
  return image, label

best_model_path = "" 
best_accuracy = 0

datasets, _ = tfds.load(name='fashion_mnist', with_info=True, as_supervised=True)
ds = datasets['test'].map(scale).cache().batch(64)

for i in range(1, 4):
  model_path = f"trained_model/saved_model_versions/{i}"
  model = keras.models.load_model(model_path)

  _, accuracy = model.evaluate(ds)

  if accuracy > best_accuracy:
    best_accuracy = accuracy
    best_model_path = model_path

destination = "trained_model/saved_model_versions/4"
if os.path.exists(destination):
  shutil.rmtree(destination)

shutil.copytree(best_model_path, destination)
print("Best model with accuracy %f is copied to %s" % (best_accuracy, destination))
