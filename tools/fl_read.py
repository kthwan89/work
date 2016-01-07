#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
try:
	import msgpack
except:
	import msgpack_pure as msgpack

##################################
### Module : read the pdb file ###
##################################
def read_pdb_file(fr):

	Atom_List = []
	for line in fr:
		s = line.lstrip()
		elements = s[:-1].split()

		if len(elements) >= 8:

			Atom_List.append(elements)

		else:
			pass
	return Atom_List

def read_pdb_msg_file(fr):
	
	msg_data = msgpack.unpackb(fr.read())
	Atom_List = msg_data["atoms"]
	
	return Atom_List


###########################################
### Module : read the mulliken.txt file ###
###########################################
def read_mulliken_file(fr):

	Mulliken_List = []
	for line in fr:
		s = line.lstrip()
		elements = s[:-1].split()

		if len(elements) == 0 or elements[1] == "X":
			continue

		try:
			elements[0] = int(elements[0])

		except ValueError:
			continue

		if len(elements) == 4:

			Mulliken_Charge = float(elements[3])
			
			Mulliken_List.append(Mulliken_Charge)
	return Mulliken_List

def read_mulliken_msg_file(fr):

	data = msgpack.unpackb(fr.read())
	Mulliken_List = data["mulliken"]

	return Mulliken_List


###################################
### Module : read the grid file ###
###################################
def read_grid_file(fr, Grid_List=[]):

	for line in fr:
		
		s = line.lstrip()
		elements = s[:-1].split()
	
		if len(elements) == 3:

			if ">>>>" not in elements[0]:
				
				Grid_List.append(elements)

		else:
			pass


def read_grid_msg_file(fr):

	grid_data = msgpack.unpackb(fr.read())
	Grid_List = grid_data["grids"]

	return Grid_List


##################################
### Module : read the esp file ###
##################################
def read_esp_file(fr, Grid_List, ESP_List):
	Ngrid = len(Grid_List)

	fr = tuple(fr)
	for i in range(Ngrid):
		elements = fr[i+1].split()
		QM_ESP = float(elements[1])
		ESP_List.append(QM_ESP)


def read_esp_msg_file(fr):

	esp_data = msgpack.unpackb(fr.read())
	ESP_List = esp_data["ESP"]

	return ESP_List


##################################
### Module : read the esp file ###
##################################
def read_cube_file(fr, Cube_List=[], Atom_List=[], Counter_Chg=[], QM_ESP_List=[]):

	for line in fr:
		s = line.lstrip()
		elements = s[:-1].split()

		try:
			elements[0] = int(elements[0])

			if len(elements) == 4:
				Cube_List.append(elements)
				
			elif len(elements) == 5 and int(elements[0]) != 0:
				Atom_List.append(elements)

			elif len(elements) == 5 and int(elements[0]) == 0:
				Counter_Chg.append(elements)

		except ValueError:
			
			try:
				elements[0] = float(elements[0])
				QM_ESP_List.append(elements)
			
			except ValueError:
				pass
	

#####################################
### Module : read the charge file ###
#####################################
def read_charge_file(fr, Charge_List=[]):

	for line in fr:
		s = line.lstrip()
		elements = s[:-1].split()

		if len(elements) == 5:
			Charge_List.append(float(elements[4]))
		
		else:
			pass


def read_charge_msg_file(fr, charge):

	data = msgpack.unpackb(fr.read())
	
	Charge_List = data[charge]

	return Charge_List


