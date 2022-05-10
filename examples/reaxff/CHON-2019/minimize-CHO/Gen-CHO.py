#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 29 15:32:50 2022

@author: chaithanya
"""
import numpy as np
import sys

# Ref: https://cccbdb.nist.gov/expgeom2.asp?casno=2597446&charge=0
d_CO  = 1.2
d_CH  = 1.2
theta = 90 * np.pi/180

if(len(sys.argv) == 3):
    d_CO  = float(sys.argv[1])
    theta = float(sys.argv[2]) * (np.pi/180)

C_pos = np.array([0,0,0])
H_pos = np.array([d_CH,0,0])
O_pos = np.array([np.cos(theta),np.sin(theta),0]) * d_CO

fw = open("CHO-pos.lmp","w")
fw.write("# CHO structure\n")
fw.write("3 atoms\n")
fw.write("3 atom types\n\n")

fw.write("-10.0 10.0 xlo xhi\n")
fw.write("-10.0 10.0 ylo yhi\n")
fw.write("-10.0 10.0 zlo zhi\n\n")

fw.write("Masses\n\n")
fw.write(" 1 12.0000\n")
fw.write(" 2  1.0000\n")
fw.write(" 3 15.9990\n\n")

fw.write("Atoms\n\n")
fw.write("1 1 0.0 %10.6E  %10.6E  %10.6E\n"%(C_pos[0], C_pos[1], C_pos[2]))
fw.write("2 2 0.0 %10.6E  %10.6E  %10.6E\n"%(H_pos[0], H_pos[1], H_pos[2]))
fw.write("3 3 0.0 %10.6E  %10.6E  %10.6E\n"%(O_pos[0], O_pos[1], O_pos[2]))

fw.close()
