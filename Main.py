#==================================================
# 1. SET-UP
# Calls the required externals (numpy etc)
#==================================================
import Seed_Star			# Calls an object creating module for stars
import Seed_Plan			# calls an object creating module for planets

planet_count = [0,0,0,0,0]		# Number of planets orbiting each star [1,2,3,4,5]
alphabet = ['a','b','c','d','e']	# Used for planet IDs
count_s = 0				# Star counter
count_p = 0				# Planet counter
#=================================================



#==================================================
# 2. STELLAR PROPERTIES
# Generates a star with all necessary parameters
# from a stellar population consisting of masses
# and metallicity.
# The number of planets orbiting the star is
# simulated. Each of the planets is then given its
# own ID, mass, etc.
# Both the star and planet data is written into 
# relevant .dat files.
# The next star is generated, repeating the cycle.
#==================================================
star = Seed_Star.star
star.open_dat_file()
plan = Seed_Plan.plan
plan.open_dat_file()

for line in open('Stellar_Popl.dat'):
	s_mass = star.get_mass(count_s)
	s_metal = star.get_metal(count_s)
	s_radius = star.get_radius(count_s)
	s_temp = star.get_temp(count_s)
	s_Tms = star.get_Tms(count_s)
	s_type = star.get_type(count_s)
	s_ID = count_s + 1
	s_Nplan = int(star.get_Nplan())
	k = 0
	while k in range(int(s_Nplan)):
		p_ID = str(s_ID) + alphabet[k]
		p_mass = plan.get_mass(s_type)
		p_radius = plan.get_radius(p_mass)
		p_ecc = plan.get_ecc()
		p_sm_axis = plan.get_sm_axis(p_radius) 
		p_t_orb = plan.get_t_orb(p_sm_axis,s_mass)
		p_incl = plan.get_incl()
		count_p += 1
		if (k+1) == int(s_Nplan):
			planet_count[k] += 1
		k += 1
		plan.write(p_ID,p_mass,p_radius,p_ecc,p_sm_axis,p_t_orb,p_incl)
	star.write(s_ID,s_mass,s_metal,s_radius,s_type,s_temp,s_Tms,s_Nplan)
	count_s +=  1
print "Number of stars =",count_s
print "Stellar type count =",star.get_type_count()
print "Number of planets =",count_p
print "Planetary system type count =",planet_count
star.close()
plan.close()

plot = raw_input("Plot? (y/n) \n")
if plot == "y":
	exec(open("Family_Portrait.py").read())
#==================================================



#==================================================
# 5. STABILITY TEST
# Tests the stability of the generated system.
# Should be stable for approx. MS lifetime of host
# star.
#==================================================
