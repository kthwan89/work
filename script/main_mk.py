#!/usr/bin/python
# coding:utf-8

import argparse
import msgpack

import fl_read
import grid_mk

def main():
	# parse args
	parser = argparse.ArgumentParser(description="output the MK grid points")
	parser.add_argument("FILE",
						nargs=1,
						help="input file(.pdb)")
	parser.add_argument("-o", "--output",
						nargs=1,
						dest="grid_path",
						default="grid.mpac",
						help="output file")
	args = parser.parse_args()

	# setting
	pdb_path = args.FILE[0]
	fr = open(pdb_path, "r")
	Atom_List = fl_read.read_pdb_file(fr)
	
	# calculation
	All_Layer1 = grid_mk.generate_All_Grid_List(Atom_List, 1)
	All_Layer2 = grid_mk.generate_All_Grid_List(Atom_List, 2)
	All_Layer3 = grid_mk.generate_All_Grid_List(Atom_List, 3)
	All_Layer4 = grid_mk.generate_All_Grid_List(Atom_List, 4)

	Layer1 = grid_mk.position_check(Atom_List, All_Layer1, 1)
	Layer2 = grid_mk.position_check(Atom_List, All_Layer2, 2)
	Layer3 = grid_mk.position_check(Atom_List, All_Layer3, 3)
	Layer4 = grid_mk.position_check(Atom_List, All_Layer4, 4)

	Grid_List = Layer1 + Layer2 + Layer3 + Layer4

	# output
	fw_path = args.grid_path[0]
	fw = open(fw_path, "wb")
	data = {}
	data["atoms"] = Atom_List
	data["grids"] = Grid_List

	packed = msgpack.packb(data)
	fw.write(packed)
	fw.close()


if __name__ == "__main__":
	main()


