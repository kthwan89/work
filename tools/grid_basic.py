#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import basic

### Parameter : vdW radii ###
C_rad = 1.50
H_rad = 1.45
O_rad = 1.70
N_rad = 1.70
S_rad = 2.00


### Module : find the shortest distance ###
def shortest_atom(grid_xyz, Atom_List):
	Natom = len(Atom_List)

	index = 0
	shortest_dist = 10.0
	for j in range(Natom):
		atom_xyz = np.array(Atom_List[j][5:])
		atom_xyz = map(float, atom_xyz)
		
		dist = np.linalg.norm(grid_xyz - atom_xyz)

		if shortest_dist > dist:

			shortest_dist = dist
			index = j

	return index


### Module : find the vdW radius ###
def radii(atom_type):
	
	if "C" in atom_type:
		radius = C_rad
	
	elif "H" in atom_type and "OH" not in atom_type:
		radius = H_rad
		
	elif "O" in atom_type:
		radius = O_rad
		
	elif "N" in atom_type:
		radius = N_rad
		
	elif "S" in atom_type:
		radius = S_rad

	return radius


