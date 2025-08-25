
# spice-fip-pfss

This repository provides a pipeline to:
1. run **SAFFRON** on SPICE rasters (radiance/FIP products),
2. **co-align** SPICE with **EUI/FSI** and update WCS (**CRVALs**),
3. (optional) run **Doppler line fitting** with `spice-line-fits`,
4. **visualize** results and perform **PFSS** extrapolation in a notebook.




## Install and Set-up

### 1) Clone THIS repo
```bash
git clone https://github.com/<your-user>/spice-fip-pfss.git
cd spice-fip-pfss
````

### 2) (optional but recommended) create a fresh env

```bash
python -m venv .venv
source .venv/bin/activate  # on Windows: .venv\Scripts\activate
```

### 3) Base Python packages

```bash
pip install numpy scipy astropy sunpy pfsspy matplotlib shapely
```

### 4) Clone & install SAFFRON (follow their README)

```bash
git clone https://github.com/slimguat/saffron-spice
```

*(install inside its own instructions, then come back here)*

### 5) Clone & install EUI–SPICE co-registration (follow their README)

```bash
git clone https://github.com/adolliou/euispice_coreg
```

*(install inside its own instructions, then come back here)*

### 6) (Optional) Install spice-line-fits if you need Doppler fits

```bash
git clone https://github.com/jeplowman/spice-line-fits
```

*(install inside its own instructions, then come back here)*

---

## Step 1 — SAFFRON

1. Install **saffron-spice** and follow their README.

2. From the **saffron-spice** repo, go to `run_saffron/` and run:

```bash
python saffron_run_fitting.py
```

3. The outputs (L2.5 products) will appear in:

```
run_saffron/saffron_run_results/
```
---

## Step 2 — Co-alignment + CRVAL update

1. Make sure `euispice_coreg` is installed and importable.

2. In **this** repo go to `coalignment/` and run:

```bash
python coalignment/coalign2.py
```

This will produce a small text log (e.g., `fsi_used_log.txt`) that lists the FSI file used for each raster.

3. Update the CRVALs in the SAFFRON outputs:

```bash
python coalignment/update_crvals.py
```

This reads rasters from:

```
run_saffron/saffron_run_results/
```

and writes corrected files to:

```
run_saffron/saffron_run_results_corrected/
```

Use these corrected **L2.5** rasters for the next steps.

---

## Step 3 (optional) — Doppler line fitting

1. Install `spice-line-fits` and follow their README.

2. Use your starting rasters (same ones used in `run_saffron.py`) to produce **PSF-corrected line-fit FITS** files.

3) Alternatively, **download the pre-computed fitted results from Google Drive** and unzip them into **`doppler_map/`**:

- **Download:** [Google Drive link](<https://drive.google.com/drive/folders/1px-ro1fIgues5GipbZfAYOwLjFHxrwXU?usp=drive_link>)
- **Unzip** the archive into the folder **`doppler_map/`** in this repo.
- **Keep the folder structure** exactly as provided: **each raster has its own subfolder** containing its FITS files.

---

## Step 4 — Notebook visualization + PFSS

1. Open the notebook:

```
analyse_2103/analyse_2103.ipynb
```

2. Ensure `pfsspy` is installed:

```bash
pip install pfsspy
```

3. Run the cells to:

* visualize radiance, FIP and Doppler maps,
* do the reprojection using the same FSI file identified during the co-alignment step (see `coalignment/fsi_used_log.txt`); a copy of this FSI file is available in the corresponding analyse_.../ folder
* load the GONG synoptic map (also in `analyse_.../`) and perform the PFSS extrapolation.

---



## External Repos

* SAFFRON for SPICE → [https://github.com/slimguat/saffron-spice](https://github.com/slimguat/saffron-spice)
* EUI–SPICE co-registration → [https://github.com/adolliou/euispice\_coreg](https://github.com/adolliou/euispice_coreg)
* SPICE line fitting → [https://github.com/jeplowman/spice-line-fits](https://github.com/jeplowman/spice-line-fits)
* PFSS (pfsspy) → [https://github.com/dstansby/pfsspy](https://github.com/dstansby/pfsspy)

```
```
