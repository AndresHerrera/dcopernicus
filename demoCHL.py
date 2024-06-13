from download import DownloadCopernicus
from convert import ConvertCopernicus

config_chl={
  "dataset_id":"cmems_obs-oc_glo_bgc-plankton_nrt_l4-gapfree-multi-4km_P1D",
  "variables":["CHL", "CHL_uncertainty"],
  "minimum_longitude":-85.0,
  "maximum_longitude":-77.0,
  "minimum_latitude":0.,
  "maximum_latitude":8.,
  "minimum_depth": 0,
  "maximum_depth": 0,
}

getCHL = DownloadCopernicus("2024-06-04","2024-06-05","chl_demo.nc","downloads/",config_chl) 
getCHL.downloadSubset()
convertCHL = ConvertCopernicus("chl_demo.nc","downloads/","chl_demo.tif","converted/","CHL","epsg:4326")
convertCHL.fromNetCDFtoGeoTiff()

