# -*- coding: utf-8 -*-
"""
Created on Mon Jun 13

@author: fangren

"""

import matplotlib.pyplot as plt
import os.path


def save_1Dplot(Qlist, IntAve, peaks, imageFilename, save_path):
    # generate a column average image
    plt.figure(2)
    plt.title('Column average')
    plt.plot(Qlist[peaks], IntAve[peaks], 'o')
    plt.plot(Qlist, IntAve)
    plt.xlabel('Q')
    plt.ylabel('Intensity')
    #plt.xlim((0.45, 5.87))

    plt.savefig(os.path.join(save_path, os.path.splitext(imageFilename)[0]+'_1D'))
    
    plt.close()
