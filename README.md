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
# (install inside its own instructions, then come back here)

### 4) Clone & install EUI–SPICE co-registration (follow their README)
git clone https://github.com/adolliou/euispice_coreg
# (install inside its own instructions, then come back here)

### 5) (Optional) Install spice-line-fits if you need Doppler fits
git clone https://github.com/jeplowman/spice-line-fits
# (install inside its own instructions, then come back here)