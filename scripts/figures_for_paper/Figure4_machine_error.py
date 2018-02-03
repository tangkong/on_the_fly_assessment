# -*- coding: utf-8 -*-
"""
Created on Wed July 13 2016

@author: fangren
"""


import numpy as np
import matplotlib.pyplot as plt
import glob
import os
from os.path import basename
import imp


path = '..\\..\\data\\'
filename = path + 'Figure4_sample_holder_blocking.csv'
save_path = '..\\..\\figures\\'

data = np.genfromtxt(filename, delimiter=',', skip_header = 1)
plate_x = data[:,1]
plate_y = data[:,2]
ROI1 = data[:,15]
ROI2 = data[:,16]
ROI3 = data[:,17]
ROI5 = data[:,19]


area = 115

plt.figure(1, figsize = (6, 4.5))
plt.scatter(plate_y, plate_x, c = ROI1, s = area, marker = 's', linewidths=.5, edgecolors= 'k', cmap = 'jet')
plt.xlim((-36, 36))
plt.ylim((-36, 36))
plt.colorbar()
plt.xlabel('x')
plt.ylabel('y')
plt.savefig(save_path+'Figure4(a)', dpi = 600)



filename = path + 'Figure4_sample_drifting_warping.csv'


data = np.genfromtxt(filename, delimiter=',', skip_header = 1)
plate_x = data[:,1]
plate_y = data[:,2]
ROI1 = data[:,15]
ROI2 = data[:,16]
ROI3 = data[:,17]
ROI5 = data[:,19]

area = 70

plt.figure(2, figsize = (6, 4.5))
plt.scatter(plate_y, plate_x, c = ROI1, s = area, marker = 's', linewidths=.5, edgecolors= 'k', cmap = 'jet')
plt.xlim((-45, 45))
plt.ylim((-45, 45))
plt.colorbar()
plt.xlabel('x')
plt.ylabel('y')
plt.savefig(save_path+'Figure4(b)', dpi = 600)

plt.close('all')