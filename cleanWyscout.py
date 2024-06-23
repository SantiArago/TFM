#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 22 20:35:34 2024

@author: santiarago
"""

import pandas as pd


df = pd.read_csv('ligue1Clean23-24.csv')
#df = pd.read_excel('belgianProLeague23-24.xlsx')
        
typeSecondaryList = ['acceleration', 'aerial_duel', 'assist', 'back_pass', 'ball_out', 'carry', 'conceded_goal', 'cross', 'deep_completion', 'defensive_duel', 'dribble', 'forward_pass', 'foul', 'foul_suffered', 'free_kick_cross', 'free_kick_shot', 'goal', 'ground_duel', 'hand_pass', 'head_pass', 'head_shot', 'interception', 'key_pass', 'lateral_pass', 'linkup_play', 'long_pass', 'loose_ball_duel', 'loss', 'opportunity', 'pass_to_final_third', 'pass_to_penalty_area', 'penalty_save', 'progressive_run', 'progressive_pass', 'recovery', 'save', 'second_assist', 'short_or_medium_pass', 'shot_after_corner', 'shot_after_free_kick', 'shot_after_throw_in', 'shot_assist', 'shot_block', 'third_assist', 'touch_in_box', 'under_pressure', 'counterpressing_recovery', 'cross_blocked', 'deep_completed_cross', 'dribbled_past_attempt', 'penalty_conceded_goal', 'save_with_reflex', 'sliding_tackle', 'smart_pass', 'through_pass', 'offensive_duel']

dummyNameList = ['isAcceleration', 'isAerialDuel', 'isAssist', 'isBackPass', 'isBallOut', 'isCarry', 'isConcededGoal', 'isCross', 'isDeepCompletion', 'isDefensiveDuel', 'isDribble', 'isForwardPass', 'isFoul', 'isFoulSuffered', 'isFreeKickCross', 'isFreeKickShot', 'isGoal', 'isGroundDuel', 'isHandPass', 'isHeadPass', 'isHeadShot', 'isInterception', 'isKeyPass', 'isLateralPass', 'isLinkupPlay', 'isLongPass', 'isLooseBallDuel', 'isLoss', 'isOpportunity', 'isPassToFinalThird', 'isPassToPenaltyArea', 'isPenaltySave', 'isProgressiveRun', 'isProgressivePass', 'isRecovery', 'isSave', 'isSecondAssist', 'isShortOrMediumPass', 'isShotAfterCorner', 'isShotAfterFreeKick', 'isShotAfterThrowIn', 'isShotAssist', 'isShotBlock', 'isThirdAssist', 'isTouchInBox', 'isUnderPressure', 'isCounterpressingRecovery', 'isCrossBlocked', 'isDeepCompletedCross', 'isDribbledPastAttempt', 'isPenaltyConcededGoal', 'isSaveWithReflex', 'isSlidingTackle', 'isSmartPass', 'isThroughPass', 'isOffensiveDuel']

possessionTypeList = ['attack', 'corner', 'counterattack', 'set_piece_attack', 'throw_in', 'transition_high', 'transition_low', 'transition_medium', 'direct_free_kick', 'free_kick', 'free_kick_cross', 'penalty']

possDummyNameList = ['isAttack', 'isCorner', 'isCounterattack', 'isSetPieceAttack', 'isThrowIn', 'isTransitionHigh', 'isTransitionLow', 'isTransitionMedium', 'isDirectFreeKick', 'isFreeKick', 'isFreeKickCross', 'isPenalty']

n = 0

m = 0

secondaryColumns = 6 #Cambia segun el número de columnas que resultan despues de separar la columna type.secondary en PowerQuery

possessionColumns = 3 #Cambia segun el número de columnas que resultan despues de separar la columna possession.types en PowerQuery
        
while n < len(typeSecondaryList):
    
    dummyList = []
    
    for index, row in df.iterrows():
       
        a=0

        i = 1
            
        while i<=secondaryColumns:
            
            column = 'type.secondary.' + str(i)
            
            if row[str(column)] == str(typeSecondaryList[n]):
               
                a = 1
                
                dummyList.append(a)
                
                break

            else:
                
                if i==secondaryColumns:
                    
                    dummyList.append(a)    
            
            i=i+1    

    
    df[str(dummyNameList[n])] = dummyList
    
    n=n+1

while m < len(possessionTypeList):
    
    dummyList = []
    
    for index, row in df.iterrows():
       
        a=0

        i = 1
        
        while i<=possessionColumns:
           
            column = 'possession.types.' + str(i)
            
            if row[str(column)] == str(possessionTypeList[m]):
                
                a = 1
                
                dummyList.append(a)
                
                break

            else:
                
                if i==possessionColumns:
                    
                    dummyList.append(a)    
            
            i=i+1    

    
    df[str(possDummyNameList[m])] = dummyList
    
    m=m+1
    
    
df.to_csv('belgiumClean22-23.csv', index=False)
