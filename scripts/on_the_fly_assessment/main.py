"""
Created on Nov 17 2016, last updated 2/28/17
@author: Fang Ren (SSRL), Robert Tang-Kong
@version: 1.1
"""

from on_the_fly import on_the_fly
import os

# PP: beam polarization, according to beamline setup. 
# Contact beamline scientist for this number
PP = 0.95   
pixelSize = 79  # detector pixel size, measured in microns
###############################################################################
# folder and file info 
###############################################################################
# specify the file path for the WxDiff calibration file
calibration_file = os.path.expanduser('~/data/bl10-2/Jan2018/LaB6_13k_th2p0_5sr.calib')
# calibration_file = 'sample_data/LaB6.calib'

# specify a folder for the software to watch
folder_path = os.path.expanduser('~/data/bl10-2/Jan2018/')  
# folder_path = 'sample_data/' 

# in order for the program to recognize newly created files
# file needs to have the same basefile, index increments by 1 for each new file.
base_filename = 'ta_LaB6_rpy1_13K_th2p0_fil0_5sr_scan1_'
# base_filename = 'SampleB2_19_24x24_t30_'

 
# For the current example, the first file is SampleB2_19_24x24_t30_0001, and second SampleB2_19_24x24_t30_0002...

# starting from this scan
# Index number, will be padded to 4 characters
index = 0  
# end with this scan. if unsure use large number
last_scan = 2  
# the number of samples in a row. Required if using nearest-neighbor distance module
num_of_smpls_per_row = 25 

###############################################################################
#### turn on/off optional moduels, change the module status to 'on' if want to use them.
###############################################################################
extract_Imax_Iave_ratio_module = 'on'      # extract maximum intensity divided by average intensity from each spectrum as a feature
extract_texture_module = 'on'              # extract texture_sum from each spectrum as a feature, and output texture spectra
extract_signal_to_noise_module = 'on'      # extract signal to noise ratio from each spectrum as a feature
extract_neighbor_distance_module = 'off'   #  this module requires a master file that indicate the positions of the sample in physical space, it needs the input "num_of_smpls_per_row"
add_feature_to_csv_module = 'on'  # if there is a master file, the feature will be added to the master file, otherwise, it will write a new file


###############################################################################
# DO NOT CHANGE ANYTHING FROM HERE
###############################################################################
on_the_fly(folder_path, base_filename, index, last_scan, calibration_file, PP,
            pixelSize, num_of_smpls_per_row, extract_Imax_Iave_ratio_module, 
            extract_texture_module, extract_signal_to_noise_module,
            extract_neighbor_distance_module, add_feature_to_csv_module)
