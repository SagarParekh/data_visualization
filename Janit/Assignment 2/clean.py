import pandas as pd
import numpy as np
from pprint import pprint

dataset = pd.read_csv('10yearAUSOpenMatches.csv')


player = ""
flag1 = False
flag2 = False
break_sum = 0
count = 0

dataset.dropna(axis=0, thresh=4)
break1 = dataset.loc[dataset['break1'] == '-']

# print((dataset.loc[(dataset['player1'] == 'Radek Stepanek') & (dataset['winner1'].isnull() )]))

x= dataset.loc[(dataset['player1'] == 'Radek Stepanek') & (dataset['player2'] != 'Michael Berry')]
print(x.isnull().sum(axis=1))
for i in range(len(break1)):

    player = break1['player1'].iloc[i]

    breaks_when_player1 = (dataset.loc[(dataset['player1'] == player) & (dataset['break1'] != '-')])

    breaks_when_player2 = (dataset.loc[(dataset['player2'] == player) & (dataset['break2'] != '-')])
    # pprint(breaks_when_player1)
    sum1 = breaks_when_player1['break1'].str.rstrip('%').astype('float')

    sum2 = breaks_when_player2['break2'].str.rstrip('%').astype('float')
    # print(sum2.sum())
    average = (sum1.sum() + sum2.sum())/(len(sum1)+len(sum2))


    break1['break1'].iloc[i] = str(round(average, 0)).rstrip('.0')+"%"

dataset.loc[dataset['break1'] == '-'] = break1


break2 = dataset.loc[dataset['break2'] == '-']

for i in range(len(break2)):

    player = break2['player2'].iloc[i]

    breaks_when_player1 = (dataset.loc[(dataset['player1'] == player) & (dataset['break1'] != '-')])

    breaks_when_player2 = (dataset.loc[(dataset['player2'] == player) & (dataset['break2'] != '-')])
    # pprint(breaks_when_player1)
    sum1 = breaks_when_player1['break1'].str.rstrip('%').astype('float')

    sum2 = breaks_when_player2['break2'].str.rstrip('%').astype('float')

    # print(sum2.sum())
    if len(sum1) != 0 and len(sum2) !=0 :
        average = (sum1.sum() + sum2.sum())/(len(sum1)+len(sum2))
    elif len(sum1) != 0:
        average = (sum1.sum())/len(sum1)
    elif len(sum2) !=0:
        average = (sum2.sum()) / len(sum2)
    else:
        average = 0.0

    if average > 1:
        break2['break2'].iloc[i] = str(round(average, 0)).rstrip('.0') + "%"
    else:
        break2['break2'].iloc[i] = "0%"



dataset.loc[dataset['break2'] == '-'] = break2


dataset.to_csv('test2.csv')

# print(a['break1'].iloc[0])
# print(a.iloc[0])
# for i in dataset:

    # print(i)
    # print(dataset)

    # break
    # if dataset[i]['break1'] == '-' :
    #     player = dataset[i]['player1']
    #     flag1 = True
    # elif dataset[i]['break2'] == '-':
    #     player = dataset[i]['player2']
    #     flag2 = True
    #
    # if flag1:
    #     flag1 = False
    #     for j in dataset:
    #         if dataset[i]['player1'] == player and dataset[i]['break1'] != '-' :
    #             break_sum += dataset[i]['break1']
    #             count += 1
    #
    #
    #     dataset[i]['break1'] = break_sum/count
    #     break_sum = count = 0
    #
    # if flag2:
    #     flag2 = False
    #     for j in dataset:
    #         if dataset[i]['player2'] == player and dataset[i]['break2'] != '-' :
    #             break_sum += dataset[i]['break2']
    #             count += 1
    #
    #
    #     dataset[i]['break2'] = break_sum/count
    #     break_sum = count = 0
    #






