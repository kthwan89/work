#!/usr/bin python
# coding:utf-8

import math

AUG_PER_AU = 0.529177721092
AU_PER_AUG = 1/AUG_PER_AU


########################################################
############ Module : calculate the distance ###########
########################################################
def calcdis(x1,y1,z1, x2,y2,z2):
	temp = float((x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2)
	distance = math.sqrt(temp)
	return distance


########################################################
############ Module : write the list of Atom_List ######
########################################################
def read_pdb_file(fr, Atom_List=[]):

	for line in fr:
		s = line.lstrip()
		elements = s[:-1].split()

		if len(elements) == 5:

			Atom_List.append(elements)

		else:
			pass


########################################################
######### Module : write the list of Mulliken Charge ###
########################################################
def read_mulliken_file(fr, Mulliken_List):
	Natom = 134
	mulliken_file = tuple(fr)

	for j in range(Natom):
		split_mulliken_file = mulliken_file[j+1].split()
		
		mulliken_charge = float(split_mulliken_file[3])
	
		Mulliken_List[j] =  mulliken_charge


##########################################
###### Module : read the charge file  ####
##########################################
def read_charge_file(fr, Charge_List):

	for line in fr:
		s = line.lstrip()
		elements = s[:-1].split()

		if len(elements) == 2:

			Charge_List.append(float(elements[1]))

		else:
			pass

	fr.close()


############################################
### Module : calculate the Dipole Moment ###
############################################
def calculate_Dipole_Moment(Atom_List, Charge_List):
	Natom = len(Atom_List)

	Dx = 0
	Dy = 0
	Dz = 0
	for j in range(Natom):

		Atom_x = float(Atom_List[j][5]) 
		Atom_y = float(Atom_List[j][6]) 
		Atom_z = float(Atom_List[j][7]) 

		Charge = float(Charge_List[j])

		Dx += Atom_x * Charge
		Dy += Atom_y * Charge
		Dz += Atom_z * Charge

	DP = math.sqrt(Dx**2 + Dy**2 + Dz**2)

	DP_debye = DP * (1.602176565*10**-29) / (3.33564 * 10**-30)

	return DP_debye












