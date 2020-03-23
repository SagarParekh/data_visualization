import pandas as pd
import numpy as np
from pprint import pprint
import json
import csv

dataset = pd.read_csv('10yearAUSOpenMatches.csv')


countries = dict()
years = dict()
wins = dict()

for i in range(len(dataset)):


    player1 = dataset['player1'].iloc[i]
    country1 = dataset['country1'].iloc[i]
    player2 = dataset['player2'].iloc[i]
    country2 = dataset['country2'].iloc[i]
    winner = dataset['winner'].iloc[i]

    if country1 not in countries:
        countries[country1] = {'players': {player1: {'matches_played': 1, 'wins':0}},
                               'player_count': 1,
                               'name': ''
                               }
    elif player1 not in countries[country1]['players']:
        countries[country1]['players'].update({player1: {'matches_played': 1, 'wins':0}})
        countries[country1]['player_count'] += 1
    else:
        countries[country1]['players'][player1]['matches_played'] += 1



    if country2 not in countries:
        countries[country2] = {'players': {player2: {'matches_played': 1, 'wins':0}},
                               'player_count': 1,
                               'name': ''
                               }
    elif player2 not in countries[country2]['players']:
        countries[country2]['players'].update({player2: {'matches_played': 1, 'wins':0}})
        countries[country2]['player_count'] += 1
    else:
        countries[country2]['players'][player2]['matches_played'] += 1

    if player1 == winner:
        countries[country1]['players'][player1]['wins'] += 1
    elif player2 ==  winner:
        countries[country2]['players'][player2]['wins'] += 1




    year = dataset['year'].iloc[i]

    if year not in years:
        years[year] = {'player_count': { country1 : 1}}
        if country2 not in years[year]['player_count']:
            years[year]['player_count'].update({country2: 1})
        else:
            years[year]['player_count'][country2] += 1
    else:
        if country1 not in years[year]['player_count']:
            years[year]['player_count'].update({country1: 1})
        else:
            years[year]['player_count'][country1] += 1
        if country2 not in years[year]['player_count']:
            years[year]['player_count'].update({country2: 1})
        else:
            years[year]['player_count'][country2] += 1

    ace1 = dataset['ace1'].iloc[i]
    ace2 =  dataset['ace2'].iloc[i]
    first_serve1 = dataset['firstServe1'].iloc[i]
    first_serve2 = dataset['firstServe2'].iloc[i]
    double1 = dataset['double1'].iloc[i]
    double2 = dataset['double2'].iloc[i]
    first_point_won1 = dataset['firstPointWon1'].iloc[i]
    first_point_won2 = dataset['firstPointWon2'].iloc[i]
    second_point_won1 = dataset['secPointWon1'].iloc[i]
    second_point_won2 = dataset['secPointWon2'].iloc[i]
    break1 = dataset['break1'].iloc[i]
    break2 = dataset['break2'].iloc[i]
    return1 = dataset['return1'].iloc[i]
    return2 = dataset['return2'].iloc[i]
    total_points1 = dataset['total1'].iloc[i]
    total_points2 = dataset['total2'].iloc[i]

    if 'aces' not in years[year]:
        years[year].update({'aces': dict()})
    else:
        if country1 not in years[year]['aces']:
            years[year]['aces'].update({country1: {'list': list(), 'average':0, 'length': 0}})
            years[year]['aces'][country1]['list'].append(ace1)
        else:
            years[year]['aces'][country1]['list'].append(ace1)
        if country2 not in years[year]['aces']:
            years[year]['aces'].update({country2: {'list': list(), 'average':0, 'length': 0}})
            years[year]['aces'][country2]['list'].append(ace2)
        else:
            years[year]['aces'][country2]['list'].append(ace2)

    if 'first_serve' not in years[year]:
        years[year].update({'first_serve': dict()})
    else:
        if country1 not in years[year]['first_serve']:
            years[year]['first_serve'].update({country1: {'list': list(), 'average':0, 'length': 0}})
            years[year]['first_serve'][country1]['list'].append(first_serve1)
        else:
            years[year]['first_serve'][country1]['list'].append(first_serve1)
        if country2 not in years[year]['first_serve']:
            years[year]['first_serve'].update({country2: {'list': list(), 'average':0, 'length': 0}})
            years[year]['first_serve'][country2]['list'].append(first_serve2)
        else:
            years[year]['first_serve'][country2]['list'].append(first_serve2)
    
    if 'double_faults' not in years[year]:
        years[year].update({'double_faults': dict()})
    else:
        if country1 not in years[year]['double_faults']:
            years[year]['double_faults'].update({country1: {'list': list(), 'average':0, 'length': 0}})
            years[year]['double_faults'][country1]['list'].append(double1)
        else:
            years[year]['double_faults'][country1]['list'].append(double1)
        if country2 not in years[year]['double_faults']:
            years[year]['double_faults'].update({country2: {'list': list(), 'average':0, 'length': 0}})
            years[year]['double_faults'][country2]['list'].append(double2)
        else:
            years[year]['double_faults'][country2]['list'].append(double2)
    
    if 'first_point_won' not in years[year]:
        years[year].update({'first_point_won': dict()})
    else:
        if country1 not in years[year]['first_point_won']:
            years[year]['first_point_won'].update({country1: {'list': list(), 'average':0, 'length': 0}})
            years[year]['first_point_won'][country1]['list'].append(first_point_won1)
        else:
            years[year]['first_point_won'][country1]['list'].append(first_point_won1)
        if country2 not in years[year]['first_point_won']:
            years[year]['first_point_won'].update({country2: {'list': list(), 'average':0, 'length': 0}})
            years[year]['first_point_won'][country2]['list'].append(first_point_won2)
        else:
            years[year]['first_point_won'][country2]['list'].append(first_point_won2)
            
            
    if 'second_point_won' not in years[year]:
        years[year].update({'second_point_won': dict()})
    else:
        if country1 not in years[year]['second_point_won']:
            years[year]['second_point_won'].update({country1: {'list': list(), 'average':0, 'length': 0}})
            years[year]['second_point_won'][country1]['list'].append(second_point_won1)
        else:
            years[year]['second_point_won'][country1]['list'].append(second_point_won1)
        if country2 not in years[year]['second_point_won']:
            years[year]['second_point_won'].update({country2: {'list': list(), 'average':0, 'length': 0}})
            years[year]['second_point_won'][country2]['list'].append(second_point_won2)
        else:
            years[year]['second_point_won'][country2]['list'].append(second_point_won2)
    
    if 'break' not in years[year]:
        years[year].update({'break': dict()})
    else:
        if country1 not in years[year]['break']:
            years[year]['break'].update({country1: {'list': list(), 'average':0, 'length': 0}})
            years[year]['break'][country1]['list'].append(break1)
        else:
            years[year]['break'][country1]['list'].append(break1)
        if country2 not in years[year]['break']:
            years[year]['break'].update({country2: {'list': list(), 'average':0, 'length': 0}})
            years[year]['break'][country2]['list'].append(break2)
        else:
            years[year]['break'][country2]['list'].append(break2)
    
    
    if 'return' not in years[year]:
        years[year].update({'return': dict()})
    else:
        if country1 not in years[year]['return']:
            years[year]['return'].update({country1: {'list': list(), 'average':0, 'length': 0}})
            years[year]['return'][country1]['list'].append(return1)
        else:
            years[year]['return'][country1]['list'].append(return1)
        if country2 not in years[year]['return']:
            years[year]['return'].update({country2: {'list': list(), 'average':0, 'length': 0}})
            years[year]['return'][country2]['list'].append(return2)
        else:
            years[year]['return'][country2]['list'].append(return2)
    
    if 'total_points' not in years[year]:
        years[year].update({'total_points': dict()})
    else:
        if country1 not in years[year]['total_points']:
            years[year]['total_points'].update({country1: {'list': list(), 'average':0, 'length': 0}})
            years[year]['total_points'][country1]['list'].append(total_points1)
        else:
            years[year]['total_points'][country1]['list'].append(total_points1)
        if country2 not in years[year]['total_points']:
            years[year]['total_points'].update({country2: {'list': list(), 'average':0, 'length': 0}})
            years[year]['total_points'][country2]['list'].append(total_points2)
        else:
            years[year]['total_points'][country2]['list'].append(total_points2)


    if country1 not in wins:
        wins[country1] = {'matches_played': 1, 'wins': 0}
    else:
        wins[country1]['matches_played'] += 1
    if country2 not in wins:
        wins[country2] = {'matches_played': 1, 'wins': 0}
    else:
        wins[country2]['matches_played'] += 1


    if player1 == winner:
        wins[country1]['wins'] += 1
    elif player2 == winner :
        wins[country2]['wins'] += 1
    #     if country2 not in wins[country1]:
    #         wins[country1].update({country2: 1})
    #     else:
    #         wins[country1][country2] += 1
    # elif player2 == winner:
    #     if country1 not in wins[country2]:
    #         wins[country2].update({country1: 1})
    #     else:
    #         wins[country2][country1] += 1


# pprint(wins)
# pprint(countries)
sum = 0
for i in years:
    for j in years[i]:
        if j == 'player_count':
            continue
        for k in years[i][j]:
            for l in range(len(years[i][j][k]['list'])):
                if type(years[i][j][k]['list'][l]) != np.int64:
                    if years[i][j][k]['list'][l] == '-':
                        years[i][j][k]['list'][l] = 0
                    else:
                        years[i][j][k]['list'][l] = float(years[i][j][k]['list'][l].strip('%'))
                sum += years[i][j][k]['list'][l]

            years[i][j][k]['average'] = sum/len(years[i][j][k]['list'])
            years[i][j][k]['length'] = len(years[i][j][k]['list'])
            sum = 0

# for i in years:
#     years[str(i)] = years.pop(i)
#
# pprint(years)
# with open('bar_graph_data.json', 'w') as fp:
#     json.dump(years, fp)

for i in countries:
    for j in years:
        for k in years[j]:
            if i not in years[j][k]:
                years[j][k].update({i: {'list': list(), 'average':0, 'length': 0}})



print(years)
