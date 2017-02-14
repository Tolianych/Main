'''
Created on Feb 14, 2017

@author: tolianych
'''


import numpy as np
import matplotlib.pyplot as plt

# columns = [d for d in xrange (1, 32)]
columns = ['1','2','3','4','5']
rows = ('Av', '2011', '2012', '2013', '2014', '2015', '2016')

ax = plt.subplot(111, frame_on=False)
ax.xaxis.set_visible(False)
ax.yaxis.set_visible(False)

the_table = plt.table(cellText=[[2210,8154,4222,9547,3887], [2210,8154,4222,9547,3887],[2210,8154,4222,9547,3887],[2210,8154,4222,9547,3887],[2210,8154,4222,9547,3887],[2210,8154,4222,9547,3887],[2210,8154,4222,9547,3887]],
                      rowLabels=rows,
                      colLabels=columns,
                      cellLoc='center',
                      loc='center')

# plt.subplots_adjust(left=0.2, bottom=0.4)

# plt.ylabel('Temp')
# plt.yticks(values * value_increment, ['%d' % val for val in values])
# plt.xticks([])
plt.title('Temperature')

plt.show()



# t = np.arange(0.0, 2.0, 0.01)
# s = 1 + np.sin(2*np.pi*t)
# plt.plot(t, s)
#
# plt.xlabel('time (s)')
# plt.ylabel('voltage (mV)')
# plt.title('About as simple as it gets, folks')
# plt.grid(True)
# plt.savefig("test.png")
# plt.show()
