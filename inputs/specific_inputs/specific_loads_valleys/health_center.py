# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 11:10:35 2021

@author: Clau
"""

'''
User: Health Center - VALLEYS
'''

from core import User, np
User_list = []

#Definig users
HC = User("Health center", 1)
User_list.append(HC)


HC_indoor_bulb = HC.Appliance(HC,20,7,2,690,0.2,10)
HC_indoor_bulb.windows([480,720],[870,1440],0.35)

HC_outdoor_bulb = HC.Appliance(HC,5,13,2,690,0.2,10)
HC_outdoor_bulb.windows([0,342],[1037,1440],0.35)

HC_Phone_charger = HC.Appliance(HC,5,2,2,300,0.2,5)
HC_Phone_charger.windows([480,720],[900,1440],0.35)

HC_TV = HC.Appliance(HC,2,150,2,360,0.1,60)
HC_TV.windows([480,720],[780,1020],0.2)

HC_radio = HC.Appliance(HC,5,40,2,300,0.3,60)
HC_radio.windows([480,720],[780,1020],0.35)

HC_PC = HC.Appliance(HC,2,200,2,300,0.1,10)
HC_PC.windows([480,720],[1050,1440],0.35)

HC_printer = HC.Appliance(HC,2,100,1,60,0.3,10)
HC_printer.windows([540,1020],[0,0],0.35)

HC_sterilizer_stove = HC.Appliance(HC,3,600,2,120,0.3,30, occasional_use=0.33)
HC_sterilizer_stove.windows([480,720],[780,1020],0.35)

HC_needle_destroyer = HC.Appliance(HC,1,70,1,60,0.3,10, occasional_use=0.33)
HC_needle_destroyer.windows([480,720],[0,0],0.35)

HC_water_pump = HC.Appliance(HC,1,400,1,45,0.2,10, occasional_use=0.33)
HC_water_pump.windows([480,720],[0,0],0.35)

HC_Freezer = HC.Appliance(HC,3,200,1,1440,0,30,'yes',2)
HC_Freezer.windows([0,1440],[0,0])
HC_Freezer.specific_cycle_1(5,15,200,15)
HC_Freezer.specific_cycle_2(5,20,200,10)
HC_Freezer.cycle_behaviour([360,1199],[0,0],[0,359],[1200,1440])

HC_microscope = HC.Appliance(HC,2,3,2,120,0.2,10, occasional_use=0.33)
HC_microscope.windows([480,720],[840,960],0.35)

HC_shower = HC.Appliance(HC,3,3000,2,60,0.1,15, occasional_use=0.33)
HC_shower.windows([360,720],[780,1400],0.35)

HC_heater = HC.Appliance(HC,2,1500,2,160,0.25,60, occasional_use=0.33)
HC_heater.windows([369,720],[1080,1260],0.35)

HC_dental_compresor = HC.Appliance(HC,2,500,2,60,0.15,10, occasional_use=0.33)
HC_dental_compresor.windows([480,720],[840,1260],0.35)

HC_centrifuge = HC.Appliance(HC,2,100,1,60,0.15,10, occasional_use=0.33)
HC_centrifuge.windows([480,720],[0,0],0.35)

HC_serological_rotator = HC.Appliance(HC,2,10,1,60,0.25,15, occasional_use=0.33)
HC_serological_rotator.windows([480,720],[0,0],0.35)