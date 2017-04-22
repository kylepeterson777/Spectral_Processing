#-------------------------------------------------------------------------------
# Name:        SpecProcess.py
# Purpose:     Spectroscopy data processing: Carlyle Lake
#
# Author:      Kyle T. Peterson
#              Saint Louis University
#              Center for Sustainability
# Created:     09/03/2017
#-------------------------------------------------------------------------------
# Import Modules
import os,csv, sys
import numpy as np
#import xlswriter
###############
# set paths and variables
# path to interpolated spec txt file
interpolatedSpec = r'E:\PythonProgramming\Final\Oct28_interpolated.txt'
outCsv = r'E:\PythonProgramming\FinalSpecCsv.txt'

#ignore first 32 rows
Specdata = np.genfromtxt(interpolatedSpec, dtype=None, skip_header=32)
#print(Specdata)

#gather wavelength values/labels
wvl = Specdata[:,0]
print("wavelengths collected")
#calculate mean for each sample site, specify each column
d1 = np.mean(Specdata[:,[1,2,3]], axis=0)
d2 = np.mean(Specdata[:,[4,5,6]], axis=0)
d3 = np.mean(Specdata[:,[7,8,9]], axis=0)
m1 = np.mean(Specdata[:,[10,11,12]], axis=0)
m2 = np.mean(Specdata[:,[13,14,15]], axis=0)
m3 = np.mean(Specdata[:,[16,17,18]], axis=0)
m4 = np.mean(Specdata[:,[19,20,21]], axis=0)
s1 = np.mean(Specdata[:,[22,23,24]], axis=0)
s2 = np.mean(Specdata[:,[25,26,27]], axis=0)
s3 = np.mean(Specdata[:,[28,29,30]], axis=0)
print("mean spectra calculated for each site")

#populate new array with ave values, axis 1=rows, axis 0=cols
newSpec = np.column_stack((wvl,d1,d2,d3,m1,m2,m3,m4,s1,s2,s3), 0)
print("created new array with mean reflectance values")

#transpose data (swap x and y axes)
newSpecT = np.transpose(newSpec)

#save array as csv file
SpecCsv = np.savetxt(outCsv, newSpecT, delimiter=",")
print("Saved data as csv file")







