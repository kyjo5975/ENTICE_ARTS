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
	with open('ENTICE_test.ybatch.xml', 'r') as f:
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
ENTICE_freq = ["118.75",
			   "118.75",
			   "118.75",
			   "118.75",
			   "183.31",
			   "183.31",
			   "183.31",
			   "243.20",
			   "310.00",
			   "380.20",
			   "380.20",
			   "380.20",
			   "380.20",
			   "664.00",
]

#Read in the Simulation Data
ENTICE_data = myxmlreader('ENTICE_test.ybatch.xml')
# The number of channels
n = 14

#Scenario Data
ENTICE_sl = ENTICE_data[0:n]
ENTICE_s2 = ENTICE_data[n:2*n]
ENTICE_s3 = ENTICE_data[2*n:3*n]
ENTICE_s4 = ENTICE_data[3*n:4*n]
ENTICE_s5 = ENTICE_data[4*n:5*n]
ENTICE_s6 = ENTICE_data[5*n:6*n]


# Figure 1
fig = plt.figure()
plt.xticks(range(len(ENTICE_sl)), ENTICE_freq, rotation=35)
plt.xlabel('Channel Frequency [GHz]')
plt.ylabel('Radiance [W/(m^2*Hz*sr]')
plt.title('Scenario 1')
plt.bar(range(len(ENTICE_sl)), ENTICE_sl)
fig.tight_layout()

# Figure 2
fig = plt.figure()
plt.xticks(range(len(ENTICE_s2)), ENTICE_freq, rotation=35)
plt.xlabel('Channel Frequency [GHz]')
plt.ylabel('Radiance [W/(m^2*Hz*sr]')
plt.title('Scenario 2')
plt.bar(range(len(ENTICE_s2)), ENTICE_s2)
fig.tight_layout()

# Figure 3
fig = plt.figure()
plt.xticks(range(len(ENTICE_s3)), ENTICE_freq, rotation=35)
plt.xlabel('Channel Frequency [GHz]')
plt.ylabel('Radiance [W/(m^2*Hz*sr]')
plt.title('Scenario 3')
plt.bar(range(len(ENTICE_s3)), ENTICE_s3)
fig.tight_layout()

# Figure 4
fig = plt.figure()
plt.xticks(range(len(ENTICE_s4)), ENTICE_freq, rotation=35)
plt.xlabel('Channel Frequency [GHz]')
plt.ylabel('Radiance [W/(m^2*Hz*sr]')
plt.title('Scenario 4')
plt.bar(range(len(ENTICE_s4)), ENTICE_s4)
fig.tight_layout()

# Figure 5
fig = plt.figure()
plt.xticks(range(len(ENTICE_s5)), ENTICE_freq, rotation=35)
plt.xlabel('Channel Frequency [GHz]')
plt.ylabel('Radiance [W/(m^2*Hz*sr]')
plt.title('Scenario 5')
plt.bar(range(len(ENTICE_s5)), ENTICE_s5)
fig.tight_layout()

# Figure 6
fig = plt.figure()
plt.xticks(range(len(ENTICE_s6)), ENTICE_freq, rotation=35)
plt.xlabel('Channel Frequency [GHz]')
plt.ylabel('Radiance [W/(m^2*Hz*sr]')
plt.title('Scenario 6')
plt.bar(range(len(ENTICE_s6)), ENTICE_s6)
fig.tight_layout()
"""
plt.figure()
plt.xticks(range(len(ICI_spe6)))
plt.xlabel('Scenario #')
plt.ylabel('Radiance [W/(m^2*Hz*sr]')
plt.title('Radiance Values over the Different Scenarios')
plt.plot(range(len(ICI_t1)), ICI_t1)
plt.plot(range(len(ICI_t2)), ICI_t2)
plt.plot(range(len(ICI_t3)), ICI_t3)
plt.plot(range(len(ICI_t4)), ICI_t4)
plt.plot(range(len(ICI_t5)), ICI_t5)
plt.plot(range(len(ICI_t6)), ICI_t6)
plt.legend(ICI_freq)
"""
plt.show()
