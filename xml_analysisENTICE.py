""" 
Created on Wed Feb 16 17:01:55 2022 
*** Insert Program Description *** 

@author: Kyle Johnson 
"""
from bs4 import BeautifulSoup
import re

# Reading the data inside the xml
with open('ENTICE_test.ybatch.xml', 'r') as f:
	data = f.read()

# Passing the stored data inside the beautifulsoup parser, storing the returned object
Bs_data = BeautifulSoup(data, "xml")

# Getting the data in one long string because arts is weird
ENTICE_data_string = Bs_data.text

# splitting that data up into individual strings
ENTICE_data_text = re.split('\n+', ENTICE_data_string)

# The number of channels
n = 14

# splitting up the data into separate channel variables
CH1_text = ENTICE_data_text[1:n+1]
CH2_text = ENTICE_data_text[n+1:2*n+1]
CH3_text = ENTICE_data_text[2*n+1:3*n+1]
CH4_text = ENTICE_data_text[3*n+1:4*n+1]
CH5_text = ENTICE_data_text[4*n+1:5*n+1]
CH6_text = ENTICE_data_text[5*n+1:6*n+1]
CH7_text = ENTICE_data_text[6*n+1:7*n+1]
CH8_text = ENTICE_data_text[7*n+1:8*n+1]
CH9_text = ENTICE_data_text[8*n+1:9*n+1]
CH10_text = ENTICE_data_text[9*n+1:10*n+1]
CH11_text = ENTICE_data_text[10*n+1:11*n+1]
CH12_text = ENTICE_data_text[11*n+1:12*n+1]
CH13_text = ENTICE_data_text[12*n+1:13*n+1]
CH14_text = ENTICE_data_text[13*n+1:14*n+1]

# Converting the String to Floats
CH1 = [float(x) for x in CH1_text]
CH2 = [float(x) for x in CH2_text]
CH3 = [float(x) for x in CH3_text]
CH4 = [float(x) for x in CH4_text]
CH5 = [float(x) for x in CH5_text]
CH6 = [float(x) for x in CH6_text]
CH7 = [float(x) for x in CH7_text]
CH8 = [float(x) for x in CH8_text]
CH9 = [float(x) for x in CH9_text]
CH10 = [float(x) for x in CH10_text]
CH11 = [float(x) for x in CH11_text]
CH12 = [float(x) for x in CH12_text]
CH13 = [float(x) for x in CH13_text]
CH14 = [float(x) for x in CH14_text]