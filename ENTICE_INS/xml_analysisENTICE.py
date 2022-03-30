""" 
Created on Wed Feb 16 17:01:55 2022 
*** Insert Program Description *** 

@author: Kyle Johnson 
"""
from bs4 import BeautifulSoup
import re
import numpy as np
import matplotlib.pyplot as plt
from sympy import rotations

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
		if num == "":
			continue
		else:
			Sim_data.append(float(num))
	return(Sim_data)

# Set the Channel Frequencies
ENTICE_freq = [118.75,
			   118.75,
			   118.75,
			   118.75,
			   183.31,
			   183.31,
			   183.31,
			   243.20,
			   310.00,
			   380.20,
			   380.20,
			   380.20,
			   380.20,
			   664.00,
			   850.00]
ICI_freq = [183.31,
			183.31,
			183.31,
			243.2,
			325.15,
			325.15,
			325.15,
			448,
			448,
			448,
			664]
Offset_freq = ['1',
			   '2',
			   3,
			   4,
			   5,
			   6,
			   6.6,
			   2.5,
			   2.5,
			   0.75,
			   1.80,
			   3.35,
			   6.20,
			   4.20,
			   4.20]
# ENTICE_freq_str = list(set(ENTICE_freq))
# ICI_freq_str = list(set(ICI_freq))
freq = ENTICE_freq+ICI_freq
freq.sort()
freq_str = list(set(freq))

#for x in ENTICE_freq:
#	ENTICE_freq_str.append(str(x))

#Read in the Simulation Data
ENTICE_data = myxmlreader('ENTICE_test.ybatch.xml')
ENTICEwC_data = myxmlreader('ENTICEwC_test.ybatch.xml')
ICI_data = myxmlreader('ICI_test.ybatch.xml')
# The number of channels
n = 15
n1 = 11
#Scenario Data
ENTICE_sl = ENTICE_data[0:n]
ENTICE_s2 = ENTICE_data[n:2*n]
ENTICE_s3 = ENTICE_data[2*n:3*n]
ENTICE_s4 = ENTICE_data[3*n:4*n]
ENTICE_s5 = ENTICE_data[4*n:5*n]
ENTICE_s6 = ENTICE_data[5*n:6*n]

ENTICEwC_sl = ENTICE_data[0:n]
ENTICEwC_s2 = ENTICE_data[n:2*n]
ENTICEwC_s3 = ENTICE_data[2*n:3*n]
ENTICEwC_s4 = ENTICE_data[3*n:4*n]
ENTICEwC_s5 = ENTICE_data[4*n:5*n]
ENTICEwC_s6 = ENTICE_data[5*n:6*n]

ICI_s1 = ICI_data[0:n1]
ICI_s2 = ICI_data[n1:2*n1]
ICI_s3 = ICI_data[2*n1:3*n1]
ICI_s4 = ICI_data[3*n1:4*n1]
ICI_s5 = ICI_data[4*n1:5*n1]
ICI_s6 = ICI_data[5*n1:6*n1]


# Figure 1
fig = plt.figure()
plt.xticks(freq_str,rotation=65)
plt.xlabel('Channel Frequency [GHz]')
plt.ylabel('Radiance [W/(m^2*Hz*sr]')
plt.title('Scenario 1')
plt.plot(ICI_freq, ICI_s1, c='b', marker= '.')
plt.plot(ENTICE_freq, ENTICE_sl, c='k', marker= '.')
plt.legend(['ICI','ENTICE'])
fig.tight_layout()

# Figure 2
fig = plt.figure()
plt.xticks(freq_str,rotation=65)
plt.xlabel('Channel Frequency [GHz]')
plt.ylabel('Radiance [W/(m^2*Hz*sr]')
plt.title('Scenario 2')
plt.plot(ICI_freq, ICI_s2, c='b', marker= '.')
plt.plot(ENTICE_freq, ENTICE_s2, c='k', marker= '.')
#plt.scatter(ENTICE_freq, ENTICEwC_s2,c='b')
plt.legend(['ICI','ENTICE'])
fig.tight_layout()

# Figure 3
fig = plt.figure()
plt.xticks(freq_str,rotation=65)
plt.xlabel('Channel Frequency [GHz]')
plt.ylabel('Radiance [W/(m^2*Hz*sr]')
plt.title('Scenario 3')
plt.plot(ICI_freq, ICI_s3, c='b', marker= '.')
plt.plot(ENTICE_freq, ENTICE_s3, c='k', marker= '.')
#plt.scatter(ENTICE_freq, ENTICEwC_s3,c='b')
plt.legend(['ICI','ENTICE'])
fig.tight_layout()

# Figure 4
fig = plt.figure()
plt.xticks(freq_str, rotation=65)
plt.xlabel('Channel Frequency [GHz]')
plt.ylabel('Radiance [W/(m^2*Hz*sr]')
plt.title('Scenario 4')
plt.plot(ICI_freq, ICI_s4, c='b', marker= '.')
plt.plot(ENTICE_freq, ENTICE_s4, c='k', marker= '.')
#plt.scatter(ENTICE_freq, ENTICEwC_s4,c='b')
plt.legend(['ICI','ENTICE'])
fig.tight_layout()

# Figure 5
fig = plt.figure()
plt.xticks(freq_str, rotation=65)
plt.xlabel('Channel Frequency [GHz]')
plt.ylabel('Radiance [W/(m^2*Hz*sr]')
plt.title('Scenario 5')
plt.plot(ICI_freq, ICI_s5, c='b', marker= '.')
plt.plot(ENTICE_freq, ENTICE_s5, c='k', marker= '.')
#plt.scatter(ENTICE_freq, ENTICEwC_s5,c='b')
plt.legend(['ICI','ENTICE'])
fig.tight_layout()

# Figure 6
fig = plt.figure()
plt.xticks(freq_str, rotation=65)
plt.xlabel('Channel Frequency [GHz]')
plt.ylabel('Radiance [W/(m^2*Hz*sr]')
plt.title('Scenario 6')
plt.plot(ICI_freq, ICI_s6, c='b', marker= '.')
plt.plot(ENTICE_freq, ENTICE_s6, c='k', marker= '.')
#plt.scatter(ENTICE_freq, ENTICEwC_s6,c='b')
plt.legend(['ICI','ENTICE'])
fig.tight_layout()

plt.show()
