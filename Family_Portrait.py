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

# System parameters

x = []		
y = []
e = []
s = []

plan = loadtxt("Planets.dat", comments="#", delimiter="\t", skiprows=1, usecols=(1,2,3,4,5,6), unpack=False)
for row in plan:
	p1.append(row[0])
	p2.append(row[1])
	p3.append(row[2])
	p4.append(row[3])
	p5.append(row[4])
	p6.append(row[5])


star = loadtxt("Stars.dat", comments="#", delimiter="\t", skiprows=1, usecols=(0,1,2,3,5,6,7), unpack=False)
n1 = star[0,-1]
n2 = star[1,-1]
n3 = star[2,-1]
n4 = star[3,-1]
n5 = star[4,-1]
n6 = star[5,-1]
n7 = star[6,-1]
n8 = star[7,-1]
n9 = star[8,-1]
n10 = star[9,-1]
n11 = star[10,-1]
ncum = int(n1+n2+n3+n4+n5+n6+n7+n8+n9+n10+n11)

x.extend(plan[0:ncum,3])
e.extend(plan[0:ncum,2]*plan[0:ncum,3])
s.extend(plan[0:ncum,1])
for i in range(11):
	for j in range(int(star[i,-1])):
		y.extend([star[i,0]])

for row in star:
	s1.append(row[1])
	s2.append(row[2])
	s3.append(row[3])
	s4.append(row[4])
	s5.append(row[5])
	s6.append(row[6])

while input != "x":
	num = raw_input("Choose a number, to finish input x  \n")
	if num == "x":
		break
	if num == "1":
		plt.figure(1)
		plt.hist(p1,bins=100)
		plt.title('Histogram of planet mass')
		plt.show()
	if num == "2":
		plt.figure(2)
		plt.hist(p2,bins=50)
		plt.title('Histogram of planet radius')
		plt.show()
	if num == "3":
		plt.figure(3)
		plt.hist(p3,bins=50)
		plt.title('Histogram of eccentricity')
		plt.show()
	if num == "4":	
		plt.figure(4)
		plt.hist(p4,bins=np.logspace(np.log10(0.1),np.log10(3),100))
		plt.gca().set_xscale("log")
		plt.title('Histogram of semi-major axis')
		plt.show()
	if num == "5":	
		plt.figure(5)
		plt.hist(p5,bins=np.logspace(np.log10(0.1),np.log10(5000),100))
		plt.gca().set_xscale("log")
		plt.title('Histogram of orbital period')
		plt.show()
	if num == "6":
		plt.figure(6)
		plt.hist(p6,bins=50)
		plt.title('Histogram of inclination')
		plt.show()
	if num == "7":
		plt.figure(7)
		plt.hist(s1,bins=100)
		plt.title('Histogram of star mass')
		plt.show()
	if num == "8":
		plt.figure(8)
		plt.hist(s2,bins=50)
		plt.title('Histogram of metallicity')
		plt.show()
	if num == "9":
		plt.figure(9)
		plt.hist(s3,bins=50)
		plt.title('Histogram of star radius')
		plt.show()
	if num == "10":	
		plt.figure(10)
		plt.hist(s4,bins=100)
		plt.title('Histogram of effective temperature')
		plt.show()
	if num == "11":	
		plt.figure(11)
		plt.hist(s5,bins=100)
		plt.title('Histogram of main sequence lifetime')
		plt.show()
	if num == "12":
		plt.figure(12)
		plt.hist(s6,bins=5)
		plt.title('Histogram of number of planets')
		plt.show()
	if num == "13":
		plt.figure(13)
		def text(x, y, text):
		    plt.text(x,y,text,ha='center',va='top')
		for i in range(0,ncum):
			plt.errorbar(x[i],y[i],xerr=e[i],fmt='o',ms=6*s[i],mew=1)
		plt.title('Family Portrait of systems 1-10 \n with the inner Solar System below for comparison')
		text(0.387,0.5,"M")
		text(0.723,0.5,"V")
		text(1.0,0.5,"E")
		text(1.52,0.5,"M")
		text(5.2,0.5,"J")
		plt.show()
print "Finished"
