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

plan = Seed_Plan.plan
star = Seed_Star.star

for line in open('Stellar_Popl.dat'): #f1:
	star_mass = star.get_mass(count_s)
	star_metal = star.get_metal(count_s)
	star_radius = star.get_radius(count_s)
	star_temp = star.get_temp(count_s)
	star_Tms = star.get_Tms(count_s)
	star_type = star.get_type(count_s)
	count_s +=  1
	star_ID = count_s
	star_Nplan = star.get_Nplan()
	k = 0
	while k in range(int(star_Nplan)):
		plan_ID = str(star_ID) + alphabet[k]
		plan_mass = plan.get_mass(star_type)
		plan_radius = plan.get_radius(plan_mass)
		plan_ecc = plan.get_ecc()
		plan_sm_axis = plan.get_sm_axis(plan_radius) 
		plan_t_orb = plan.get_t_orb(plan_sm_axis,star_mass)
		plan_incl = plan.get_incl()
		count_p += 1
		if (k+1) == int(star_Nplan):
			planet_count[k] += 1
		k += 1

		print plan_ID,plan_mass,plan_radius,plan_ecc,plan_sm_axis,plan_t_orb,plan_incl

#		fplan.write(plan.description() + '\n')
#	fstar1.write(star.description() + '\n')
print "Number of stars =",count_s
print "Stellar type count =",star.get_type_count()
print "Number of planets =",count_p
print "Planetary system type count =",planet_count
fstar1.close()
fplan.close()
#==================================================



#==================================================
# 5. STABILITY TEST
# Tests the stability of the generated system.
# Should be stable for approx. MS lifetime of host
# star.
#==================================================
