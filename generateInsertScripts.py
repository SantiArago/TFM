import pandas as pd
import csv

import numpy as np

Table_Name = 'laLiga2223'
#df = pd.read_csv('bundesliga22-23.csv')
df = pd.read_excel('laLiga22-23.xlsx')

df = df.rename(columns={'type.primary':'typePrimary', 'type.secondary.1':'typeSecondary1', 'type.secondary.2':'typeSecondary2', 'type.secondary.3':'typeSecondary3', 'type.secondary.4':'typeSecondary4', 'type.secondary.5':'typeSecondary5', 'type.secondary.6':'typeSecondary6', 'type.secondary.7':'typeSecondary7', 'type.secondary.8':'typeSecondary8','minute':'minutes','second':'seconds','location.x':'xLocation','location.y':'yLocation','team.id':'teamId','team.name':'teamName','team.formation':'teamFormation','opponentTeam.id':'opponentTeamId','opponentTeam.name':'opponentTeamName','opponentTeam.formation':'opponentTeamFormation','player.id':'playerId','player.name':'playerName','player.position':'playerPosition','pass.accurate':'passAccurate','pass.angle':'passAngle','pass.height':'passHeight','pass.length':'passLength','pass.recipient.id':'passRecipientId','pass.recipient.name':'passRecipientName','pass.recipient.position':'passRecipientPosition','pass.endLocation.x':'passEndLocationX','pass.endLocation.y':'passEndLocationY','possession.id':'possessionId','possession.duration':'possessionDuration','possession.types.1':'possessionTypes1','possession.types.2':'possessionTypes2','possession.types.3':'possessionTypes3','possession.startLocation.x':'possessionStartLocationX','possession.startLocation.y':'possessionStartLocationY','possession.endLocation.x':'possessionEndLocationX','possession.endLocation.y':'possessionEndLocationY','possession.team.id':'possessionTeamId','possession.team.name':'possessionTeamName','possession.team.formation':'possessionTeamFormation','possession.attack.withShot':'possessionAttackWithShot','possession.attack.withShotOnGoal':'possessionAttackWithShotOnGoal','possession.attack.withGoal':'possessionAttackWithGoal','possession.attack.flank':'possessionAttackFlank','possession.attack.xg':'possessionAttackXg','carry.progression':'carryProgression','carry.endLocation.x':'carryEndLocationX','carry.endLocation.y':'carryEndLocationY', 'aerialDuel.opponent.id':'aerialDuelOpponentId','aerialDuel.opponent.name':'aerialDuelOpponentName','aerialDuel.opponent.position':'aerialDuelOpponentPosition','aerialDuel.opponent.height':'aerialDuelOpponentHeight','aerialDuel.firstTouch':'aerialDuelFirstTouch','aerialDuel.height':'aerialDuelHeight','aerialDuel.relatedDuelId':'aerialDuelRelatedDuelId','groundDuel.opponent.id':'groundDuelOpponentId','groundDuel.opponent.name':'groundDuelOpponentName','groundDuel.opponent.position':'groundDuelOpponentPosition','groundDuel.duelType':'groundDuelDuelType','groundDuel.keptPossession':'groundDuelKeptPossession','groundDuel.progressedWithBall':'groundDuelProgressedWithBall','groundDuel.stoppedProgress':'groundDuelStoppedProgress','groundDuel.recoveredPossession':'groundDuelRecoveredPossession','groundDuel.takeOn':'groundDuelTakeOn','groundDuel.side':'groundDuelSide','groundDuel.relatedDuelId':'groundDuelRelatedDuelId','shot.bodyPart':'shotBodyPart','shot.isGoal':'shotIsGoal','shot.onTarget':'shotOnTarget','shot.goalZone':'shotGoalZone','shot.xg':'shotXg','shot.postShotXg':'shotPostShotXg','infraction.yellowCard':'infractionYellowCard','infraction.redCard':'infractionRedCard','infraction.type':'infractionType','infraction.opponent.id':'infractionOpponentId','infraction.opponent.name':'infractionOpponentName','infraction.opponent.position':'infractionOpponentPosition','shot.goalkeeper.id':'shotGoalkeeperId','shot.goalkeeper.name':'shotGoalkeeperName'})

df = df[['id', 'matchId', 'matchPeriod', 'minutes', 'seconds', 'relatedEventId', 'typePrimary','typeSecondary1' ,'typeSecondary2','typeSecondary3','typeSecondary4','typeSecondary5','typeSecondary6','typeSecondary7','typeSecondary8','xLocation', 'yLocation', 'teamId', 'teamName', 'opponentTeamId', 'opponentTeamName', 'playerId', 'playerName', 'playerPosition', 'passAccurate', 'passAngle', 'passHeight', 'passLength', 'passRecipientId', 'passRecipientName', 'passRecipientPosition', 'passEndLocationX', 'passEndLocationY', 'possessionId', 'possessionDuration', 'possessionTypes1', 'possessionTypes2', 'possessionTypes3', 'possessionStartLocationX', 'possessionStartLocationY', 'possessionEndLocationX', 'possessionEndLocationY', 'possessionTeamId', 'possessionTeamName', 'possessionAttackWithShot', 'possessionAttackWithShotOnGoal', 'possessionAttackWithGoal', 'possessionAttackFlank', 'possessionAttackXg', 'carryProgression', 'carryEndLocationX', 'carryEndLocationY', 'aerialDuelOpponentId', 'aerialDuelOpponentName', 'aerialDuelOpponentPosition', 'aerialDuelOpponentHeight', 'aerialDuelFirstTouch', 'aerialDuelHeight', 'aerialDuelRelatedDuelId', 'groundDuelOpponentId', 'groundDuelOpponentName', 'groundDuelOpponentPosition', 'groundDuelDuelType', 'groundDuelKeptPossession', 'groundDuelProgressedWithBall', 'groundDuelStoppedProgress', 'groundDuelRecoveredPossession', 'groundDuelTakeOn', 'groundDuelSide', 'groundDuelRelatedDuelId', 'shotBodyPart', 'shotIsGoal', 'shotOnTarget', 'shotGoalZone', 'shotXg', 'shotPostShotXg', 'infractionYellowCard', 'infractionRedCard', 'infractionType', 'infractionOpponentId', 'infractionOpponentName', 'infractionOpponentPosition', 'shotGoalkeeperId', 'shotGoalkeeperName']]

df[['id', 'matchId', 'matchPeriod', 'minutes', 'seconds', 'relatedEventId', 'typePrimary','typeSecondary1' ,'typeSecondary2','typeSecondary3','typeSecondary4','typeSecondary5','typeSecondary6','typeSecondary7','typeSecondary8', 'xLocation', 'yLocation', 'teamId', 'teamName', 'opponentTeamId', 'opponentTeamName', 'playerId', 'playerName', 'playerPosition', 'passAccurate', 'passAngle', 'passHeight', 'passLength', 'passRecipientId', 'passRecipientName', 'passRecipientPosition', 'passEndLocationX', 'passEndLocationY', 'possessionId', 'possessionDuration', 'possessionTypes1', 'possessionTypes2', 'possessionTypes3', 'possessionStartLocationX', 'possessionStartLocationY', 'possessionEndLocationX', 'possessionEndLocationY', 'possessionTeamId', 'possessionTeamName', 'possessionAttackWithShot', 'possessionAttackWithShotOnGoal', 'possessionAttackWithGoal', 'possessionAttackFlank', 'possessionAttackXg', 'carryProgression', 'carryEndLocationX', 'carryEndLocationY', 'aerialDuelOpponentId', 'aerialDuelOpponentName', 'aerialDuelOpponentPosition', 'aerialDuelOpponentHeight', 'aerialDuelFirstTouch', 'aerialDuelHeight', 'aerialDuelRelatedDuelId', 'groundDuelOpponentId', 'groundDuelOpponentName', 'groundDuelOpponentPosition', 'groundDuelDuelType', 'groundDuelKeptPossession', 'groundDuelProgressedWithBall', 'groundDuelStoppedProgress', 'groundDuelRecoveredPossession', 'groundDuelTakeOn', 'groundDuelSide', 'groundDuelRelatedDuelId', 'shotBodyPart', 'shotIsGoal', 'shotOnTarget', 'shotGoalZone', 'shotXg', 'shotPostShotXg', 'infractionYellowCard', 'infractionRedCard', 'infractionType', 'infractionOpponentId', 'infractionOpponentName', 'infractionOpponentPosition', 'shotGoalkeeperId', 'shotGoalkeeperName']] = df[['id', 'matchId', 'matchPeriod', 'minutes', 'seconds', 'relatedEventId', 'typePrimary','typeSecondary1' ,'typeSecondary2','typeSecondary3','typeSecondary4','typeSecondary5','typeSecondary6','typeSecondary7','typeSecondary8', 'xLocation', 'yLocation', 'teamId', 'teamName', 'opponentTeamId', 'opponentTeamName', 'playerId', 'playerName', 'playerPosition', 'passAccurate', 'passAngle', 'passHeight', 'passLength', 'passRecipientId', 'passRecipientName', 'passRecipientPosition', 'passEndLocationX', 'passEndLocationY', 'possessionId', 'possessionDuration', 'possessionTypes1', 'possessionTypes2', 'possessionTypes3', 'possessionStartLocationX', 'possessionStartLocationY', 'possessionEndLocationX', 'possessionEndLocationY', 'possessionTeamId', 'possessionTeamName', 'possessionAttackWithShot', 'possessionAttackWithShotOnGoal', 'possessionAttackWithGoal', 'possessionAttackFlank', 'possessionAttackXg', 'carryProgression', 'carryEndLocationX', 'carryEndLocationY', 'aerialDuelOpponentId', 'aerialDuelOpponentName', 'aerialDuelOpponentPosition', 'aerialDuelOpponentHeight', 'aerialDuelFirstTouch', 'aerialDuelHeight', 'aerialDuelRelatedDuelId', 'groundDuelOpponentId', 'groundDuelOpponentName', 'groundDuelOpponentPosition', 'groundDuelDuelType', 'groundDuelKeptPossession', 'groundDuelProgressedWithBall', 'groundDuelStoppedProgress', 'groundDuelRecoveredPossession', 'groundDuelTakeOn', 'groundDuelSide', 'groundDuelRelatedDuelId', 'shotBodyPart', 'shotIsGoal', 'shotOnTarget', 'shotGoalZone', 'shotXg', 'shotPostShotXg', 'infractionYellowCard', 'infractionRedCard', 'infractionType', 'infractionOpponentId', 'infractionOpponentName', 'infractionOpponentPosition', 'shotGoalkeeperId', 'shotGoalkeeperName']].fillna(value='NULL')

with open("output.txt", "w"):
  print('USE futbol;', file=open("output.txt", "a"))
  for index, row in df.iterrows():
    print('INSERT INTO '+ Table_Name + '(id, matchId, matchPeriod, minutes, seconds, relatedEventId, typePrimary, typeSecondary1, typeSecondary2, typeSecondary3, typeSecondary4, typeSecondary5, typeSecondary6, typeSecondary7, typeSecondary8, xLocation, yLocation, teamId, teamName, opponentTeamId, opponentTeamName, playerId, playerName, playerPosition, passAccurate, passAngle, passHeight, passLength, passRecipientId, passRecipientName, passRecipientPosition, passEndLocationX, passEndLocationY, possessionId, possessionDuration, possessionTypes1, possessionTypes2, possessionTypes3, possessionStartLocationX, possessionStartLocationY, possessionEndLocationX, possessionEndLocationY, possessionTeamId, possessionTeamName, possessionAttackWithShot, possessionAttackWithShotOnGoal, possessionAttackWithGoal, possessionAttackFlank, possessionAttackXg, carryProgression, carryEndLocationX, carryEndLocationY, aerialDuelOpponentId, aerialDuelOpponentName, aerialDuelOpponentPosition, aerialDuelOpponentHeight, aerialDuelFirstTouch, aerialDuelHeight, aerialDuelRelatedDuelId, groundDuelOpponentId, groundDuelOpponentName, groundDuelOpponentPosition, groundDuelDuelType, groundDuelKeptPossession, groundDuelProgressedWithBall, groundDuelStoppedProgress, groundDuelRecoveredPossession, groundDuelTakeOn, groundDuelSide, groundDuelRelatedDuelId, shotBodyPart, shotIsGoal, shotOnTarget, shotGoalZone, shotXg, shotPostShotXg, infractionYellowCard, infractionRedCard, infractionType, infractionOpponentId, infractionOpponentName, infractionOpponentPosition, shotGoalkeeperId, shotGoalkeeperName) VALUES(',
          row['id'],',',row['matchId'],',','\''+str(row['matchPeriod'])+'\'',',',row['minutes'],',',row['seconds'],',',row['relatedEventId'],',','\''+str(row['typePrimary'])+'\'',',','\''+str(row['typeSecondary1'])+'\'',',','\''+str(row['typeSecondary2'])+'\'',',','\''+str(row['typeSecondary3'])+'\'',',','\''+str(row['typeSecondary4'])+'\'',',','\''+str(row['typeSecondary5'])+'\'',',','\''+str(row['typeSecondary6'])+'\'',',','\''+str(row['typeSecondary7'])+'\'',',','\''+str(row['typeSecondary8'])+'\'',',',row['xLocation'],',',row['yLocation'],',',row['teamId'],',','\''+str(row['teamName'])+'\'',',',row['opponentTeamId'],',','\''+str(row['opponentTeamName'])+'\'',',',row['playerId'],',','\''+str(row['playerName'])+'\'',',','\''+str(row['playerPosition'])+'\'',',',row['passAccurate'],',',row['passAngle'],',','\''+str(row['passHeight'])+'\'',',',row['passLength'],',',row['passRecipientId'],',','\''+str(row['passRecipientName'])+'\'',',','\''+str(row['passRecipientPosition'])+'\'',',',row['passEndLocationX'],',',row['passEndLocationY'],',',row['possessionId'],',',row['possessionDuration'],',','\''+str(row['possessionTypes1'])+'\'',',','\''+str(row['possessionTypes2'])+'\'',',','\''+str(row['possessionTypes3'])+'\'',',',row['possessionStartLocationX'],',',row['possessionStartLocationY'],',',row['possessionEndLocationX'],',',row['possessionEndLocationY'],',',row['possessionTeamId'],',','\''+str(row['possessionTeamName'])+'\'',',',row['possessionAttackWithShot'],',',row['possessionAttackWithShotOnGoal'],',',row['possessionAttackWithGoal'],',','\''+str(row['possessionAttackFlank'])+'\'',',',row['possessionAttackXg'],',',row['carryProgression'],',',row['carryEndLocationX'],',',row['carryEndLocationY'],',',row['aerialDuelOpponentId'],',','\''+str(row['aerialDuelOpponentName'])+'\'',',','\''+str(row['aerialDuelOpponentPosition'])+'\'',',',row['aerialDuelOpponentHeight'],',',row['aerialDuelFirstTouch'],',',row['aerialDuelHeight'],',',row['aerialDuelRelatedDuelId'],',',row['groundDuelOpponentId'],',','\''+str(row['groundDuelOpponentName'])+'\'',',','\''+str(row['groundDuelOpponentPosition'])+'\'',',','\''+str(row['groundDuelDuelType'])+'\'',',',row['groundDuelKeptPossession'],',',row['groundDuelProgressedWithBall'],',',row['groundDuelStoppedProgress'],',',row['groundDuelRecoveredPossession'],',',row['groundDuelTakeOn'],',','\''+str(row['groundDuelSide'])+'\'',',',row['groundDuelRelatedDuelId'],',','\''+str(row['shotBodyPart'])+'\'',',',row['shotIsGoal'],',',row['shotOnTarget'],',','\''+str(row['shotGoalZone'])+'\'',',','\''+str(row['shotXg'])+'\'',',','\''+str(row['shotPostShotXg'])+'\'',',',row['infractionYellowCard'],',',row['infractionRedCard'],',','\''+str(row['infractionType'])+'\'',',',row['infractionOpponentId'],',','\''+str(row['infractionOpponentName'])+'\'',',','\''+str(row['infractionOpponentPosition'])+'\'',',',row['shotGoalkeeperId'],',','\''+str(row['shotGoalkeeperName'])+'\'',');', file=open("output.txt", "a") )
