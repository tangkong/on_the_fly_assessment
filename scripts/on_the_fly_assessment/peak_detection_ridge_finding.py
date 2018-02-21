# -*- coding: utf-8 -*-
"""
Created on Nov 17 2016

@author: Fang Ren, Robert Tang-Kong
"""


from scipy.signal import cwt, ricker, find_peaks_cwt
import matplotlib.pyplot as plt
import numpy as np
import glob
import os
from os.path import basename


path = os.path.expanduser('~/img/JaeProcPeakTst/')

save_path = path + 'peak_detection/'
if not os.path.exists(save_path):
    os.makedirs(save_path)


for file in glob.glob(os.path.join(path, '*.csv')):
    if basename(file)[-5] == 'D':
        print file
        data = np.genfromtxt(file, delimiter = ',')
        Qlist = data[:,0]
        IntAve = data[:,1]

        widths = np.arange(1, 64, 2)
        cwt_coefficient = cwt(IntAve, ricker, widths)
        a1 = 1
        a2 = 20
        peaks = find_peaks_cwt(IntAve, np.arange(a1, a2, 0.05))
        peaks = peaks[1:-1]

        h = 15  # number of points skipped in finite differences

        peaks_accepted = []
        window = h

        for peak in peaks:

            filter = np.nan_to_num(np.sqrt(-(IntAve[2 * h:] 
                                              - 2 * IntAve[h:-h] 
                                              + IntAve[0:-2 * h])))
            filterwindow = filter[max(peak - h - window, 0)
                                    :min(peak - h + window, len(filter))]
            spectrawindow = IntAve[max(peak - window, h)
                                    :min(peak + window, len(filter))]

            try:
                # np.percentile(filter,85) is also a good threshold
                if np.any(filterwindow > spectrawindow / 200):
                    peaks_accepted.append(peak)
            except ValueError:
                continue


        plt.figure(1)
        plt.subplot((311))
        plt.title('wavelet grid: ridge finding')
        plt.pcolormesh(Qlist, widths, cwt_coefficient)
        plt.plot(Qlist, [a1]* len(Qlist), 'r--')
        plt.plot(Qlist, [a2]* len(Qlist), 'r--')
        plt.autoscale(axis='x')
        plt.ylim(a1, a2-1)
        # plt.clim(np.nanmin(np.log(cwt_coefficient)), np.nanmax(np.log(cwt_coefficient)))

        plt.subplot((312))
        plt.title('Data with accepted peaks')
        plt.plot(Qlist[peaks_accepted], IntAve[peaks_accepted], linestyle='None', c='r', marker='o', markersize=10, label='accepted peaks')
        plt.plot(Qlist[peaks], IntAve[peaks], linestyle='None', c='b', marker='o', markersize=3, label='peaks')
        plt.plot(Qlist, IntAve, label='data')
        plt.legend()
        plt.autoscale()

        plt.subplot((313))
        plt.plot(Qlist[15:-15], filter, label='filter')
        plt.legend()
        plt.autoscale()

        plt.savefig(save_path + basename(file)[:-7])
        plt.close('all')
