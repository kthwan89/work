#!/usr/bin/python
#-*-coding:utf-8-*-

import numpy as np
import lebedev

def expand_point(List, radian, All_Grid_List_number):
	length = len(List)

	for i in range(length):
		expansion_constant = 1.2 + All_Grid_List_number * 0.2

		for j in range(3):
			List[i][j] = List[i][j] * radian * expansion_constant


def move_point(List, x, y, z):
	length = len(List)
	
	for i in range(length):
		List[i][0] += x
		List[i][1] += y
		List[i][2] += z


def calcdis(x1, y1, z1, x2, y2, z2):
	temp = ((x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2)
	temp = np.sqrt(temp)
	return temp




