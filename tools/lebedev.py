#!/usr/bin/python
#-*-coding:utf-8-*-

import numpy as np

def Grid_TYPE1(List):
	a = 1.0
	
	TYPE1_List = [[a, 0.0, 0],
				  [-a, 0.0, 0.0],
				  [0.0, a, 0.0],
				  [0.0, -a, 0.0],
				  [0.0, 0.0, a],
				  [0.0, 0.0, -a]]
	
	List += TYPE1_List


def Grid_TYPE2(List):
	a = np.sqrt(1.0/2)
	
	TYPE2_List = [[a, a, 0.0],
				  [a, -a, 0.0],
				  [-a, a, 0.0],
				  [-a, -a, 0.0],
				  [0.0, a, a],
				  [0.0, a, -a],
				  [0.0, -a, a],
				  [0.0, -a, -a],
				  [a, 0.0, a],
				  [a, 0.0, -a],
				  [-a, 0.0, a],
				  [-a, 0.0, -a]]
	
	List += TYPE2_List


def Grid_TYPE3(List):
	a = np.sqrt(1.0/3)
	
	TYPE3_List = [[a, a, a],
				  [a, a, -a],
				  [a, -a, a],
				  [a, -a, -a],
				  [-a, a, a],
				  [-a, a, -a],
				  [-a, -a, a],
				  [-a, -a, -a]]
	
	List += TYPE3_List


def Grid_TYPE4(List, a):
	b = np.sqrt(1 -2*a**2)

	TYPE4_List = [[a, a, b],
				  [a, -a, b],
				  [-a, a, b],
				  [-a, -a, b],
				  [a, a, -b],
				  [a, -a, -b],
				  [-a, a, -b],
				  [-a, -a, -b],
				  [a, b, a],
				  [a, b, -a],
				  [-a, b, a],
				  [-a, b, -a],
				  [a, -b, a],
				  [a, -b, -a],
				  [-a, -b, a],
				  [-a, -b, -a],
				  [b, a, a],
				  [b, a, -a],
				  [b, -a, a],
				  [b, -a, -a],
				  [-b, a, a],
				  [-b, a, -a],
				  [-b, -a, a],
				  [-b, -a, -a]]
	
	List += TYPE4_List

def Grid_TYPE5(List, a):
	b = np.sqrt(1- a**2)

	TYPE5_List = [[a, b, 0.0],
    			  [a, -b, 0.0],
    			  [-a, b, 0.0],
    			  [-a, -b, 0.0],
    			  [b, a, 0.0],
    			  [b, -a, 0.0],
    			  [-b, a, 0.0],
    			  [-b, -a, 0.0],
    			  [a, 0.0, b],
    			  [a, 0.0, -b],
    			  [-a, 0.0, b],
    			  [-a, 0.0, -b],
    			  [b, 0.0, a],
    			  [b, 0.0, -a],
    			  [-b, 0.0, a],
    			  [-b, 0.0, -a],
    			  [0.0, a, b],
    			  [0.0, a, -b],
    			  [0.0, -a, b],
    			  [0.0, -a, -b],
    			  [0.0, b, a],
    			  [0.0, b, -a],
    			  [0.0, -b, a],
    			  [0.0, -b, -a]]

	List += TYPE5_List


def Grid_TYPE6(List, a, b):
	c = np.sqrt(1- a**2 - b**2)

	TYPE6_List = [[a, b, c],
				  [a, b, -c],
				  [a, -b, c],
				  [a, -b, -c],
				  [a, c, b],
	              [a, c, -b],
	              [a, -c, b],
	              [a, -c, -b],
	              [-a, b, c],
	              [-a, b, -c],
	              [-a, -b, c],
	              [-a, -b, -c],
	              [-a, c, b],
	              [-a, c, -b],
	              [-a, -c, b],
	              [-a, -c, -b],
	              [b, c, a],
	              [b, c, -a],
	              [b, -c, a],
	              [b, -c, -a],
	              [b, a, c],
	              [b, a, -c],
	              [b, -a, c],
	              [b, -a, -c],
	              [-b, c, a],
	              [-b, c, -a],
	              [-b, -c, a],
	              [-b, -c, -a],
	              [-b, a, c],
	              [-b, a, -c],
	              [-b, -a, c],
	              [-b, -a, -c],
	              [c, a, b],
	              [c, a, -b],
	              [c, -a, b],
	              [c, -a, -b],
	              [c, b, a],
	              [c, b, -a],
	              [c, -b, a],
	              [c, -b, -a],
	              [-c, a, b],
	              [-c, a, -b],
	              [-c, -a, b],
	              [-c, -a, -b],
	              [-c, b, a],
				  [-c, b, -a],
	              [-c, -b, a],
	              [-c, -b, -a]]

	List += TYPE6_List
	

def Grid_38(List):
	Grid_TYPE1(List)
	Grid_TYPE3(List)
	Grid_TYPE5(List, 0.459701)


def Grid_50(List):
	Grid_TYPE1(List)
	Grid_TYPE2(List)
	Grid_TYPE3(List)
	Grid_TYPE4(List, 0.301511)


def Grid_74(List):
	Grid_TYPE1(List)
	Grid_TYPE2(List)
	Grid_TYPE3(List)
	Grid_TYPE4(List, 0.480384)
	Grid_TYPE4(List, 0.320773)


def Grid_86(List):
	Grid_TYPE1(List)
	Grid_TYPE3(List)
	Grid_TYPE4(List, 0.369603)
	Grid_TYPE4(List, 0.694354)
	Grid_TYPE5(List, 0.374243)


def Grid_110(List):
	Grid_TYPE1(List)
	Grid_TYPE3(List)
	Grid_TYPE4(List, 0.185116)
	Grid_TYPE4(List, 0.690421)
	Grid_TYPE4(List, 0.395689)
	Grid_TYPE5(List, 0.478369)


def Grid_146(List):
	Grid_TYPE1(List)
	Grid_TYPE2(List)
	Grid_TYPE3(List)
	Grid_TYPE4(List, 0.676441)
	Grid_TYPE4(List, 0.417496)
	Grid_TYPE4(List, 0.157468)
	Grid_TYPE6(List, 0.140355, 0.449333)


def Grid_170(List):
	Grid_TYPE1(List)
	Grid_TYPE2(List)
	Grid_TYPE3(List)
	Grid_TYPE4(List, 0.255125)
	Grid_TYPE4(List, 0.674360)
	Grid_TYPE4(List, 0.431891)
	Grid_TYPE5(List, 0.261393)
	Grid_TYPE6(List, 0.499045, 0.144663)


