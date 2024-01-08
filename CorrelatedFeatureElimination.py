import numpy as np
import csv
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
import warnings
warnings.filterwarnings("ignore")
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import confusion_matrix
import statsmodels.api as sm
import gc
gc.collect()
cols = [int(0)]
for i in range(5726, 7854):
    print(i)
    cols.append(i)
with open("/media/rahul/cd854f04-608f-4627-9e70-9096a8520b95/rahul2022/features_file_ml7.csv", mode='r') as csv_read:
    csv_reader = csv.DictReader(csv_read)
    data = pd.read_csv("/media/rahul/cd854f04-608f-4627-9e70-9096a8520b95/rahul2022/features_file_ml7.csv", usecols = cols)
    label_encoder = LabelEncoder()
    data.iloc[:,0] = label_encoder.fit_transform(data.iloc[:,0]).astype('float64')
    corr = data.corr()
    columns = np.full((corr.shape[0],), True, dtype=bool)
    for i in range(corr.shape[0]):
        print(i)
        for j in range(i+1, corr.shape[0]):
            if corr.iloc[i,j] >= 0.9:
                if corr.iloc[i,j] >= 0.9:
                    if columns[j]:
                        columns[j] = False
    selected_columns = data.columns[columns]
    selected_columns = selected_columns[1:].values
    
    data = data[selected_columns]
    with open("/media/rahul/cd854f04-608f-4627-9e70-9096a8520b95/rahul2022/permissions_correl.csv", mode='w', newline='') as csvfilew1:
        fields = ['index', 'f_name']
        csvwriter1 = csv.DictWriter(csvfilew1, fieldnames= fields)
        csvwriter1.writeheader()
        col_names = []
        col_names = data.columns
        c = 0
        for ycol in data.columns:
            c = c+1
            print(ycol)
        print(c)
        
        j=0
        for i in range(1, 5502):
            matrixrows= dict().fromkeys(fields)
            if(j==c):
                break
            else:
                if(csv_reader.fieldnames[i] == col_names[j]):
                    matrixrows['index'] = i
                    matrixrows['f_name'] = data.columns[j]
                    csvwriter1.writerow(matrixrows)
                    j = j + 1
                else:
                    pass
        print(j)
        
        del cols
        del col_names
        del data
        gc.collect()