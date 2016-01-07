#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import msgpack

import fl_read

def add_Atom_List(File):
	
	fr = open(File, "r")
	Atom_List = []
	fl_read.read_pdb_file(fr, Atom_List)

	return Atom_List

def add_Grid_List(File):

	fr = open(File, "rb")
	Grid_List = fl_read.read_grid_msg_file(fr)

	return Grid_List

def add_ESP_List(File):

	fr = open(File, "rb")
	ESP_List = fl_read.read_esp_msg_file(fr)

	return ESP_List






	
