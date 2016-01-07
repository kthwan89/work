#!/usr/bin/env python
#-*-coding:utf-8-*-

import numpy as np
import basic

AUG_PER_AU = 0.529177721092
AU_PER_AUG = 1/AUG_PER_AU


# Module : matrix X #
def matrixX(Atom_List, Grid_List):
	Natom = len(Atom_List)
	Ngrid = len(Grid_List)

	X = np.zeros((Ngrid, Natom))
	for i in range(Ngrid):
		
		Grid_x = float(Grid_List[i][0])
		Grid_y = float(Grid_List[i][1])
		Grid_z = float(Grid_List[i][2])
		
		#grid_xyz = np.array(Grid_List[i])

		for j in range(Natom):
			Atom_x = float(Atom_List[j][5])
			Atom_y = float(Atom_List[j][6])
			Atom_z = float(Atom_List[j][7])
			
			#dist = basic.calcdis(Atom_x, Atom_y, Atom_z, Grid_x, Grid_y, Grid_z) * AU_PER_AUG
			dist = basic.calcdis(Atom_x, Atom_y, Atom_z, Grid_x, Grid_y, Grid_z)
			"""
			atom_xyz = np.array(Atom_List[j][5:])
			atom_xyz = map(float, atom_xyz)
			
			dist = np.linalg.norm(grid_xyz - atom_xyz) * AU_PER_AUG
			"""

			X[i][j] = 1/dist
	return X


### Module : matrix Y ###
def matrixY(ESP_List):
	Ngrid = len(ESP_List)
	Y = np.zeros((Ngrid, 1))
	Y = ESP_List[:]
	Y = map(float, Y)


# matrix A
def matrixA(X, Y):
	transX = X.T
	Natom = len(transX)
	xTx = np.array(transX * np.matrix(X))
	A = np.ones((Natom+1, Natom+1))
	for j in range(Natom):
		for k in range(Natom):
			A[j][k] = xTx[j][k]
	A[Natom][Natom] = 0
	
	return A


#matrix B
def matrixB(X, Y, net_charge):
	transX = X.T
	Natom = len(transX)
	Ngrid = len(Y)
	xTy = np.array(transX * np.matrix(Y))
	B = np.zeros(Natom+1)
	for j in range(Natom):
		B[j] = xTy[j][0]
	B[Natom] = net_charge

	return B


#CEEM_matrixS
def matrixS(Atom_List):

	N = len(Atom_List)
	S = np.ones((N, N))

	for j in range(N):
		S[j , j] = 0
		Atom_j = Atom_List[j]
		for k in range(j):
			Atom_k = Atom_List[k]
			dist = np.linalg.norm(Atom_j - Atom_k)
			
			S[j, k] = 1/dist
			S[k, j] = S[j, k]

	return S
