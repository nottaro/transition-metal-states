#Investigation 3, Periodic Table trends
#This lets me create mathematical functions and equations
import math
#This lets me create time delays for effects
import time
#This lets me access the states of matter
State1 = 'solid'
State2 = 'liquid'
State3 = 'gas'
#These lists let me access the properties from each element, from chemical name, metal number, melting point and boiling point.
Sc = ['Sc', 'Scandium','3']
CSc = ['1540.85', '2829.85']
KSc = ['1814', '3103']
FSc = ['2805.53', '4963.73']
Ti = ['Ti', 'Titanium', '4'] 
CTi = ['1667.85', '3286.85']
KTi = ['1941', '3560']
FTi = ['3034.13', '5948.33']
V = ['V', 'Vanadium','5']
CV = ['1909.85', '3406.85']
KV = ['2183', '3680']
FV = ['3469.73', '6164.33']
Cr = ['Cr', 'Chromium', '6']
CCr = ['1906.85', '2670.85']
KCr = ['2180', '2944']
FCr = ['3464.33', '4839.53']
Mn = ['Mn', 'Magnesium', '7']
CMn = ['1245.85', '2060.85']
KMn = ['1519', '2334']
FMn = ['2274.53', '3741.53']
Fe = ['Fe', 'Iron', '8']
CFe = ['1537.85', '2860.85']
KFe = ['1811', '3134']
FFe = ['2800.13', '5181.53']
Co = ['Co', 'Cobalt', '9']
CCo = ['1494.85', '2926.85']
KCo = ['1768', '3200']
FCo = ['2722.73', '5300.33']
Ni = ['Ni', 'Nickel', '10']
CNi = ['1454.85', '2912.85']
KNi = ['1728', '3186']
FNi = ['2650.73', '5275.13']
Cu = ['Cu', 'Copper', '11']
CCu = ['1084.62', '2926.85']
KCu = ['1357.77', '3200']
FCu = ['1984.316', '5300.33']
Zn = ['Zn', 'Zinc', '12']
CZn = ['419.53', '906.85']
KZn = ['692.68', '1180']
FZn = ['787.154', '1664.33']


print('Insert a temperature and the state of matter of the transition metals will be generated.')
x = input('Would you like to proceed? Y/N: ')
if x == 'Y':
  y = input('Please select a temperature type. Celsius(C), Kelvin(K) or Farenheit(F). Input "C", "K", or "F": ')
  
  #Celsius
  if y == 'C':
    z = float(input('Temperature in Celsius: '))
    #This is the Scandium code
    if (str(z)) < CSc[0]:
      print(Sc[1] + ', a.k.a ' + Sc[0] + ', from group ' + Sc[2] + ' would be a ' + State1)
    elif CSc[0] > (str(z)) < CSc[1]:
      print(Sc[1] + ', a.k.a. ' + Sc[0] + ', from group ' + Sc[2] + ' would be a ' + State2)
    elif (str(z)) > CSc[1]:
      print(Sc[1] + ', a.k.a. ' + Sc[0] + ', from group ' + Sc[2] + ' would be a ' + State3)
    #This is the Titanium code
    if (str(z)) < CTi[0]:
      print(Ti[1] + ', a.k.a ' + Ti[0] + ', from group ' + Ti[2] + ' would be a ' + State1)
    elif CTi[0] > (str(z)) < CTi[1]:
      print(Ti[1] + ', a.k.a. ' + Ti[0] + ', from group ' + Ti[2] + ' would be a ' + State2)
    elif (str(z)) > CTi[1]:
      print(Ti[1] + ', a.k.a. ' + Ti[0] + ', from group ' + Ti[2] + ' would be a ' + State3)
    #This is the Vanadium code
    if (str(z)) < CV[0]:
      print(V[1] + ', a.k.a ' + V[0] + ', from group ' + V[2] + ' would be a ' + State1)
    elif CV[0] > (str(z)) < CV[1]:
      print(V[1] + ', a.k.a. ' + V[0] + ', from group ' + V[2] + ' would be a ' + State2)
    elif (str(z)) > CV[1]:
      print(V[1] + ', a.k.a. ' + V[0] + ', from group ' + V[2] + ' would be a ' + State3)
    #This is the Chromium     code
    if (str(z)) < CCr[0]:
      print(Cr[1] + ', a.k.a ' + Cr[0] + ', from group ' + Cr[2] + ' would be a ' + State1)
    elif CCr[0] > (str(z)) < CCr[1]:
      print(Cr[1] + ', a.k.a. ' + Cr[0] + ', from group ' + Cr[2] + ' would be a ' + State2)
    elif (str(z)) > CCr[1]:
      print(Cr[1] + ', a.k.a. ' + Cr[0] + ', from group ' + Cr[2] + ' would be a ' + State3)
    #This is the Maganese code
    if (str(z)) < CMn[0]:
      print(Mn[1] + ', a.k.a ' + Mn[0] + ', from group ' + Mn[2] + ' would be a ' + State1)
    elif CMn[0] > (str(z)) < CMn[1]:
      print(Mn[1] + ', a.k.a. ' + Mn[0] + ', from group ' + Mn[2] + ' would be a ' + State2)
    elif (str(z)) > CMn[1]:
      print(Mn[1] + ', a.k.a. ' + Mn[0] + ', from group ' + Mn[2] + ' would be a ' + State3)
    #This is the Iron code
    if (str(z)) < CFe[0]:
      print(Fe[1] + ', a.k.a ' + Fe[0] + ', from group ' + Fe[2] + ' would be a ' + State1)
    elif CFe[0] > (str(z)) < CFe[1]:
      print(Fe[1] + ', a.k.a. ' + Fe[0] + ', from group ' + Fe[2] + ' would be a ' + State2)
    elif (str(z)) > CFe[1]:
      print(Fe[1] + ', a.k.a. ' + Fe[0] + ', from group ' + Fe[2] + ' would be a ' + State3)
    #This is the Cobalt code
    if (str(z)) < CCo[0]:
      print(Co[1] + ', a.k.a ' + Co[0] + ', from group ' + Co[2] + ' would be a ' + State1)
    elif CCo[0] > (str(z)) < CCo[1]:
      print(Co[1] + ', a.k.a. ' + Co[0] + ', from group ' + Co[2] + ' would be a ' + State2)
    elif (str(z)) > CCo[1]:
      print(Co[1] + ', a.k.a. ' + Co[0] + ', from group ' + Co[2] + ' would be a ' + State3)
    #This is the Nickel code
    if (str(z)) < CNi[0]:
      print(Ni[1] + ', a.k.a ' + Ni[0] + ', from group ' + Ni[2] + ' would be a ' + State1)
    elif CNi[0] > (str(z)) < CNi[1]:
      print(Ni[1] + ', a.k.a. ' + Ni[0] + ', from group ' + Ni[2] + ' would be a ' + State2)
    elif (str(z)) > CNi[1]:
      print(Ni[1] + ', a.k.a. ' + Ni[0] + ', from group ' + Ni[2] + ' would be a ' + State3)
    #This is the Copper code
    if (str(z)) < CCu[0]:
      print(Cu[1] + ', a.k.a ' + Cu[0] + ', from group ' + Cu[2] + ' would be a ' + State1)
    elif CCu[0] > (str(z)) < CCu[1]:
      print(Cu[1] + ', a.k.a. ' + Cu[0] + ', from group ' + Cu[2] + ' would be a ' + State2)
    elif (str(z)) > CCu[1]:
      print(Cu[1] + ', a.k.a. ' + Cu[0] + ', from group ' + Cu[2] + ' would be a ' + State3)
    #This is the Zinc code
    if (str(z)) < CZn[0]:
      print(Zn[1] + ', a.k.a ' + Zn[0] + ', from group ' + Zn[2] + ' would be a ' + State1)
    elif CZn[0] > (str(z)) < CZn[1]:
      print(Zn[1] + ', a.k.a. ' + Zn[0] + ', from group ' + Zn[2] + ' would be a ' + State2)
    elif (str(z)) > CZn[1]:
      print(Zn[1] + ', a.k.a. ' + Zn[0] + ', from group ' + Zn[2] + ' would be a ' + State3)
  
#Kelvin
  elif y == 'K':
    a = float(input('Temperature in Kelvin: '))
    #This is the Scandium code
    if (str(a)) < KSc[0]:
      print(Sc[1] + ', a.k.a ' + Sc[0] + ', from group ' + Sc[2] + ' would be a ' + State1)
    elif KSc[0] > (str(a)) < KSc[1]:
      print(Sc[1] + ', a.k.a. ' + Sc[0] + ', from group ' + Sc[2] + ' would be a ' + State2)
    elif (str(a)) > KSc[1]:
      print(Sc[1] + ', a.k.a. ' + Sc[0] + ', from group ' + Sc[2] + ' would be a ' + State3)
    #This is the Titanium code
    if (str(a)) < KTi[0]:
      print(Ti[1] + ', a.k.a ' + Ti[0] + ', from group ' + Ti[2] + ' would be a ' + State1)
    elif KTi[0] > (str(a)) < KTi[1]:
      print(Ti[1] + ', a.k.a. ' + Ti[0] + ', from group ' + Ti[2] + ' would be a ' + State2)
    elif (str(a)) > KTi[1]:
      print(Ti[1] + ', a.k.a. ' + Ti[0] + ', from group ' + Ti[2] + ' would be a ' + State3)
    #This is the Vanadium code
    if (str(a)) < KV[0]:
      print(V[1] + ', a.k.a ' + V[0] + ', from group ' + V[2] + ' would be a ' + State1)
    elif KV[0] > (str(a)) < KV[1]:
      print(V[1] + ', a.k.a. ' + V[0] + ', from group ' + V[2] + ' would be a ' + State2)
    elif (str(a)) > KV[1]:
      print(V[1] + ', a.k.a. ' + V[0] + ', from group ' + V[2] + ' would be a ' + State3)
    #This is the Chromium code
    if (str(a)) < KCr[0]:
      print(Cr[1] + ', a.k.a ' + Cr[0] + ', from group ' + Cr[2] + ' would be a ' + State1)
    elif KCr[0] > (str(a)) < KCr[1]:
      print(Cr[1] + ', a.k.a. ' + Cr[0] + ', from group ' + Cr[2] + ' would be a ' + State2)
    elif (str(a)) > KCr[1]:
      print(Cr[1] + ', a.k.a. ' + Cr[0] + ', from group ' + Cr[2] + ' would be a ' + State3)
    #This is the Maganese code
    if (str(a)) < KMn[0]:
      print(Mn[1] + ', a.k.a ' + Mn[0] + ', from group ' + Mn[2] + ' would be a ' + State1)
    elif KMn[0] > (str(a)) < KMn[1]:
      print(Mn[1] + ', a.k.a. ' + Mn[0] + ', from group ' + Mn[2] + ' would be a ' + State2)
    elif (str(a)) > KMn[1]:
      print(Mn[1] + ', a.k.a. ' + Mn[0] + ', from group ' + Mn[2] + ' would be a ' + State3)
    #This is the Iron code
    if (str(a)) < KFe[0]:
      print(Fe[1] + ', a.k.a ' + Fe[0] + ', from group ' + Fe[2] + ' would be a ' + State1)
    elif KFe[0] > (str(a)) < KFe[1]:
      print(Fe[1] + ', a.k.a. ' + Fe[0] + ', from group ' + Fe[2] + ' would be a ' + State2)
    elif (str(a)) > KFe[1]:
      print(Fe[1] + ', a.k.a. ' + Fe[0] + ', from group ' + Fe[2] + ' would be a ' + State3)
    #This is the Cobalt code
    if (str(a)) < KCo[0]:
      print(Co[1] + ', a.k.a ' + Co[0] + ', from group ' + Co[2] + ' would be a ' + State1)
    elif KCo[0] > (str(a)) < KCo[1]:
      print(Co[1] + ', a.k.a. ' + Co[0] + ', from group ' + Co[2] + ' would be a ' + State2)
    elif (str(a)) > KCo[1]:
      print(Co[1] + ', a.k.a. ' + Co[0] + ', from group ' + Co[2] + ' would be a ' + State3)
    #This is the Nickel code
    if (str(a)) < KNi[0]:
      print(Ni[1] + ', a.k.a ' + Ni[0] + ', from group ' + Ni[2] + ' would be a ' + State1)
    elif KNi[0] > (str(a)) < KNi[1]:
      print(Ni[1] + ', a.k.a. ' + Ni[0] + ', from group ' + Ni[2] + ' would be a ' + State2)
    elif (str(a)) > KNi[1]:
      print(Ni[1] + ', a.k.a. ' + Ni[0] + ', from group ' + Ni[2] + ' would be a ' + State3)
    #This is the Copper code
    if (str(a)) < KCu[0]:
      print(Cu[1] + ', a.k.a ' + Cu[0] + ', from group ' + Cu[2] + ' would be a ' + State1)
    elif KCu[0] > (str(a)) < KCu[1]:
      print(Cu[1] + ', a.k.a. ' + Cu[0] + ', from group ' + Cu[2] + ' would be a ' + State2)
    elif (str(a)) > KCu[1]:
      print(Cu[1] + ', a.k.a. ' + Cu[0] + ', from group ' + Cu[2] + ' would be a ' + State3)
    #This is the Zinc code
    if (str(a)) < KZn[0]:
      print(Zn[1] + ', a.k.a ' + Zn[0] + ', from group ' + Zn[2] + ' would be a ' + State1)
    elif KZn[0] > (str(a)) < KZn[1]:
      print(Zn[1] + ', a.k.a. ' + Zn[0] + ', from group ' + Zn[2] + ' would be a ' + State2)
    elif (str(a)) > KZn[1]:
      print(Zn[1] + ', a.k.a. ' + Zn[0] + ', from group ' + Zn[2] + ' would be a ' + State3)
  
  #Farenheit
  elif y == 'F':
    b = float(input('Temperature in Farenheit: '))
    #This is the Scandium code
    if (str(b)) < FSc[0]:
      print(Sc[1] + ', a.k.a ' + Sc[0] + ', from group ' + Sc[2] + ' would be a ' + State1)
    elif FSc[0] > (str(b)) < FSc[1]:
      print(Sc[1] + ', a.k.a. ' + Sc[0] + ', from group ' + Sc[2] + ' would be a ' + State2)
    elif (str(b)) > FSc[1]:
      print(Sc[1] + ', a.k.a. ' + Sc[0] + ', from group ' + Sc[2] + ' would be a ' + State3)
    #This is the Titanium code
    if (str(b)) < FTi[0]:
      print(Ti[1] + ', a.k.a ' + Ti[0] + ', from group ' + Ti[2] + ' would be a ' + State1)
    elif FTi[0] > (str(b)) < FTi[1]:
      print(Ti[1] + ', a.k.a. ' + Ti[0] + ', from group ' + Ti[2] + ' would be a ' + State2)
    elif (str(b)) > FTi[1]:
      print(Ti[1] + ', a.k.a. ' + Ti[0] + ', from group ' + Ti[2] + ' would be a ' + State3)
    #This is the Vanadium code
    if (str(b)) < FV[0]:
      print(V[1] + ', a.k.a ' + V[0] + ', from group ' + V[2] + ' would be a ' + State1)
    elif FV[0] > (str(b)) < FV[1]:
      print(V[1] + ', a.k.a. ' + V[0] + ', from group ' + V[2] + ' would be a ' + State2)
    elif (str(b)) > FV[1]:
      print(V[1] + ', a.k.a. ' + V[0] + ', from group ' + V[2] + ' would be a ' + State3)
    #This is the Chromium     code
    if (str(b)) < FCr[0]:
      print(Cr[1] + ', a.k.a ' + Cr[0] + ', from group ' + Cr[2] + ' would be a ' + State1)
    elif FCr[0] > (str(b)) < FCr[1]:
      print(Cr[1] + ', a.k.a. ' + Cr[0] + ', from group ' + Cr[2] + ' would be a ' + State2)
    elif (str(b)) > FCr[1]:
      print(Cr[1] + ', a.k.a. ' + Cr[0] + ', from group ' + Cr[2] + ' would be a ' + State3)
    #This is the Maganese code
    if (str(b)) < FMn[0]:
      print(Mn[1] + ', a.k.a ' + Mn[0] + ', from group ' + Mn[2] + ' would be a ' + State1)
    elif FMn[0] > (str(b)) < FMn[1]:
      print(Mn[1] + ', a.k.a. ' + Mn[0] + ', from group ' + Mn[2] + ' would be a ' + State2)
    elif (str(b)) > FMn[1]:
      print(Mn[1] + ', a.k.a. ' + Mn[0] + ', from group ' + Mn[2] + ' would be a ' + State3)
    #This is the Iron code
    if (str(b)) < FFe[0]:
      print(Fe[1] + ', a.k.a ' + Fe[0] + ', from group ' + Fe[2] + ' would be a ' + State1)
    elif FFe[0] > (str(b)) < FFe[1]:
      print(Fe[1] + ', a.k.a. ' + Fe[0] + ', from group ' + Fe[2] + ' would be a ' + State2)
    elif (str(b)) > FFe[1]:
      print(Fe[1] + ', a.k.a. ' + Fe[0] + ', from group ' + Fe[2] + ' would be a ' + State3)
    #This is the Cobalt code
    if (str(b)) < FCo[0]:
      print(Co[1] + ', a.k.a ' + Co[0] + ', from group ' + Co[2] + ' would be a ' + State1)
    elif FCo[0] > (str(b)) < FCo[1]:
      print(Co[1] + ', a.k.a. ' + Co[0] + ', from group ' + Co[2] + ' would be a ' + State2)
    elif (str(b)) > FCo[1]:
      print(Co[1] + ', a.k.a. ' + Co[0] + ', from group ' + Co[2] + ' would be a ' + State3)
    #This is the Nickel code
    if (str(b)) < FNi[0]:
      print(Ni[1] + ', a.k.a ' + Ni[0] + ', from group ' + Ni[2] + ' would be a ' + State1)
    elif FNi[0] > (str(b)) < FNi[1]:
      print(Ni[1] + ', a.k.a. ' + Ni[0] + ', from group ' + Ni[2] + ' would be a ' + State2)
    elif (str(b)) > FNi[1]:
      print(Ni[1] + ', a.k.a. ' + Ni[0] + ', from group ' + Ni[2] + ' would be a ' + State3)
    #This is the Copper code
    if (str(b)) < FCu[0]:
      print(Cu[1] + ', a.k.a ' + Cu[0] + ', from group ' + Cu[2] + ' would be a ' + State1)
    elif FCu[0] > (str(b)) < FCu[1]:
      print(Cu[1] + ', a.k.a. ' + Cu[0] + ', from group ' + Cu[2] + ' would be a ' + State2)
    elif (str(b)) > FCu[1]:
      print(Cu[1] + ', a.k.a. ' + Cu[0] + ', from group ' + Cu[2] + ' would be a ' + State3)
    #This is the Zinc code
    if (str(b)) < FZn[0]:
      print(Zn[1] + ', a.k.a ' + Zn[0] + ', from group ' + Zn[2] + ' would be a ' + State1)
    elif FZn[0] > (str(b)) < FZn[1]:
      print(Zn[1] + ', a.k.a. ' + Zn[0] + ', from group ' + Zn[2] + ' would be a ' + State2)
    elif (str(b)) > FZn[1]:
      print(Zn[1] + ', a.k.a. ' + Zn[0] + ', from group ' + Zn[2] + ' would be a ' + State3)
elif x == 'N':
  print('Code end')
