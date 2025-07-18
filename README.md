# Credit-Card-Fraud-Detection-
Credit card fraud detection using logistic regression 

This project involves building a credit card fraud detection model using logistic regression.
We begin by downloading the dataset from Kaggle: https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud?resource=download. In this dataset, confidential details have been anonymized using Principal Component Analysis (PCA), which transforms the original features into numerical components.

The dataset is highly imbalanced, as the number of legitimate (non-fraudulent) transactions vastly outnumbers the fraudulent ones. To address this imbalance, we split the data into two separate subsets: one for legitimate transactions and one for fraudulent transactions. We then sample an equal number of legitimate and fraudulent transactions to create a balanced dataset.

Next, we apply logistic regression to this balanced dataset. The data is split into 80% training and 20% testing, with a random state set to 2 to ensure reproducibility.

The model achieves an accuracy of 94.79% on the training data and 93.40% on the testing data.

👨‍💻 Author
 
Chandrajit Banerjee 

Email: chandrajitbanerjee.bcrec@gmail.com

Phone: 6289317043 / 9163306289
