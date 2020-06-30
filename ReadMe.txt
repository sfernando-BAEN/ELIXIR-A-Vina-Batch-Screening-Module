Name:
Batch mode script for small molecules docking tests via Autodock Vina

Description:
This is a python based batch mode script for the docking of small molecules to a pre-defined receptor in parallel. The package also provides an overall evaluation of the performance of the entire docking simulation.

Supported operating systems:
macOS (Runs on macOS Mojave or later)
Linux (Runs on Ubuntu 16.04 or later ,or Centos 3.10.0)

Requirements & Installation:
To run the script, you need to install python in your environment, python versions can be 2.7.16, 3.7.4 or later. The numpy package version 1.17.2 or later is required to generate the evaluation table.

AutoDock Vina 4.2.6
AutoDock Vina has already been included in the folder. AutoDock Vina could also be downloaded from its official website:
http://autodock.scripps.edu/downloads/autodock-registration/autodock-4-2-download-page/

Open Babel is a good choice for ligand preparation and is not used directly in this script.

UCSF Chimera 1.14 or MGLtools 1.5.7 can prepare the protein pdbqt files and docking grids.

Batch docking procedures:
To do a batch docking, the (protein) receptor, small molecules, and the desired grid box size should be prepared. These files should be placed in the working folder.
1. The protein receptor file should be placed in "./protein" folder with the extension ".pdbqt".

2. The grid box will determine the space for small molecules to dock on the receptor. It should be noted that the larger the grid box, the slower the docking speed.
A tutorial for the grid options using MTLtools is given below:
http://vina.scripps.edu/tutorial.html 
Then, all the information in the ".conf.txt" file including "receptor, 'center_x, center_y, center_z, size_x, size_y, size_z" should be updated using the visualization software (such as Chimera or MGLtools).

3. The small molecules can be prepared with open babel command lines.
For example: file names of the molecules: Molecules_XXXX.mol2; XXXX is the IDs of the small molecules from 0001 to 2000.
*******
$obabel -imol2 *.mol2 -opdbqt -m
*******
Then, all files should be saved in pdbqt format into the "./ligands" folder.

4. Open a terminal in the path of the script folder, or "cd /path_to_the_script_folder"
*******
$python Quickrun.py
*******
(Optional: the replications for each small molecule can be edited in line34 of ".Quickrun.py", default value of the replications is 3.)

5. The output files with docking poses will be saved in "./out" folder, which can be analyzed via Chimera or MGLtools.
Also, the files ".VinaScore.csv" located in the script folder shows the overall performance of the docking simulation.

The expected run time for a normal computer:
This demo of 20 example small molecules on an 8-threaded computer (10 minutes)
A library of 1,600 small molecules on a 16-threaded computer (3-5 hours).
* If the average number of atoms of small molecules is greater than 100, the time of simulation will be quite long.
