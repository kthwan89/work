#!/usr/bin/python
# coding:utf-8

################## Import modules ####################
import sys
import argparse
import numpy as np
import msgpack

import fl_read
import chg_resp


def main():
	# parse args
	parser = argparse.ArgumentParser(description="make data file")
	parser.add_argument("-a", "--atom",
						nargs=1,
						dest="atom_path",
						default=False)
	parser.add_argument("-g", "--grid",
						nargs=1,
						dest="grid_path",
						default=False)
	parser.add_argument("-m", "--mulliken",
						nargs=1,
						dest="mulliken_path",
						default=False)
	parser.add_argument("-o", "--output",
						nargs=1,
						dest="data_path",)

	# read the data
	fatom = open(args.atom_path[0], "r")
	Atom_List = fl_read.read_pdb_file(fatom)

	fgrid = open(args.grid_path[0], "rb")
	Grid_List = fl_read.read_grid_msg_file(fgrid)

	fesp = open(args.grid_path[0], "rb")
	ESP_List = fl_read.read_esp_msg_file(fesp)

	fmulliken = open(args.mulliken_path[0], "r")
	Mulliken_List = fl_read.read_mulliken_file(fmulliken)

	# calculate the data
	X = mkmat.matrixX(Atom_List, Grid_List)
	Y = mkmat.matrixY(Grid_List)
	

	# write the msgpack file
	fw_path = args.data_path[0]
	fw = open(fw_path, "wb")

	data = {}
	data["atoms"] = Atom_List
	data["grids"] = Grid_List
	data["ESP"] = ESP_List
	data["mulliken"] = Mulliken_List
	data["matrixX"] = np.array(X)
	data["matrixY"] = np.array(Y)
	data["net_charge"] = -2
	data["Nelec"] = 3000
	
	packed = msgpack.packb(data)
	fw.write(packed)
	fw.close()


if _name__ == "__main__":
	main()
