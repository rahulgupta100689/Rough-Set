import csv
import pandas as pd
import numpy as np
import multiprocessing
from joblib import Parallel, delayed
import os, signal
from tqdm import tqdm
p_id = os.getpid()
print(p_id)
with open(r"/media/rahul/cd854f04-608f-4627-9e70-9096a8520b95/rahul2022/opcode_chi.csv", mode='r') as csv_file:
    num_cores = multiprocessing.cpu_count()
    csv_reader_index = csv.DictReader(csv_file)
    indexCol = []
    indexCol.append(int(0))
    for i, row in enumerate(csv_reader_index):
        indexCol.append(int(row['index']))
    resIndexCol = indexCol[1:]
    df1 = pd.read_csv(r"/media/rahul/cd854f04-608f-4627-9e70-9096a8520b95/rahul2022/features_file_ml7.csv", usecols=indexCol)

    Mat = np.full([22000, 22000], '', dtype='object')
    def my_function(j, i):
        my_Mat = np.full([1, 1], '', dtype='object')
        if df1.iloc[i, 0] != df1.iloc[j, 0]:
            # print(f"i({df1.iloc[i, 0]}) and j({df1.iloc[j, 0]})")
            indexCount = 0
            for k in resIndexCol:
                indexCount = indexCount + 1
                x = df1.iloc[i, indexCount]
                y = df1.iloc[j, indexCount]
                # print(f"permission value i({x}) and j({y})")
                if (((x == 0) and (y !=0)) or((x != 0) and (y ==0))):
                    #print(f"permission value i({x}) and j({y})")
                    if my_Mat == '':
                        my_Mat = str(k)
                    else:
                        my_Mat += '#' + str(k)
                else:
                    pass
        else:
            pass
        return my_Mat
    my_list = list(range(0, 22000))
    #final_list = tqdm(my_list)
    for i in my_list:
        #print(f"value_i({i})")
        inputs = list(range(0, i))
        if __name__ == "__main__":
            processed_list = Parallel(n_jobs=num_cores)(delayed(my_function)(j, i) for j in inputs)
            jlen = len(processed_list)
            for l in range(0, jlen):
                if(processed_list[l] != ''):
                    Mat[i][l] = processed_list[l]
                else:
                    pass
    np.save(r"/media/rahul/cd854f04-608f-4627-9e70-9096a8520b95/rahul2022/opcodeMat", Mat)
    print("finished")
    os.kill(p_id, signal.SIGTERM)