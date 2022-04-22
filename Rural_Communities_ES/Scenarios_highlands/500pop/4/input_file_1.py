# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 18:33:20 2022

@author: pietr
"""

'''
Paper: Energy sufficiency (SDEWES LA 2022)
User: High Income Household - HIGHLANDS
'''
from core import User, np
User_list = []


###################### Residential ##############

#Defining users
H1 = User("low income household", 85) 
User_list.append(H1)
    
#Appliances
H1_indoor_bulb = H1.Appliance(H1,3,7,2,120,0.2,10)
H1_indoor_bulb.windows([1082,1440],[0,30],0.35)

H1_outdoor_bulb = H1.Appliance(H1,1,13,2,600,0.2,10)
H1_outdoor_bulb.windows([0,330],[1082,1440],0.35)

H1_TV = H1.Appliance(H1,1,60,2,90,0.1,5)
H1_TV.windows([750,840],[1082,1440],0.35)

H1_Radio = H1.Appliance(H1,1,36,2,60,0.1,5)
H1_Radio.windows([390,450],[1082,1260],0.35)

H1_Phone_charger = H1.Appliance(H1,2,2,1,300,0.2,5)
H1_Phone_charger.windows([1080,1440],[0,0],0.35)

#Defining users
H2 = User("high income household", 77)
User_list.append(H2)

#Appliances
H2_indoor_bulb = H2.Appliance(H2,4,7,2,120,0.2,10)
H2_indoor_bulb.windows([1082,1440],[0,30],0.35)
         
H2_outdoor_bulb = H2.Appliance(H2,2,13,2,600,0.2,10)
H2_outdoor_bulb.windows([0,330],[1082,1440],0.35)

H2_TV = H2.Appliance(H2,2,60,2,120,0.1,5)
H2_TV.windows([1082,1440],[0,60],0.35)

H2_DVD = H2.Appliance(H2,1,8,2,40,0.1,5)
H2_DVD.windows([1082,1440],[0,60],0.35)

H2_Radio = H2.Appliance(H2,1,36,2,60,0.1,5)
H2_Radio.windows([390,450],[1082,1260],0.35)

H2_Phone_charger = H2.Appliance(H2,4,2,2,300,0.2,5)
H2_Phone_charger.windows([1110,1440],[0,30],0.35)

H2_Freezer = H2.Appliance(H2,1,200,1,1440,0,30,'yes',3)
H2_Freezer.windows([0,1440],[0,0])
H2_Freezer.specific_cycle_1(200,15,5,15)
H2_Freezer.specific_cycle_2(200,15,5,15)
H2_Freezer.specific_cycle_3(200,10,5,20)
H2_Freezer.cycle_behaviour([480,1200],[0,0],[300,479],[0,0],[0,299],[1201,1440])

H2_Mixer = H2.Appliance(H2,1,50,3,30,0.1,1, occasional_use = 0.33)
H2_Mixer.windows([420,450],[660,750],0.35,[1020,1170])

H2_Iron = H2.Appliance(H2,1,1000,2,15,0.2,5,occasional_use =0.33)
H2_Iron.windows([420,480],[720,780],0.35)

H2_Laptop = H2.Appliance(H2,1,70,1,90,0.3,30)
H2_Laptop.windows([960,1200],[0,0],0.35)

########################### Community services ##
#Definig users

PL = User("Public lighting ", 16)
User_list.append(PL)

#Appliances

PL_lamp_post = PL.Appliance(PL,1,40,2,310,0,300, 'yes', flat = 'yes')
PL_lamp_post.windows([0,362],[1082,1440],0.1)

#Definig users

WSS = User("water supply system", 2)
User_list.append(WSS)

#Appliances

WSS_water_pump = WSS.Appliance(WSS,1,1700,2,60,0.2,10,occasional_use = 0.33)
WSS_water_pump.windows([420,720],[840,1020],0.35)

#Definig users

SB = User("School type B", 1)
User_list.append(SB)

#Appliances

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

SB_PC = SB.Appliance(SB,1,50,2,210,0.1,10)
SB_PC.windows([480,780],[840,1140],0.35)

SB_Phone_charger = SB.Appliance(SB,3,2,2,180,0.2,5)
SB_Phone_charger.windows([480,780],[840,1140],0.35)

#Defining users
HP = User("Health post", 1)
User_list.append(HP)

#Appliances

# indoor_bulb OK!
HP_indoor_bulb = HP.Appliance(HP,12,7,2,630,0.1,10)
HP_indoor_bulb.windows([420,870],[870,1440],0.35)

HP_outdoor_bulb = HP.Appliance(HP,1,13,2,690,0.2,10)
HP_outdoor_bulb.windows([0,342],[1037,1440],0.35)

HP_Phone_charger = HP.Appliance(HP,5,2,2,300,0.2,5)
HP_Phone_charger.windows([480,720],[900,1440],0.35)

HP_TV = HP.Appliance(HP,1,150,2,360,0.1,60)
HP_TV.windows([480,720],[780,1020],0.2)

HP_radio = HP.Appliance(HP,1,40,2,300,0.1,60)
HP_radio.windows([480,720],[780,1020],0.35)

HP_PC = HP.Appliance(HP,1,200,2,300,0.1,10)
HP_PC.windows([480,720],[1050,1440],0.35)

HP_printer = HP.Appliance(HP,1,100,1,60,0.3,10)
HP_printer.windows([540,1020],[0,0],0.35)

HP_sterilizer_stove = HP.Appliance(HP,1,600,2,120,0.3,30, occasional_use=0.33)
HP_sterilizer_stove.windows([480,720],[780,1020],0.35)

HP_needle_destroyer = HP.Appliance(HP,1,70,1,60,0.3,10, occasional_use=0.33)
HP_needle_destroyer.windows([480,720],[0,0],0.35)

HP_water_pump = HP.Appliance(HP,1,400,1,30,0.2,10)
HP_water_pump.windows([480,720],[0,0],0.35)

HP_Freezer = HP.Appliance(HP,1,200,1,1440,0,30,'yes',3)
HP_Freezer.windows([0,1440],[0,0])
HP_Freezer.specific_cycle_1(200,15,5,15)
HP_Freezer.specific_cycle_2(200,15,5,15)
HP_Freezer.specific_cycle_3(200,10,5,20)
HP_Freezer.cycle_behaviour([480,1200],[0,0],[300,479],[0,0],[0,299],[1201,1440])


#################### IGA agricultural ####################
#Definig users

IW = User("Irrigation Water", 5)
User_list.append(IW)

#Appliances

IW_water_pump = IW.Appliance(IW,1,1700,2,60,0.2,10,occasional_use = 0.33)
IW_water_pump.windows([420,720],[840,1020],0.35)

#Definig users

LAU = User("Lowlands agro-productive unit", 1)
User_list.append(LAU)

#Appliances

LAU_grain_dryer = LAU.Appliance(LAU,1,9360,1,180,0.2,30,occasional_use = 0.33)
LAU_grain_dryer.windows([420,1080],[0,0],0.35)

LAU_grain_miller = LAU.Appliance(LAU,1,11700,1,180,0.2,15,occasional_use = 0.33)
LAU_grain_miller.windows([420,1080],[0,0],0.35)

LAU_water_pump = LAU.Appliance(LAU,1,1170,1,480,0.2,15,occasional_use = 0.33)
LAU_water_pump.windows([420,1140],[0,0],0.35)

LAU_wool_clipper = LAU.Appliance(LAU,1,350,1,60,0.2,15,occasional_use = 0.33)
LAU_wool_clipper.windows([390,540],[0,0],0.35)

################################## IGA non agricultural ##########

#Definig users

R = User("Restaurant", 5)
User_list.append(R)

#Appliances

R_indoor_bulb = R.Appliance(R,2,7,2,120,0.2,10)
R_indoor_bulb.windows([1107,1440],[0,30],0.35)

R_Blender = R.Appliance(R,1,350,2,20,0.375,5)
R_Blender.windows([420,480],[720,780],0.5)

R_Freezer = R.Appliance(R,1,200,1,1440,0,30,'yes',3)
R_Freezer.windows([0,1440],[0,0])
R_Freezer.specific_cycle_1(200,15,5,15)
R_Freezer.specific_cycle_2(200,15,5,15)
R_Freezer.specific_cycle_3(200,10,5,20)
R_Freezer.cycle_behaviour([480,1200],[0,0],[300,479],[0,0],[0,299],[1201,1440])

#Definig users
GS = User("Grocery Store 1", 6)
User_list.append(GS)

#Appliances
GS_indoor_bulb = GS.Appliance(GS,2,7,2,120,0.2,10)
GS_indoor_bulb.windows([1107,1440],[0,30],0.35)

GS_outdoor_bulb = GS.Appliance(GS,1,13,2,600,0.2,10)
GS_outdoor_bulb.windows([0,330],[1107,1440],0.35)

GS_Freezer = GS.Appliance(GS,1,200,1,1440,0,30,'yes',3)
GS_Freezer.windows([0,1440],[0,0])
GS_Freezer.specific_cycle_1(200,15,5,15)
GS_Freezer.specific_cycle_2(200,15,5,15)
GS_Freezer.specific_cycle_3(200,10,5,20)
GS_Freezer.cycle_behaviour([480,1200],[0,0],[300,479],[0,0],[0,299],[1201,1440])

GS_Radio = GS.Appliance(GS,1,36,2,60,0.1,5)
GS_Radio.windows([390,450],[1140,1260],0.35)

#Definig users

EB = User("Entertainment Business", 2)
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

EB_freezer = EB.Appliance(EB,1,200,1,1440,0,30,'yes',3)
EB_freezer.windows([0,1440],[0,0])
EB_freezer.specific_cycle_1(200,20,5,10)
EB_freezer.specific_cycle_2(200,15,5,15)
EB_freezer.specific_cycle_3(200,10,5,20)
EB_freezer.cycle_behaviour([480,1200],[0,0],[300,479],[0,0],[0,299],[1201,1440])

#Definig users

WS = User("Workshop", 2)
User_list.append(WS)

#Appliances

WS_indoor_bulb = WS.Appliance(WS,2,7,2,120,0.2,10)
WS_indoor_bulb.windows([1107,1440],[0,30],0.35)

WS_welding_machine = WS.Appliance(WS,1,5500,1,60,0.5,30, occasional_use = 0.3)
WS_welding_machine.windows([0,1440],[0,0],0.35)

WS_grinding_machine = WS.Appliance(WS,1,750,1,480,0.2,60, occasional_use = 0.3)
WS_grinding_machine.windows([0,1440],[0,0],0.35)

WS_Radio = WS.Appliance(WS,1,36,2,60,0.1,5)
WS_Radio.windows([390,450],[1140,1260],0.35)