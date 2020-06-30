# ELIXIR-A Vina Batch Screening Module
Batch mode script for small molecules docking tests via Autodock Vina

# Overview
This is a python based batch mode script for the docking of small molecules to a pre-defined receptor in parallel. The package also provides an overall evaluation of the performance of the entire docking simulation.

- [Repo Contents](#Repo-Contents)
- [System Requirements](#System-requirements)
- [Installation Guide](#Installation-Guide)
- [Expected run time](#Expected-run-time)
- [Demo batch docking procedures](#demo)
- [License](#license)

# Repo Contents
- [Vina_Docking_batch_source_code](./Vina_Docking_batch_source_code/): `Python` source code with data input
- [Vina_docking_batch_example_output_demo](./Vina_docking_batch_example_output_demo/): Demo with sample inputs and outputs

# System Requirements
The package has been tested on the following systems:

- Linux:  Ubuntu 16.04  
- Linux:  Centos 3.10.0
- MacOS:  macOS Mojave

# Installation Guide
To run the script, you need to install python in your environment, python versions can be 2.7.16, 3.7.4 or later. The numpy package version 1.17.2 or later is required to generate the evaluation table.

To install python on OS X & Linux:

```sh
sudo apt-get install python3
```

To install numpy package on OS X & Linux:

```sh
sudo apt install python3-pip
pip install numpy
```

## AutoDock Vina 4.2.6
AutoDock Vina has already been included in this [package](./Vina_Docking_batch_source_code/autodock_vina). AutoDock Vina could also be downloaded from its [official website](http://autodock.scripps.edu/downloads/autodock-registration/autodock-4-2-download-page/)

## Open Babel 2.4.0
[Open Babel](http://openbabel.org/wiki/Main_Page) is a good choice for ligand preparation and is not used directly in this script.

## UCSF Chimera 1.14 and MGLtools 1.5.7
Both [UCSF Chimera](https://www.cgl.ucsf.edu/chimera/download.html) and [MGLtools](http://mgltools.scripps.edu/downloads) can prepare the protein pdbqt files and docking grids.

# Installation time
You can directly run [Quickrun.py](./Vina_Docking_batch_source_code/Quickrun.py) from the working folder without installation of the program itself.

# Expected run time
This demo of 20 example small molecules on an 8-threaded computer (10 minutes)
A library of 1,600 small molecules on a 16-threaded computer (3-5 hours).
\* If the average number of atoms of small molecules is greater than 100, the time of simulation will be quite long.

# Demo batch docking procedures
To do a batch docking, the (protein) receptor, small molecules, and the desired grid box size should be prepared. These files should be placed in the working folder.
1. The protein receptor file should be placed in [protein](./Vina_docking_batch_example_output_demo/protein/) folder with the extension [".pdbqt"](./Vina_docking_batch_example_output_demo/protein/SARS-COVID-2_RBD.pdbqt).

2.The grid box will determine the space for small molecules to dock on the receptor. It should be noted that the larger the grid box, the slower the docking speed.
Here is a [tutorial](http://vina.scripps.edu/tutorial.html) for the grid options using MTLtools.
Then, all the information in the [conf.txt](./Vina_docking_batch_example_output_demo/conf.txt) file including "receptor, 'center_x, center_y, center_z, size_x, size_y, size_z" should be updated using the visualization software (such as Chimera or MGLtools).

3.

# License
+ [Apache-2.0 License](./LICENSE)