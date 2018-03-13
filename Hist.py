import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

#f = open('Nplan_per_star.dat','r')
#lines = f.readlines()
#f.close()

#x = []

with open('Nplan_per_star.dat') as f:
	for line in f:
#for line in lines:
		data = map(float,line.split())
		x = data[0]

plt.hist(x, bins='auto')


# Show plot on screen
plt.show()
