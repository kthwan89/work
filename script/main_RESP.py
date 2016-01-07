#!/usr/bin/python
# coding:utf-8

import argparse
import numpy as np
try:
	import msgpack
except:
	import msgpack_pure as msgpack

import fl_read
import mkmat
import resp

def main():
	# parse args
	parser = argparse.ArgumentParser(description="calculate the ESP/RESP Charge")
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

	# Unit Matrix
	I = np.matrix(np.identity(Natom))

	# matrix
	A = mkmat.matrixA(X, Y)
	B = mkmat.matrixB(X, Y, net_charge)

	# ESP CHARGE
	ESP_CHARGE = np.linalg.solve(A, B)

	# RESP CHARGE
	# === #
	#Q_target = Mulliken_List
	Q_target = np.zeros(Natom)
	Q_new = np.zeros(Natom+1)
	SCF_A = resp.copy_matrixA(A)
	SCF_B = resp.copy_matrixB(B)
	SCF_iteration = 200
	SCF_threshold = 1e-6
	#rstr_type = "harmonic"
	rstr_type = "hyperbolic"
	# === #

	for NSCF in range(SCF_iteration):
	
		Q_old = Q_new
		resp.SCF_convert_matrix(Atom_List, Q_old, Q_target, A, B, SCF_A, SCF_B, rstr_type)
		Q_new = np.linalg.solve(SCF_A, SCF_B)
		error = resp.SCF_error(Q_new, Q_old)
		if error < SCF_threshold:
			print "convergence"
			break
		Q_new = resp.SimpleMixing(Q_new, Q_old, 0.85)

	RESP_CHARGE = Q_new

	# RRMS
	MSE = resp.MSE(X, Y, RESP_CHARGE)
	ESP_square_sum = resp.ESP_square_sum(Y)
	RRMS = np.sqrt(MSE/ESP_square_sum)

	# write the data
	fw_path = args.charge_path[0]
	fw = open(fw_path, "wb")

	data["RESP"] = RESP_CHARGE[:-1]
	packed = msgpack.packb(data)
	fw.write(packed)
	fw.close()

if __name__ == "__main__":
	main()

