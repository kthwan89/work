#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np

### Module : SCF calculation ###
def SCF_convert_matrix(ATOM_LIST, Q_old, Q_target, A, B, SCF_A, SCF_B, TYPE):
	Natom = len(ATOM_LIST)
	wt = 5e-4
	b = 0.1

	for j in range(Natom):
		
		atom_type = ATOM_LIST[j][2]

		if "H" not in atom_type or "OH" in atom_type or "NH" in atom_type:
			
			if TYPE == "harmonic":
				pnlt_func = wt
				
				SCF_A[j][j] = A[j][j] + pnlt_func
				SCF_B[j] = B[j] + Q_target[j] * pnlt_func
				
			elif TYPE == "hyperbolic":
				pnlt_func = wt / np.sqrt((Q_old[j]-Q_target[j])**2 + b**2)
				
				SCF_A[j][j] = A[j][j] + pnlt_func
				SCF_B[j] = B[j] + Q_target[j] * pnlt_func
			
		"""
		if TYPE == "harmonic":
			pnlt_func = wt
				
			SCF_A[j][j] = A[j][j] + pnlt_func
			SCF_B[j] = B[j] + Q_target[j] * pnlt_func
				
		elif TYPE == "hyperbolic":
			pnlt_func = wt / np.sqrt((Q_old[j]-Q_target[j])**2 + b**2)
			
			SCF_A[j][j] = A[j][j] + pnlt_func
			SCF_B[j] = B[j] + Q_target[j] * pnlt_func
		"""

def Ridge_convert_matrix(ATOM_LIST, A, SCF_A, wt):
	Natom = len(ATOM_LIST)

	for j in range(Natom):
		SCF_A[j][j] = A[j][j] + 2*wt
				

def SCF_error(Q_new, Q_old):
	Natom = len(Q_new)

	Q_new = np.array(Q_new)
	Q_old = np.array(Q_old)

	error = np.linalg.norm(Q_new - Q_old)
	error = error / Natom
	
	return error


def SimpleMixing(Q_new, Q_old, rate):
	Natom = len(Q_new) - 1

	for j in range(Natom+1):
		Q_new[j] = rate * Q_old[j] + (1-rate) * Q_new[j]
		
	return Q_new   
	
	
	
def MSE(X, Y, Charge_List):
	Ngrid = len(Y)
	Natom = len(X[0]) 

	E = np.zeros(Ngrid)
	for i in range(Ngrid):

		temp = 0
		for j in range(Natom):

			temp2 = X[i][j] * Charge_List[j]
		
			temp += temp2

		E[i] = Y[i] - temp

	MSE_value = 0
	for i in range(Ngrid):
		error = E[i] ** 2

		MSE_value += error

	return MSE_value

def ESP_square_sum(Y):
	ndim = len(Y)

	ESP_square_sum = 0
	for i in range(ndim):
		QM_ESP = Y[i] ** 2

		ESP_square_sum += QM_ESP
	
	return ESP_square_sum


def RRMS(X, Y, charge):
	MSE_value = MSE(X, Y, charge)
	ESP_square = ESP_square_sum(Y)

	RRMS = np.sqrt(MSE_value / ESP_square)

	return RRMS


def change_shape(List, new_List):
	ndim = len(List)

	for a in range(ndim):

		new_List[a] = float(List[a][0])


def copy_matrixA(matrix):
	dimension = len(matrix)
	copied_matrix = [[0 for col in range(dimension)] for row in range(dimension)]
	for row in range(dimension):
		for col in range(dimension):
			copied_matrix[row][col] = matrix[row][col]
	return copied_matrix


def copy_matrixB(matrix):
	dimension = len(matrix)
	copied_matrix = [0 for col in range(dimension)]
	for col in range(dimension):
		copied_matrix[col] = matrix[col]
	return copied_matrix


### Module : write Charge ###
def write_charge(fw, Atom_List, Charge_List, RRMS):
	
	fw.write(">>>>charge" + "\n")

	Natom = len(Atom_List)
	for j in range(Natom):

		atom_type = Atom_List[j][2]
		residue_name = Atom_List[j][3]
		residue_number = int(Atom_List[j][4])
		charge = float(Charge_List[j])

		fw.write("%5d"%(j+1) + "%6s"%atom_type + "%6s"%residue_name + "%5d"%residue_number + "%10.3f"%charge + "\n")

	fw.write("\n" + ">>>>RRMS : %0.6f"%RRMS)

