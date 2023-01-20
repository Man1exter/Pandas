import pandas as pd

a = [['Ana',47],['Mario',22],['Jano',52],['Misa',21]]
df_a = pd.DataFrame(a)
df_a.columns = 'Name','Age'
print(df_a)