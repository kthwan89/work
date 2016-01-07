#!/usr/bin/python
#-*-coding:utf-8-*-

import lebedev
import basic_mk

def generate_All_Grid_List(Atom_List, layer_number):
	All_Grid_List = []
	Natom = len(Atom_List)

	for j in range(Natom):
		List = []

		Atom_Number = Atom_List[j][1]
		Atom_Type = Atom_List[j][2]
		Atom_x = float(Atom_List[j][5])
		Atom_y = float(Atom_List[j][6])
		Atom_z = float(Atom_List[j][7])

		if "C" in Atom_Type or "N" in Atom_Type:

			radian = 1.5

			if layer_number == 1:
				lebedev.Grid_74(List)

			elif layer_number == 2:
				lebedev.Grid_74(List)

			elif layer_number == 3:
				lebedev.Grid_110(List)

			elif layer_number == 4:
				lebedev.Grid_146(List)

			basic_mk.expand_point(List, radian, layer_number)
			basic_mk.move_point(List, Atom_x, Atom_y, Atom_z)
			
		elif "H" in Atom_Type and "OH" not in Atom_Type:

			radian = 1.2
			
			if layer_number == 1:
				lebedev.Grid_38(List)
			
			elif layer_number == 2:
				lebedev.Grid_50(List)
			
			elif layer_number == 3:
				lebedev.Grid_74(List)
			
			elif layer_number == 4:
				lebedev.Grid_74(List)

			basic_mk.expand_point(List, radian, layer_number)
			basic_mk.move_point(List, Atom_x, Atom_y, Atom_z)

		elif "O" in Atom_Type:

			radian = 1.4
			
			if layer_number == 1:
				lebedev.Grid_50(List)
				
			elif layer_number == 2:
				lebedev.Grid_74(List)
				
			elif layer_number == 3:
				lebedev.Grid_86(List)
				
			elif layer_number == 4:
				lebedev.Grid_110(List)
			
			basic_mk.expand_point(List, radian, layer_number)
			basic_mk.move_point(List, Atom_x, Atom_y, Atom_z)

		elif "S" in Atom_Type:
			
			radian = 1.75  
			
			if layer_number == 1:
				lebedev.Grid_86(List)
				
			elif layer_number == 2:
				lebedev.Grid_110(List)
				
			elif layer_number == 3:
				lebedev.Grid_146(List)
				
			elif layer_number == 4:
				lebedev.Grid_170(List)
			
			basic_mk.expand_point(List, radian, layer_number)
			basic_mk.move_point(List, Atom_x, Atom_y, Atom_z)

		for i in range(len(List)):
			List[i] += [j+1, layer_number]

		All_Grid_List += List
	return All_Grid_List


def position_check(Atom_List, All_Grid_List, layer_number):
	Grid_List = []
	Natom = len(Atom_List)
	Ngrid = len(All_Grid_List)

	for i in range(Ngrid):
		Grid_x = float(All_Grid_List[i][0])
		Grid_y = float(All_Grid_List[i][1])
		Grid_z = float(All_Grid_List[i][2])

		for j in range(Natom):
			Atom_Number = Atom_List[j][1]
			Grid_Number = All_Grid_List[i][3]
#			print Atom_Number, Grid_Number
			if Atom_Number != Grid_Number:
				Atom_Type = Atom_List[j][2]
				Atom_x = float(Atom_List[j][5])
				Atom_y = float(Atom_List[j][6])
				Atom_z = float(Atom_List[j][7])

				distance = basic_mk.calcdis(Grid_x, Grid_y, Grid_z, Atom_x, Atom_y, Atom_z)

				if distance > 7.0:
					pass

				if "C" in Atom_Type or "N" in Atom_Type:
					radian = 1.5

				elif "H" in Atom_Type and "OH" not in Atom_Type:
					radian = 1.2

				elif "O" in Atom_Type:
					radian = 1.4
			
				elif "S" in Atom_Type:
					radian = 1.75
			
				layer_distance = radian * (1.2 + 0.2 * layer_number)
	#			print distance - layer_distance
				if distance - layer_distance < -1e-10:
					break

				if j == Natom-1:
					Grid_List.append((Grid_x, Grid_y, Grid_z))
	
	return Grid_List
