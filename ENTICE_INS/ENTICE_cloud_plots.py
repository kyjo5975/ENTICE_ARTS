from bs4 import BeautifulSoup
import re
import matplotlib.pyplot as plt
import matplotlib.lines as mlines
import numpy as np

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

n = 49
#Read in the Simulation Data
ENTICE_C = myxmlreader("C:/Users/kbayj/Documents/JPL/ENTICE_ARTS/ENTICE_INS/CloudCase.xml")
ENTICE_NC = myxmlreader("C:/Users/kbayj/Documents/JPL/ENTICE_ARTS/ENTICE_INS/NoCloudCase.xml")
array1 = np.array(ENTICE_NC)
array2 = np.array(ENTICE_C)
subtracted_array = np.subtract(array1, array2)
ENTICE_D = list(subtracted_array)
FGRID = myxmlreader("C:/Users/kbayj/Documents/JPL/ENTICE_ARTS/ENTICE_INS/FGRID.xml")
f_grid = np.divide(FGRID,1e9)
P = myxmlreader("C:/Users/kbayj/Documents/JPL/ENTICE_ARTS/ENTICE_INS/pressure.xml")
z = myxmlreader("C:/Users/kbayj/Documents/JPL/ENTICE_ARTS/ENTICE_INS/altitude.xml")
T = myxmlreader("C:/Users/kbayj/Documents/JPL/ENTICE_ARTS/ENTICE_INS/temperature.xml")
RWCIWC = myxmlreader("C:/Users/kbayj/Documents/JPL/ENTICE_ARTS/ENTICE_INS/pbf.xml")
RWC = RWCIWC[n*0:n*1]
IWC = RWCIWC[n*1:n*2]
vmr = myxmlreader("C:/Users/kbayj/Documents/JPL/ENTICE_ARTS/ENTICE_INS/vmr.xml")
vmr1 = vmr[n*0:n*1]
vmr2 = vmr[n*1:n*2]
vmr3 = vmr[n*2:n*3]


# Figure 1
fig = plt.figure()
#plt.xticks(freq_str,rotation=65)
plt.xlabel('Channel Frequency [GHz]')
plt.ylabel('Radiance [W/(m^2*Hz*sr]')
plt.title('Scenario 1')
plt.plot(f_grid, ENTICE_NC, c='b', marker= '.')
plt.plot(f_grid, ENTICE_C, c='k', marker= '.')
plt.legend(['No Clouds','Clouds'])
fig.tight_layout()

# Figure 1
fig = plt.figure()
#plt.xticks(freq_str,rotation=65)
plt.xlabel('Channel Frequency [GHz]')
plt.ylabel('Radiance [W/(m^2*Hz*sr]')
plt.title('Difference between No Clouds and Clouds')
plt.plot(f_grid, ENTICE_D, c='c', marker= '.')
#plt.legend(['No Clouds','Clouds'])
fig.tight_layout()

fig, ax1 = plt.subplots()
l = ax1.plot(P, z, c='k')
ax2 = ax1.twiny()
l2 = ax2.plot(T, z, c='r')
ax1.set_xlabel('Pressure [HPa]')
ax2.set_xlabel('Temperature [K]')
ax1.set_ylabel('Altitude [m]')
#plt.title("Scenario 1")
black_line = mlines.Line2D([], [], color='k', label='Pressure')
red_line = mlines.Line2D([], [], color='r', label='Temperature')
plt.legend(handles=[black_line, red_line])
fig.tight_layout()

fig = plt.figure()
plt.semilogx(RWC, z, c='b')
plt.semilogx(IWC, z, c='c')
plt.xlabel('Water Content [kg/m^3]')
plt.ylabel('Altitude [m]')
#plt.ylim((0, 20000))
#plt.xlim(left=1e-4)
blue_line = mlines.Line2D([], [], color='b', label='RWC')
cyan_line = mlines.Line2D([], [], color='c', label='IWC')
plt.legend(loc='upper right',handles=[blue_line, cyan_line])
plt.tight_layout()

fig = plt.figure()
plt.semilogx(vmr1, z, c='m')
plt.semilogx(vmr2, z, c='r')
plt.semilogx(vmr3, z, c='b')
plt.xlabel('VMR Data [%]')
plt.ylabel('Altitude [m]')
#plt.ylim((0, 20000))
vmr1_line = mlines.Line2D([], [], color='m', label='N2')
vmr2_line = mlines.Line2D([], [], color='r', label='O2')
vmr3_line = mlines.Line2D([], [], color='b', label='H20')
plt.legend(handles=[vmr1_line, vmr2_line, vmr3_line])
plt.tight_layout()

plt.show()