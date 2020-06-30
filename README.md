# Autodock-Vina-batch-mode
Batch mode script for small molecules docking tests via Autodock Vina

#Overview
This is a python based batch mode script for the docking of small molecules to a pre-defined receptor in parallel. The package also provides an overall evaluation of the performance of the entire docking simulation.

- [System Requirements](#System-requirements)
- [Installation](#installation)
- [Installation Guide](#Installation-Guide)
- [Expected run time](#Expected-run-time)
- [License](#license)

# System Requirements
The package has been tested on the following systems:

- Linux:  Ubuntu 16.04  
- Linux:  Centos 3.10.0
- MacOS:  macOS Mojave


# Expected run time
This demo of 20 example small molecules on an 8-threaded computer (10 minutes)
A library of 1,600 small molecules on a 16-threaded computer (3-5 hours).
* If the average number of atoms of small molecules is greater than 100, the time of simulation will be quite long.

# Results