# spice-fip-pfss

This repository provides a pipeline to:
1. run **SAFFRON** on SPICE rasters (radiance/FIP products),
2. **co-align** SPICE with **EUI/FSI** and update WCS (**CRVALs**),
3. (optional) run **Doppler line fitting** with `spice-line-fits`,
4. **visualize** results and perform **PFSS** extrapolation in a notebook.

# Install and Set-up

### 1) Clone THIS repo
git clone https://github.com/<your-user>/spice-fip-pfss.git
cd spice-fip-pfss

### (optional but recommended) create a fresh env
python -m venv .venv
source .venv/bin/activate  # on Windows: .venv\Scripts\activate

### 2) Base Python packages
pip install numpy scipy astropy sunpy pfsspy matplotlib shapely

### 3) Clone & install SAFFRON (follow their README)
git clone https://github.com/slimguat/saffron-spice
### (install inside its own instructions, then come back here)

### 4) Clone & install EUI–SPICE co-registration (follow their README)
git clone https://github.com/adolliou/euispice_coreg
### (install inside its own instructions, then come back here)

### 5) (Optional) Install spice-line-fits if you need Doppler fits
git clone https://github.com/jeplowman/spice-line-fits
### (install inside its own instructions, then come back here)

# Step 1 — SAFFRON

### 1) Install saffron-spice and follow their README.

### 2) In this repo go to run_saffron/ and run:

python saffron_run_fitting.py

### 3) The outputs (L2.5 products) will appear in:

run_saffron/saffron_run_results/

# Step 2 — Co-alignment + CRVAL update

### 1) Make sure euispice_coreg is installed and importable.

### 2) In this repo go to coalignment/ and run:
python coalign2.py

This will produce a small text log (e.g., coalign_log.txt) that lists the FSI file used for each raster.

### 3) Update the CRVALs in the SAFFRON outputs : 
python update_crvals.py

This reads rasters from : run_saffron/saffron_run_results/
and writes corrected files to : run_saffron/saffron_run_results_corrected/

Use these corrected L2.5 rasters for the next steps.

# Step 3 (optional) — Doppler line fitting

### 1) Install spice-line-fits and follow their README.

### 2) Use your starting rasters (same ones used in run_saffron.py) to produce PSF-corrected line-fit FITS files.

### 3) Alternatively, download from this drive link pre-computed fitted results locally:
Put each FITS inside its raster-specific subfolder.
analyse_2103/

# Step 4 — Notebook visualization + PFSS

### 1) Open the notebook:
analyse_2103/analyse_2103.ipynb
### 2) Ensure pfsspy is installed:
pip install pfsspy
### 3) Run the cells to:
visualize radiance/FIP maps,
reprojection using the FSI file provided in analyse_2103/,
load the GONG synoptic map (also in analyse_2103/) and perform the PFSS extrapolation.
