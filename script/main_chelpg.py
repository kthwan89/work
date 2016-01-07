#!/usr/bin/python
# coding:utf-8

################## Import modules ####################
import argparse
import msgpack

import fl_read
import grid_chelpg

def main():
	# parse args
	parser = argparse.ArgumentParser(description="output the CHELPG grid points")
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
	range_List = grid_chelpg.range_List(Atom_List)
	all_grid_List = grid_chelpg.CHELPG_List_all(range_List)
	chelpg_List = grid_chelpg.CHELPG_List(Atom_List, all_grid_List)

	# output
	fw_path = args.grid_path[0]
	fw = open(fw_path, "wb")
	data = {}
	data["atoms"] = Atom_List
	data["grids"] = chelpg_List

	packed = msgpack.packb(data)
	fw.write(packed)
	fw.close()


if __name__ == "__main__":
	main()

