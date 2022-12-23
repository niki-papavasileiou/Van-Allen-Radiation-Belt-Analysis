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

startdate = pd.to_datetime("2005-12-29 00:50:13").date()
enddate = pd.to_datetime("2015-01-01 00:07:53").date()
date_1 = df_1.loc[startdate:enddate]
l = date_1['odi_unilib_l']

startdate = pd.to_datetime("2005-01-01 00:50:13").date()
enddate = pd.to_datetime("2015-01-01 00:07:53").date()
date_2= df_2.loc[startdate:enddate]
l = date_2['odi_unilib_l']

date_1['epoch'] = date_1.index
df_new = date_1.filter(['epoch','odi_unilib_l','fedo_3','fedo_2','fedo_1'], axis= 1)
fedo3= df_new['fedo_3']
fedo1= df_new['fedo_1']
fedo2= df_new['fedo_2']

startdate = pd.to_datetime("2005-01-01 00:50:13").date()
enddate = pd.to_datetime("2005-12-30 00:07:53").date()
date_2005= df_2.loc[startdate:enddate]
date_2005['epoch'] = date_2005.index
fedo3_2005= date_2005['fedo_3']
fedo1_2005= date_2005['fedo_1']
fedo2_2005= date_2005['fedo_2']

startdate = pd.to_datetime("2006-01-01 00:50:13").date()
enddate = pd.to_datetime("2006-12-30 00:07:53").date()
date_2006= df_2.loc[startdate:enddate]
date_2006['epoch'] = date_2006.index
fedo3_2006= date_2006['fedo_3']
fedo1_2006= date_2006['fedo_1']
fedo2_2006= date_2006['fedo_2']

startdate = pd.to_datetime("2007-01-01 00:50:13").date()
enddate = pd.to_datetime("2007-12-30 00:07:53").date()
date_2007= df_2.loc[startdate:enddate]
date_2007['epoch'] = date_2007.index
fedo3_2007= date_2007['fedo_3']
fedo1_2007= date_2007['fedo_1']
fedo2_2007= date_2007['fedo_2']

startdate = pd.to_datetime("2008-01-01 00:50:13").date()
enddate = pd.to_datetime("2008-12-30 00:07:53").date()
date_2008= df_2.loc[startdate:enddate]
date_2008['epoch'] = date_2008.index
fedo3_2008= date_2008['fedo_3']
fedo1_2008= date_2008['fedo_1']
fedo2_2008= date_2008['fedo_2']

startdate = pd.to_datetime("2009-01-01 00:50:13").date()
enddate = pd.to_datetime("2009-12-30 00:07:53").date()
date_2009= df_2.loc[startdate:enddate]
date_2009['epoch'] = date_2009.index
fedo3_2009= date_2009['fedo_3']
fedo1_2009= date_2009['fedo_1']
fedo2_2009= date_2009['fedo_2']

startdate = pd.to_datetime("2010-01-01 00:50:13").date()
enddate = pd.to_datetime("2010-12-30 00:07:53").date()
date_2010= df_2.loc[startdate:enddate]
date_2010['epoch'] = date_2010.index
fedo3_2010= date_2010['fedo_3']
fedo1_2010= date_2010['fedo_1']
fedo2_2010= date_2010['fedo_2']

startdate = pd.to_datetime("2011-01-01 00:50:13").date()
enddate = pd.to_datetime("2011-12-30 00:07:53").date()
date_2011= df_2.loc[startdate:enddate]
date_2011['epoch'] = date_2011.index
fedo3_2011= date_2011['fedo_3']
fedo1_2011= date_2011['fedo_1']
fedo2_2011= date_2011['fedo_2']

startdate = pd.to_datetime("2012-01-01 00:50:13").date()
enddate = pd.to_datetime("2012-12-30 00:07:53").date()
date_2012= df_2.loc[startdate:enddate]
date_2012['epoch'] = date_2012.index
fedo3_2012= date_2012['fedo_3']
fedo1_2012= date_2012['fedo_1']
fedo2_2012= date_2012['fedo_2']

startdate = pd.to_datetime("2013-01-01 00:50:13").date()
enddate = pd.to_datetime("2013-12-30 00:07:53").date()
date_2013= df_2.loc[startdate:enddate]
date_2013['epoch'] = date_2013.index
fedo3_2013= date_2013['fedo_3']
fedo1_2013= date_2013['fedo_1']
fedo2_2013= date_2013['fedo_2']

startdate = pd.to_datetime("2014-01-01 00:50:13").date()
enddate = pd.to_datetime("2014-12-30 00:07:53").date()
date_2014= df_2.loc[startdate:enddate]
date_2014['epoch'] = date_2014.index
fedo3_2014= date_2014['fedo_3']
fedo1_2014= date_2014['fedo_1']
fedo2_2014= date_2014['fedo_2']

startdate = pd.to_datetime("2015-01-01 00:50:13").date()
enddate = pd.to_datetime("2015-12-30 00:07:53").date()
date_2015 = df_2.loc[startdate:enddate]
date_2015['epoch'] = date_2015.index
fedo3_2015= date_2015['fedo_3']
fedo1_2015= date_2015['fedo_1']
fedo2_2015= date_2015['fedo_2']


startdate = pd.to_datetime("2006-01-01 00:50:13").date()
enddate = pd.to_datetime("2006-02-01 00:07:53").date()
date_3 = df_2.loc[startdate:enddate]

fedo_1_1month = date_3['fedo_1'].notna()
fedo_2_1month = date_3['fedo_2'].notna()
fedo_3_1month = date_3['fedo_3'].notna()

fedo_1 = date_2['fedo_1'].notna()
fedo_2 = date_2['fedo_2'].notna()
fedo_3 = date_2['fedo_3'].notna()

anova = f_oneway(date_3['fedo_1'].notna(), date_3['fedo_2'].notna(), date_3['fedo_3'].notna())

startdate = pd.to_datetime("2006-01-01 23:50:13").date()
enddate = pd.to_datetime("2006-01-02 23:50:13").date()
date_4 = df_2.loc[startdate:enddate]

anova_1day = f_oneway(date_4['fedo_1'].notna(), date_4['fedo_2'].notna(), date_4['fedo_3'].notna())

fname='./Kp_and_ap_since_1932.txt'
colnames=['YYY', 'MM', 'DD', 'hh.h', 'hh._m', 'days', 'days_m', 'Kp', 'ap', 'D'] 
Kp_df = pd.read_csv(fname, delim_whitespace=True,skiprows=30, names = colnames, header=None,dtype='unicode')

Kp_2005 = Kp_df.loc[Kp_df['YYY'] == '2005']
Kp_2005['Kp'] = pd.to_numeric(Kp_2005['Kp'])

corr_3hours = Kp_2005['Kp'].autocorr(lag = 1)     #3 ores
corr_1day = Kp_2005['Kp'].autocorr(lag = 8)     #1 day
corr_1month = Kp_2005['Kp'].autocorr(lag = 240)     #1 mina

Kp_00_10 = Kp_df.loc[(Kp_df['YYY'] >= '2005') & (Kp_df['YYY'] <= '2015')]
Kp_00_10['Kp'] = pd.to_numeric(Kp_00_10['Kp'])

corr_1year = Kp_00_10['Kp'].autocorr(lag = 3650)     #1 xrono
corr_2years = Kp_00_10['Kp'].autocorr(lag = 7300)     #2 xronia
corr_5years = Kp_00_10['Kp'].autocorr(lag = 18250)     #5 xronia

inpt = input("please choose a number\n\n--------FEDO HEATMAPS--------\n\ni.fedo 1 2005-1015\nii.fedo 2 2005-1015\niii.fedo 3 2005-2015\n1.fedo 1, 2005\n2.fedo 2 2005\n3.fedo 3 2005\n4.fedo 1 2006\n5.fedo 2 2006\n6.fedo 3 2006\n7.fedo 1 2007\n8.fedo 2 2007\n9.fedo 3 2007\n10.fedo 1 2008\n11.fedo 2 2008\n12.fedo 3 2008\n13.fedo 1 2009\n14.fedo 2 2009\n15.fedo 3 2009\n16.fedo 1 2010\n17.fedo 2 2010\n18.fedo 3 2010\n19.fedo 1 2011\n20.fedo 2 2011\n21.fedo 3 2011\n22.fedo 1 2012\n23.fedo 2 2012\n24.fedo 3 2012\n25.fedo 1 2013\n26.fedo 2 2013\n27.fedo 3 2013\n28.fedo 1 2014\n29.fedo 2 2014\n30.fedo 3 2014\n31.fedo 1 2015\n32.fedo 2 2015\n33.fedo 3 2015\n\n\n----------BOXPLOTS----------\n\nib.2005-2015\na.2005\nb.2006\nc.2007\nd.2008\ne.2009\nf.2010\ng.2011\nh.2012\ni.2013\nj.2014\nk.2015\n\n\n---------STANDARD DEVIATION-----------\n\n1i.2005-2015\n1ii.(2006-01-01-2006-02-01) one month\n\n\n----------ANOVA----------\n\n2i.anova one month (2006-01-01-2006-02-01) \n2ii.anova one day(2006-01-01-2006-01-02) \n\n\n----------Kp AUTOCORRELATION----------\n\n1a.plot 2005 autocorrelation\n1b.(2005) 3 hours\n1c.(2005) 1 day\n1d.(2005) 1 month\n1e. plot 2005-2015 autocorrelation\n1f.(2005-2015) 1 year\n1g.(2005-2015) 2 years\n1h.(2005-2015) 5 years\n")

if inpt in ['1']:
    date_2005.plot(kind = 'scatter', x = 'epoch' , y = 'odi_unilib_l', c = np.log10(fedo1_2005) ,colorbar = True, cmap = cm.jet)
    plt.show()
elif inpt in ['2']:
    date_2005.plot(kind = 'scatter', x = 'epoch' , y = 'odi_unilib_l', c = np.log10(fedo2_2005) ,colorbar = True, cmap = cm.jet)
    plt.show()
elif inpt in ['3']:
    date_2005.plot(kind = 'scatter', x = 'epoch' , y = 'odi_unilib_l', c = np.log10(fedo3_2005) ,colorbar = True, cmap = cm.jet)
    plt.show()
elif inpt in ['4']:
    date_2006.plot(kind = 'scatter', x = 'epoch' , y = 'odi_unilib_l', c = np.log10(fedo1_2006) ,colorbar = True, cmap = cm.jet)
    plt.show()
elif inpt in ['5']:
    date_2006.plot(kind = 'scatter', x = 'epoch' , y = 'odi_unilib_l', c = np.log10(fedo2_2006) ,colorbar = True, cmap = cm.jet)
    plt.show()
elif inpt in ['6']:
    date_2006.plot(kind = 'scatter', x = 'epoch' , y = 'odi_unilib_l', c = np.log10(fedo3_2006) ,colorbar = True, cmap = cm.jet)
    plt.show()
elif inpt in ['7']:
    date_2007.plot(kind = 'scatter', x = 'epoch' , y = 'odi_unilib_l', c = np.log10(fedo1_2007) ,colorbar = True, cmap = cm.jet)
    plt.show()
elif inpt in ['8']:
    date_2007.plot(kind = 'scatter', x = 'epoch' , y = 'odi_unilib_l', c = np.log10(fedo2_2007) ,colorbar = True, cmap = cm.jet)
    plt.show()
elif inpt in ['9']:
    date_2007.plot(kind = 'scatter', x = 'epoch' , y = 'odi_unilib_l', c = np.log10(fedo3_2007) ,colorbar = True, cmap = cm.jet)
    plt.show()
elif inpt in ['10']:
    date_2008.plot(kind = 'scatter', x = 'epoch' , y = 'odi_unilib_l', c = np.log10(fedo1_2008) ,colorbar = True, cmap = cm.jet)
    plt.show()
elif inpt in ['11']:
    date_2008.plot(kind = 'scatter', x = 'epoch' , y = 'odi_unilib_l', c = np.log10(fedo2_2008) ,colorbar = True, cmap = cm.jet)
    plt.show()
elif inpt in ['12']:
    date_2008.plot(kind = 'scatter', x = 'epoch' , y = 'odi_unilib_l', c = np.log10(fedo3_2008) ,colorbar = True, cmap = cm.jet)
    plt.show()
elif inpt in ['13']:
    date_2009.plot(kind = 'scatter', x = 'epoch' , y = 'odi_unilib_l', c = np.log10(fedo1_2009) ,colorbar = True, cmap = cm.jet)
    plt.show()
elif inpt in ['14']:
    date_2009.plot(kind = 'scatter', x = 'epoch' , y = 'odi_unilib_l', c = np.log10(fedo2_2009) ,colorbar = True, cmap = cm.jet)
    plt.show()
elif inpt in ['15']:
    date_2009.plot(kind = 'scatter', x = 'epoch' , y = 'odi_unilib_l', c = np.log10(fedo3_2009) ,colorbar = True, cmap = cm.jet)
    plt.show()
elif inpt in ['16']:
    date_2010.plot(kind = 'scatter', x = 'epoch' , y = 'odi_unilib_l', c = np.log10(fedo1_2010) ,colorbar = True, cmap = cm.jet)
    plt.show()
elif inpt in ['17']:
    date_2010.plot(kind = 'scatter', x = 'epoch' , y = 'odi_unilib_l', c = np.log10(fedo2_2010) ,colorbar = True, cmap = cm.jet)
    plt.show()
elif inpt in ['18']:
    date_2010.plot(kind = 'scatter', x = 'epoch' , y = 'odi_unilib_l', c = np.log10(fedo3_2010) ,colorbar = True, cmap = cm.jet)
    plt.show()
elif inpt in ['19']:
    date_2011.plot(kind = 'scatter', x = 'epoch' , y = 'odi_unilib_l', c = np.log10(fedo1_2011) ,colorbar = True, cmap = cm.jet)
    plt.show()
elif inpt in ['20']:
    date_2011.plot(kind = 'scatter', x = 'epoch' , y = 'odi_unilib_l', c = np.log10(fedo2_2011) ,colorbar = True, cmap = cm.jet)
    plt.show()
elif inpt in ['21']:
    date_2011.plot(kind = 'scatter', x = 'epoch' , y = 'odi_unilib_l', c = np.log10(fedo3_2011) ,colorbar = True, cmap = cm.jet)
    plt.show()
elif inpt in ['22']:
    date_2012.plot(kind = 'scatter', x = 'epoch' , y = 'odi_unilib_l', c = np.log10(fedo1_2012) ,colorbar = True, cmap = cm.jet)
    plt.show()
elif inpt in ['23']:
    date_2012.plot(kind = 'scatter', x = 'epoch' , y = 'odi_unilib_l', c = np.log10(fedo2_2012) ,colorbar = True, cmap = cm.jet)
    plt.show()
elif inpt in ['24']:
    date_2012.plot(kind = 'scatter', x = 'epoch' , y = 'odi_unilib_l', c = np.log10(fedo3_2012) ,colorbar = True, cmap = cm.jet)
    plt.show()
elif inpt in ['25']:
    date_2013.plot(kind = 'scatter', x = 'epoch' , y = 'odi_unilib_l', c = np.log10(fedo1_2013) ,colorbar = True, cmap = cm.jet)
    plt.show()
elif inpt in ['26']:
    date_2013.plot(kind = 'scatter', x = 'epoch' , y = 'odi_unilib_l', c = np.log10(fedo2_2013) ,colorbar = True, cmap = cm.jet)
    plt.show()
elif inpt in ['27']:
    date_2013.plot(kind = 'scatter', x = 'epoch' , y = 'odi_unilib_l', c = np.log10(fedo3_2013) ,colorbar = True, cmap = cm.jet)
    plt.show()
elif inpt in ['30']:
    date_2014.plot(kind = 'scatter', x = 'epoch' , y = 'odi_unilib_l', c = np.log10(fedo1_2014) ,colorbar = True, cmap = cm.jet)
    plt.show()
elif inpt in ['31']:
    date_2014.plot(kind = 'scatter', x = 'epoch' , y = 'odi_unilib_l', c = np.log10(fedo2_2014) ,colorbar = True, cmap = cm.jet)
    plt.show()
elif inpt in ['32']:
    date_2014.plot(kind = 'scatter', x = 'epoch' , y = 'odi_unilib_l', c = np.log10(fedo3_2014) ,colorbar = True, cmap = cm.jet)
    plt.show()
elif inpt in ['33']:
    date_2015.plot(kind = 'scatter', x = 'epoch' , y = 'odi_unilib_l', c = np.log10(fedo1_2015) ,colorbar = True, cmap = cm.jet)
    plt.show()
elif inpt in ['34']:
    date_2015.plot(kind = 'scatter', x = 'epoch' , y = 'odi_unilib_l', c = np.log10(fedo2_2015) ,colorbar = True, cmap = cm.jet)
    plt.show()
elif inpt in ['35']:
    date_2015.plot(kind = 'scatter', x = 'epoch' , y = 'odi_unilib_l', c = np.log10(fedo3_2015) ,colorbar = True, cmap = cm.jet)
    plt.show()
elif inpt in ['i']:
    df_new.plot(kind = 'scatter', x = 'epoch' , y = 'odi_unilib_l', c = np.log10(fedo1) ,colorbar = True, cmap = cm.jet)
    plt.show()
elif inpt in ['ii']:
    df_new.plot(kind = 'scatter', x = 'epoch' , y = 'odi_unilib_l', c = np.log10(fedo2) ,colorbar = True, cmap = cm.jet)
    plt.show()
elif inpt in ['iii']:
    df_new.plot(kind = 'scatter', x = 'epoch' , y = 'odi_unilib_l', c = np.log10(fedo3) ,colorbar = True, cmap = cm.jet)
    plt.show()

elif inpt in ['ib']:
    b_plot = date_2.boxplot(column = ['fedo_1', 'fedo_2', 'fedo_3']) 
    plt.yscale('log')
    b_plot.plot()
    plt.show()
elif inpt in ['a']:
    b_plot = date_2005.boxplot(column = ['fedo_1', 'fedo_2', 'fedo_3']) 
    plt.yscale('log')
    b_plot.plot()
    plt.show()
elif inpt in ['b']:
    b_plot = date_2006.boxplot(column = ['fedo_1', 'fedo_2', 'fedo_3']) 
    plt.yscale('log')
    b_plot.plot()
    plt.show()
elif inpt in ['c']:
    b_plot = date_2007.boxplot(column = ['fedo_1', 'fedo_2', 'fedo_3']) 
    plt.yscale('log')
    b_plot.plot()
    plt.show()
elif inpt in ['d']:
    b_plot = date_2008.boxplot(column = ['fedo_1', 'fedo_2', 'fedo_3']) 
    plt.yscale('log')
    b_plot.plot()
    plt.show()
elif inpt in ['e']:
    b_plot = date_2009.boxplot(column = ['fedo_1', 'fedo_2', 'fedo_3']) 
    plt.yscale('log')
    b_plot.plot()
    plt.show()
elif inpt in ['f']:
    b_plot = date_2010.boxplot(column = ['fedo_1', 'fedo_2', 'fedo_3']) 
    plt.yscale('log')
    b_plot.plot()
    plt.show()
elif inpt in ['g']:
    b_plot = date_2011.boxplot(column = ['fedo_1', 'fedo_2', 'fedo_3']) 
    plt.yscale('log')
    b_plot.plot()
    plt.show()
elif inpt in ['h']:
    b_plot = date_2012.boxplot(column = ['fedo_1', 'fedo_2', 'fedo_3']) 
    plt.yscale('log')
    b_plot.plot()
    plt.show()
elif inpt in ['i']:
    b_plot = date_2013.boxplot(column = ['fedo_1', 'fedo_2', 'fedo_3']) 
    plt.yscale('log')
    b_plot.plot()
    plt.show()
elif inpt in ['j']:
    b_plot = date_2014.boxplot(column = ['fedo_1', 'fedo_2', 'fedo_3']) 
    plt.yscale('log')
    b_plot.plot()
    plt.show()
elif inpt in ['k']:
    b_plot = date_2015.boxplot(column = ['fedo_1', 'fedo_2', 'fedo_3']) 
    plt.yscale('log')
    b_plot.plot()
    plt.show()

elif inpt in ['1a']:
    plot2005 = np.array(Kp_2005['Kp'])
    x = pd.plotting.autocorrelation_plot(plot2005)
    x.plot()
    plt.show()
elif inpt in ['1b']:
    print(corr_3hours)
elif inpt in ['1c']:
    print(corr_1day)
elif inpt in ['1d']:
    print(corr_1month)
elif inpt in ['1e']:
    plot_00_10 = np.array(Kp_2005['Kp'])
    x = pd.plotting.autocorrelation_plot(plot_00_10)
    x.plot()
    plt.show()
elif inpt in ['1f']:
    print(corr_1year)
elif inpt in ['1g']:
    print(corr_2years)
elif inpt in ['1h']:
    print(corr_5years)

elif inpt in ['1i']:
    print(fedo_1.std(), fedo_2.std(), fedo_3.std())
elif inpt in ['1ii']:
    print(fedo_1_1month.std(), fedo_2_1month.std(), fedo_3_1month.std())
elif inpt in ['1i']:
    print(anova)
elif inpt in ['1i']:
    print(anova_1day)
