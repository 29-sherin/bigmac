#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  8 16:06:30 2023

@author: sherin
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime

#Read the csv file

my_data = pd.read_csv("/Users/sherin/Library/Containers/com.microsoft.Excel/Data/Downloads/big mac.csv")

my_data 
#to function the header
my_data.head()

#Exploratory Data Analysis

my_data.info()

my_data.describe()

my_data.isnull().sum()

#Selecting 5 Countries for multiple line plot

group_argentina = my_data[(my_data['name'] == "Argentina")]
group_australia = my_data[(my_data['name'] == "Australia")] 
group_brazil = my_data[my_data['name'] == "Brazil"]
group_britain = my_data[my_data['name'] == "Britain"]
group_canada = my_data[my_data['name'] == "Canada"]

#Extracting year from the date for 5 Countries

group_argentina['year'] = pd.to_datetime(group_argentina['date']).dt.year
group_australia['year'] = pd.to_datetime(group_australia['date']).dt.year
group_brazil['year'] = pd.to_datetime(group_brazil['date']).dt.year
group_britain['year'] = pd.to_datetime(group_britain['date']).dt.year
group_canada['year'] = pd.to_datetime(group_canada['date']).dt.year

#TO Function Multi line plot

plt.plot(group_argentina['year'], group_argentina['dollar_price'], label="Argentina")
plt.plot(group_australia['year'], group_australia['dollar_price'], label="Australia")
plt.plot(group_brazil['year'], group_brazil['dollar_price'], label="Brazil")
plt.plot(group_britain['year'], group_britain['dollar_price'], label="Britain")
plt.plot(group_canada['year'], group_canada['dollar_price'], label="Canada")
plt.legend()
plt.ylabel('Dollar Price')
plt.xlabel("Years")
plt.title("Big mac Year Wise Dollar Price for 5 Countries", fontsize="15")
plt.savefig("Bigmac year 5 countries.png")
plt.show()

#Extracting year from date in original dataset

my_data['year'] = pd.to_datetime(my_data['date']).dt.year

my_data.head()


#to plot multi bar plots from different 5 countries


plt.bar(group_argentina['year'], group_argentina['dollar_price'], label="Argentina")
plt.bar(group_australia['year'], group_australia['dollar_price'], label="Australia")
plt.bar(group_brazil['year'], group_brazil['dollar_price'], label="Brazil")
plt.bar(group_britain['year'], group_britain['dollar_price'], label="Britain")
plt.bar(group_canada['year'], group_canada['dollar_price'], label="Canada")
plt.legend()
plt.ylabel('Dollar Price')
plt.xlabel("Years")
plt.title("Big mac Year Wise Dollar Price for 5 Countries", fontsize="15")
plt.savefig("Bigmac year 5 countries.png")
plt.show()



#to plot multi scatter from different 5 countries


plt.scatter(group_argentina['year'], group_argentina['dollar_price'], label="Argentina")
plt.scatter(group_australia['year'], group_australia['dollar_price'], label="Australia")
plt.scatter(group_brazil['year'], group_brazil['dollar_price'], label="Brazil")
plt.scatter(group_britain['year'], group_britain['dollar_price'], label="Britain")
plt.scatter(group_canada['year'], group_canada['dollar_price'], label="Canada")
plt.legend()
plt.ylabel('Dollar Price')
plt.xlabel("Years")
plt.title("Big mac Year Wise Dollar Price for 5 Countries", fontsize="15")
plt.savefig("Bigmac year 5 countries.png")
plt.show()