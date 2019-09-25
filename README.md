# AquaResp Swim V.0.5
Automating Aquatic Swimming Respirometry. Focused on automating intermittent respirometry experiments for aquatic animals.

September 25th 2019

<i>Finally</i>. Aquaresp Swim has arrived. 

The current version has been tested in several experiments, but there might still be bugs - thus version 0.5. As with Aquaresp, it only works on Windows 10 64-bit. Please create issues in this repo (upper left corner in the menu) if you have any issues when using it.

This repo contains the GUI and code controlling of the experiment, and the code calculating the results are licensed under Creative Commons BY-SA.

<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/4.0/88x31.png" /></a><br />This work is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">Creative Commons Attribution-ShareAlike 4.0 International License</a>.

We have not yet published the code or a paper reference to cite. 

## Installation
The present version is only supported on Windows 10 64 bit.

Download the by pressing "Clone or Download" button in the top right corner of this screen. 

### Windows 10 - 64bit:

#### Step 1 - downloading Python
##### First run 1.vbs in the Installation folder
This downloads Python for you, the version that has been used for testing (3.7.4. - 64-bit)

#### Step 2 - installing Python and libraries
##### Run 2.bat
This initiates  Python installation for you.

If this fails, open the downloaded Python (InstallPython.exe), and make sure to enable the option "Add to PATH" during the first step of installation


#### After Python has been installed
##### Double click the CheckLibraries.py in the installation folder.
This installs the libraries needed to run AquaResp 3.0 ASAP
The buttons will change to green and display "OK" when libraries are installed.

---
If this step is failing, open the command prompt (WinButton + R, write "cmd", and press enter), and run the installation commands for the specific library. The following are needed for AQ3

python -m pip install bokeh

python -m pip install numpy

python -m pip install scipy

python -m pip install matplotlib

python -m pip install -U wxPython

python -m pip install mcculw

--

#### Step 3 - adding Icons to your desktop
##### Run Create Links on Desktop.vbs  (in the Aquaresp 3 main folder)
This creates icons on the desktop. You can do that manually aswell.
