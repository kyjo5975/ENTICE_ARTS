""" 
Created on Mon Feb 28 11:52:46 2022 
*** Insert Program Description *** 

@author: Kyle Johnson 
"""
from bs4 import BeautifulSoup
import re
import numpy as np
import matplotlib.pyplot as plt

def myxmlreader(xmlfile):
    # Reading the data inside the xml
    with open(xmlfile, 'r') as f:
        data = f.read()

    # Passing the stored data inside the beautifulsoup parser, storing the returned object
    Bs_data = BeautifulSoup(data, "xml")
    
    # Getting the data in one long string because arts is weird
    Sim_data_string = Bs_data.text

    # splitting that data up into individual strings
    Sim_data_text = re.split('\n+', Sim_data_string)
    Sim_data = []
    for num in Sim_data_text:
        if len(num) != 0:
            try:
                float(num)
                Sim_data.append(num)
            except:
                Sim_data.append(num)
        else:
            continue
    return(Sim_data)

chev = myxmlreader('chevallierl91_all_extract.xml')
o = 8
n = 92

# Scenario 1
P1 = chev[o:o+n]
for x in P1: float(x)
T1 = float(chev[o+n:o+2*n])
z1 = float(chev[o+2*n:o+3*n])
LWC1 = float(chev[o+3*n:o+4*n])
IWC1 = float(chev[o+4*n:o+5*n])
RR1 = float(chev[o+5*n:o+6*n])
SR1 = float(chev[o+6*n:o+7*n])
H2O1 = float(chev[o+7*n:o+8*n])
O3_1 = float(chev[o+8*n:o+9*n])

# Scenario 2
P2 = chev[2*o+9*n:2*o+10*n]
T2 = chev[2*o+10*n:2*o+11*n]
z2 = chev[2*o+11*n:2*o+12*n]
LWC2 = chev[2*o+12*n:2*o+13*n]
IWC2 = chev[2*o+13*n:2*o+14*n]
RR2 = chev[2*o+14*n:2*o+15*n]
SR2 = chev[2*o+15*n:2*o+16*n]
H2O2 = chev[2*o+16*n:2*o+17*n]
O3_2 = chev[2*o+17*n:2*o+18*n]

# Scenario 3
P3 = chev[3*o+18*n:3*o+19*n]
T3 = chev[3*o+19*n:3*o+20*n]
z3 = chev[3*o+20*n:3*o+21*n]
LWC3 = chev[3*o+21*n:3*o+22*n]
IWC3 = chev[3*o+22*n:3*o+23*n]
RR3 = chev[3*o+23*n:3*o+24*n]
SR3 = chev[3*o+24*n:3*o+25*n]
H2O3 = chev[3*o+25*n:3*o+26*n]
O3_3 = chev[3*o+26*n:3*o+27*n]

# Scenario 4
P4 = chev[4*o+27*n:4*o+28*n]
T4 = chev[4*o+28*n:4*o+29*n]
z4 = chev[4*o+29*n:4*o+30*n]
LWC4 = chev[4*o+30*n:4*o+31*n]
IWC4 = chev[4*o+31*n:4*o+32*n]
RR4 = chev[4*o+32*n:4*o+33*n]
SR4 = chev[4*o+33*n:4*o+34*n]
H2O4 = chev[4*o+34*n:4*o+35*n]
O3_4 = chev[4*o+35*n:4*o+36*n]

# Scenario 5
P5 = chev[5*o+36*n:5*o+37*n]
T5 = chev[5*o+37*n:5*o+38*n]
z5 = chev[5*o+38*n:5*o+39*n]
LWC5 = chev[5*o+39*n:5*o+40*n]
IWC5 = chev[5*o+40*n:5*o+41*n]
RR5 = chev[5*o+41*n:5*o+42*n]
SR5 = chev[5*o+42*n:5*o+43*n]
H2O5 = chev[5*o+43*n:5*o+44*n]
O3_5 = chev[5*o+44*n:5*o+45*n]

# Scenario 6
P6 = chev[6*o+45*n:6*o+46*n]
T6 = chev[6*o+46*n:6*o+47*n]
z6 = chev[6*o+47*n:6*o+48*n]
LWC6 = chev[6*o+48*n:6*o+49*n]
IWC6 = chev[6*o+49*n:6*o+50*n]
RR6 = chev[6*o+50*n:6*o+51*n]
SR6 = chev[6*o+51*n:6*o+52*n]
H2O6 = chev[6*o+52*n:6*o+53*n]
O3_6 = chev[6*o+53*n:6*o+54*n]

## Figures

# Figure 1
fig = plt.figure()
#plt.xticks(ENTICE_freq_str)
plt.xlabel('Pressure [HPa]')
plt.ylabel('Altitude [m]')
plt.title('Scenario 1')
plt.plot(P1, z1,c='k')
fig.tight_layout()
plt.show()