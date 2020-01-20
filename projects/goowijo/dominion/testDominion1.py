# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 15:22:22 2020

@author: goodwijo
"""

import Dominion
import random
import testUtility
from collections import defaultdict

#Get player names
player_names = ["*Annie","*Ben","*Carla"]

#number of curses and victory cards
nV, nC = testUtility.victoryCurses(player_names)

#define boxes
box = testUtility.getBoxes(nV)

################################################################################## TEST INDICATOR
#introducing a duplicate for testing
box["Village"] = [Dominion.Estate()] * 10

supply_order = {0:['Curse','Copper'],2:['Estate','Cellar','Chapel','Moat'],
                3:['Silver','Chancellor','Village','Woodcutter','Workshop'],
                4:['Gardens','Bureaucrat','Feast','Militia','Moneylender','Remodel','Smithy','Spy','Thief','Throne Room'],
                5:['Duchy','Market','Council Room','Festival','Laboratory','Library','Mine','Witch'],
                6:['Gold','Adventurer'],8:['Province']}

#Pick 10 cards from box to be in the supply.
boxlist = [k for k in box]
random.shuffle(boxlist)
random10 = boxlist[:10]
supply = defaultdict(list,[(k,box[k]) for k in random10])

#adds default cards to the supply
supply = testUtility.getSupply(nV,supply, player_names, nC)

#initialize the trash
trash = []

#create player objects
players = testUtility.getPlayers(player_names)


#Play the game
turn  = 0
while not Dominion.gameover(supply):
    turn += 1    
    print("\r")    
    for value in supply_order:
        print (value)
        for stack in supply_order[value]:
            if stack in supply:
                print (stack, len(supply[stack]))
    print("\r")
    for player in players:
        print (player.name,player.calcpoints())
    print ("\rStart of turn " + str(turn))    
    for player in players:
        if not Dominion.gameover(supply):
            print("\r")
            player.turn(players,supply,trash)
            

# Final score
testUtility.getFinal(players)
