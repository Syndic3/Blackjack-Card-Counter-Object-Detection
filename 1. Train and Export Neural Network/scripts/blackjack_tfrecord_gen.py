"""
Usage:
  # From tensorflow/models/
  # Create train data:
  python generate_tfrecord.py --csv_input=data/train_labels.csv  --output_path=train.record
  # Create test data:
  python generate_tfrecord.py --csv_input=data/test_labels.csv  --output_path=test.record
  python generate_tfrecord.py --csv_input=data/test_labels.csv  --output_path=data/test.record --image_dir=images/

  python tfrecord.py --csv_input=data/csv_inputs/_annotations_test.csv  --output_path=test.record --image_dir=data/test

"""

# taken from https://github.com/datitran/raccoon_dataset

from __future__ import division
from __future__ import print_function
from __future__ import absolute_import

import os
import io
import pandas as pd
#import tensorflow as tf
import tensorflow.compat.v1 as tf

from PIL import Image
from object_detection.utils import dataset_util
from collections import namedtuple, OrderedDict

flags = tf.app.flags
flags.DEFINE_string('csv_input', '', 'Path to the CSV input')
flags.DEFINE_string('output_path', '', 'Path to output TFRecord')
flags.DEFINE_string('image_dir', '', 'Path to images')
FLAGS = flags.FLAGS


# replace row_label with the name you annotated your images as
def class_text_to_int(row_label):
    if row_label == 'AH':
        return 1
    elif row_label == '2H':
        return 2
    elif row_label == '3H':
        return 3
    elif row_label == '4H':
        return 4
    elif row_label == '5H':
        return 5
    elif row_label == '6H':
        return 6
    elif row_label == '7H':
        return 7
    elif row_label == '8H':
        return 8
    elif row_label == '9H':
        return 9
    elif row_label == '10H':
        return 10
    elif row_label == 'JH':
        return 11
    elif row_label == 'QH':
        return 12
    elif row_label == 'KH':
        return 13
    elif row_label == 'AS':
        return 14
    elif row_label == '2S':
        return 15
    elif row_label == '3S':
        return 16
    elif row_label == '4S':
        return 17
    elif row_label == '5S':
        return 18
    elif row_label == '6S':
        return 19
    elif row_label == '7S':
        return 20
    elif row_label == '8S':
        return 21
    elif row_label == '9S':
        return 22
    elif row_label == '10S':
        return 23
    elif row_label == 'JS':
        return 24
    elif row_label == 'QS':
        return 25
    elif row_label == 'KS':
        return 26
    elif row_label == 'AC':
        return 27
    elif row_label == '2C':
        return 28
    elif row_label == '3C':
        return 29
    elif row_label == '4C':
        return 30
    elif row_label == '5C':
        return 31
    elif row_label == '6C':
        return 32
    elif row_label == '7C':
        return 33
    elif row_label == '8C':
        return 34
    elif row_label == '9C':
        return 35
    elif row_label == '10C':
        return 36
    elif row_label == 'JC':
        return 37
    elif row_label == 'QC':
        return 38
    elif row_label == 'KC':
        return 39
    elif row_label == 'AD':
        return 40
    elif row_label == '2D':
        return 41
    elif row_label == '3D':
        return 42
    elif row_label == '4D':
        return 43
    elif row_label == '5D':
        return 44
    elif row_label == '6D':
        return 45
    elif row_label == '7D':
        return 46
    elif row_label == '8D':
        return 47
    elif row_label == '9D':
        return 48
    elif row_label == '10D':
        return 49
    elif row_label == 'JD':
        return 50
    elif row_label == 'QD':
        return 51
    elif row_label == 'KD':
        return 52
    else:
        return 0  # originalyl as "None" we need int therefore changed to 0


def split(df, group):
    data = namedtuple('data', ['filename', 'object'])
    gb = df.groupby(group)
    return [data(filename, gb.get_group(x)) for filename, x in zip(gb.groups.keys(), gb.groups)]


def create_tf_example(group, path):
    with tf.gfile.GFile(os.path.join(path, '{}'.format(group.filename)), 'rb') as fid:
        encoded_jpg = fid.read()
    encoded_jpg_io = io.BytesIO(encoded_jpg)
    image = Image.open(encoded_jpg_io)
    width, height = image.size

    filename = group.filename.encode('utf8')
    image_format = b'jpg'
    xmins = []
    xmaxs = []
    ymins = []
    ymaxs = []
    classes_text = []
    classes = []

    for index, row in group.object.iterrows():
        xmins.append(row['xmin'] / width)
        xmaxs.append(row['xmax'] / width)
        ymins.append(row['ymin'] / height)
        ymaxs.append(row['ymax'] / height)
        classes_text.append(row['class'].encode('utf8'))
        classes.append(class_text_to_int(row['class']))

    tf_example = tf.train.Example(features=tf.train.Features(feature={
        'image/height': dataset_util.int64_feature(height),
        'image/width': dataset_util.int64_feature(width),
        'image/filename': dataset_util.bytes_feature(filename),
        'image/source_id': dataset_util.bytes_feature(filename),
        'image/encoded': dataset_util.bytes_feature(encoded_jpg),
        'image/format': dataset_util.bytes_feature(image_format),
        'image/object/bbox/xmin': dataset_util.float_list_feature(xmins),
        'image/object/bbox/xmax': dataset_util.float_list_feature(xmaxs),
        'image/object/bbox/ymin': dataset_util.float_list_feature(ymins),
        'image/object/bbox/ymax': dataset_util.float_list_feature(ymaxs),
        'image/object/class/text': dataset_util.bytes_list_feature(classes_text),
        'image/object/class/label': dataset_util.int64_list_feature(classes),
    }))
    return tf_example


def main(_):
    writer = tf.python_io.TFRecordWriter(FLAGS.output_path)
    path = os.path.join(FLAGS.image_dir)
    examples = pd.read_csv(FLAGS.csv_input)
    grouped = split(examples, 'filename')
    for group in grouped:
        tf_example = create_tf_example(group, path)
        writer.write(tf_example.SerializeToString())

    writer.close()
    output_path = os.path.join(os.getcwd(), FLAGS.output_path)
    print('Successfully created the TFRecords: {}'.format(output_path))


if __name__ == '__main__':
    tf.app.run()
