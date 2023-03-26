
"""
PROTOBUF:

The data in a TFRecord file is stored as binary records, with each record being a serialized protocol buffer (protobuf).
A protocol buffer is a compact binary data format that stores data structures in a compact and efficient manner. 
It provides a compact binary representation of structured data and is used to exchange data between systems or to store data in a file.
The structure of the data in a protobuf is defined using a schema, which specifies the data type of each field in the record.
The schema is typically defined in a .proto file, which is used to generate code that can serialize and deserialize the data.
"""

"""
.proto: 

Protobufs work by defining the structure of the data to be encoded in a .proto file, which serves as a contract between the client and the server.
The .proto file contains a list of fields, their data types, and the order in which they appear.
Once the .proto file is defined, the protobuf compiler generates code in multiple languages that can be used to encode and decode the data in the defined format. 
During encoding, the data is packed into binary format and written to a file or transmitted over the network. During decoding, 
the binary data is read, unpacked, and transformed back into the original data structure.

Protobufs provide several benefits compared to other data serialization formats, such as smaller message sizes, 
faster serialization and deserialization times, and backwards and forwards compatibility. This makes protobufs well-suited for use in high-performance systems 
where low latency and small payload sizes are important.
"""

"""
TFRECORD:

The data in a TFRecord file is stored as binary records, with each record being a serialized protocol buffer (protobuf).
To create a TFRecord file, you first need to serialize each record (i.e., convert it from a Python object to a binary representation), 
and then write each serialized record to the file.

- Tf records are Tensorflow custom data format
- They are not required to train a model with Tensorflow but muy help to speed up data loading. 
- Their Structure is defined by proto files
- Tf records are created using Protocol buffers (protobuf), a mechanism to serialize data. 

"""

import tensorflow as tf

tfrecord_file = 'data.tfrecord'
# STORE TFRECORD DATA

def serialize_example(label, image_string):
    feature = {
        'label': tf.train.Feature(int64_list=tf.train.Int64List(value=[label])),
        'image': tf.train.Feature(bytes_list=tf.train.BytesList(value=[image_string])),
    }

    example_proto = tf.train.Example(features=tf.train.Features(feature=feature))
    return example_proto.SerializeToString()

def write_to_tfrecord(tfrecord_file, labels, images):
    with tf.io.TFRecordWriter(tfrecord_file) as writer:
        for label, image in zip(labels, images):
            serialized_example = serialize_example(label, image)
            writer.write(serialized_example)

# example usage
labels = [0, 1, 2, 3]
images = [b'image1', b'image2', b'image3', b'image4']
write_to_tfrecord(tfrecord_file, labels, images)


# LOAD TFRECORD DATA

def parse_example(serialized_example):
    feature_description = {
        'label': tf.io.FixedLenFeature([], tf.int64, default_value=0),
        'image': tf.io.FixedLenFeature([], tf.string, default_value=''),
    }
    example = tf.io.parse_single_example(serialized_example, feature_description)
    return example['label'], example['image']

def read_from_tfrecord(tfrecord_file):
    dataset = tf.data.TFRecordDataset(tfrecord_file)
    
    
dataset = read_from_tfrecord(tfrecord_file)