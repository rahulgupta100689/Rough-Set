#Reduct calculation
import numpy as np
import csv
#Mat = np.full([300, 300], '', dtype='object')
Mat = np.load(r"/media/rahul/cd854f04-608f-4627-9e70-9096a8520b95/rahul2022/Matsys_cmd.npy", allow_pickle= True)

with open(r"/media/rahul/cd854f04-608f-4627-9e70-9096a8520b95/rahul2022/syscmd_rank.csv") as csv_read:
    csv_reader = csv.DictReader(csv_read)
    perDic = {}
    fNameDic = {}
    for i, row in enumerate(csv_reader):
        #print(row['index'])
        #perDic = dict().fromkeys(row['index'])
        perDic[row['index']] = row['score']
        fNameDic[row['index']] = row['featureName']
    #print(perDic)
    fields = ['index', 'featureName', 'score']
    with open(r"/media/rahul/cd854f04-608f-4627-9e70-9096a8520b95/rahul2022/syscmd_red.csv", mode='w', newline='') as csv_read1:
        csv_writter1 = csv.DictWriter(csv_read1, fieldnames=fields)
        csv_writter1.writeheader()
        redSetRows = dict().fromkeys(fields)
        redlist = []
        for i in range(0,22000):
            for j in range(0,22000):
                x = Mat[i][j]
                x = x.split('#')
                l = len(x)
                #print(l)
                #print(x)
                if l > 1:
                    red = x[0]
                    z = x[1:]
                    for y in z:
                        if(perDic[red]>perDic[y]):
                            red = y
                    if(red in redlist):
                        pass
                    else:
                        redlist.append(red)
                        redSetRows['index'] = red
                        redSetRows['featureName'] = fNameDic[red]
                        redSetRows['score'] = perDic[red]
                        csv_writter1.writerow(redSetRows)
