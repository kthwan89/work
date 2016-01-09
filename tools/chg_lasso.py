#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
try:
	import msgpack
except:
	import msgpack_pure as msgpack

import chg_resp


def iteration(A, B, lasso_param):
	Natom = len(A)
	SCF_A = chg_resp.copy_matrixA(A)
	Q_new = np.linalg.solve(A, B)
	SCF_iteration = 100000
	SCF_threshold = 1e-6
	zero_threshold = 1e-200
	
	for Nscf in range(SCF_iteration):
		Q_old = Q_new

		for j in range(Natom-1):

			if abs(Q_old[j]) < zero_threshold:
				Q_old[j] = 0.0

		for j in range(Natom-1):
			if abs(Q_old[j]) >= zero_threshold:
				param = lasso_param / abs(Q_old[j])

			else:
				param = 0

			SCF_A[j][j] = A[j][j] + param

		Q_new = np.linalg.solve(SCF_A, B)

		error = chg_resp.SCF_error(Q_new, Q_old)
		if error < SCF_threshold:
			print "convergence &",Nscf
			break

	#	Q_new = chg_resp.SimpleMixing(Q_new, Q_old, 0.85)
	return Q_new
	

def L1_norm_sum(charge):
	Natom = len(charge) -1

	L1_norm = 0
	for j in range(Natom):
		
		chg_value = abs(charge[j])

		L1_norm += chg_value
	
	return L1_norm


def L1_evaluation(X, Y, charge):
	MSE = resp.MSE(X, Y, charge)
	L1_norm = L1_norm_sum(charge)
	L1_evaluation = MSE + L1_norm

	return L1_evaluation


def count_sparse(charge):
	Natom = len(charge) -1

	Nsparse = 0
	for j in range(Natom):
		chg_value = charge[j]
		if abs(chg_value) < 1e-3:
			Nsparse += 1

	return Nsparse

