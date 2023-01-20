import pandas as pd

a = pd.Series([-1,-5,2,3,4,9])
#print(a)

#b = a * 10
#print(b)

#c = a.abs()
#d = a.describe()
#print(c/d)

a.index = ['Mario','Jano','Miszka','Ana','Zbi','Pieta']
print(a['Pieta'])
print(a)