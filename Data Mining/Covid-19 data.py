#!/usr/bin/env python
# coding: utf-8

# In[81]:


import pandas as pd
import matplotlib
from matplotlib import pyplot as plt
import numpy as np
from scipy import stats


# In[82]:


covidData = '71347427-covid-data.xlsx'
#choose columns
require_cols = [0,3,9,11,12,14,16,24,25,31,32,33,34]


# In[83]:


df = pd.read_excel(covidData, usecols = require_cols)


# In[84]:


#delete negative values (all values in this dataset are positive)
num = df._get_numeric_data()
num[num < 0] = 0


# In[92]:


#replace all zero value with nan for readability of Plot
df.replace(0, np.nan, inplace = True)


# In[93]:


#delete Outliers
cols = df.select_dtypes('number').columns
df_sub = df.loc[:, cols]
lim = np.abs((df_sub - df_sub.mean()) / df_sub.std(ddof=0)) < 3
df.loc[:, cols] = df_sub.where(lim, np.nan)
#df.dropna(inplace=True)


# In[94]:


#1b
countryNamelist=['DEU','NLD','ROU']
columnNamelist=['new_cases_per_million','new_deaths_per_million','reproduction_rate','icu_patients_per_million',
                'hosp_patients_per_million','new_tests_per_thousand','positive_rate','total_vaccinations_per_hundred',
                'people_vaccinated_per_hundred','people_fully_vaccinated_per_hundred','total_boosters_per_hundred']

for columnName in columnNamelist:
    for countryName in countryNamelist:
        select_country = df.loc[df['iso_code'] == countryName]
        y = list(select_country[columnName])
        x = list(select_country['date'])
        datetimes = pd.to_datetime(x)
        x = datetimes
        
        plt.figure(figsize=(10,10))
        plt.style.use('seaborn')
        plt.scatter(x,y,marker=".",s=100,edgecolors="black",c="red")
        plt.title(countryName + ' ' + columnName)
        plt.savefig(countryName + ' ' + columnName+'.png')
        plt.show()       
               
plt.close()


# In[95]:


#erwthma 1c
countryNamelist=['DEU','NLD','ROU']
columnNamelist=['new_cases_per_million','new_deaths_per_million','reproduction_rate','icu_patients_per_million',
                'hosp_patients_per_million','new_tests_per_thousand','positive_rate','total_vaccinations_per_hundred',
                'people_vaccinated_per_hundred','people_fully_vaccinated_per_hundred','total_boosters_per_hundred']

for columnName in columnNamelist:
    for countryName in countryNamelist:
        select_country = df.loc[df['iso_code'] == countryName]
        y = list(select_country[columnName])
        x = list(select_country['date'])
        trm = [] 
        for i in range(len(x)):
            YMD = x[i].split('-')
            for i in range(len(YMD)):
                YMD[i] = int(YMD[i])
            if YMD[1]<= 3 and YMD[1]>=1:
                trm.append(1)
            elif YMD[1]<= 6 and YMD[1]>=4:
                trm.append(2)
            elif YMD[1]<= 9 and YMD[1]>=7:
                trm.append(3)
            else:
                trm.append(4)
        if len(trm)==len(x) and len(x)==len(y):
            trm.append(trm[-1])
            z=[]
            for i in range(len(trm)-1):
                if trm[i]==trm[i+1]:
                    z.append(y[i])
                else:
                    plt.boxplot(z)
                    plt.title(countryName + ' ' + columnName + ' ' + x[i])
                    plt.savefig(countryName + ' ' + columnName + ' ' + x[i]+'.png')
                    plt.show()
                    sorted_z = sorted(z)
                    
                    #Outlier 1
                    Out1 = min(sorted_z)
                    
                    #Outlier 2
                    Out2 = max(sorted_z)
                    
                    #middle index
                    mid = len(sorted_z) // 2
                    median = (sorted_z[mid] + sorted_z[-mid-1]) / 2
                    
                    #Quartile 1
                    z1 = sorted_z[:mid]
                    mid1 = len(z1) // 2
                    Q1 = (z1[mid1] + z1[-mid1-1]) / 2
                    
                    #Quartile 3
                    z2 = sorted_z[mid:]
                    mid2 = len(z2) // 2
                    Q3 = (z2[mid2] + z2[-mid2-1]) / 2
                    
                    print('Outlier 1: ',Out1)
                    print('Outlier 2: ',Out2)
                    print('Q1: ',Q1)
                    print('Median: ',median)
                    print('Q3: ',Q3)
                    
                    z1.clear()
                    z2.clear()
                    sorted_z.clear()
                    z.clear() 
        else:
            print("Lists need to be the same length")
plt.close()


# In[ ]:




