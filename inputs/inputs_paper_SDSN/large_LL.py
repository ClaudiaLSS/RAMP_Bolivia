# -*- coding: utf-8 -*-
"""
Created on Wed Mar  9 11:45:02 2022

@author: Clau

Large family - Lowlands
"""

import pandas as pd

from core import User, np
User_list = []

#Create new user classes

L = User("large",1)
User_list.append(L)

L_shower_P = pd.read_csv('shower_P.csv')

#Appliances

L_indoor_bulb = L.Appliance(L,7,7,2,300,0.2,10)
L_indoor_bulb.windows([1170,1440],[0,30],0.35)

L_outdoor_bulb = L.Appliance(L,2,13,2,300,0.2,10)
L_outdoor_bulb.windows([0,330],[1170,1440],0.35)

L_Phone_charger = L.Appliance(L,6,6,2,60,0.2,15)
L_Phone_charger.windows([420,1440],[0,400],0.35)

L_Radio = L.Appliance(L,2,7,1,180,0.1,10)
L_Radio.windows([420,840],[0,0],0.35)

L_TV = L.Appliance(L,2,150,2,300,0.3,5)
L_TV.windows([720,900],[1170,1440],0.35)

L_Laptop = L.Appliance(L,2,100,1,240,0.3,30)
L_Laptop.windows([960,1200],[0,0],0.35)

L_TV_cable = L.Appliance(L,2,35,2,300,0.3,5)
L_TV_cable.windows([720,900],[1170,1440],0.35)

L_Stereo = L.Appliance(L,1,450,1,250,0.3,15, occasional_use = 0.5)
L_Stereo.windows([840,1320],[0,0],0.35)

L_Washing_machine = L.Appliance(L,1,800,2,90,0.3,30, occasional_use = 0.5)
L_Washing_machine.windows([480,720],[900,1200],0.35)

L_Microwave = L.Appliance(L,1,800,3,30,0.3,1, occasional_use = 0.5)
L_Microwave.windows([420,540],[720,900],0.3,[1080,1260])

L_water_pump = L.Appliance(L,1,250,2,30,0.3,15, occasional_use = 0.5)
L_water_pump.windows([420,720],[960,1260],0.35)

L_Freezer = L.Appliance(L,1,200,1,1440,0,30,'yes',3)
L_Freezer.windows([0,1440],[0,0])
L_Freezer.specific_cycle_1(200,20,5,10)
L_Freezer.specific_cycle_2(200,15,5,15)
L_Freezer.specific_cycle_3(200,10,5,20)
L_Freezer.cycle_behaviour([480,1200],[0,0],[300,479],[0,0],[0,299],[1201,1440])


L_shower = L.Appliance(L,1,L_shower_P,2,45,0.1,3, thermal_P_var = 0.2, P_series=True, occasional_use = 0.6)
L_shower.windows([390,540],[1080,1200],0.2)

L_Air_Conditioner = L.Appliance(L,2,1000,2,120,0.2,15)
L_Air_Conditioner.windows([720,900],[1020,1260],0.35)
