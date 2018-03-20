#==================================================
# 1. SET-UP
# Calls the required externals (numpy etc)
#==================================================
from random import *
import numpy as np
from numpy import loadtxt
import Seed				# Calls an object creating module for stars
import Seed_Plan			# calls an object creating module for planets
#==================================================

#Testing if this has worked on Git hub too

#==================================================
# 2. CONSTANTS MODULE
# Declares/calls all the constants and sates units
# 2.1 Add variables here as well?
#=================================================
Msun = 1.98850000E+30			#[kg]
# Rsun = 6.95700000E+08			#[m]
# Me   = 5.97240000E+24			#[kg]
# Re   = 6.37100000E+06			#[m]
Day  = 8.64000000E+04			#[s]
AU   = 1.49597871E+11			#[m]
G    = 6.67408000E-11			#[m^3 kg^-1 s^-2]
pi   = np.pi
type_count = [0,0,0,0,0]		# Number of spectral type [A,F,G,K,M]
planet_count = [0,0,0,0,0]		# Number of planets orbiting each star [1,2,3,4,5]
alphabet = ['a','b','c','d','e','f','g','h','i','j']	# Used for planet IDs
count_s = 0
count_p = 0
#=================================================



#==================================================
# 3. STAR GENERATOR
# Generates apopulation of stars. Initally all suns
# 3.1 add options for more than 1 star?
#==================================================
#Currently the Stellar_Popl.dat file has 100 solar clones
#==================================================



#==================================================
# 4. STELLAR PROPERTIES
# Uses the values from 3. to calculate the rest of
# the star's properties (radius, temp, MS lifetime,
# stellar type, etc)
#==================================================
fstar1 = open('Stars.dat','w')
fstar1.write('ID\t' + 'Mass\t' + '[Fe/H]\t' + 'Radius\t' + 'Type\t' + 'Teff\t' + 'Tms\t' + 'Nplan\t' + '\n')
fplan = open('Planets.dat','w')
fplan.write('ID\t' + 'Mass\t' + 'Radius\t' + 'e\t' + 'a\t' + 'Torb\t' + 'Incl\t' + '\n')

N_p_star = loadtxt("Nplan_per_star.dat", comments="#", delimiter="\t",unpack=False)	# Data from Dressing & Charbonneau 2013
cum_freq = N_p_star[-1,-1]
#type_dat = loadtxt("Type.dat", comments="#", delimiter="\t",unpack=False)
f3 = open('Type.dat','r')		# Type categorised by masses
type_line = f3.readlines()
upper = [type_line[1].split()[-1],type_line[2].split()[-1],type_line[3].split()[-1],type_line[4].split()[-1],type_line[5].split()[-1]]
lower = [type_line[1].split()[-2],type_line[2].split()[-2],type_line[3].split()[-2],type_line[4].split()[-2],type_line[5].split()[-2]]


with open('Stellar_Popl.dat') as f1:		# Data file with mass and metallicity for a stellar population
	for line in f1:
		Input = map(float,line.split())
		star = Seed.star
		count_s +=  1
		star.ID = count_s
		star.mass = Input[0]
		star.metal = Input[1]
		star.radius = Input[0]**(3.0/7)	# Relation due to p-p chain fusion
		star.temp = star.mass*5700	# Relation due to 0.43Ms < M* < 2Ms
		star.Tms = 10*star.mass**(-3)	# Relation due to M* ~ Ms
		RaNdOm = randint(1,int(cum_freq))
		for i in range(len(planet_count)):
			if N_p_star[i,2] < RaNdOm <= N_p_star[i+1,2]:	
				star.Nplan = N_p_star[i+1,0]	
				if (i+1) == int(star.Nplan):
					planet_count[i] += 1
			if lower[i] < str(star.mass) <= upper[i]:
				star.type = type_line[i+1].split()[0]
				type_count[i] += 1 
		fstar1.write(star.description() + '\n')
print "Stellar type count =",type_count 	# Redundant atm as they're all sun clones
print "Planet count =",planet_count
f1.close()
fstar1.close()
#==================================================



#==================================================
# 5. PLANET MULTIPLICITY
# Determines the number of planets (Nplan) orbiting
# the seed star
# 5.1 as almost all work is biased towards planets
# with short periods, add a random factor to
# include planets with periods outside the scope of
# those in research
#==================================================
#==================================================



#==================================================
# 6/7. PLANET PARAMETERS
# For each planet, uses probability functions to 
# determine masses and radii. From there can
# compute density
#==================================================
# a,b,c,d... = Naming system for the planets
# M = Mass of planet
# Ra = Radius of planet 'a'
# Da = Density of planet 'a'
#==================================================
#fstar2 = open('Stars.dat','r').readlines()
#star_ID = []
#star_mass = []
#star_Nplan = []
#plan_ID = []
#plan = Seed_Plan.plan
#for i in range(len(fstar2)-1):
#	star_ID.append(fstar2[i+1].split()[0])
#	star_mass.append(fstar2[i+1].split()[1])
#	star_Nplan.append(fstar2[i+1].split()[-1])
#star_ID = np.array(star_ID)
#star_mass = map(float, np.array(star_mass)[:])
#star_Nplan = np.array(star_Nplan)
#for i in range(len(fstar2)-1):
#	n = 0
#	while n in range(int(star_Nplan[i])):
#		plan.ID = str(star_ID[i]) + alphabet[n]
#		plan.mass = randint(1,20)*1.0/randint(1,19)
#		plan.radius = plan.mass*3.0*random()
#		plan.ecc = random()
#		plan.sm_axis = random()+0.1
#		plan.t_orb = ((4*pi*(AU*plan.sm_axis)**3/(G*Msun*star_mass[i]))**0.5)/(Day)
#		plan.incl = 180*(random()-0.5)
#		n += 1
#		fplan.write(plan.description() + '\n')
#		count_p += 1
#print count_p
#fplan.close()
#==================================================



#==================================================
# 6/7. ORBIT PARAMETERS
# For each planet, uses probability functions to
# attribute them with their orbital characteristics
# (eccentricity, semi-major axis/period, 
# inclination)
#==================================================
# Ea = Eccentricity of planet 'a's orbit
# Aa = Semi-major axis of planet 'a's orbit
# Torba = Orbital period of planet 'a'
# Ia = Planet 'a's orbit's inclination as seen from Earth
#==================================================



#==================================================
# 9. STABILITY TEST
# Tests the stability of the generated system.
# Should be stable for approx. MS lifetime of host
# star.
#==================================================
