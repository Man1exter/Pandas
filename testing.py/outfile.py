import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('http://analityk.edu.pl/wp-content/uploads/2020/01/Countries.csv')
type(df)

#print(df)
#print(df[:3])
#print(df[['Country','Region']])

#print(df.iloc[0:3,0:3])
#print(df.loc[:3,['Country','Region','Population']])


df_pop = df[['Country','Region','Population']].copy()

#print(df_pop)
#print(df_pop['Population'] /= 10000)
#print(df_pop.head())

#for index,row in df_pop.iterrows():
    #if row['Population'] > 100:
        #df_pop.loc[index,'Size'] = 'BigCC'
        #print(row['Country'],df_pop.loc[index,'Size'])
        
#print(df_pop)

#df_pop.Population == 147.35636
#print(df_pop[df_pop.Population == 147.35636])
#print(df_pop[df_pop['Population'] == 147.35636])

#print(df_pop.groupby('Region')['Population'].agg([min,max,sum]))

#pd.merge(df_a,dfa_b,on='Imię')
#pd.merge(df_a,dfa_b,on='Imię',how='left')
#pd.merge(df_a,dfa_b,on='Imię',how='right')
#pd.merge(df_a,dfa_b,on='Imię',how='outer')


df_pop.groupby('Region')['Population'].sum()
df_pop.groupby('Region')['Population'].sum().sort_values().plot(kind='bar',figsize=(17,5))
plt.show()