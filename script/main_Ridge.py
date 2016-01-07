#!/usr/bin/python
# coding:utf-8

################## Import modules ####################
import argparse
import numpy as np
try:
	import msgpack
except:
	import msgpack_pure as msgpack

import fl_read
import mkmat
import chg_resp

def main():
	# parse args
	parser = argparse.ArgumentParser(description="calculate the Ridge Charge")
	parser.add_argument("FILE",
						nargs=1,
						help="input file(.mpac)")
	parser.add_argument("-o", "--output",
						nargs=1,
						dest="charge_path",
						help="charge file")
	args = parser.parse_args()

	# setting
	db_path = args.FILE[0]
	fr = open(db_path, "rb")
	data = msgpack.unpackb(fr.read())
	
	Atom_List = data["atoms"]
	Grid_List = data["grids"]
	ESP_List = data["ESP"]
	Mulliken_List = data["mulliken"]
	X = np.array(data["matrixX"])
	Y = np.array(data["matrixY"])
	net_charge = data["net_charge"]
	
	Natom = len(Atom_List)
	Ngrid = len(Grid_List)

	# matrix
	A = mkmat.matrixA(X, Y)
	B = mkmat.matrixB(X, Y, net_charge)
	I = np.matrix(np.identity(Natom))

	# Ridge CHARGE
	Q_new = np.zeros(Natom+1)
	Ridge_A = chg_resp.copy_matrixA(A)
	wt = 1e-1

	chg_resp.Ridge_convert_matrix(Atom_List, A, Ridge_A, wt)
	Ridge_CHARGE = np.linalg.solve(Ridge_A, B)

	# RRMS
	MSE = chg_resp.MSE(X, Y, Ridge_CHARGE)
	ESP_square_sum = chg_resp.ESP_square_sum(Y)
	RRMS = np.sqrt(MSE/ESP_square_sum)
	print RRMS
	# write the data
	fw_path = args.charge_path[0]
	fw = open(fw_path, "wb")

	data["Ridge"] = Ridge_CHARGE[:-1]
	packed = msgpack.packb(data)
	fw.write(packed)
	fw.close()

if __name__ == "__main__":
	main()

