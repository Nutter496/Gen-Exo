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
fplan = open('Planets.dat','w')			# Opens file for the data on the exoplanets


class Seed_Plan:
	def open_dat_file(self):
		fplan.write('ID\t'+'Mass\t'+'Radius\t'+'e\t'+'a\t'+'Torb\t'+'Incl\t'+'\n') 
		fplan.write('Mer\t'+'0.0553\t'+'0.383\t'+'0.205\t'+'0.387\t'+'88.0\t'+'7.0\t'+'\n')
		fplan.write('Ven\t'+'0.815\t'+'0.949\t'+'0.007\t'+'0.723\t'+'224.7\t'+'3.4\t'+'\n')
		fplan.write('Ear\t' + '1.0\t' + '1.0\t' + '0.017\t' + '1.0\t' + '365.2\t' + '0.0\t' + '\n')
		fplan.write('Mar\t'+'0.107\t'+'0.2724\t'+'0.094\t'+'1.52\t'+'687.0\t'+'1.9\t'+'\n')
		fplan.write('Jup\t'+'317.8\t'+'11.21\t'+'0.049\t'+'5.2\t'+'4331\t'+'1.3\t'+'\n')
	ID = 0								# Identification number 
	def get_mass(self,star_type):
		if star_type == 'K' or star_type == 'M':
			return 0.01+random()*2				# Small stars more liekly to have small planets
		else:
			return 0.1+random()*3				# Large stars less likely to have small planets
	def get_radius(self,mass):					# Measured in Earth radii
		if MR_rel_dat[0,0] < mass <= MR_rel_dat[1,0]:
			return mass**MR_rel_dat[0,1]*(1+2*MR_rel_dat[0,3]*(0.5-random()))+MR_rel_dat[0,2]
		elif MR_rel_dat[1,0] < mass <= MR_rel_dat[2,0]:
			return mass**MR_rel_dat[1,1]*(1+2*MR_rel_dat[1,3]*(0.5-random()))+MR_rel_dat[1,2]
	def get_ecc(self):						# Orbital eccentricity
		return np.exp(-4.519*random())				# Adapted from exoplanet.eu catalog
	def get_sm_axis(self,radius):					# Semi-major axis of orbit measured in AU
		rand0 = random()
		sma = 100*rand0**2*np.exp(-0.5*(5*rand0)**2)+2*radius*Rsun/AU
		return sma 
	def get_t_orb(self,a,star_mass):				# Orbital period measured in days
		return ((4*pi*(AU*a)**3/(G*Msun*star_mass))**0.5)/(Day)
	def get_incl(self):						# Orbital inclination as seen from Earth
		return 180*(random()-0.5)
	def description(self,ID,mas,rad,ecc,sma,torb,inc):
		desc_str = "%s\t%4.2f\t%4.2f\t%4.3f\t%4.3f\t%4.2f\t%4.2f\t" % (ID,mas,rad,ecc,sma,torb,inc)
		return desc_str
	def write(self,ID,mas,rad,ecc,sma,torb,inc):
		fplan.write(plan.description(ID,mas,rad,ecc,sma,torb,inc) + '\n')
	def close(self):
		fplan.close()

plan = Seed_Plan()


