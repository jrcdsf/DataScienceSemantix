# -*- coding: utf-8 -*-
"""
Created on Tue Oct  2 20:01:45 2018

@author: JR
"""

import pandas as pds

bank_full = pds.read_csv('E:/semantix/bank/bank-full.csv')

data = bank_full.groupby('job').y.value_counts().sort_index()
data.unstack().plot(kind='bar', subplots=False, layout=(2,2), title='JOB vs Y', grid=True, figsize = (15,20))

data1 = bank_full.groupby('job').housing.value_counts().sort_index()
data1.unstack().plot(kind='bar', subplots=False, layout=(2,2), title='JOB vs HOUSING', grid=True, figsize = (15,20))

data2 = bank_full.groupby('job').loan.value_counts().sort_index()
data2.unstack().plot(kind='bar', subplots=False, layout=(2,2), title='JOB vs LOAN', grid=True, figsize = (15,20))

data3 = bank_full.groupby('campaign').y.value_counts().sort_index()
data3.unstack().plot(kind='bar', subplots=False, layout=(2,2), title='CAMPAIGN vs Y', grid=True, figsize = (15,20))

data4 = bank_full.groupby('previous').y.value_counts().sort_index()
data4.unstack().plot(kind='bar', subplots=False, layout=(2,2), title='PREVIOUS vs Y', grid=True, figsize = (15,20))

data5 = bank_full.groupby('education').housing.value_counts().sort_index()
data5.unstack().plot(kind='bar', subplots=False, layout=(2,2), title='EDUCATION vs HOUSING', grid=True, figsize = (15,20))

data6 = bank_full.groupby('marital').housing.value_counts().sort_index()
data6.unstack().plot(kind='bar', subplots=False, layout=(2,2), title='MARITAL vs HOUSING', grid=True, figsize = (15,20))

data7 = bank_full.groupby('age').housing.value_counts().sort_index()
data7.unstack().plot(kind='bar', subplots=False, layout=(2,2), title='AGE vs HOUSING', grid=True, figsize = (30,10))

data8 = bank_full.groupby('poutcome').previous.value_counts().sort_index()
data8.unstack().plot(kind='bar', subplots=False, layout=(2,2), title='POUTCOME vs PREVIOUS', grid=True, figsize = (30,10))

