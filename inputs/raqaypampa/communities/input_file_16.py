#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 12 20:10:05 2023

@author: claudia

Laguna Grande
"""
from core import User, np
User_list = []

#Users

HI = User("high income",6)
User_list.append(HI)

LI = User("low income",35)
User_list.append(LI)

HC = User("health center",1)
User_list.append(HC)

SB = User("School type B", 1)
User_list.append(SB)
#Appliances

#High consumption household


HI_indoor_bulb = HI.Appliance(HI,3,7,1,300,0.2,180)
HI_indoor_bulb.windows([1080,1440],[0,0],0.35)

HI_outdoor_bulb = HI.Appliance(HI,1,13,1,320,0.2,120)
HI_outdoor_bulb.windows([1100,1440],[0,0],0.35)

HI_Radio = HI.Appliance(HI,1,7,2,280,0.2,120)
HI_Radio.windows([420,708],[840,1020],0.35)

HI_TV = HI.Appliance(HI,1,60,2,120,0.2,60)
HI_TV.windows([840,1080],[1140,1440],0.35)

HI_Phone_charger = HI.Appliance(HI,2,5,3,240,0.2,95)
HI_Phone_charger.windows([421,660],[1190,1440],0.35,[0,420])

HI_Freezer = HI.Appliance(HI,1,200,1,1440,0,30,'yes',3)
HI_Freezer.windows([0,1440],[0,0])
HI_Freezer.specific_cycle_1(200,15,5,15)
HI_Freezer.specific_cycle_2(200,15,5,15)
HI_Freezer.specific_cycle_3(200,10,5,20)
HI_Freezer.cycle_behaviour([480,1200],[0,0],[300,479],[0,0],[0,299],[1201,1440])


#Low consumption household

HI_indoor_bulb = HI.Appliance(HI,2,7,1,300,0.2,180)
HI_indoor_bulb.windows([1080,1440],[0,0],0.35)

HI_outdoor_bulb = HI.Appliance(HI,1,13,1,320,0.2,120)
HI_outdoor_bulb.windows([1100,1440],[0,0],0.35)

HI_Radio = HI.Appliance(HI,1,7,2,280,0.2,120)
HI_Radio.windows([420,708],[840,1020],0.35)

HI_TV = HI.Appliance(HI,1,60,2,120,0.2,60)
HI_TV.windows([840,1080],[1140,1440],0.35)

HI_Phone_charger = HI.Appliance(HI,1,5,3,240,0.2,95)
HI_Phone_charger.windows([421,660],[1190,1440],0.35,[0,420])


#Type B school
SB_indoor_bulb = SB.Appliance(SB,12,7,2,120,0.25,30)
SB_indoor_bulb.windows([480,780],[840,1140],0.35)

SB_outdoor_bulb = SB.Appliance(SB,3,13,1,60,0.2,10)
SB_outdoor_bulb.windows([960,1080],[0,0],0.35)

SB_TV = SB.Appliance(SB,1,60,2,120,0.1,5, occasional_use = 0.5)
SB_TV.windows([480,780],[840,1140],0.2)

SB_radio = SB.Appliance(SB,3,4,2,120,0.1,5, occasional_use = 0.5)
SB_radio.windows([480,780],[840,1140],0.2)

SB_DVD = SB.Appliance(SB,2,8,2,120,0.1,5, occasional_use = 0.5)
SB_DVD.windows([480,780],[840,1140],0.2)

SB_Freezer = SB.Appliance(SB,1,200,1,1440,0,30,'yes',3)
SB_Freezer.windows([0,1440],[0,0])
SB_Freezer.specific_cycle_1(200,15,5,15)
SB_Freezer.specific_cycle_2(200,15,5,15)
SB_Freezer.specific_cycle_3(200,10,5,20)
SB_Freezer.cycle_behaviour([480,1200],[0,0],[300,479],[0,0],[0,299],[1201,1440])

SB_PC = SB.Appliance(SB,1,50,2,210,0.2,10)
SB_PC.windows([480,780],[840,1140],0.35)

SB_Phone_charger = SB.Appliance(SB,3,2,2,180,0.2,5)
SB_Phone_charger.windows([480,780],[840,1140],0.35)

#Health center

HC_indoor_bulb = HC.Appliance(HC,8,7,2,690,0.2,10)
HC_indoor_bulb.windows([480,720],[870,1440],0.35)

HC_outdoor_bulb = HC.Appliance(HC,5,13,2,690,0.2,10)
HC_outdoor_bulb.windows([0,342],[1037,1440],0.35)

HC_Phone_charger = HC.Appliance(HC,5,2,2,300,0.2,5)
HC_Phone_charger.windows([480,720],[900,1440],0.35)

HC_TV = HC.Appliance(HC,1,150,2,360,0.1,60)
HC_TV.windows([480,720],[780,1020],0.2)

HC_radio = HC.Appliance(HC,3,40,2,360,0.3,60)
HC_radio.windows([480,720],[780,1020],0.2)

HC_PC = HC.Appliance(HC,2,200,2,300,0.1,10)
HC_PC.windows([480,720],[1050,1440],0.35)

HC_printer = HC.Appliance(HC,2,100,1,60,0.3,10)
HC_printer.windows([540,1020])

HC_sterilizer_stove = HC.Appliance(HC,1,600,2,120,0.3,30, occasional_use=0.3)
HC_sterilizer_stove.windows([540,600],[900,960],)

HC_needle_destroyer = HC.Appliance(HC,1,70,1,60,0.2,10, occasional_use=0.3)
HC_needle_destroyer.windows([540,600])

HC_water_pump = HC.Appliance(HC,1,400,1,30,0.2,10)
HC_water_pump.windows([480,510])

HC_Fridge = HC.Appliance(HC,1,150,1,1440,0,30, 'yes',3)
HC_Fridge.windows([0,1440],[0,0])
HC_Fridge.specific_cycle_1(150,20,5,10)
HC_Fridge.specific_cycle_2(150,15,5,15)
HC_Fridge.specific_cycle_3(150,10,5,20)
HC_Fridge.cycle_behaviour([580,1200],[0,0],[420,579],[0,0],[0,419],[1201,1440])

HC_Fridge2 = HC.Appliance(HC,1,150,1,1440,0,30, 'yes',3)
HC_Fridge2.windows([0,1440],[0,0])
HC_Fridge2.specific_cycle_1(150,20,5,10)
HC_Fridge2.specific_cycle_2(150,15,5,15)
HC_Fridge2.specific_cycle_3(150,10,5,20)
HC_Fridge2.cycle_behaviour([580,1200],[0,0],[420,579],[0,0],[0,299],[1201,1440])

HC_microscope = HC.Appliance(HC,1,3,2,120,0.2,10, occasional_use=0.3)
HC_microscope.windows([480,720],[840,960],0.35)

HC_shower = HC.Appliance(HC,1,3000,2,120,0,1,15)
HC_shower.windows([360,720],[780,2400],0.35)

HC_heater = HC.Appliance(HC,2,1500,2,180,0.25,60, occasional_use=0.3)
HC_heater.windows([369,720],[1080,1260],0.35)

HC_dental_compresor = HC.Appliance(HC,1,500,2,60,0.15,10, occasional_use=0.3)
HC_dental_compresor.windows([480,720],[840,1260],0.2)

HC_centrifuge = HC.Appliance(HC,1,100,1,60,0.15,10, occasional_use=0.3)
HC_centrifuge.windows([480,720],[0,0])

HC_serological_rotator = HC.Appliance(HC,1,10,1,60,0.25,15, occasional_use=0.2)
HC_serological_rotator.windows([480,720],[0,0])
