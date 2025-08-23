import os
from pathlib import Path
import numpy as np
from astropy.io import fits
from sunpy.map import Map
import astropy.units as u
from getmap import to_submap
from euispice_coreg.hdrshift.alignment import Alignment
from euispice_coreg.plot.plot import PlotFunctions
from euispice_coreg.utils.Util import AlignCommonUtil
from scipy.optimize import minimize
import warnings

USE_DATEAVG_METHOD = True

# L3_folder = folder containing SAFFRON results (produced after running run_saffron)
L3_folder = Path("/home/wmouici/stage/data/saffron_run_results")
L3_path = list(L3_folder.glob('*/*770.42*'))

# FSI_folder = folder containing EUI/FSI input data (must be available to the user)
FSI_folder = Path("/archive/SOLAR-ORBITER/EUI/data_internal/L2/")
FSI_path = []


for i in range(len(L3_path)):

    if USE_DATEAVG_METHOD:
        hdul = fits.open(L3_path[i])
        dateavg = np.datetime64(hdul[0].header['DATE-AVG'])
        year = dateavg.astype(object).year
        month = dateavg.astype(object).monthdans 
        day = dateavg.astype(object).day
        hour = dateavg.astype(object).hour

        FSI_all_path = []
        FSI_all_path.extend(list(FSI_folder.glob(f"{year}/{month:02d}/{day:02d}/*fsi174-image_{year}{month:02d}{day:02d}T{hour:02d}*")))
        FSI_all_path.extend(list(FSI_folder.glob(f"{year}/{month:02d}/{day:02d}/*fsi174-image_{year}{month:02d}{day:02d}T{hour-1:02d}*")))

        FSI_all_path = np.array(FSI_all_path, dtype=object)
        FSI_times = np.array([fits.open(path)[1].header['DATE-OBS'] for path in FSI_all_path], dtype='datetime64[ms]')
        FSI_path.append(FSI_all_path[np.argmin((FSI_times - dateavg).astype(int)**2)])

        path_fsi = Path(str(FSI_path[i]))
        path_hri = Path(str(L3_path[i]))

    else:
        all_dates = L3_path[i].parent.name[22:37]
        year = all_dates[:4]
        month = all_dates[4:6]
        day = all_dates[6:8]
        hour = all_dates[9:11]
        minute = all_dates[11:13]

        FSI_path.append(list(FSI_folder.glob(f"{year}/{month}/{day}/*fsi304-image_{year}{month}{day}T{hour}*"))[0])
        path_fsi = Path(str(FSI_path[i]))
        path_hri = Path(str(L3_path[i]))


    raster_name = path_hri.parent.name
    path_save_fig = Path(f"../data/coalign_results_ne8_fsi174_avg/{raster_name}")
    path_save_fits = path_save_fig
    path_save_fig.mkdir(parents=True, exist_ok=True)

    tmp_path = Path("./tmp/")
    tmp_path.mkdir(exist_ok=True)
    fsi_map = Map(path_fsi)
    hdul = fits.open(path_hri)
    data = hdul[0].data * hdul[2].data
    map_ = Map([data, hdul[0].header])
    sub_map = to_submap(target_map=fsi_map, source_map=map_, expand=[50, 50] * u.arcsec)
    sub_map.save(tmp_path / path_fsi.name, overwrite=True)
    map_.save(tmp_path / path_hri.name, overwrite=True)
    path_fsi = str(tmp_path / path_fsi.name)
    path_hri = str(tmp_path / path_hri.name)

    lag_crval1 = np.arange(-80, 0, 2)
    lag_crval2 = np.arange(-80, 0, 2)
    lag_crota = [0]
    lag_cdelta1 = [0]
    lag_cdelta2 = [0]

    A = Alignment(
        large_fov_known_pointing=path_fsi,
        small_fov_to_correct=path_hri,
        lag_crval1=lag_crval1,
        lag_crval2=lag_crval2,
        lag_cdelta1=lag_cdelta1,
        lag_cdelta2=lag_cdelta2,
        lag_crota=lag_crota,
        parallelism=True,
        use_tqdm=True,
        small_fov_window=-1,
        large_fov_window=-1
    )

    corr = A.align_using_helioprojective(method='correlation')

    parameter_alignment = {
        "lag_crval1": lag_crval1,
        "lag_crval2": lag_crval2,
        "lag_crota": lag_crota,
        "lag_cdelta1": lag_cdelta1,
        "lag_cdelta2": lag_cdelta2,
    }

    PlotFunctions.plot_correlation(
        corr, show=True,
        path_save=os.path.join(path_save_fig, "correlation.pdf"),
        **parameter_alignment
    )
    PlotFunctions.plot_co_alignment(
        small_fov_window=-1,
        large_fov_window=-1,
        corr=corr,
        small_fov_path=path_hri,
        large_fov_path=path_fsi,
        show=True,
        results_folder=path_save_fig,
        levels_percentile=[95],
        **parameter_alignment
    )
    AlignCommonUtil.write_corrected_fits(
        path_l2_input=path_hri,
        window_list=[-1],
        path_l3_output=str(Path(path_save_fits) / "output.fits"),
        corr=corr,
        **parameter_alignment
    )
