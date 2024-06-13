from download import DownloadCopernicus
from convert import ConvertCopernicus

config_spm={
  "dataset_id":"cmems_obs-oc_glo_bgc-transp_my_l3-multi-4km_P1D",
  "variables":["SPM"],
  "minimum_longitude":-85.0,
  "maximum_longitude":-77.0,
  "minimum_latitude":0.,
  "maximum_latitude":8.,
  "minimum_depth": 0,
  "maximum_depth": 0,
}

getSPM = DownloadCopernicus("2024-05-28","2024-05-29","spm_demo.nc","downloads/",config_spm) 
getSPM.downloadSubset()
convertSPM = ConvertCopernicus("spm_demo.nc","downloads/","spm_demo.tif","converted/","SPM","epsg:4326")
convertSPM.fromNetCDFtoGeoTiff()