class Seed_Plan:
	ID = 0			# Identification number 
	mass = ""		# Measured in Earth masses
	radius = ""		# Measured in Earth radii
	ecc = ""		# Orbital eccentricity
	sm_axis = ""		# Semi-major axis of orbit
	t_orb = ""		# Orbital period
	incl = ""		# Orbital inclination as seen from Earth
	def description(self):
		desc_str = "%s\t%4.2f\t%4.2f\t%4.3f\t%4.3f\t%4.2f\t%4.2f" % (self.ID, self.mass, self.radius, self.ecc, self.sm_axis, self.t_orb, self.incl)
#		desc_str = "%r\t%4.2f\t%4.2f\t%4.3f\t%5.2f\t%5.2f\t%5.3f" % (self.ID, self.mass, self.radius, self.ecc, self.sm_axis, self.t_orb, self.incl)
		return desc_str

plan = Seed_Plan()
