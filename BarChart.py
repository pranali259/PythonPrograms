# Plot bar plot
#https://www.youtube.com/watch?v=iedmZlFxjfA

import matplotlib.pyplot as plt
import numpy as np

company=['Google','Amzn','MSFT','FS']
revenue=[90,136,89,27]

ypos = np.arange(len(company))
plt.bar(ypos,revenue)
plt.show()
