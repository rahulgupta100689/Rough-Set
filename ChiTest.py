import pandas as pd
import csv
from sklearn.preprocessing import LabelEncoder
from sklearn.feature_selection import chi2
with open("/media/rahul/cd854f04-608f-4627-9e70-9096a8520b95/rahul2022/permissions_chi.csv", 'w', newline='') as csvfilew1:
    fields = ['index', 'feature name', 'p_value']
    csvwriter1 = csv.DictWriter(csvfilew1, fieldnames = fields)
    csvwriter1.writeheader()
    with open("/media/rahul/cd854f04-608f-4627-9e70-9096a8520b95/rahul2022/permissions_correl.csv") as csv_read:
        csv_reader = csv.DictReader(csv_read)
        for i, row in enumerate(csv_reader):
            csv_data = dict().fromkeys(fields)
            csv_data['index'] = row['index']
            cols = []
            cols.append(int(0))
            cols.append(int(row['index']))
            
            df = pd.read_csv("/media/rahul/cd854f04-608f-4627-9e70-9096a8520b95/rahul2022/features_file_ml7.csv", usecols = cols)
            df.apply(LabelEncoder().fit_transform)
            x = df.drop(labels='label', axis=1)
            y = df['label']
            chi_scores = chi2(x,y)
            if(chi_scores[1] < 0.05):
                f_name = str(x.columns)
                f_name = f_name[8:-19]
                csv_data['feature name'] = f_name
                p_val = str(chi_scores[1])
                p_val = p_val[1:-1]
                csv_data['p_value'] = p_val
                csvwriter1.writerow(csv_data)
            