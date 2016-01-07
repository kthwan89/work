# coding:utf-8

import numpy as np
try:
	import msgpack
except:
	import msgpack_pure as msgpack

### Module : write Charge ###
def write_charge(fw, Atom_List, Charge_List, RRMS):
	
	fw.write(">>>>charge" + "\n")

	Natom = len(Atom_List)
	for j in range(Natom):

		atom_number = int(Atom_List[j][1])
		atom_type = Atom_List[j][2]
		residue_name = Atom_List[j][3]
		residue_number = int(Atom_List[j][4])
		charge = float(Charge_List[j])

		fw.write("%5d"%atom_number + "%6s"%atom_type + "%6s"%residue_name + "%5d"%residue_number + "%10.2f"%charge + "\n")

	fw.write("\n" + ">>>>RRMS : %0.6f"%RRMS)


### Module : write Charge ###
def MSE(X, Y, Charge):
	ndim = len(Y)
	Natom = len(Charge) -1

	E = zeros(ndim)
	for i in range(ndim):
		
		temp = 0
		for j in range(Natom):

			temp2 = X[i][j] * Charge[j]

			temp += temp2

		E[i] = Y[i] - temp
	
	MSE_value = 0
	for i in range(ndim):
		error = E[i] ** 2	
		
		MSE_value += error

	return MSE_value


def ESP_square_sum(Y):
	ndim = len(Y)

	ESP_square_sum = 0
	for i in range(ndim):
		QM_ESP = Y[i] ** 2

		ESP_square_sum += QM_ESP
	
	return ESP_square_sum


def RRMS(MSE_List, ESP_square_sum,  RRMS):

	RRMS = math.sqrt(MSE_value / ESP_square_sum)



def change_shape(List, new_List):
	ndim = len(List)

	for a in range(ndim):

		new_List[a] = float(List[a][0])
	


### Module : write the CHELPG grid point on the file ###
def write_CHELPG(fw, CHELPG_List):
	Ngrid = int(len(CHELPG_List))

	fw.write(">>>>CHELPG grid points" + "\n")

	for i in range(Ngrid):

		grid_x = float(CHELPG_List[i][0])
		grid_y = float(CHELPG_List[i][1])
		grid_z = float(CHELPG_List[i][2])
		
		fw.write("%7.3f"%grid_x + "%7.3f"%grid_y + "%7.3f"%grid_z + "\n")

	fw.write("\n" + ">>>>num_of_grids : " + "%5d"%Ngrid)


### Module : write the CHELPG grid point on the msgpack file ###
def write_grid_msgpack(fw, Grid_List):

	data = {}
	data["version"] = "2015.0"

	data["num_of_grids"] = len(Grid_List)

	data["grid_unit"] = "angstroam"

	data["grids"] = Grid_List

	packed = msgpack.packb(data)

	fw.write(packed)
	fw.close()


### Module : write Charge ###
def write_cube(fw, Cube_List, Atom_List, Counter_Chg, ESP_List):
	fw.write("comment line:" + "\n")
	fw.write("comment line:" + "\n")

	Nx, Ny, Nz = int(Cube_List[1][0]), int(Cube_List[2][0]), int(Cube_List[3][0])
	Ncube = len(Cube_List)
	for i in range(Ncube):
		CL1 = int(Cube_List[i][0])
		CL2, CL3, CL4 = float(Cube_List[i][1]), float(Cube_List[i][2]), float(Cube_List[i][3])
		
		fw.write("%5d"%CL1 + "%13.6f"%CL2 + "%13.6f"%CL3 + "%13.6f"%CL4 + "\n")

	Natom = len(Atom_List)
	for j in range(Natom):
		atom_number = int(Atom_List[j][0])
		atom_number_ = float(Atom_List[j][1])
		atom_x = float(Atom_List[j][2])
		atom_y = float(Atom_List[j][3])
		atom_z = float(Atom_List[j][4])

		fw.write("%5d"%atom_number + "%13.6f"%atom_number_ + "%13.6f"%atom_x + "%13.6f"%atom_y + "%13.6f"%atom_z + "\n")

	for j_ in range(len(Counter_Chg)):
		atom_number = int(Counter_Chg[j_][0])
		atom_number_ = float(Counter_Chg[j_][1])
		atom_x = float(Counter_Chg[j_][2])
		atom_y = float(Counter_Chg[j_][3])
		atom_z = float(Counter_Chg[j_][4])

		fw.write("%5d"%atom_number + "%13.6f"%atom_number_ + "%13.6f"%atom_x + "%13.6f"%atom_y + "%13.6f"%atom_z + "\n")	
	
	for k in range(Nx * Ny * Nz):

		fw.write("%13.5E"%ESP_List[k])
		if k % Nz == Nz-1:
				fw.write("\n")
		
		if (k % Nz) % 6 == 5:
			fw.write("\n")


