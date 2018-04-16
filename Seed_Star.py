from random import *
from numpy import loadtxt

type_count = [0,0,0,0,0]								# Number of each spectral type [A,F,G,K,M]
Star_Popl_dat = loadtxt("Stellar_Popl.dat", comments="#", delimiter="\t", unpack=False)	# Sample population from exoplanet.eu
N_p_star = loadtxt("Nplan_per_star.dat", comments="#", delimiter="\t",unpack=False)	# Data from Dressing & Charbonneau 2013
cum_freq = N_p_star[-1,-1]
type_dat = loadtxt("Type.dat", comments="#", dtype='S4', delimiter="\t",unpack=False)	#########################################


class Seed:
	ID = 0						# Identification number 
	def get_mass(self,i):				# Measured in solar masses
		return Star_Popl_dat[i,0]
	def get_metal(self,i):				# [Fe/H]
		return Star_Popl_dat[i,1]
	def get_radius(self,i):				# Measured in solar radii
		return Star_Popl_dat[i,0]**(3.0/7)	# Relation due to p-p chain fusion
	def get_type(self,i):				# Spectral type
		for n in range(5):
			if type_dat[n,1] < str(Star_Popl_dat[i,0]) <= type_dat[n,2]:
				type_count[n] += 1 
				return type_dat[n,0]
	def get_temp(self,i):				# Effective temperature
		return Star_Popl_dat[i,0]*5700		# Relation due to 0.43Ms < M* < 2Ms
	def get_Tms(self,i):				# Main Sequence Lifetime in Giga-years
		return 10*Star_Popl_dat[i,0]**(-3)	# Relation due to M* ~ Ms
	def get_Nplan(self):				# Number of planets hosted by star
		rand_int = randint(1,int(cum_freq))
		for m in range(5):
			if N_p_star[m,2] < rand_int <= N_p_star[m+1,2]:	
				return N_p_star[m+1,0]	
	def get_type_count(self):
		return type_count
	def description(self):
#		desc_str = "%d\t%4.2f\t%4.2f\t%4.2f\t%s\t%d\t%5.3f\t%.1s" % (self.ID, self.get_mass, self.get_metal, self.radius, self.type, self.temp, self.Tms, self.Nplan)
		desc_str = "%d\t%4.2f\t%4.2f" % (self.ID, self.get_mass, self.get_metal)
		return desc_str
star = Seed()

