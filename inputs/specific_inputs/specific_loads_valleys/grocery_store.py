# -*- coding: utf-8 -*-
"""
Created on Sun Sep 19 12:12:02 2021

@author: Clau
"""

from core import User, np
User_list = []

'''
User: Grocery Store - VALLEYS
'''
#Definig users
GS = User("Grocery Store 1", 1)
User_list.append(GS)

#Appliances
GS_indoor_bulb = GS.Appliance(GS,2,7,2,120,0.2,10)
GS_indoor_bulb.windows([1107,1440],[0,30],0.35)

GS_outdoor_bulb = GS.Appliance(GS,1,13,2,600,0.2,10)
GS_outdoor_bulb.windows([0,330],[1107,1440],0.35)

GS_Freezer = GS.Appliance(GS,1,200,1,1440,0,30,'yes',2)
GS_Freezer.windows([0,1440],[0,0])
GS_Freezer.specific_cycle_1(5,15,200,15)
GS_Freezer.specific_cycle_2(5,20,200,10)
GS_Freezer.cycle_behaviour([360,1199],[0,0],[0,359],[1200,1440])

GS_Radio = GS.Appliance(GS,1,36,2,60,0.1,5)
GS_Radio.windows([390,450],[1140,1260],0.35)