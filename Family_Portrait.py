import numpy as np
from numpy import loadtxt
import matplotlib.pyplot as plt

# Planet parameters

p1 = []			# Planet mass
p2 = []			# Planet radius
p3 = []			# Eccentricity
p4 = []			# Semi-major axis
p5 = []			# Orbital period
p6 = []			# Inclination

# Star parameters

s1 = []			# Stellar mass
s2 = []			# Metallicity [Fe/H]
s3 = []			# Stellar radius
s4 = []			# Effective temperature
s5 = []			# Main sequence lifetime
s6 = []			# Number of planets

print "got this far 1"

plan = loadtxt("Planets.dat", comments="#", delimiter="\t", skiprows=1, usecols=(1,2,3,4,5,6), unpack=False)
for row in plan:
	p1.append(row[0])
	p2.append(row[1])
	p3.append(row[2])
	p4.append(row[3])
	p5.append(row[4])
	p6.append(row[5])

print "got this far 2"

star = loadtxt("Stars.dat", comments="#", delimiter="\t", skiprows=1, usecols=(1,2,3,5,6,7), unpack=False)
for row in star:
	s1.append(row[0])
	s2.append(row[1])
	s3.append(row[2])
	s4.append(row[3])
	s5.append(row[4])
	s6.append(row[5])

print "got this far 3"

plt.figure(1)
plt.hist(p1)
plt.title('Histogram of planet mass')

plt.figure(2)
plt.hist(p2)
plt.title('Histogram of planet radius')

plt.figure(3)
plt.hist(p3)
plt.title('Histogram of eccentricity')

plt.figure(4)
plt.hist(p4)
plt.title('Histogram of semi-major axis')

plt.figure(5)
plt.hist(p5)
plt.title('Histogram of orbital period')

plt.figure(6)
plt.hist(p6,bins=50)
plt.title('Histogram of inclination')
#plt.xlabel('x2')
#plt.ylabel('x1')
#plt.legend()
plt.show()
