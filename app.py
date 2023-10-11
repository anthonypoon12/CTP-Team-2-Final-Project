import pandas as pd
# import numpy as np
# import seaborn as sns
# import matplotlib.pyplot as plt
# from sklearn.preprocessing import LabelEncoder
# from sklearn.model_selection import train_test_split
# # from imblearn.over_sampling import SMOTE
# from sklearn.preprocessing import StandardScaler
# from sklearn.linear_model import LogisticRegression
from zipfile import ZipFile
import os

file_name = 'fraudulent-transactions-data.zip' #the file is your dataset exact name
if not os.path.isfile("Fraud.csv"):
    with ZipFile(file_name, 'r') as zip:
        zip.extractall()
        print('Done')

df = pd.read_csv('Fraud.csv')

print(df.head())