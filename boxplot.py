import pandas as pd 
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
pd.options.mode.chained_assignment = None

df = pd.read_csv('High_MEO_FEDO.csv')

df['epoch'] = pd.to_datetime(df['epoch']).dt.date
df = df.set_index('epoch')   

df['fedo_1'][df['fedo_1']< 0] = np.nan
#df = df[df['fedo_1'].notna()]
df['fedo_2'][df['fedo_2']< 0] = np.nan
#df = df[df['fedo_2'].notna()]
df['fedo_3'][df['fedo_3']< 0] = np.nan 
#df = df[df['fedo_3'].notna()]

one = np.random.normal(df['fedo_1'].mean(),df['fedo_1'].std(),2000 )
two = np.random.normal(df['fedo_2'].mean(),df['fedo_2'].std(),2000 )
three = np.random.normal(df['fedo_3'].mean(),df['fedo_3'].std(),2000 )

startdate = pd.to_datetime("2006-01-10 23:50:13").date()
enddate = pd.to_datetime("2006-01-13 12:07:53").date()
df = df.loc[startdate:enddate]

df = df.loc[(df['odi_unilib_l'] > 1 ) & (df['odi_unilib_l'] < 8) &(df['odi_unilib_alpha_eq']<90)  &(df['odi_unilib_alpha_eq']>0) ]

data = [one ,two ,three]
fig = plt.figure(figsize =(6, 6))

plt.boxplot(data)
plt.show()