#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 23:56:41 2024

@author: santiarago
"""

import pandas as pd

df = pd.read_csv('serieAClean23-24.csv')

passCompletedList = []
realPassRecipientName = []

for index, row in df.iterrows():
  if index < len(df) - 1:  # Check if next row exists
    next_row = df.loc[index + 1]
    
    
  if row['typePrimary']  == 'pass': 
      
      if row['teamName'] == next_row['teamName']:
      
          passCompletedList.append(1)
          realPassRecipientName.append(str(next_row['playerName']))
      
      else:
          passCompletedList.append(0)
          realPassRecipientName.append('')
                             
  else:
      passCompletedList.append(0)
      realPassRecipientName.append('')
        
df['isCompletedPass'] = passCompletedList
df['realPassRecipientName'] = realPassRecipientName


#Data for radar
leagueInput = df[['playerName', 'playerPosition', 'isProgressivePass', 'isCompletedPass', 'isLoss']]
goalkeepers = leagueInput[leagueInput['playerPosition'] == 'GK']
goalkeepers = goalkeepers[goalkeepers['isProgressivePass'] == 1]
def j(goalkeepers):
    return goalkeepers.groupby('playerName').agg(progressivePasses=pd.NamedAgg(column='isProgressivePass', aggfunc='sum'),
                                         completedProgressivePasses=pd.NamedAgg(column='isCompletedPass', aggfunc='sum'),
                                         losses=pd.NamedAgg(column='isLoss', aggfunc='sum'))

eredivisieGoalkeeperProgressivePasses = j(goalkeepers.copy())
eredivisieGoalkeeperProgressivePasses = eredivisieGoalkeeperProgressivePasses.reset_index()

portugalGoalkeeperProgressivePasses = j(goalkeepers.copy())
portugalGoalkeeperProgressivePasses = portugalGoalkeeperProgressivePasses.reset_index()

laLigaGoalkeeperProgressivePasses = j(goalkeepers.copy())
laLigaGoalkeeperProgressivePasses = laLigaGoalkeeperProgressivePasses.reset_index()

eplGoalkeeperProgressivePasses = j(goalkeepers.copy())
eplGoalkeeperProgressivePasses = eplGoalkeeperProgressivePasses.reset_index()

ligue1GoalkeeperProgressivePasses = j(goalkeepers.copy())
ligue1GoalkeeperProgressivePasses = ligue1GoalkeeperProgressivePasses.reset_index()

bundesligaGoalkeeperProgressivePasses = j(goalkeepers.copy())
bundesligaGoalkeeperProgressivePasses = bundesligaGoalkeeperProgressivePasses.reset_index()

serieAGoalkeeperProgressivePasses = j(goalkeepers.copy())
serieAGoalkeeperProgressivePasses = serieAGoalkeeperProgressivePasses.reset_index()


#Append 

goalkeeperPassingData = pd.concat([eredivisieGoalkeeperProgressivePasses, portugalGoalkeeperProgressivePasses, laLigaGoalkeeperProgressivePasses, eplGoalkeeperProgressivePasses, ligue1GoalkeeperProgressivePasses, bundesligaGoalkeeperProgressivePasses, serieAGoalkeeperProgressivePasses], ignore_index=True)

df.to_csv('premierLeagueCompletedPasses23-24.csv')