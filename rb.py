import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm 
from scipy.stats import f_oneway

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

df_1 = df.loc[(df['odi_unilib_l'] > 1 ) & (df['odi_unilib_l'] < 8) &(df['odi_unilib_alpha_eq']<90)  &(df['odi_unilib_alpha_eq']>0) ]
df_2 = df.loc[(df['odi_unilib_l'] > 4.5 ) & (df['odi_unilib_l'] < 7.5) &(df['odi_unilib_alpha_eq']<90)  &(df['odi_unilib_alpha_eq']>0)]

startdate = pd.to_datetime("2000-01-01 00:50:13").date()
enddate = pd.to_datetime("2010-01-01 00:07:53").date()
date_1 = df_1.loc[startdate:enddate]
l = date_1['odi_unilib_l']

startdate = pd.to_datetime("2000-01-01 00:50:13").date()
enddate = pd.to_datetime("2010-01-01 00:07:53").date()
date_2= df_2.loc[startdate:enddate]
l = date_2['odi_unilib_l']

date_1['epoch'] = date_1.index
df_new = date_1.filter(['epoch','odi_unilib_l','fedo_3'], axis= 1)
fedo3= df_new['fedo_3']

df_new.plot(kind = 'scatter', x = 'epoch' , y = 'odi_unilib_l', c = np.log10(fedo3) ,colorbar = True, cmap = cm.hsv)
plt.show()

b_plot = date_2.boxplot(column = ['fedo_1', 'fedo_2', 'fedo_3']) 
plt.yscale('log')
b_plot.plot()
plt.show()

startdate = pd.to_datetime("2006-01-01 00:50:13").date()
enddate = pd.to_datetime("2006-02-01 00:07:53").date()
date_3 = df_2.loc[startdate:enddate]

anova = f_oneway(date_3['fedo_1'].notna(), date_3['fedo_2'].notna(), date_3['fedo_3'].notna())
print(anova)

startdate = pd.to_datetime("2006-01-01 23:50:13").date()
enddate = pd.to_datetime("2006-01-02 23:50:13").date()
date_4 = df_2.loc[startdate:enddate]

anova_1day = f_oneway(date_4['fedo_1'].notna(), date_4['fedo_2'].notna(), date_4['fedo_3'].notna())
print(anova_1day)


fname='./Kp_and_ap_since_1932.txt'
colnames=['YYY', 'MM', 'DD', 'hh.h', 'hh._m', 'days', 'days_m', 'Kp', 'ap', 'D'] 
Kp_df = pd.read_csv(fname, delim_whitespace=True,skiprows=30, names = colnames, header=None,dtype='unicode')

Kp_2000 = Kp_df.loc[Kp_df['YYY'] == '2000']
Kp_2000['Kp'] = pd.to_numeric(Kp_2000['Kp'])

plot2000 = np.array(Kp_2000['Kp'])
x = pd.plotting.autocorrelation_plot(plot2000)
x.plot()
plt.show()

corr_1hour = Kp_2000['Kp'].autocorr(lag = 1)     #3 ores
print(corr_1hour)

corr_1day = Kp_2000['Kp'].autocorr(lag = 8)     #1 day
print(corr_1day)

corr_1month = Kp_2000['Kp'].autocorr(lag = 240)     #1 mina
print(corr_1month)

Kp_00_10 = Kp_df.loc[(Kp_df['YYY'] >= '2000') & (Kp_df['YYY'] <= '2010')]
Kp_00_10['Kp'] = pd.to_numeric(Kp_00_10['Kp'])

plot_00_10 = np.array(Kp_2000['Kp'])
x = pd.plotting.autocorrelation_plot(plot_00_10)
x.plot()
plt.show()

corr_1year = Kp_00_10['Kp'].autocorr(lag = 3650)     #1 xrono
print(corr_1year)

corr_2years = Kp_00_10['Kp'].autocorr(lag = 7300)     #2 xronia
print(corr_2years)

corr_5years = Kp_00_10['Kp'].autocorr(lag = 18250)     #5 xronia
print(corr_5years)
