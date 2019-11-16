import matplotlib.pyplot as plt
import numpy as np

#plt.plot([1,2,3],[4,5,1])

#plt.show()
languages= 'python','Java','PHP','JS','C#','C++'
popularity = [22.2,17.6,8.8,8,7.7,6.7]
colors = ["red","yellow","blue","pink","orange","green"]

explode = (0.1,0,0,0,0,0)
plt.pie(popularity, explode=explode, labels=languages, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
plt.show()
