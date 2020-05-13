# py-vfinder

A simple program to represent the input file (matrix) of temperatures as a heat-map.

## Requirements
This program is meant to be run with Python3. 
The required packets are ```numpy 1.18.4 or higher``` and ```matplotlib 3.2.1 or higher``` but it may work with older versions.

### Getting the code
Run ```https://github.com/Aritzherrero4/py-vfinder.git``` or download the source code directly as a zip from this repo.
### Installing the requirements

To install these packets, install pip3 if not installed and run ```pip3 install -r requirements.txt```

You can also manually install them by running ```pip install numpy``` and ```pip install matplotlib```.

### Input requirements

This code expects the following format, for the file .emaitza and .txipak:
Both of them must start with a line followed by a line with the dimensions of the matrix:
```
Tmin_hasi 20.0  Tmax_hasi 160.0  
1000	  2000 
```
After that, the matrix to use. m rows of n float numbers separated by a space (" ").
```
20.00 20.00 [...] 20.00 20.0
            [...]
20.00 20.00 [...] 20.00 20.0
```

The file-type ```.emaitza``` must end with 4 lines:
```



 >>> Konfigurazio onena: 2	 Tbb: 69.36
```
## Time to run it

To execute the code run: ```python3 py-vfinder.py <inputfile>```

A window with the visualization should open and a file with the name <filename>.png should be generated.