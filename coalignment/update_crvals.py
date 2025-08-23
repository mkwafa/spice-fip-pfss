from astropy.io import fits
from pathlib import Path

def obtain_crval(path):
    hdul = fits.open(path)
    for hdu in hdul:
        return hdu.header.get('CRVAL1'), hdu.header.get('CRVAL2')

def update_crvals(target_path, new_crval1, new_crval2, output_path=None):
    hdul = fits.open(target_path, mode='update' if output_path is None else 'readonly')

    for hdu in hdul:
        header = hdu.header
        if 'CRVAL1' in header and 'CRVAL2' in header:
            print(f"[MODIF] {target_path.name} - Ancien CRVAL1/2: {header['CRVAL1']:.2f}, {header['CRVAL2']:.2f}")
            header['CRVAL1'] = new_crval1
            header['CRVAL2'] = new_crval2
            print(f"         Nouveau CRVAL1/2: {new_crval1:.2f}, {new_crval2:.2f}")

    if output_path:
        output_path.parent.mkdir(parents=True, exist_ok=True)
        hdul.writeto(output_path, overwrite=True)
        print(f"→ Fichier sauvegardé dans : {output_path}")
    else:
        hdul.flush()
        print(f"→ Fichier mis à jour sur place : {target_path}")

    hdul.close()

input_root = Path("../run_saffron/saffron_run_results")
matching_dirs = [p for p in input_root.rglob("solo_L2.5_spice-n*0600*") if p.is_dir()]
coalign_root = Path("./coalign_results")
output_root = Path("../run_saffron/saffron_run_results_corrige")

for raster_dir in matching_dirs:
    if not raster_dir.is_dir():
        continue

    raster_name = raster_dir.name
    coalign_fits = coalign_root / raster_name / "output.fits"

    if not coalign_fits.exists():
        print(f"[SKIP] Aucun fichier output.fits trouvé pour {raster_name}")
        continue

    try:
        new_crval1, new_crval2 = obtain_crval(coalign_fits)
    except Exception as e:
        print(f"[ERREUR CRVAL] {raster_name} : {e}")
        continue
    output_subdir = output_root / raster_name
    output_subdir.mkdir(parents=True, exist_ok=True)

    for fits_file in raster_dir.glob("*.fits"):
        output_file = output_subdir / fits_file.name
        try:
            update_crvals(fits_file, new_crval1, new_crval2, output_file)
        except Exception as e:
            print(f"[ERREUR update] {fits_file.name} : {e}")

