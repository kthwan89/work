#!/usr/bin python
#coding: utf-8

import numpy as np

# Module : calculate the ESP on grids
def calc_ESP(Cube_List, Atom_List, Charge_List, ESP_List):
	ini_x, ini_y, ini_z = float(Cube_List[0][1]), float(Cube_List[0][2]), float(Cube_List[0][3])
	Nx, Ny, Nz = int(Cube_List[1][0]), int(Cube_List[2][0]), int(Cube_List[3][0])
	itv = float(Cube_List[1][1])
	Natom = len(Atom_List)

	for i in range(Nx):
		x = ini_x + itv * i

		for j in range(Ny):
			y = ini_y + itv * j

			for k in range(Nz):
				z = ini_z + itv * k

				grid_list = np.array([x, y, z])
				esp = 0
				for t in range(Natom):
					atom_x, atom_y, atom_z = float(Atom_List[t][2]), float(Atom_List[t][3]), float(Atom_List[t][4])
					atom_list = np.array([atom_x, atom_y, atom_z])

					dist = np.linalg.norm(atom_list - grid_list)
					charge = float(Charge_List[t])
					esp_ = charge / dist
					
					esp += esp_

				ESP_List.append(esp)
	
	ESP_List = np.array(ESP_List)
	ESP_List = ESP_List.reshape(Nx * Ny, Nz)

