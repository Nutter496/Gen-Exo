f1 = open('Stellar_Popl.dat')
line = f1.readline()
Input = map(float,line.split())
class Seed:
	ID = 0			# Identification number 
	mass = ""		# Measured in solar masses
	metal = "" 		# [Fe/H]
	radius = ""		# Measured in solar radii
	type = ""		# Spectral type
	temp = ""		# Effective temperature measured in Kelvin
	Tms = ""		# Main Sequence Lifetime in Giga-years
	Nplan = ""		# Number of planets
	def description(self):
		desc_str = "%d\t%4.2f\t%4.2f\t%4.2f\t%s\t%d\t%5.3f\t%.1s" % (self.ID, self.mass, self.metal, self.radius, self.type, self.temp, self.Tms, self.Nplan)
		return desc_str
	def starmass():
		return float(Input[0])		# Taken a sample from exoplant.eu catalog
	print starmass()

star = Seed()

#	star.metal = Input[1]		# Taken a sample from exoplanet.eu catalog
#	star.radius = Input[0]**(3.0/7)	# Relation due to p-p chain fusion
#	star.temp = star.mass*5700	# Relation due to 0.43Ms < M* < 2Ms
#	star.Tms = 10*star.mass**(-3)	# Relation due to M* ~ Ms

