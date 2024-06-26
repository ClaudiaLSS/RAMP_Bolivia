# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 13:44:54 2021

@author: Clau
"""

'''
User: Entertainment Bussines - VALLEYS
'''

from core import User, np
User_list = []

#Definig users

EB = User("Entertainment Business", 1)
User_list.append(EB)

#Appliances

EB_indoor_bulb = EB.Appliance(EB,2,7,2,120,0.2,10)
EB_indoor_bulb.windows([1107,1440],[0,30],0.35)

EB_outdoor_bulb = EB.Appliance(EB,1,13,2,600,0.2,10)
EB_outdoor_bulb.windows([0,330],[1107,1440],0.35)


EB_Stereo = EB.Appliance(EB,1,150,2,90,0.1,5, occasional_use = 0.33)
EB_Stereo.windows([480,780],[0,0],0.35)

EB_TV = EB.Appliance(EB,1,60,2,120,0.1,5, occasional_use = 0.33)
EB_TV.windows([480,780],[840,1140],0.2)
    
EB_PC = EB.Appliance(EB,1,50,2,210,0.1,10, occasional_use = 0.33)
EB_PC.windows([480,780],[840,1140],0.35)

EB_Freezer = EB.Appliance(EB,1,200,1,1440,0,30,'yes',2)
EB_Freezer.windows([0,1440],[0,0])
EB_Freezer.specific_cycle_1(5,15,200,15)
EB_Freezer.specific_cycle_2(5,20,200,10)
EB_Freezer.cycle_behaviour([360,1199],[0,0],[0,359],[1200,1440])