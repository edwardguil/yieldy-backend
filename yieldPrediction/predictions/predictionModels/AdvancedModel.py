from __future__ import absolute_import, division, print_function, unicode_literals

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import tensorflow as tf

dftrain = pd.read_csv('~\\Toowoomba - Barley.csv')
dfeval = pd.read_csv('~\\Toowoomba - Barley.csv')
y_train = dftrain.pop('Yield')
y_eval = dfeval.pop('Yield')
dftrain.pop('DISCARD')
dfeval.pop('DISCARD')

CATEGORICAL_COLUMNS = ['Month', 'Postcode']
NUMERIC_COLUMNS = ['SolarExposure', 'Rainfall', 'Year']

feature_columns = []
for feature_name in CATEGORICAL_COLUMNS:
    vocabulary = dftrain[feature_name].unique()
    feature_columns.append(tf.feature_column.categorical_column_with_vocabulary_list(feature_name, vocabulary))

for feature_name in NUMERIC_COLUMNS:
    feature_columns.append(tf.feature_column.numeric_column(feature_name, dtype=tf.float32))


def make_input_fn(data_df, label_df, num_epochs=1, shuffle=False, batch_size=32):
  def input_function():
    ds = tf.data.Dataset.from_tensor_slices((dict(data_df), label_df))
    if shuffle:
      ds = ds.shuffle(1000)
    ds = ds.batch(batch_size).repeat(num_epochs)
    return ds
  return input_function

train_input_fn = make_input_fn(dftrain, y_train)
eval_input_fn = make_input_fn(dfeval, y_eval, num_epochs=1, shuffle=False)

linear_est = tf.estimator.LinearClassifier(feature_columns=feature_columns)

linear_est.train(train_input_fn)
result = linear_est.evaluate(eval_input_fn)
