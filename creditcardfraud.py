# -*- coding: utf-8 -*-
"""creditcardFraud.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1SZxqllZ6T_lHQYK2NYzGa26xUAwedIJb
"""

#importing Libaries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

#reading the dataset
df=pd.read_csv("/content/creditcard.csv")
df

# dataset informations
df.info()

# checking the number of missing values in each column
df.isnull().sum()

df['Class'].value_counts()

sns.countplot(x='Class', data=df)
plt.title('Distribution of Class (Good vs. Fraud)')
plt.xlabel('Class (0: Good, 1: Fraud)')
plt.ylabel('Count')
plt.show()

good=df[df.Class==0]
fraud=df[df.Class==1]
print(good.shape)
print(fraud.shape)

good.Amount.describe()

fraud.Amount.describe()

good1=good.sample(n=492)

dff=pd.concat([good1,fraud],axis=0)
dff

sns.countplot(x='Class', data=dff)
plt.title('Distribution of Class (Good vs. Fraud)')
plt.xlabel('Class (0: Good, 1: Fraud)')
plt.ylabel('Count')
plt.show()

x=dff.drop(columns='Class')
y=dff['Class']

print(x)
print(y)

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,stratify=y,random_state=2)

model=LogisticRegression()

model.fit(x_train,y_train)

x_train_prediction=model.predict(x_train)
training_data_accuracy=accuracy_score(x_train_prediction,y_train)
print('Accuracy on Training data : ', training_data_accuracy*100)

x_test_prediction=model.predict(x_test)
training_data_accuracy=accuracy_score(x_test_prediction,y_test)
print('Accuracy on Testing data : ', training_data_accuracy*100)
