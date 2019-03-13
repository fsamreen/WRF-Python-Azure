![Image of Ensemble](https://github.com/fsamreen/WRFV1/blob/Single-node/Images/ensemble-no-sub-100mm.jpg)

https://www.ensembleprojects.org


This code is written as part of the EPSRC project - "Models in the Cloud".
This code creates a cluster of machines having WRF installed on it to support running multiple simulations.

# Required inputs
 1) Machine images of WRF-master and WRF-client. These images can be created by following a code on the Ensemble web page.
 2) We have provided some options of VM machine configurations to run a simulation of 4 months data.
 3) You have to provide Azure credentials in a file, credentials.txt. Make sure not to add any extra blank space at end of the line.
 4) You have to use same login and password which are used while creating mother machine images.
 5) For new users, we would recommend to stick with the default settings/values in the code.
