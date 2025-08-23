from astropy.coordinates import SkyCoord
from astropy import units as u
from sunpy.physics.differential_rotation import solar_rotate_coordinate
import sunpy
import numpy as np

def get_coord_mat(map, as_skycoord=False):
    res = sunpy.map.maputils.all_coordinates_from_map(map)
    if as_skycoord:
        return res
    try:
        lon = res.spherical.lon.arcsec
        lat = res.spherical.lat.arcsec
    except AttributeError:
        lon = res.lon.value
        lat = res.lat.value
    return lon, lat

def to_submap(target_map,source_map , expand=[0, 0] * u.arcsec,solar_rotation=True): #expand bords x et y en arcsec
      """
      Rotates the boundary coordinates of source_map to target_map's observer's perspective
      and creates a submap from target_map using the rotated boundaries.
      Parameters:
      - source_map: SunPy map object to rotate boundaries from.
      - target_map: SunPy map object to create the submap from.
      Returns:
      - SunPy map object: Submap of target_map with the rotated boundary coordinates from source_map.
      """
      map1 =  source_map
      map2 =  target_map
      lonlat_coords = get_coord_mat(map1, as_skycoord=True)
      # Get the boundaries of map1 in SkyCoord format
      bottom_left = SkyCoord(lonlat_coords.Tx.min(), lonlat_coords.Ty.min(), frame=lonlat_coords.frame)
      top_right = SkyCoord(lonlat_coords.Tx.max(), lonlat_coords.Ty.max(), frame=lonlat_coords.frame)
      # print(bottom_left,top_right)
      # print('values in map1',bottom_left,top_right)
      if solar_rotation:
        # Solar rotate the boundaries to map2's observer time and perspective
        bottom_left_rotated = solar_rotate_coordinate(bottom_left, observer=map2.observer_coordinate,)
        top_right_rotated = solar_rotate_coordinate(top_right, observer=map2.observer_coordinate,)
      else:
        #reporojecting to the observer of map2
        bottom_left_rotated = bottom_left.transform_to(map2.coordinate_frame)
        top_right_rotated = top_right.transform_to(map2.coordinate_frame)
        # print(bottom_left_rotated,top_right_rotated)
      if any([np.isnan(bottom_left_rotated.Tx),np.isnan(top_right_rotated.Tx),np.isnan(bottom_left_rotated.Ty),np.isnan(top_right_rotated.Ty)]):
        # print in red color
        print("\033[91mThere is a nan in the coordinates\033[00m")
        print(bottom_left_rotated,top_right_rotated)
        new_lonlat_coords = lonlat_coords.transform_to(map2.coordinate_frame)
        bottom_left_rotated = SkyCoord(np.nanmin(new_lonlat_coords.Tx), np.nanmin(new_lonlat_coords.Ty), frame=new_lonlat_coords.frame)
        top_right_rotated = SkyCoord(np.nanmax(new_lonlat_coords.Tx),np.nanmax( new_lonlat_coords.Ty), frame=new_lonlat_coords.frame)
      # print('values rotated to map2',bottom_left_rotated,top_right_rotated)
      offset_bottom_left = SkyCoord(
          bottom_left_rotated.Tx - expand[0],
          bottom_left_rotated.Ty - expand[1],
          frame=bottom_left_rotated.frame,
      )
      offset_top_right = SkyCoord(
          top_right_rotated.Tx + expand[0],
          top_right_rotated.Ty + expand[1],
          frame=top_right_rotated.frame,
      )
      # print("offsets",offset_bottom_left,offset_top_right)
      # Create a submap in map2 using the pixel coordinates
      submap = map2.submap(
          bottom_left=offset_bottom_left,
          top_right=offset_top_right,
      )
      return submap