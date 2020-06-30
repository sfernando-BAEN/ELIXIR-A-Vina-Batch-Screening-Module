# ELIXIR-A Vina Batch Screening Module
Batch mode script for small molecules docking tests via Autodock Vina

# Overview
This is a python based batch mode script for the docking of small molecules to a pre-defined receptor in parallel. The package also provides an overall evaluation of the performance of the entire docking simulation.

- [System Requirements](#System-requirements)
- [Installation Guide](#Installation-Guide)
- [Expected run time](#Expected-run-time)
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
## Installation time
You can directly run [Quickrun.py](./Vina_Docking_batch_source_code/Quickrun.py) from the working folder without installation of the program itself.

# Expected run time
This demo of 20 example small molecules on an 8-threaded computer (10 minutes)
A library of 1,600 small molecules on a 16-threaded computer (3-5 hours).
\* If the average number of atoms of small molecules is greater than 100, the time of simulation will be quite long.

# Results

# License
+ [Apache-2.0 License](./LICENSE)