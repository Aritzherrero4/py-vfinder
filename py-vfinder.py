#!/usr/bin/python3
#A simple program to represent the input file (matrix) of temperatures as a heat-map.
#Aritz Herrero Perez de Albeniz

import sys
import numpy as np
import matplotlib.pylab as plt

#Generate, plot and save as .png the results of the file
def heatmap2d(arr: np.ndarray, name):
    plt.imshow(arr, cmap='magma')
    plt.axis('off')
    plt.savefig(name+".png",bbox_inches='tight')
    plt.show()

#Error checking: Ensure the require parameter is provided
if (len(sys.argv)!=2):
    print("Missing file to open.\nUse: py-vfinder.py <filename>")
    exit(1)
#Check the provided file exists
try:
    f = open ( sys.argv[1] , 'r')
except: 
    print("Error: The input file does not exist.")
    exit(1)

#Discard the first line. Read and print the dimensions of the file    
f.readline()
dat = f.readline().split("\t")
print("Matrix dimensions:" , dat[0], "  x",dat[1])
f.close()

#Decide which file type is. Clear unnecessary data and read the matrix 
if (sys.argv[1].split(".")[1]=="emaitza"):
    sareta =  np.genfromtxt(sys.argv[1],skip_header=2,skip_footer=4)
else:
    sareta =  np.genfromtxt(sys.argv[1],skip_header=2)

#Call the function to plot the matrix
heatmap2d(sareta, sys.argv[1])
exit(0)