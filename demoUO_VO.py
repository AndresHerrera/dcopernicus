from download import DownloadCopernicus
from convert import ConvertCopernicus

config_uo_vo={
  "dataset_id":"cmems_mod_glo_phy-cur_anfc_0.083deg_P1D-m",
  "variables":["uo","vo"],
  "minimum_longitude":-85.0,
  "maximum_longitude":-77.0,
  "minimum_latitude":0.,
  "maximum_latitude":8.,
  "minimum_depth": 0,
  "maximum_depth": 0,
}

getUO = DownloadCopernicus("2024-06-04","2024-06-05","uo_demo.nc","downloads/",config_uo_vo)
getVO = DownloadCopernicus("2024-06-04","2024-06-05","vo_demo.nc","downloads/",config_uo_vo) 

getUO.downloadSubset()
getVO.downloadSubset()

convertUO = ConvertCopernicus("uo_demo.nc","downloads/","uo_demo.tif","converted/","uo","epsg:4326")
convertVO = ConvertCopernicus("vo_demo.nc","downloads/","vo_demo.tif","converted/","vo","epsg:4326")

convertUO.fromNetCDFtoGeoTiff()
convertVO.fromNetCDFtoGeoTiff()
