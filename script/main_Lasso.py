#!/usr/bin/python
# coding:utf-8

import argparse
import numpy as np
try:
	import msgpack
except:
	import msgpack_pure as msgpack

import mkmat
import chg_resp
import chg_lasso


def main():
	# parse args
	parser = argparse.ArgumentParser(description="output the Lasso charge")
	parser.add_argument("FILE",
						nargs=1,
						help="input file(.mpac)")
	parser.add_argument("-o", "--output",
						nargs=1,
						dest="charge_path",
						default="LASSOcharge.mpac",
						help="output file")
	args = parser.parse_args()
	
	# setting
	db_path = args.FILE[0]
	fr = open(db_path, "rb")
	data = msgpack.unpackb(fr.read())
	
	Atom_List = np.array(data["atoms"])
	atoms = np.array(Atom_List[:, 5:])
	atoms = atoms.astype(np.float)
	X = np.array(data["matrixX"])
	Y = np.array(data["matrixY"])
	net_charge = data["net_charge"]
	
	Natom = len(Atom_List)
	Ngrid = len(X)

	# matrixA, B
	A = mkmat.matrixA(X, Y)
	B = mkmat.matrixB(X, Y, net_charge)

	# scf calculation
	Lasso_parameter = 1e-4
	Lasso_Charge = chg_lasso.iteration(A, B, Lasso_parameter)

	# RRMS
	RRMS = chg_resp.RRMS(X, Y, Lasso_Charge)
	print RRMS
	# write the data
	fw_path = args.charge_path[0]
	fw = open(fw_path, "wb")

	data["Lasso"] = Lasso_Charge[:-1]
	packed = msgpack.packb(data)
	fw.write(packed)
	fw.close()

if __name__ == "__main__":
	main()

