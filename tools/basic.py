#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np

# Module : calculate the distance
def calcdis(x1,y1,z1, x2,y2,z2):
	
	temp = float((x1-x2)**2 + (y1-y2)**2 + (z1-z2)**2)
	dist = np.sqrt(temp)
	
	return dist

