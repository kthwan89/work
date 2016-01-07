#!/usr/bin/env python
# -*- coding: utf-8 -*-

import grid_basic
import numpy as np


### Parameter : vdW radii ###
C_rad = 1.50
H_rad = 1.45
O_rad = 1.70
N_rad = 1.70
S_rad = 2.00


### Module : find the maximum and minimum ###
def range_List(Atom_List):
	range_List=[]
	Natom = len(Atom_List)

	x_List = []
	y_List = []
	z_List = []

	for j in range(Natom):

		x = float(Atom_List[j][5])
		y = float(Atom_List[j][6])
		z = float(Atom_List[j][7])

		x_List.append(x)
		y_List.append(y)
		z_List.append(z)

	
	max_x, min_x = max(x_List), min(x_List)
	max_y, min_y = max(y_List), min(y_List)
	max_z, min_z = max(z_List), min(z_List)


	range_List.append(max_x + 2.8)
	range_List.append(min_x - 2.8)
	range_List.append(max_y + 2.8)
	range_List.append(min_y - 2.8)
	range_List.append(max_z + 2.8)
	range_List.append(min_z - 2.8)
	return range_List

### Module : calculate the all grid points ###
def CHELPG_List_all(range_List):
	all_grid_List = []

	max_x, min_x = float(range_List[0]), float(range_List[1])
	max_y, min_y = float(range_List[2]), float(range_List[3])
	max_z, min_z = float(range_List[4]), float(range_List[5])

#Important:::: grid_itv means the distance betweeen grids
	grid_itv = 5.0 
	print "grid_interval is %4.2f angstrom"%grid_itv

	Nx_itv = int((max_x - min_x) // grid_itv)
	Ny_itv = int((max_y - min_y) // grid_itv)
	Nz_itv = int((max_z - min_z) // grid_itv)

	
	for x in range(Nx_itv +1):

		for y in range(Ny_itv +1):

			for z in range(Nz_itv +1):

				grid_x = min_x + x * grid_itv
				grid_y = min_y + y * grid_itv
				grid_z = min_z + z * grid_itv

				temp = [[round(grid_x, 3), round(grid_y, 3), round(grid_z, 3)]]

				all_grid_List += temp
	
	return all_grid_List


### Module : calculate the CHELPG grid points ###
def CHELPG_List(Atom_List, all_grid_List):
	chelpg_List=[]

	Natom = len(Atom_List)
	Ngrid = len(all_grid_List)

	for i in range(Ngrid):

		grid_xyz = np.array(all_grid_List[i])

		shortest_atom_index = grid_basic.shortest_atom(grid_xyz, Atom_List)

		atom_xyz = np.array(Atom_List[shortest_atom_index][5:])
		atom_xyz = map(float, atom_xyz)
		shortest_dist = np.linalg.norm(grid_xyz - atom_xyz)
		
		shortest_atom_type = str(Atom_List[shortest_atom_index][2])
		vdW_radius = grid_basic.radii(shortest_atom_type)

		if shortest_dist < 2.8 and shortest_dist > vdW_radius:

			chelpg_List.append(grid_xyz)

	return chelpg_List



