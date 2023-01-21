import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math as math

#%matplotlib line

h1 = pd.read_csv('exp_isp_sz_demografia_pow_6.csv')
#print(h1)

#plt.plot([1,2,3,4,5])
#plt.ylabel('Numbers')
#plt.show()

#plt.plot([1,2,3,4,5],[34,12,44,55,66],'ro')
#plt.show()

#t = np.arange(0.,5.,1.2)
#plt.plot(t,t,'r--',t,t**2,'bs',t,t**3,'g^')
#plt.show()


#################
min = 0
max = 4 * np.pi
step = 0.1

x = np.arange(min,max,step)
y = np.sin(x)

plt.plot(x,y)
plt.xlabel('angle')
plt.ylabel('sin(angle')
plt.show()
################