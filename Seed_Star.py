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

star = Seed()
