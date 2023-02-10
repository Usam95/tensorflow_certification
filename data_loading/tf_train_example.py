

"""
tf.train.Example is a protocol buffer structure in TensorFlow that is used to store a single instance of data. 
It consists of a set of named fields, where each field contains one or more values. The fields can store values 
of different data types such as integers, bytes, floating-point numbers, etc.
The tf.train.Example protocol buffer can be used to store instances of data in a TensorFlow TFRecord file. The TFRecord
file format is a common format for storing large datasets in TensorFlow and is often used in machine learning applications for storing and loading training and testing data.
To create an instance of tf.train.Example, you need to first create a tf.train.Features object that contains the 
fields and their values. Then you can pass the tf.train.Features object to the tf.train.Example constructor to create an instance of tf.train.Example.
"""


"""
Here is an example of how you can use tf.train.Example to store data in a TensorFlow TFRecord file:
"""
import tensorflow as tf

# EXAMPLE 1

# Define the features you want to store
feature = {
    'age': tf.train.Feature(int64_list=tf.train.Int64List(value=[32])),
    'name': tf.train.Feature(bytes_list=tf.train.BytesList(value=[b'John Doe'])),
    'height': tf.train.Feature(float_list=tf.train.FloatList(value=[1.75]))
}

# Create a Features object
features = tf.train.Features(feature=feature)

# Create an Example object
example = tf.train.Example(features=features)

# Serialize the Example object to a string
serialized_example = example.SerializeToString()

# Write the serialized Example object to a TFRecord file
with tf.io.TFRecordWriter("example.tfrecord") as writer:
    writer.write(serialized_example)
    
    
# EXAMPLE 2: 

# Sample person data
name = "John Doe"
age = 30
address = "123 Main St, Anytown USA"
is_employed = True

# Creating features
name_feature = tf.train.Feature(bytes_list=tf.train.BytesList(value=[name.encode()]))
age_feature = tf.train.Feature(int64_list=tf.train.Int64List(value=[age]))
address_feature = tf.train.Feature(bytes_list=tf.train.BytesList(value=[address.encode()]))
is_employed_feature = tf.train.Feature(int64_list=tf.train.Int64List(value=[int(is_employed)]))

# Creating a Example
person_example = tf.train.Example(features=tf.train.Features(feature={
    'name': name_feature,
    'age': age_feature,
    'address': address_feature,
    'is_employed': is_employed_feature
}))

# Serializing the Example
person_example_serialized = person_example.SerializeToString()

# Write the serialized Example object to a TFRecord file
with tf.io.TFRecordWriter("example.tfrecord") as writer:
    writer.write(person_example_serialized)
    
    
    
# DESERIALIZING: 

# Load the serialized example from disk
with tf.io.TFRecordReader("path/to/example.tfrecord") as reader:
  serialized_example = reader.read()

# Deserialize the example into a dictionary
example = tf.train.Example.FromString(serialized_example)
parsed_example = example.features.feature

# Extract values from the parsed example
age = parsed_example["age"].int64_list.value[0]
name = parsed_example["name"].bytes_list.value[0].decode()

"""
In this example, we use a tf.io.TFRecordReader to read a single serialized example from disk. 
The tf.train.Example.FromString method is then used to deserialize the serialized_example back into a tf.train.Example protocol buffer.
"""
