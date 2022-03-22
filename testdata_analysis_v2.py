""" 
Created on Mon Feb 28 11:52:46 2022 
*** Insert Program Description *** 

@author: Kyle Johnson 
"""
from bs4 import BeautifulSoup
import re
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.lines as mlines

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
                num = float(num)
                Sim_data.append(num)
            except:
                Sim_data.append(num)
        else:
            continue
    return(Sim_data)

def scenarioplots(P,T,z,LWC,IWC,RR,SR,H2O,O3,n):
    plt.subplots_adjust(top=0.841, bottom=0.109, left=0.092, right=0.943, hspace=0.522, wspace=0.274)
    plt.suptitle(f"Scenario {n}")
    # Plot the subplots
    # Plot 1
    ax1 = plt.subplot(2,2,1)
    ax2 = ax1.twiny()
    ax1.plot(P, z, c='k')
    ax1.set_xlabel('Pressure [HPa]')
    ax1.set_ylabel('Altitude [m]')
    ax2.plot(T, z, c='r')
    ax2.set_xlabel('Temperature [K]')
    plt.ylim((0, 20000))
    black_line = mlines.Line2D([], [], color='k', label='Pressure')
    red_line = mlines.Line2D([], [], color='r', label='Temperature')
    plt.legend(handles=[black_line, red_line])
    plt.tight_layout()

    # Plot 2
    plt.subplot(2,2,2)
    plt.semilogx(LWC, z, c='b')
    plt.semilogx(IWC, z, c='c')
    plt.xlabel('Water Content [kg/m^3]')
    plt.ylabel('Altitude [m]')
    plt.ylim((0, 20000))
    plt.xlim(left=1e-4)
    blue_line = mlines.Line2D([], [], color='b', label='LWC')
    cyan_line = mlines.Line2D([], [], color='c', label='IWC')
    plt.legend(loc='upper right',handles=[blue_line, cyan_line])
    plt.tight_layout()
    
    # Plot 3
    plt.subplot(2,2,3)
    plt.semilogx(RR, z, c='0.4')
    plt.semilogx(SR, z, c='0.8')
    plt.xlabel('Rain and Snow Rate [kg/(m2*s)]')
    plt.ylabel('Altitude [m]')
    plt.ylim((0, 20000))
    grey1_line = mlines.Line2D([], [], color='0.4', label='RR')
    grey2_line = mlines.Line2D([], [], color='0.8', label='SR')
    plt.legend(loc='upper right',handles=[grey1_line, grey2_line])
    plt.tight_layout()

    # Plot 4
    plt.subplot(2,2,4)
    plt.semilogx(H2O, z, c='b')
    plt.semilogx(O3, z, c='g')
    plt.xlabel('H2O and O3 [%]')
    plt.ylabel('Altitude [m]')
    plt.ylim((0, 20000))
    water_line = mlines.Line2D([], [], color='b', label='H2O')
    ozone_line = mlines.Line2D([], [], color='g', label='O3')
    plt.legend(handles=[water_line, ozone_line])
    plt.tight_layout()


chev = myxmlreader('chevallierl91_all_extract.xml')
o = 8
n = 92

# Scenario 1
P1 = chev[o:o+n]
T1 = chev[o+n:o+2*n]
z1 = chev[o+2*n:o+3*n]
LWC1 = chev[o+3*n:o+4*n]
IWC1 = chev[o+4*n:o+5*n]
RR1 = chev[o+5*n:o+6*n]
SR1 = chev[o+6*n:o+7*n]
H2O1 = chev[o+7*n:o+8*n]
O3_1 = chev[o+8*n:o+9*n]

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
#scenarioplots(P1,T1,z1,LWC1,IWC1,RR1,SR1,H2O1,O3_1,1)
#scenarioplots(P2,T2,z2,LWC2,IWC2,RR2,SR2,H2O2,O3_2,2)
#scenarioplots(P3,T3,z3,LWC3,IWC3,RR3,SR3,H2O3,O3_3,3)
#scenarioplots(P4,T4,z4,LWC4,IWC4,RR4,SR4,H2O4,O3_4,4)
#scenarioplots(P5,T5,z5,LWC5,IWC5,RR5,SR5,H2O5,O3_5,5)
scenarioplots(P6,T6,z6,LWC6,IWC6,RR6,SR6,H2O6,O3_6,6)
plt.show()
