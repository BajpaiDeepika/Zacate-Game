# Automatic Zacate game player
# B551 Fall 2015
# 
# Name: Deepika Bajpai
# User Id: dbajpai
#
# Based on skeleton code by D. Crandall
#*********************************************************************************************************************************************************
# Report:
 
#                                1. Problem Formulation: 
# The smart zacate player program basically focuses on three aspects :
# 
# 1. Re-rolling the dice for first time:
# Since we get two dice re roll, so we have more sample space in re-roll 1 to get a category of higher points.and hence the probability is more that we can achieve a higher
# category if re-roll the dice.
# so, we will be re rolling the dices which have the least value for ex: if dice roll is [2,1,3,1,4], then
# we will be rolling dices 2 and 4 which have the least number 1. 
#
# 2. Re-rolling the dices for the second time:
# It is the second re roll and we have already tried one re roll, so chance is more that we can assign some higher category this time and need not to re roll.
# So we will first check the condition that if we have 
# any of the dice configuration matching to the high points categories like Quintupulo ,Pupusa de queso,Pupusa de frijol,Elote,Triple,Cuadruple,
# then we will skip re-rolling the dice and will stick to the existing configuration and move on to assign the dice.
# But, if any of the above condition is not matching, we will again find out the dices with the maximum value and re-roll them
#
# 3. Category Assignment:
# The main concept used in the program to maximize the score is to first assign the categories with more points to the dice roll for each complete turn
# We have programmed the category assignment as higher score categories gets assign first followed by the lesser ones.
#The high scoring categories are in the order:
    # 1.Quintupulo:-50 points  
    # 2.Pupusa de queso:-40 points
    # 3.Pupusa de frijol:-30 points
    # 4.Elote:-25 points to their score.
    # 5.Triple
    # 6.Cuadruple
    # 7.seises
    # 8.Cincos
    # 9.Cuatros
    # 10.Treses
    # 11.Doses
    # 12.Unos
    # 13.Tamal
    #Bonus: In case we get at least 63 score totaled across the first six categories
#    
#                    2.Problems Faced and Assumptions:
#    
#  The problems faced during the solution formulation is on how to re-roll the dice to get the max score category assigned for each turn.  
#  Also, how to assign the categories such that no categories will be assigned more than once. For this I implemented a check point to check if the category to be assigned at each turn is already resent in the scorecard or not.  
#  Also , It was confusing on when to assign the category Tamal so I assigned it at the end when no other condition is getting fulfilled or the condition which is getting fullfiled,already have the corresponding category assigned in the scorecard.  
#                    
#                    3. How well the smart zacate player program Works:
#
# Results achieved for various runs: 
# After running this program several times, I have observed that the mean score averages around 128-135.
# Further Improvement:
# The performance of the program can still be increased if we somehow manage to assign the first 6 categories so that the total score in them becomes above 63
# and we can target bonus points as well.
#
#**********************************************************************************************************************************************************************************
#
#This is the file you should modify to create your new smart Zacate player.
# The main program calls this program three times for each turn. 
#   1. First it calls first_roll, passing in a Dice object which records the
#      result of the first roll (state of 5 dice) and current Scorecard.
#      You should implement this method so that it returns a (0-based) list 
#      of dice indices that should be re-rolled.
#   
#   2. It then re-rolls the specified dice, and calls second_roll, with
#      the new state of the dice and scorecard. This method should also return
#      a list of dice indices that should be re-rolled.
#
#   3. Finally it calls third_roll, with the final state of the dice.
#      This function should return the name of a scorecard category that 
#      this roll should be recorded under. The names of the scorecard entries
#      are given in Scorecard.Categories.
#

from ZacateState import Dice
from ZacateState import Scorecard
import random
import operator

class ZacateAutoPlayer:
    def __init__(self):
        pass

    def first_roll(self, dice, scorecard):
        list1=[]   # This will return the dice number with least score.
        counts = [dice.dice.count(i) for i in range(1,7)]
        least=min(dice.dice)
        
       
        for k in [k for k,x in enumerate(dice.dice) if x == least]:
            list1.append(k)

        return list1
    
    def second_roll(self, dice, scorecard):
        list2=[]   # This will return the dice number with least score.
        counts = [dice.dice.count(i) for i in range(1,7)]
        least=min(dice.dice)
        if [sorted(dice.dice) == [1,2,3,4,5] or sorted(dice.dice) == [2,3,4,5,6] or len(set([1,2,3,4]) - set(dice.dice)) == 0 or len(set([2,3,4,5]) - set(dice.dice)) == 0 or len(set([3,4,5,6]) - set(dice.dice)) == 0 or((2 in counts) and (3 in counts)) or max(counts) >= 3 or max(counts) >= 4 or max(counts) == 5]:
            return []
        else:
            for l in [l for l,y in enumerate(dice.dice) if y == least]:
                list2.append(y)

            return list2 # will return the dices with lowest counts
      
    def third_roll(self, dice, scorecard):
            # This assigns the categories with higher score first.
            counts = [dice.dice.count(i) for i in range(1,7)]
            Categories = [ "unos", "doses", "treses", "cuatros", "cincos", "seises", "pupusa de queso", "pupusa de frijol", "elote", "triple", "cuadruple", "quintupulo", "tamal" ]
            
            if max(counts) == 5 and ("quintupulo" not in scorecard.scorecard):
                return "quintupulo"
            elif ((sorted(dice.dice) == [1,2,3,4,5] or sorted(dice.dice) == [2,3,4,5,6])) and ("pupusa de queso" not in scorecard.scorecard):
                return "pupusa de queso"
            elif ((len(set([1,2,3,4]) - set(dice.dice)) == 0 or len(set([2,3,4,5]) - set(dice.dice)) == 0 or len(set([3,4,5,6]) - set(dice.dice)) == 0)) and ("pupusa de frijol" not in scorecard.scorecard):
                return "pupusa de frijol"
            elif (2 in counts) and (3 in counts) and ("elote" not in scorecard.scorecard):
                return "elote"
            elif max(counts) >= 3 and ("triple" not in scorecard.scorecard):
                return "triple"
            elif max(counts) >= 4 and ("cuadruple" not in scorecard.scorecard):
                return "cuadruple"          
            elif counts[5]>0 and ("seises" not in scorecard.scorecard):
                return "seises"
            elif counts[4]>0 and ("cincos" not in scorecard.scorecard):
                return "cincos"
            elif counts[3]>0 and ("cuatros" not in scorecard.scorecard):
                return "cuatros"
            elif counts[2]>0 and ("treses" not in scorecard.scorecard):
                return "treses"
            elif counts[1]>0 and ("doses" not in scorecard.scorecard):
                return "doses"
            elif counts[0]>0 and ("unos" not in scorecard.scorecard):
                return "unos"
            elif "tamal" not in scorecard.scorecard:
                return "tamal"
            else:
                if scorecard.scorecard:
#                     return random.choice( list(set(Scorecard.Categories) - set(scorecard.scorecard.keys())) )
                    return list(set(Categories)-set(scorecard.scorecard))[0]
