#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 20:44:12 2024

@author: santiarago
"""

import pandas as pd


premierLeague2324 = pd.read_csv('premierLeagueClean23-24.csv')
laLiga2324 = pd.read_csv('laLigaClean23-24.csv')
bundesliga2324 = pd.read_csv('bundesligaClean23-24.csv')
serieA2324 = pd.read_csv('serieAClean23-24.csv')
ligue12324 = pd.read_csv('ligue1Clean23-24.csv')

df = pd.concat([premierLeague2324, laLiga2324, bundesliga2324, serieA2324, ligue12324], ignore_index=True)

#Finding Successful Passes

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



#Finding Won Duels

wonDuelList = []

for index, row in df.iterrows():
    
    if row['groundDuelKeptPossession'] == 1 or row['aerialDuelFirstTouch'] == 1 or row['groundDuelProgressedWithBall'] == 1 or row['groundDuelRecoveredPossession'] == 1 or row['groundDuelStoppedProgress'] == 1:
        wonDuelList.append(1)
    else:
        wonDuelList.append(0)


df['isWonDuel'] = wonDuelList

#Finding All Duels

duelList = []

for index, row in df.iterrows():
    
    if row['typePrimary'] == 'duel' :
        duelList.append(1)
    else:
        duelList.append(0)

df['isDuel'] = duelList


#Finding Won Aerial Duels

wonAerialDuelList = []

for index, row in df.iterrows():
    
    if row['aerialDuelFirstTouch'] == 1 :
        wonAerialDuelList.append(1)
    else:
        wonAerialDuelList.append(0)

df['isWonAerialDuel'] = wonAerialDuelList


#Finding Won Ground Duels

wonGroundDuelList = []

for index, row in df.iterrows():
    
    if row['groundDuelKeptPossession'] == 1 or  row['groundDuelProgressedWithBall'] == 1 or row['groundDuelRecoveredPossession'] == 1 or row['groundDuelStoppedProgress'] == 1:
        wonGroundDuelList.append(1)
    else:
        wonGroundDuelList.append(0)

df['isWonGroundDuel'] = wonGroundDuelList


#Finding Won Defensive Duels

wonDefensiveDuelList = []

for index, row in df.iterrows():
    
    if row['isDefensiveDuel'] == 1 and  row['isWonDuel'] == 1 :
        wonDefensiveDuelList.append(1)
    else:
        wonDefensiveDuelList.append(0)

df['isWonDefensiveDuel'] = wonDefensiveDuelList


#Finding Won Loose Ball Duels

wonLooseBallDuelList = []

for index, row in df.iterrows():
    
    if row['isLooseBallDuel'] == 1 and  row['isWonDuel'] == 1 :
        wonLooseBallDuelList.append(1)
    else:
        wonLooseBallDuelList.append(0)

df['isWonLooseBallDuel'] = wonLooseBallDuelList


#Finding Won Offensive Duels

wonOffensiveDuelList = []

for index, row in df.iterrows():
    
    if row['isOffensiveDuel'] == 1 and  row['isWonDuel'] == 1 :
        wonOffensiveDuelList.append(1)
    else:
        wonOffensiveDuelList.append(0)

df['isWonOffensiveDuel'] = wonOffensiveDuelList


#Finding Successful Crosses

successfulCrossList = []

for index, row in df.iterrows():
    
    if row['isCross'] == 1 and row['isCompletedPass'] == 1 :
        successfulCrossList.append(1)
    else:
        successfulCrossList.append(0)

df['isCompletedCross'] = successfulCrossList

#Finding Successful Progressive Passes

successfulProgressivePassList = []

for index, row in df.iterrows():
    
    if row['isProgressivePass'] == 1 and row['isCompletedPass'] == 1 :
        successfulProgressivePassList.append(1)
    else:
        successfulProgressivePassList.append(0)

df['isCompletedProgressivePass'] = successfulProgressivePassList

#Finding Successful Forward Passes

successfulForwardPassList = []

for index, row in df.iterrows():
    
    if row['isForwardPass'] == 1 and row['isCompletedPass'] == 1 :
        successfulForwardPassList.append(1)
    else:
        successfulForwardPassList.append(0)

df['isCompletedForwardPass'] = successfulForwardPassList


#Finding Successful Long Passes

successfulLongPassList = []

for index, row in df.iterrows():
    
    if row['isLongPass'] == 1 and row['isCompletedPass'] == 1 :
        successfulLongPassList.append(1)
    else:
        successfulLongPassList.append(0)

df['isCompletedLongPass'] = successfulLongPassList


#Finding Successful Passes To Final Third

successfulPassesToFinalThirdList = []

for index, row in df.iterrows():
    
    if row['isPassToFinalThird'] == 1 and row['isCompletedPass'] == 1 :
        successfulPassesToFinalThirdList.append(1)
    else:
        successfulPassesToFinalThirdList.append(0)

df['isCompletedPassToFinalThird'] = successfulPassesToFinalThirdList

#Finding Successful Passes To Penalty Area

successfulPassesToPenaltyAreaList = []

for index, row in df.iterrows():
    
    if row['isPassToPenaltyArea'] == 1 and row['isCompletedPass'] == 1 :
        successfulPassesToPenaltyAreaList.append(1)
    else:
        successfulPassesToPenaltyAreaList.append(0)

df['isCompletedPassToPenaltyArea'] = successfulPassesToPenaltyAreaList


#Finding Shots 

shotsList = []

for index, row in df.iterrows():
    
    if row['typePrimary'] == 'shot':
        shotsList.append(1)
    else:
        shotsList.append(0)

df['isShot'] = shotsList


#Finding Shots On Target

shotsOnTargetList = []

for index, row in df.iterrows():
    
    if row['shotOnTarget'] == 1:
        shotsOnTargetList.append(1)
    else:
        shotsOnTargetList.append(0)

df['isShotOnTarget'] = shotsOnTargetList



column_names = df.columns.tolist()
print(column_names)

df.to_csv('big5Events.csv')


#Group By All Players
def groupByPlayer(df):
    return df.groupby('playerName').agg(crosses=pd.NamedAgg(column='isCross', aggfunc='sum'),
                                         recoveries=pd.NamedAgg(column='isRecovery', aggfunc='sum'),
                                         progressivePasses=pd.NamedAgg(column='isProgressivePass', aggfunc='sum'),
                                         duels=pd.NamedAgg(column='isDuel', aggfunc='sum'),
                                         losses=pd.NamedAgg(column='isLoss', aggfunc='sum'),
                                         wonDuels=pd.NamedAgg(column='isWonDuel', aggfunc='sum'),
                                         shotAssists=pd.NamedAgg(column='isShotAssist', aggfunc='sum'),
                                         accelerations=pd.NamedAgg(column='isAcceleration', aggfunc='sum'),
                                         longPasses=pd.NamedAgg(column='isLongPass', aggfunc='sum'),
                                         completedPasses=pd.NamedAgg(column='isCompletedPass', aggfunc='sum'),
                                         completedProgressivePasses=pd.NamedAgg(column='isCompletedProgressivePass', aggfunc='sum'),
                                         completedLongPasses=pd.NamedAgg(column='isCompletedLongPass', aggfunc='sum'),
                                         completedCrosses=pd.NamedAgg(column='isCompletedCross', aggfunc='sum'),
                                         carries=pd.NamedAgg(column='isCarry', aggfunc='sum'),
                                         xG=pd.NamedAgg(column='shotXg', aggfunc='sum'),
                                         psxG=pd.NamedAgg(column='shotPostShotXg', aggfunc='sum'),
                                         defensiveDuels=pd.NamedAgg(column='isDefensiveDuel', aggfunc='sum'),
                                         wonDefensiveDuels=pd.NamedAgg(column='isWonDefensiveDuel', aggfunc='sum'),
                                         aerialDuels=pd.NamedAgg(column='isAerialDuel', aggfunc='sum'),
                                         wonAerialDuels=pd.NamedAgg(column='isWonAerialDuel', aggfunc='sum'),
                                         dribbles=pd.NamedAgg(column='isDribble', aggfunc='sum'),
                                         forwardPasses=pd.NamedAgg(column='isForwardPass', aggfunc='sum'),
                                         completedForwardPasses=pd.NamedAgg(column='isCompletedForwardPass', aggfunc='sum'),
                                         goals=pd.NamedAgg(column='isGoal', aggfunc='sum'),
                                         groundDuels=pd.NamedAgg(column='isGroundDuel', aggfunc='sum'),
                                         wonGroundDuels=pd.NamedAgg(column='isWonGroundDuel', aggfunc='sum'),
                                         interceptions=pd.NamedAgg(column='isInterception', aggfunc='sum'),
                                         keyPasses=pd.NamedAgg(column='isKeyPass', aggfunc='sum'),
                                         looseBallDuels=pd.NamedAgg(column='isLooseBallDuel', aggfunc='sum'),
                                         wonLooseBallDuels=pd.NamedAgg(column='isWonLooseBallDuel', aggfunc='sum'),
                                         opportunities=pd.NamedAgg(column='isOpportunity', aggfunc='sum'),
                                         passesToFinalThird=pd.NamedAgg(column='isPassToFinalThird', aggfunc='sum'),
                                         completedPassesToFinalThird=pd.NamedAgg(column='isCompletedPassToFinalThird', aggfunc='sum'),
                                         passesToPenaltyArea=pd.NamedAgg(column='isPassToPenaltyArea', aggfunc='sum'),
                                         completedPassesToPenaltyArea=pd.NamedAgg(column='isCompletedPassToPenaltyArea', aggfunc='sum'),
                                         progressiveRuns=pd.NamedAgg(column='isProgressiveRun', aggfunc='sum'),
                                         secondAssists=pd.NamedAgg(column='isSecondAssist', aggfunc='sum'),
                                         assists=pd.NamedAgg(column='isAssist', aggfunc='sum'),
                                         shotsAfterCorner=pd.NamedAgg(column='isShotAfterCorner', aggfunc='sum'),
                                         shotsAfterFreeKick=pd.NamedAgg(column='isShotAfterFreeKick', aggfunc='sum'),
                                         shotBlocks=pd.NamedAgg(column='isShotBlock', aggfunc='sum'),
                                         touchesInBox=pd.NamedAgg(column='isTouchInBox', aggfunc='sum'),
                                         counterpressingRecoveries=pd.NamedAgg(column='isCounterpressingRecovery', aggfunc='sum'),
                                         offensiveDuels=pd.NamedAgg(column='isOffensiveDuel', aggfunc='sum'),
                                         wonOffensiveDuels=pd.NamedAgg(column='isWonOffensiveDuel', aggfunc='sum'),
                                         shots=pd.NamedAgg(column='isShot', aggfunc='sum'),
                                         shotsOnTarget=pd.NamedAgg(column='isShotOnTarget', aggfunc='sum'))

allStats = groupByPlayer(df.copy())

allStats = allStats.reset_index()

#Retrieve Database Stats
databaseStats = pd.read_excel('completePlayerDatabase.xlsx')

databaseStats = databaseStats[['playerName', 'Posición específica.1','age', 'teamName', 'Liga', 'minutesPlayed', 'height', 'marketValue', 'contractExpiration', 'dominantFoot', 'onLoan']]

allStats = allStats.set_index('playerName').join(databaseStats.set_index('playerName'), how='inner')

allStats = allStats.reset_index()

allStats.to_csv('allPlayerStats.csv')

#Expected Goals Calculations

allStats['Goals-xG'] = allStats['goals'] - allStats['xG']
allStats['psxG-xG'] = allStats['psxG'] - allStats['xG']

positionsList = []

for index, row in allStats.iterrows():
    
    if row['Posición específica.1'] == 'CF':
        positionsList.append('ST')
    elif row['Posición específica.1'] == 'AMF' or row['Posición específica.1'] == 'RAMF' or row['Posición específica.1'] == 'LAMF':
            positionsList.append('CAM')
    elif row['Posición específica.1'] == 'CB' or row['Posición específica.1'] == 'RCB' or row['Posición específica.1'] == 'LCB':
            positionsList.append('CB')
    elif row['Posición específica.1'] == 'LB' or row['Posición específica.1'] == 'LWB' :
            positionsList.append('LB')
    elif row['Posición específica.1'] == 'RB' or row['Posición específica.1'] == 'RWB':
            positionsList.append('RB')
    elif row['Posición específica.1'] == 'LCMF' or row['Posición específica.1'] == 'RCMF':
            positionsList.append('CM')
    elif row['Posición específica.1'] == 'DMF' or row['Posición específica.1'] == 'LDMF' or row['Posición específica.1'] == 'RDMF' :
            positionsList.append('CDM')
    elif row['Posición específica.1'] == 'LW' or row['Posición específica.1'] == 'LWF':
            positionsList.append('LW')
    elif row['Posición específica.1'] == 'RW' or row['Posición específica.1'] == 'RWF':
            positionsList.append('CM')
    else:
        positionsList.append('')

allStats['standardPositions'] = positionsList

allStats = allStats[allStats['Posición específica.1'] != 'GK']

#Per 90 Calculations

column_names = allStats.columns.tolist()
print(column_names)

allStats['90s'] = allStats['minutesPlayed']/90.0

allStats['completedCrosses/90'] = allStats['completedCrosses']/allStats['90s']
allStats['recoveries/90'] = allStats['recoveries']/allStats['90s']
allStats['completedProgressivePasses/90'] = allStats['completedProgressivePasses']/allStats['90s']
allStats['accelerations/90'] = allStats['accelerations']/allStats['90s']
allStats['wonDuels/90'] = allStats['wonDuels']/allStats['90s']
allStats['losses/90'] = allStats['losses']/allStats['90s']
allStats['shotAssists/90'] = allStats['shotAssists']/allStats['90s']
allStats['completedLongPasses/90'] = allStats['completedProgressivePasses']/allStats['90s']
allStats['carries/90'] = allStats['carries']/allStats['90s']
allStats['xG/90'] = allStats['xG']/allStats['90s']
allStats['psxG/90'] = allStats['psxG']/allStats['90s']
allStats['secondAssists/90'] = allStats['secondAssists']/allStats['90s']
allStats['wonDefensiveDuels/90'] = allStats['wonDefensiveDuels']/allStats['90s']
allStats['progressiveRuns/90'] = allStats['progressiveRuns']/allStats['90s']
allStats['wonAerialDuels/90'] = allStats['wonAerialDuels']/allStats['90s']
allStats['dribbles/90'] = allStats['dribbles']/allStats['90s']
allStats['forwardPasses/90'] = allStats['forwardPasses']/allStats['90s']
allStats['completedForwardPasses/90'] = allStats['completedForwardPasses']/allStats['90s']
allStats['goals/90'] = allStats['goals']/allStats['90s']
allStats['completedPassesToPenaltyArea/90'] = allStats['completedPassesToPenaltyArea']/allStats['90s']
allStats['wonGroundDuels/90'] = allStats['wonGroundDuels']/allStats['90s']
allStats['interceptions/90'] = allStats['interceptions']/allStats['90s']
allStats['keyPasses/90'] = allStats['keyPasses']/allStats['90s']
allStats['assists/90'] = allStats['assists']/allStats['90s']
allStats['wonLooseBallDuels/90'] = allStats['wonLooseBallDuels']/allStats['90s']
allStats['opportunities/90'] = allStats['opportunities']/allStats['90s']
allStats['completedPassesToFinalThird/90'] = allStats['completedPassesToFinalThird']/allStats['90s']
allStats['shotsAfterCorner/90'] = allStats['shotsAfterCorner']/allStats['90s']
allStats['shotsAfterFreeKick/90'] = allStats['shotsAfterFreeKick']/allStats['90s']
allStats['shotBlocks/90'] = allStats['shotBlocks']/allStats['90s']
allStats['touchesInBox/90'] = allStats['touchesInBox']/allStats['90s']
allStats['counterpressingRecoveries/90'] = allStats['counterpressingRecoveries']/allStats['90s']
allStats['wonOffensiveDuels/90'] = allStats['wonOffensiveDuels']/allStats['90s']
allStats['shots/90'] = allStats['shots']/allStats['90s']
allStats['shotsOnTarget/90'] = allStats['shotsOnTarget']/allStats['90s']
allStats['Goals-xG/90'] = allStats['Goals-xG']/allStats['90s']
allStats['psxG-xG/90'] = allStats['psxG-xG']/allStats['90s']

#Percentage Calculations

allStats['%duelsWon'] = (allStats['wonDuels']/allStats['duels'])*100
allStats['%completedCrosses'] = (allStats['completedCrosses']/allStats['crosses'])*100
allStats['%completedProgressivePasses'] = (allStats['completedProgressivePasses']/allStats['progressivePasses'])*100
allStats['%completedLongPasses'] = (allStats['completedLongPasses']/allStats['longPasses'])*100
allStats['%completedPassesToFinalThird'] = (allStats['completedPassesToFinalThird']/allStats['passesToFinalThird'])*100
allStats['%completedPassesToPenaltyArea'] = (allStats['completedPassesToPenaltyArea']/allStats['passesToPenaltyArea'])*100
allStats['%wonLooseBallDuels'] = (allStats['wonLooseBallDuels']/allStats['looseBallDuels'])*100
allStats['%wonGroundDuels'] = (allStats['wonGroundDuels']/allStats['groundDuels'])*100
allStats['%wonAerialDuels'] = (allStats['wonAerialDuels']/allStats['aerialDuels'])*100
allStats['%wonDefensiveDuels'] = (allStats['wonDefensiveDuels']/allStats['defensiveDuels'])*100
allStats['%wonOffensiveDuels'] = (allStats['wonOffensiveDuels']/allStats['offensiveDuels'])*100
allStats['%shotsOnTarget'] = (allStats['shotsOnTarget']/allStats['shots'])*100








#Filter For Position and Games Played

#positionStats = allStats.query("standardPosition == 'CB'  or playerPosition == 'LCB' or playerPosition == 'RCB' or playerPosition == 'LCB3' or playerPosition == 'RCB3'")

positionStats = allStats[allStats['standardPositions'] == 'ST']
positionStats = positionStats[positionStats['minutesPlayed'] >= 180]

column_names = positionStats.columns.tolist()
print(column_names)

#Percentile Calculations

positionStats['percentileMinutesPlayed'] = positionStats['minutesPlayed'].rank(pct=True).mul(100)
positionStats['percentileCompletedCrosses/90'] = positionStats['completedCrosses/90'].rank(pct=True).mul(100)
positionStats['percentileRecoveries/90'] = positionStats['recoveries/90'].rank(pct=True).mul(100)
positionStats['percentileCompletedProgressivePasses/90'] = positionStats['completedProgressivePasses/90'].rank(pct=True).mul(100)
positionStats['percentileAccelerations/90'] = positionStats['accelerations/90'].rank(pct=True).mul(100)
positionStats['percentileWonDuels/90'] = positionStats['wonDuels/90'].rank(pct=True).mul(100)
positionStats['percentileLosses/90'] = 100 - positionStats['losses/90'].rank(pct=True).mul(100)
positionStats['percentileShotAssists/90'] = positionStats['shotAssists/90'].rank(pct=True).mul(100)
positionStats['percentileCompletedLongPasses/90'] = positionStats['completedLongPasses/90'].rank(pct=True).mul(100)
positionStats['percentileCarries/90'] = positionStats['carries/90'].rank(pct=True).mul(100)
positionStats['percentileXG/90'] = positionStats['xG/90'].rank(pct=True).mul(100)
positionStats['percentilePsxG/90'] = positionStats['psxG/90'].rank(pct=True).mul(100)
positionStats['percentileSecondAssists/90'] = positionStats['secondAssists/90'].rank(pct=True).mul(100)
positionStats['percentileProgressiveRuns/90'] = positionStats['progressiveRuns/90'].rank(pct=True).mul(100)
positionStats['percentileWonAerialDuels/90'] = positionStats['wonAerialDuels/90'].rank(pct=True).mul(100)
positionStats['percentileDribbles/90'] = positionStats['dribbles/90'].rank(pct=True).mul(100)
positionStats['percentileCompletedForwardPasses/90'] = positionStats['completedForwardPasses/90'].rank(pct=True).mul(100)
positionStats['percentileGoals/90'] = positionStats['goals/90'].rank(pct=True).mul(100)
positionStats['percentileCompletedPassesToPenaltyArea/90'] = positionStats['completedPassesToPenaltyArea/90'].rank(pct=True).mul(100)
positionStats['percentileInterceptions/90'] = positionStats['interceptions/90'].rank(pct=True).mul(100)
positionStats['percentileAssists/90'] = positionStats['assists/90'].rank(pct=True).mul(100)
positionStats['percentileOpportunities/90'] = positionStats['opportunities/90'].rank(pct=True).mul(100)
positionStats['percentileCompletedPassesToFinalThird/90'] = positionStats['completedPassesToFinalThird/90'].rank(pct=True).mul(100)
positionStats['percentileShotsAfterCorner/90'] = positionStats['shotsAfterCorner/90'].rank(pct=True).mul(100)
positionStats['percentileShotsAfterFreeKick/90'] = positionStats['shotsAfterFreeKick/90'].rank(pct=True).mul(100)
positionStats['percentileShotBlocks/90'] = positionStats['shotBlocks/90'].rank(pct=True).mul(100)
positionStats['percentileTouchesInBox/90'] = positionStats['touchesInBox/90'].rank(pct=True).mul(100)
positionStats['percentileCounterpressingRecoveries/90'] = positionStats['counterpressingRecoveries/90'].rank(pct=True).mul(100)
positionStats['percentileWonOffensiveDuels/90'] = positionStats['wonOffensiveDuels/90'].rank(pct=True).mul(100)
positionStats['percentileShotsOnTarget/90'] = positionStats['shotsOnTarget/90'].rank(pct=True).mul(100)
positionStats['percentileGoals-xG/90'] = positionStats['Goals-xG/90'].rank(pct=True).mul(100)
positionStats['percentilePsxG-xG/90'] = positionStats['psxG-xG/90'].rank(pct=True).mul(100)




#Generate KPI's

# Define the weights for each column
weights = {'percentileGoals-xG/90': 0.15, 'percentileDribbles/90': 0.15,'percentilePsxG-xG/90': 0.15,  'percentileAssists/90': 0.1, 'percentileProgressiveRuns/90': 0.25, 'percentileGoals/90': 0.2}

# Calculate the KPI using weighted sum with 'apply'
positionStats['astonVillaKPI'] = positionStats.apply(lambda row: sum(row[col] * weights[col] for col in weights), axis=1)


positionStats = positionStats[positionStats['minutesPlayed'] >= 900]

positionStats.to_csv('leftBackStats.csv')

leftBackStats = positionStats
rightBackStats = positionStats
centerBackStats = positionStats
centerMidStats = positionStats
cdmStats = positionStats
rightWingStats = positionStats
leftWingStats = positionStats
strikerStats = positionStats

kpi = positionStats[['playerName', 'KPI', 'Liga']]

radarStats = positionStats[['playerName', 'teamName', 'Liga', 'KPI', 'age', 'marketValue','%duelsWon', 'percentileCompletedProgressivePasses/90', 'percentileAccelerations/90', 'percentileRecoveries/90',  'percentileLosses/90']]
centerBackRadarStats = radarStats

centerBackRadarStats.to_csv('leftBackKpi.csv')

#Combining Dataframes With Appropriate Percentiles

percentilesByPosition = pd.concat([leftBackStats, rightBackStats, centerBackStats, centerMidStats, cdmStats, rightWingStats, leftWingStats, strikerStats], ignore_index=True)


#Goalkeeper Group By Functions
def g(df):
    return df.groupby(['matchId','shotGoalkeeperName']).agg(goalsAllowed=pd.NamedAgg(column='isGoal', aggfunc='sum'),
                                         shotPsxg_sum=pd.NamedAgg(column='shotPostShotXg', aggfunc='sum'))


shootingGoalkeeperStats = g(df.copy())

shootingGoalkeeperStats = shootingGoalkeeperStats.reset_index()


def h(shootingGoalkeeperStats):    
  
    return shootingGoalkeeperStats[shootingGoalkeeperStats['goalsAllowed'] == 0].count()

cleanSheets = shootingGoalkeeperStats.groupby('shotGoalkeeperName').apply(h)

cleanSheets = cleanSheets.rename(columns={'shotGoalkeeperName':'cleanSheets'})

cleanSheets = cleanSheets.reset_index()

cleanSheets = cleanSheets[['shotGoalkeeperName', 'cleanSheets']]


def i(df):
    return shootingGoalkeeperStats.groupby('shotGoalkeeperName').agg(PsxG=pd.NamedAgg(column='shotPsxg_sum', aggfunc='sum'),
                                         goalsAllowed=pd.NamedAgg(column='goalsAllowed', aggfunc='sum'))

shootingGoalkeeperStats = i(shootingGoalkeeperStats.copy())

shootingGoalkeeperStats = shootingGoalkeeperStats.reset_index()

goalPreventionStats = shootingGoalkeeperStats.set_index('shotGoalkeeperName').join(cleanSheets.set_index('shotGoalkeeperName'), how='inner')

goalPreventionStats = goalPreventionStats.reset_index()


def j(df):
    return df.groupby('playerName').agg(progressivePasses=pd.NamedAgg(column='isProgressivePass', aggfunc='sum'),
                                         losses=pd.NamedAgg(column='isLoss', aggfunc='sum'))

passingGoalkeeperStats = j(df.copy())

passingGoalkeeperStats = passingGoalkeeperStats.reset_index()




#Data for radar and group by's (Goalkeeper)

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

goalkeeperRadarStats = goalPreventionStats.set_index('shotGoalkeeperName').join(goalkeeperPassingData.set_index('playerName'), how='inner')

goalkeeperRadarStats = goalkeeperRadarStats.reset_index()



#Retrieve Database Stats
databaseStats = pd.read_excel('completePlayerDatabase.xlsx')

databaseStats = databaseStats[['playerName', 'age', 'teamName', 'Liga', 'minutesPlayed', 'height']]

goalkeeperCombinedStats = databaseStats.set_index('playerName').join(goalkeeperRadarStats.set_index('shotGoalkeeperName'), how='inner')

goalkeeperCombinedStats['PsxG-Goals Allowed'] = goalkeeperCombinedStats['PsxG'] - goalkeeperCombinedStats['goalsAllowed']

goalkeeperCombinedStats['90s'] = goalkeeperCombinedStats['minutesPlayed']/90.0

goalkeeperCombinedStats['goalsPreventedPer90Minutes'] = goalkeeperCombinedStats['PsxG-Goals Allowed']/goalkeeperCombinedStats['90s']

goalkeeperCombinedStats['cleanSheetsPer90'] = goalkeeperCombinedStats['cleanSheets']/goalkeeperCombinedStats['90s']

goalkeeperCombinedStats['completedProgressivePassesPer90'] = goalkeeperCombinedStats['completedProgressivePasses']/goalkeeperCombinedStats['90s']

goalkeeperCombinedStats['lossesPer90'] = goalkeeperCombinedStats['losses']/goalkeeperCombinedStats['90s']

goalkeeperCombinedStats['goalsAllowedPer90'] = goalkeeperCombinedStats['goalsAllowed']/goalkeeperCombinedStats['90s']


goalkeeperCombinedStats = goalkeeperCombinedStats[goalkeeperCombinedStats['minutesPlayed'] >= 900]


#Calculate Percentiles
goalkeeperCombinedStats['percentilesMinutesPlayed'] = goalkeeperCombinedStats['minutesPlayed'].rank(pct=True).mul(100)
goalkeeperCombinedStats['percentilesGoalsPrevented'] = goalkeeperCombinedStats['goalsPreventedPer90Minutes'].rank(pct=True).mul(100)
goalkeeperCombinedStats['percentilesCleanSheets'] = goalkeeperCombinedStats['cleanSheets'].rank(pct=True).mul(100)
goalkeeperCombinedStats['percentilesLosses'] = goalkeeperCombinedStats['losses'].rank(pct=True).mul(100)
goalkeeperCombinedStats['percentilesGoalsAllowed'] = goalkeeperCombinedStats['goalsAllowed'].rank(pct=True).mul(100)
goalkeeperCombinedStats['percentilespsxg'] = goalkeeperCombinedStats['PsxG'].rank(pct=True).mul(100)
goalkeeperCombinedStats['percentilesCompletedProgressivePasses'] = goalkeeperCombinedStats['completedProgressivePasses'].rank(pct=True).mul(100)
goalkeeperCombinedStats['percentilesCleanSheetsPer90'] = goalkeeperCombinedStats['cleanSheetsPer90'].rank(pct=True).mul(100)
goalkeeperCombinedStats['percentileCompletedProgressivePassesPer90'] = goalkeeperCombinedStats['completedProgressivePassesPer90'].rank(pct=True).mul(100)
goalkeeperCombinedStats['inversePercentilelossesPer90'] = goalkeeperCombinedStats['lossesPer90'].rank(pct=True).mul(100)
goalkeeperCombinedStats['percentilelossesPer90'] = 100 - goalkeeperCombinedStats['inversePercentilelossesPer90']
goalkeeperCombinedStats['percentileGoalsAllowedPer90'] = goalkeeperCombinedStats['goalsAllowedPer90'].rank(pct=True).mul(100)

goalkeeperCombinedStats = goalkeeperCombinedStats[goalkeeperCombinedStats['age'] <= 25]

#Generate KPI's
df = goalkeeperCombinedStats
# Define the weights for each column
weights = {'percentilesGoalsPrevented': 0.5, 'percentileCompletedProgressivePassesPer90': 0.2, 'percentilesCleanSheetsPer90': 0.1, 'percentilelossesPer90': 0.2}

# Calculate the KPI using weighted sum with 'apply'
df['KPI'] = df.apply(lambda row: sum(row[col] * weights[col] for col in weights), axis=1)

df = df.reset_index()

kpi = df[['playerName', 'KPI']]

kpiGoalkeepeers = kpi.reset_index()

kpiGoalkeepeers = kpiGoalkeepeers[['playerName', 'KPI']]

#Sort by KPI
goalkeeperCombinedStats = goalkeeperCombinedStats.sort_values(by='KPI', ascending=False)










