# CTP9-Credit Card Fraud Detection using Neural Networks

![image](https://github.com/user-attachments/assets/aaacb2c0-4961-4758-b8f8-9090749d4a92)


- In this project, we aim to expand upon current methods of binary classification of fraudulent credit card transactions in a synthesized dataset. Current methods with this dataset have been with Support Vector Machine (SVM) and Logisitc Regression. We propose a neural network as it can take advantage of the large number of samples within the dataset and potentially pick out complex patterns more effectively.
- In this notebook, we explore the dataset's features by checking for multicollinearity, analyzing feature distributions and class distribution, and augmenting the dataset by appending a new column called "Per Change" which represents the percent change from the beginning of a transaction to the end of the transaction.
- We implement a leakyReLu acitivation function to take into account the negative values that our augmented dataset contains. We also perform Synthetic Minority Oversampling Technique to make up in our dataset's class imbalance. 
