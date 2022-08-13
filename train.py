#!/usr/bin/env python
# coding: utf-8

import pickle

import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction import DictVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score
from sklearn.pipeline import make_pipeline 


input_data = './data/data.csv'
output_model = './artifacts/pipeline.bin'

print(f'reading data from {input_data}...')
df = pd.read_csv(input_data)


df_train_all, df_test = train_test_split(df, test_size=0.2, random_state=1)


categorical = [
    'type_school', 'school_accreditation', 'gender', 'interest', 'residence',
    'parent_was_in_college'
]

numerical = [
    'parent_age', 'parent_salary', 'house_area', 'average_grades'
]

df_train, df_val = train_test_split(df_train_all, test_size=0.25, random_state=1)

y_train = df_train.in_college.astype(int).values
y_val = df_val.in_college.astype(int).values


train_dicts = df_train[categorical + numerical].to_dict(orient='records')
val_dicts = df_val[categorical + numerical].to_dict(orient='records')


pipeline = make_pipeline(
    DictVectorizer(),
    LogisticRegression()
)

pipeline.fit(train_dicts, y_train)
y_pred = pipeline.predict_proba(val_dicts)[:, 1]

auc = roc_auc_score(y_val, y_pred)

print(f'validation score: {auc:0.3f}')


print(f'saving model to {output_model}... ')

with open(output_model, 'wb') as f_out:
    pickle.dump(pipeline, f_out)
