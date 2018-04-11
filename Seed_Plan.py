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
		return desc_str

plan = Seed_Plan()

#	plan.mass = 0.01+random()*2	# Small stars more liekly to have small planets
#	plan.mass = 0.05+random()*3	# Large stars less likely to have small planets
#	plan.radius = plan.mass**MR_rel_dat[0,1]*2*MR_rel_dat[0,3]*random()+(1-MR_rel_dat[0,3])	# Low mass planet
#	plan.radius = plan.mass**MR_rel_dat[1,1]*2*MR_rel_dat[1,3]*random()+(1-MR_rel_dat[1,3])	# High mass planet
#	plan.ecc = np.exp(-4.519*random())	# Adapted from exoplanet.eu catalog
#	plan.sm_axis = (2.0/pi)**0.5*random()**2*np.exp(-0.5*random()**2)+2*star.mass*Rsun/AU	# 
#	plan.t_orb = ((4*pi*(AU*plan.sm_axis)**3/(G*Msun*star.mass))**0.5)/(Day)
#	plan.incl = 180*(random()-0.5)	# Uniform distribtuion
