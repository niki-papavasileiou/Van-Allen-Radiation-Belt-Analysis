import pandas as pd 
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm
pd.options.mode.chained_assignment = None

df = pd.read_csv('High_MEO_FEDO.csv')

df['epoch'] = pd.to_datetime(df['epoch']).dt.date
df = df.set_index('epoch')   

df['fedo_1'][df['fedo_1']< 0] = np.nan
#df = df[df['fedo_1'].notna()]
df['fedo_2'][df['fedo_2']< 0] = np.nan
#df = df[df['fedo_2'].notna()]
df['fedo_3'][df['fedo_3']< 0] = np.nan 
df = df[df['fedo_3'].notna()]

startdate = pd.to_datetime("2006-01-10 23:50:13").date()
enddate = pd.to_datetime("2006-01-13 12:07:53").date()
df = df.loc[startdate:enddate]

df1 = df.loc[(df['odi_unilib_l'] > 1 ) & (df['odi_unilib_l'] < 8) &(df['odi_unilib_alpha_eq']<90)  &(df['odi_unilib_alpha_eq']>0) ]

#df1 = df1.groupby(['odi_unilib_l', 'epoch'],sort=False).agg(['mean'])

df2matrix = df1.pivot_table(index='odi_unilib_l', columns='epoch',values='fedo_3')

t = sns.heatmap(df2matrix, cmap="crest",norm=LogNorm())
plt.xlabel("epoch", size=14)
plt.ylabel("L", size=14)
plt.title("FEDO ", size=14)
plt.tight_layout()
plt.savefig('heatmap.jpg',dpi=150)