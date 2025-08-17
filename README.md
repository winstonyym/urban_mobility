# GeoAI for Urban Mobility

# Overview

This repository includes code notebooks detailing the exploration analysis on the [open-access mobile app dataset](https://zenodo.org/records/13327082) provided by and [data documentation](https://www.ucl.ac.uk/bartlett/sites/bartlett/files/casa_working_paper_240.pdf).


# System Requirements

## Hardware Requirements

To run the demo workflow, users require only a standard computer with enough RAM to support the operations defined by a user. Having >4GB RAM would be preferable. 

The demo was implemented on a MacBook Pro, M1 Chip with 16GB RAM and 512GB storage.

## Software Requirements

### OS Requirements

The package development version is tested on MacOS operating systems. The implementation would work on the following systems:

Linux: Ubuntu 22.04  
Mac OSX:  
Windows:  

Before running the demo, users should have Python version 3.8.0 or higher.

# Installation Guide & Dependencies

1. Clone the code repository either with CLI or by accessing the code base

```
$ git clone https://github.com/winstonyym/urban_mobility.git
```

2. Navigate to the local folder location
```
$ cd urban_mobility
```

3. Open up a terminal/command prompt and install the conda environment (works for Linux/MacOS/Windows)

```
$ chmod +x ./setup.sh
$ ./setup.sh
```

4. Installation completed

(Optional) For JupyterLab / JupyterNotebook users, you can additionally add a notebook kernel via:

5. Use environment

```
$ conda activate urban_mobility
$ jupyter lab
```

# Repository Structure
- `data` (Placeholder folder for mobility data)
- `notebooks` (Notebooks for exploratory analysis)



# Citation

Zhong, Chen., et al., Anonymised human location data for urban mobility research. CASA working paper 240, 2024. Accessed from https://www.ucl.ac.uk/bartlett/sites/bartlett/files/casa_working_paper_240.pdf
