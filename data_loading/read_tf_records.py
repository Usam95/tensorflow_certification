
import tensorflow as tf


# Create a description of the features.
feature_description = {
    'feature0': tf.io.FixedLenFeature([], tf.int64, default_value=0),
    'feature1': tf.io.FixedLenFeature([], tf.int64, default_value=0),
    'feature2': tf.io.FixedLenFeature([], tf.string, default_value=''),
    'feature3': tf.io.FixedLenFeature([], tf.float32, default_value=0.0),
}

def _parse_function(example_proto):
  # Parse the input `tf.train.Example` proto using the dictionary above.
  return tf.io.parse_single_example(example_proto, feature_description)


"""
DESCRIPTION: 
tf.io.FixedLenFeature is a TensorFlow function that is used to parse features in TensorFlow's tf.train.Example format. 
The FixedLenFeature function allows you to specify that a certain feature should have a fixed length when being parsed from a tf.train.Example protobuf.

For example, if you have a feature called "age" that you expect to always be a scalar value, you can specify this as follows:

features = {
    "age": tf.io.FixedLenFeature([], tf.int64)
}
When parsing a tf .train.Example protobuf using tf.io.parse_single_example, you can pass in the features dictionary to specify the expected format of the features. 
TensorFlow will then use the specified formats to parse the tf.train.Example and extract the values of the features.
"""
