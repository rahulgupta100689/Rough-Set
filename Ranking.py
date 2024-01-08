#ranking
import numpy as np
import csv
#Mat = np.full([300, 300], '', dtype='object')
Mat = np.load(r"/media/rahul/cd854f04-608f-4627-9e70-9096a8520b95/rahul2022/Matsys_cmd.npy", allow_pickle= True)

with open(r"/media/rahul/cd854f04-608f-4627-9e70-9096a8520b95/rahul2022/syscmd_chi.csv") as csv_read:
    csv_reader = csv.DictReader(csv_read)
    perDic = {}
    fNameDic = {}
    for i, row in enumerate(csv_reader):
        #print(row['index'])
        #perDic = dict().fromkeys(row['index'])
        perDic[row['index']] = 0
        fNameDic[row['index']] = row['feature name']
    #print(perDic)

    for i in range(0,22000):
        for j in range(0,22000):
            x = Mat[i][j]
            x = x.split('#')
            l = len(x)
            #print(l)
            #print(x)
            if l > 1:
                for y in x:
                    #print(y)
                    perDic[y] = perDic[y] + (52/l)
    fields = ['index', 'featureName', 'score']
    with open(r"/media/rahul/cd854f04-608f-4627-9e70-9096a8520b95/rahul2022/syscmd_rank.csv", mode='w', newline='') as csv_read1:
        csv_writter1 = csv.DictWriter(csv_read1, fieldnames=fields)
        csv_writter1.writeheader()
        matrixrows = dict().fromkeys(fields)
        for k in perDic.keys():
            matrixrows['index'] = k
            matrixrows['featureName'] = fNameDic[k]
            matrixrows['score'] = perDic[k]
            csv_writter1.writerow(matrixrows)
        #print(matrixrows)
        #for data in matrixrows:
            #csv_writter1.writerow(data)


    #print(perDic)