""" 
Created on Wed Feb 16 17:01:55 2022 
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
ENTICE_freq_str = list(set(ENTICE_freq))
#for x in ENTICE_freq:
#	ENTICE_freq_str.append(str(x))

#Read in the Simulation Data
ENTICE_data = myxmlreader('ENTICE/ENTICE_test.ybatch.xml')
ENTICEwC_data = myxmlreader('ENTICE/ENTICEwC_test.ybatch.xml')
# The number of channels
n = 15

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


# Figure 1
fig = plt.figure()
plt.xticks(ENTICE_freq_str)
plt.xlabel('Channel Frequency [GHz]')
plt.ylabel('Radiance [W/(m^2*Hz*sr]')
plt.title('Scenario 1')
plt.scatter(ENTICE_freq, ENTICE_sl,c='k')
plt.scatter(ENTICE_freq, ENTICEwC_sl,c='b')
plt.legend(['Without Clouds','With Clouds'])
fig.tight_layout()

# Figure 2
fig = plt.figure()
plt.xticks(ENTICE_freq_str)
plt.xlabel('Channel Frequency [GHz]')
plt.ylabel('Radiance [W/(m^2*Hz*sr]')
plt.title('Scenario 2')
plt.scatter(ENTICE_freq, ENTICE_s2, c='k')
plt.scatter(ENTICE_freq, ENTICEwC_s2,c='b')
plt.legend(['Without Clouds','With Clouds'])
fig.tight_layout()

# Figure 3
fig = plt.figure()
plt.xticks(ENTICE_freq_str)
plt.xlabel('Channel Frequency [GHz]')
plt.ylabel('Radiance [W/(m^2*Hz*sr]')
plt.title('Scenario 3')
plt.scatter(ENTICE_freq, ENTICE_s3,c='k')
plt.scatter(ENTICE_freq, ENTICEwC_s3,c='b')
plt.legend(['Without Clouds','With Clouds'])
fig.tight_layout()

# Figure 4
fig = plt.figure()
plt.xticks(ENTICE_freq_str)
plt.xlabel('Channel Frequency [GHz]')
plt.ylabel('Radiance [W/(m^2*Hz*sr]')
plt.title('Scenario 4')
plt.scatter(ENTICE_freq, ENTICE_s4,c='k')
plt.scatter(ENTICE_freq, ENTICEwC_s4,c='b')
plt.legend(['Without Clouds','With Clouds'])
fig.tight_layout()

# Figure 5
fig = plt.figure()
plt.xticks(ENTICE_freq_str)
plt.xlabel('Channel Frequency [GHz]')
plt.ylabel('Radiance [W/(m^2*Hz*sr]')
plt.title('Scenario 5')
plt.scatter(ENTICE_freq, ENTICE_s5,c='k')
plt.scatter(ENTICE_freq, ENTICEwC_s5,c='b')
plt.legend(['Without Clouds','With Clouds'])
fig.tight_layout()

# Figure 6
fig = plt.figure()
plt.xticks(ENTICE_freq_str)
plt.xlabel('Channel Frequency [GHz]')
plt.ylabel('Radiance [W/(m^2*Hz*sr]')
plt.title('Scenario 6')
plt.scatter(ENTICE_freq, ENTICE_s6,c='k')
plt.scatter(ENTICE_freq, ENTICEwC_s6,c='b')
plt.legend(['Without Clouds','With Clouds'])
fig.tight_layout()

plt.show()
