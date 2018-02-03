# -*- coding: utf-8 -*-
"""
Created on Mon May 23

@author: fangren

"""

import pyFAI
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

# open MARCCD tiff image
path = '..\\..\\data\\'
im = Image.open(path + 'Figure1_LaB6.tif')
save_path = '..\\..\\figures\\'

# change image object into an array
imArray = np.array(im)
s = int(imArray.shape[0])
im.close()

detector_mask = np.ones((s,s))*(imArray <= 0)

# parameters I originally used.
d_in_pixel = 2462.69726489     # distance from sample to detector plane along beam direction in pixel space
Rot = (np.pi*2-4.69729438873)/(2*np.pi)*360  #detector rotation
tilt = 0.503226642865/(2*np.pi)*360   # detector tilt
lamda = 0.97621599151  # wavelength
x0 = 969.878684978     # beam center in pixel-space
y0 = 2237.93277884    # beam center in pixel-space
PP = 0.95   # beam polarization, decided by beamline setup


pixelsize = 79    # measured in microns
d = d_in_pixel*pixelsize*0.001  # measured in milimeters

p = pyFAI.AzimuthalIntegrator(wavelength=lamda)
p.setFit2D(d,x0,y0,tilt,Rot,pixelsize,pixelsize)
cake,Q,chi = p.integrate2d(imArray,1000, 1000, mask = detector_mask, polarization_factor = PP)
Q = Q * 10e8
chi = chi+90
Qlist, IntAve = p.integrate1d(imArray, 1000, mask=detector_mask, polarization_factor=PP)
Qlist = Qlist * 10e8


# generate a tiff image
X = [i+1 for i in range(s)]
Y = [i+1 for i in range(s)]
X, Y = np.meshgrid(X, Y)
plt.figure(1, (4,4))
plt.pcolormesh(X, Y, imArray, cmap = 'jet')
plt.clim(0, 2000)
plt.ylim((0, s))
plt.xlim((0, s))
plt.savefig(save_path+ 'Figure1(a)', dpi = 600)

# generate a vertical Q-gamma image with polar correction
Q, chi = np.meshgrid(Q, chi)
plt.figure(2, (5,4))
# plt.title('Q-$\Psi$')
plt.pcolormesh(chi, Q, cake, cmap = 'jet')
#plt.imshow(cake)
plt.xlabel('$\gamma$')
plt.ylabel('Q')
plt.ylim((0.6, 5.87))
plt.xlim((-58, 63))
plt.colorbar()
plt.clim(0, 2000)
plt.tight_layout()
plt.savefig(save_path+ 'Figure1(b)', dpi = 600)

twoTheta = np.arcsin(Qlist*1.54/4/np.pi) *2 *180/np.pi
# generate a 1D spectra with both Q axis and 2 theta axis
fig = plt.figure(3, (4,4))
ax1 = fig.add_subplot(111)
ax2 = ax1.twinx()

ax1.plot(IntAve,Qlist, 'b')
ax1.set_ylim(0.6, 5.87)
ax1.set_ylabel("Q")
ax1.set_xlabel("Intensity")

new_tick_locations = np.arange(1, 6, 1)

ax2.set_ylim(ax1.get_ylim())
ax2.set_yticks(new_tick_locations)
ax2.set_yticklabels(np.round(np.arcsin(new_tick_locations*1.54/4/np.pi) *2 *180/np.pi, 1))
ax2.set_ylabel("2$\\theta$")
plt.tight_layout()
plt.savefig(save_path+ 'Figure1(c)', dpi = 600)

plt.close("all")



# # generate a vertical column average image
# plt.figure(3, (5,4))
# # plt.title('Column sum')
# Qlist, IntAve = p.integrate1d(imArray, 1000, mask = detector_mask, polarization_factor = PP)
# Qlist = Qlist * 10e8
# plt.plot(IntAve, Qlist)
# plt.ylabel('Q')
# plt.xlabel('Intensity')
# plt.ylim((0.6, 5.87))
# plt.tight_layout()
# plt.savefig(path+ '1D', dpi = 600)
#
#
#
#
# twoTheta = np.arcsin(Qlist*1.54/4/np.pi) *2 *180/np.pi
# # generate a column average image
# plt.figure(9, (5,4))
# # plt.title('Column sum')
# plt.plot(IntAve, twoTheta)
# plt.ylabel('2 theta')
# plt.xlabel('Intensity')
# plt.ylim((8, 90))
# plt.tight_layout()
# plt.savefig(path+ '1D_2theta', dpi = 600)


# # generate a texture image
# plt.figure(4, (5,4))
# # plt.title('texture')
#
# keep = np.where(cake != 0)
# chi = chi*np.pi/180
#
# IntSum = np.bincount((Q[keep].ravel()*100).astype(int), cake[keep].ravel().astype(int))
# count = np.bincount((Q[keep].ravel()*100).astype(int), np.ones((s,s))[keep].ravel().astype(int))
# IntAve = list(np.array(IntSum)/np.array(count))
#
# textureSum = np.bincount((Q[keep].ravel()*100).astype(int), (cake[keep]*np.cos(chi[keep])).ravel())
# chiCount = np.bincount((Q[keep].ravel()*100).astype(int), (np.cos(chi[keep])).ravel())
#
# texture = list(np.array(textureSum)/np.array(IntAve)/np.array(chiCount)-1)
#
# step = 0.01
# Qlen = len(textureSum)
# Qlist_texture = [i*step for i in range(Qlen)]
#
#
# plt.plot(Qlist_texture, texture)
# plt.xlabel('Q')
# plt.ylabel('Texture')
# plt.xlim((0.6, 5.87))
# plt.tight_layout()
# plt.savefig(path+ 'texture', dpi = 600)