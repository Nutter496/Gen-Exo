#==================================================
# 1. SET-UP
# Calls the required externals (numpy etc)
#==================================================
from random import *
import numpy as np
from numpy import loadtxt
import Seed_Star			# Calls an object creating module for stars
import Seed_Plan			# calls an object creating module for planets
#==================================================



#==================================================
# 2. CONSTANTS MODULE
# Declares/calls all the constants and states units
#=================================================
Msun = 1.98850000E+30			#[kg]
Rsun = 6.95700000E+08			#[m]
# Me   = 5.97240000E+24			#[kg]
# Re   = 6.37100000E+06			#[m]
Day  = 8.64000000E+04			#[s]
AU   = 1.49597871E+11			#[m]
G    = 6.67408000E-11			#[m^3 kg^-1 s^-2]
pi   = np.pi
type_count = [0,0,0,0,0]		# Number of spectral type [A,F,G,K,M]
planet_count = [0,0,0,0,0]		# Number of planets orbiting each star [1,2,3,4,5]
alphabet = ['a','b','c','d','e']	# Used for planet IDs
count_s = 0
count_p = 0
#=================================================



#==================================================
# 3. STAR GENERATOR
# Generates apopulation of stars.
#==================================================
#==================================================



#==================================================
# 4. STELLAR PROPERTIES
# Uses the values from 3. to calculate the rest of
# the star's properties (radius, temp, MS lifetime,
# stellar type, etc)
#==================================================
fstar1 = open('Stars.dat','w')			# Opens file for the data on the stars from the given stellar populations
fstar1.write('ID\t' + 'Mass\t' + '[Fe/H]\t' + 'Radius\t' + 'Type\t' + 'Teff\t' + 'Tms\t' + 'Nplan\t' + '\n')
fplan = open('Planets.dat','w')			# Opens file for the data on the exoplanets
fplan.write('ID\t' + 'Mass\t' + 'Radius\t' + 'e\t' + 'a\t' + 'Torb\t' + 'Incl\t' + '\n') # Worth putting in Seed.py & Seed_Plan.py?

N_p_star = loadtxt("Nplan_per_star.dat", comments="#", delimiter="\t",unpack=False)	# Data from Dressing & Charbonneau 2013
cum_freq = N_p_star[-1,-1]
type_dat = loadtxt("Type.dat", comments="#", dtype='S4', delimiter="\t",unpack=False)
MR_rel_dat = loadtxt("MR_Relation.dat", comments="#", delimiter="\t", unpack=False)


plan = Seed_Plan.plan
star = Seed_Star.star

with open('Stellar_Popl.dat') as f1:		# Data file with mass and metallicity for a stellar population
	for line in f1:
		Input = map(float,line.split())
		count_s +=  1
		star.ID = count_s
#		star.mass = Input[0]
		star.starmass
#		star.metal = Input[1]
		print star.starmass
#		star.radius = str(star.mass)**(3.0/7)	# Relation due to p-p chain fusion
#		star.temp = star.mass*5700	# Relation due to 0.43Ms < M* < 2Ms
#		star.Tms = 10*star.mass**(-3)	# Relation due to M* ~ Ms
#		RaNdOm = randint(1,int(cum_freq))
#		for i in range(len(planet_count)):
#			if N_p_star[i,2] < RaNdOm <= N_p_star[i+1,2]:	
#				star.Nplan = N_p_star[i+1,0]	
#				n = 0
#				while n in range(int(star.Nplan)):
#					plan.ID = str(star.ID) + alphabet[n]
#					if star.type == 'K' or star.type == 'M':
#						plan.mass = 0.01+random()*2	# Small stars more liekly to have small planets
#					else:
#						plan.mass = 0.1+random()*3	# Large stars less likely to have small planets
#					if MR_rel_dat[0,0] < plan.mass <= MR_rel_dat[1,0]:
#						plan.radius = plan.mass**MR_rel_dat[0,1]*2*MR_rel_dat[0,3]*random()+(1-MR_rel_dat[0,3])
#					elif MR_rel_dat[1,0] < plan.mass <= MR_rel_dat[2,0]:
#						plan.radius = plan.mass**MR_rel_dat[1,1]*2*MR_rel_dat[1,3]*random()+(1-MR_rel_dat[1,3])
#					plan.ecc = np.exp(-4.519*random())	# Adapted from exoplanet.eu catalog
#					rand0 = random()
#					plan.sm_axis = 100*rand0**2*np.exp(-0.5*(5*rand0)**2)+2*star.radius*Rsun/AU 
#					plan.t_orb = ((4*pi*(AU*plan.sm_axis)**3/(G*Msun*star.mass))**0.5)/(Day)
#					plan.incl = 180*(random()-0.5)	# Plan to leave this, could make it more gaussian/normal dist
#					n += 1
#					fplan.write(plan.description() + '\n')
#					count_p += 1
#				if (i+1) == int(star.Nplan):
#					planet_count[i] += 1
#			if type_dat[i,1] < str(star.mass) <= type_dat[i,2]:
#				star.type = type_dat[i,0]
#				type_count[i] += 1 
#		fstar1.write(star.description() + '\n')
print "Stellar type count =",type_count
print "Planet count =",planet_count
print "count_p =",count_p
fstar1.close()
fplan.close()
#==================================================



#==================================================
# 5. STABILITY TEST
# Tests the stability of the generated system.
# Should be stable for approx. MS lifetime of host
# star.
#==================================================
