#!/usr/bin/python
# coding:utf-8

import argparse
import msgpack

import DipoleMoment
import fl_read

def main():
	# parse args
	parser = argparse.ArgumentParser(description="output the Dipole Moment")
	parser.add_argument("FILE",
						nargs=1,
						help="input file"
						)
	parser.add_argument("-o", "--output",
						nargs=1,
						dest="Dipole_path",
						default="Dipole.mpac",
						help="output file")
	args = parser.parse_args()

	# setting
	db_path = args.FILE[0]
	fr = open(db_path, "rb")
	data = msgpack.unpackb(fr.read())

	Atom_List = data["atoms"]
	Charge_List = data["Lasso"]
	

	# calculate the Dipole Moment
	DP_debye = DipoleMoment.calculate_Dipole_Moment(Atom_List, Charge_List)
	print (DP_debye)

if __name__ == "__main__":
	main()

