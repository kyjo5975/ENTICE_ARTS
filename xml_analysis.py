""" 
Created on Wed Feb 09 15:47:01 2022 
*** Insert Program Description *** 

@author: Kyle Johnson 
"""
import numpy as np
import matplotlib.pyplot as plt

def Extract(lst,n):
    return [item[n] for item in lst]

ICI_freq = ['183.31', 
            '183.31',
            '183.31',
            '243.2',
            '325.15',
            '325.15',
            '325.15',
            '448',
            '448',
            '448',
            '664']


ICI_spe1 = [264.038216293179, 
            254.304949981301,
            247.236174413316,
            271.194838512349,
            261.442740888644,
            252.699687493936,
            243.691496776014,
            243.246178246614,
            236.452200369482,
            230.385547885292,
            246.073738679877]

ICI_spe2 = [262.131026153591,
            251.878608206717,
            244.817474770674,
            269.699046219389,
            259.380965434441,
            250.311167778492,
            241.48078184256,
            241.14660406849,
            234.928676004534,
            229.226695120828,
            243.764791785401]

ICI_spe3 = [273.691844633427,
            266.173009664091,
            263.071339920201,
            282.541680577324,
            270.478368295685,
            264.963901945198,
            261.210555860037,
            260.373159006173,
            255.716758947193,
            244.348415257577,
            261.32968462692]

ICI_spe4 = [255.943832195764,
            253.947356653393,
            246.094394445288,
            234.279856348407,
            258.518556940146,
            252.181734361751,
            242.113109522447,
            240.903280516535,
            232.004846037952,
            223.412404550607,
            243.928376275697]

ICI_spe5 = [265.511386447226,
            253.956090897357,
            245.492779499734,
            274.009269134187,
            262.520273548806,
            252.151607582753,
            241.353562590994,
            241.083541466718,
            232.143682717541,
            222.273500656762,
            244.300130430864]

ICI_spe6 = [268.49360496033,
            261.080724654245,
            256.002155982346,
            276.576194115727,
            265.820296193392,
            259.821354297455,
            252.516155808788,
            251.941539269113,
            241.524187028587,
            227.859815941527,
            254.387483914968]

ICI_spe = [ICI_spe1, ICI_spe2, ICI_spe3, ICI_spe4, ICI_spe5, ICI_spe6]
ICI_spe = np.asarray(ICI_spe)

ICI_t1 = Extract(ICI_spe,0)
ICI_t2 = Extract(ICI_spe,1)
ICI_t3 = Extract(ICI_spe,2)
ICI_t4 = Extract(ICI_spe,3)
ICI_t5 = Extract(ICI_spe,4)
ICI_t6 = Extract(ICI_spe,5)

# Figures
plt.figure()
plt.xticks(range(len(ICI_spe1)), ICI_freq)
plt.xlabel('Channel Frequency [GHz]')
plt.ylabel('Radiance [W/(m^2*Hz*sr]')
plt.title('Scenario 1')
plt.bar(range(len(ICI_spe1)), ICI_spe1)

plt.figure()
plt.xticks(range(len(ICI_spe2)), ICI_freq)
plt.xlabel('Channel Frequency [GHz]')
plt.ylabel('Radiance [W/(m^2*Hz*sr]')
plt.title('Scenario 2')
plt.bar(range(len(ICI_spe2)), ICI_spe2)

plt.figure()
plt.xticks(range(len(ICI_spe3)), ICI_freq)
plt.xlabel('Channel Frequency [GHz]')
plt.ylabel('Radiance [W/(m^2*Hz*sr]')
plt.title('Scenario 3')
plt.bar(range(len(ICI_spe3)), ICI_spe3)

plt.figure()
plt.xticks(range(len(ICI_spe4)), ICI_freq)
plt.xlabel('Channel Frequency [GHz]')
plt.ylabel('Radiance [W/(m^2*Hz*sr]')
plt.title('Scenario 4')
plt.bar(range(len(ICI_spe4)), ICI_spe4)

plt.figure()
plt.xticks(range(len(ICI_spe5)), ICI_freq)
plt.xlabel('Channel Frequency [GHz]')
plt.ylabel('Radiance [W/(m^2*Hz*sr]')
plt.title('Scenario 5')
plt.bar(range(len(ICI_spe5)), ICI_spe5)

plt.figure()
plt.xticks(range(len(ICI_spe6)), ICI_freq)
plt.xlabel('Channel Frequency [GHz]')
plt.ylabel('Radiance [W/(m^2*Hz*sr]')
plt.title('Scenario 6')
plt.bar(range(len(ICI_spe6)), ICI_spe6)

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

plt.show()
