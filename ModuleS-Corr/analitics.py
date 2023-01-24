import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

base = pd.read_csv('exp_isp_sz_demografia_pow_6.csv')

print(base)
#base.plot()
#plt.show()

data_pie = base["Ludność"]
data_pie.plot.pie(autopct='%1.1f%%')
plt.title("Ludność")
plt.show()