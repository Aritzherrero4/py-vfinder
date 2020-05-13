#!/usr/bin/python3
import sys
import numpy as np
import matplotlib.pylab as plt

def heatmap2d(arr: np.ndarray, name):
    plt.imshow(arr, cmap='magma')
    plt.axis('off')
    plt.savefig(name+".png",bbox_inches='tight')
    plt.show()

if (len(sys.argv)!=2):
    print("Missing file to open.\nUse: py-vfinder.py <filename>")
    exit(1)

try:
    f = open ( sys.argv[1] , 'r')
except: 
    print("Error: The input file does not exist.")
f.readline()
dat = f.readline().split("\t")
print("Matrix dimmensions:" , dat[0], "  x",dat[1])
f.close()

if (sys.argv[1].split(".")[1]=="emaitza"):
    sareta =  np.genfromtxt(sys.argv[1],skip_header=2,skip_footer=4)
else:
    sareta =  np.genfromtxt(sys.argv[1],skip_header=2)

heatmap2d(sareta, sys.argv[1])
exit(0)