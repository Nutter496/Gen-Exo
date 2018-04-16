from random import *
import numpy as np
from numpy import loadtxt
Msun = 1.98850000E+30							# Solar mass [kg]
Rsun = 6.95700000E+08							# Solar radius [m]
AU   = 1.49597871E+11							# Astronomical unit [m]
Day  = 8.64000000E+04							# One earth day [s]
G    = 6.67408000E-11							# Gravitational constant [m^3 kg^-1 s^-2]
pi   = np.pi
MR_rel_dat = loadtxt("MR_Relation.dat", comments="#", delimiter="\t", unpack=False)

class Seed_Plan:
	ID = 0								# Identification number 
	def get_mass(self,star_type):
		if star_type == 'K' or star_type == 'M':
			return 0.01+random()*2				# Small stars more liekly to have small planets
		else:
			return 0.1+random()*3				# Large stars less likely to have small planets
	def get_radius(self,mass):					# Measured in Earth radii
		if MR_rel_dat[0,0] < mass <= MR_rel_dat[1,0]:
			return mass**MR_rel_dat[0,1]*2*MR_rel_dat[0,3]*random()+(1-MR_rel_dat[0,3])
		elif MR_rel_dat[1,0] < mass <= MR_rel_dat[2,0]:
			return mass**MR_rel_dat[1,1]*2*MR_rel_dat[1,3]*random()+(1-MR_rel_dat[1,3])
	def get_ecc(self):						# Orbital eccentricity
		return np.exp(-4.519*random())				# Adapted from exoplanet.eu catalog
	def get_sm_axis(self,radius):					# Semi-major axis of orbit measured in AU
		rand0 = random()
		return 100*rand0**2*np.exp(-0.5*(5*rand0)**2)+2*radius*Rsun/AU 
	def get_t_orb(self,a,star_mass):				# Orbital period measured in days
		return ((4*pi*(AU*a)**3/(G*Msun*star_mass))**0.5)/(Day)
	def get_incl(self):						# Orbital inclination as seen from Earth
		return 180*(random()-0.5)				# Plan to leave this, could make it more gaussian/normal dist
	def description(self):
		desc_str = "%s\t%4.2f\t%4.2f\t%4.3f\t%4.3f\t%4.2f\t%4.2f" % (self.ID, self.get_mass, self.get_radius, self.get_ecc, self.get_sm_axis, self.get_t_orb, self.get_incl)
		return desc_str

plan = Seed_Plan()

#		plan.ecc = np.exp(-4.519*random())	# Adapted from exoplanet.eu catalog
#		plan.t_orb = ((4*pi*(AU*plan.sm_axis)**3/(G*Msun*star_mass))**0.5)/(Day)
#		plan.incl = 180*(random()-0.5)	# Plan to leave this, could make it more gaussian/normal dist
#		fplan.write(plan.description() + '\n')
#		count_p += 1
