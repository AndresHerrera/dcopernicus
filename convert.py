import os
import sys
import xarray as xr
import rioxarray as rio
import numpy as np
import rasterio
from rasterio.transform import from_origin

os.environ['GDAL_DATA'] = 'C:/Users/User/miniconda3/envs/copernicus/Lib/site-packages/rasterio/gdal_data/'
os.environ['PROJ_LIB']  = 'C:/Users/User/miniconda3/envs/copernicus/Lib/site-packages/pyproj/proj_dir/share/proj/'

class ConvertCopernicus:
  def __init__(self, input_filename,input_directory, output_filename, output_directory, variable, epsg):
    self.input_filename = input_filename
    self.input_directory = input_directory
    self.output_filename=output_filename
    self.output_directory = output_directory
    self.variable = variable
    self.epsg = epsg
    
  def fromNetCDFtoGeoTiff(self):
    if os.path.isfile(os.path.join(self.input_directory,self.input_filename)):
      # Open the downloaded NetCDF file
      xds = xr.open_dataset(os.path.join(self.input_directory,self.input_filename), decode_coords="all")
      #xds = rio.open_rasterio(os.path.join(self.input_directory,self.input_filename), lock=False,cache=False)
      xds.rio.write_crs(self.epsg, inplace=True)
     
      if isinstance(xds, xr.DataArray):
        # Print the DataArray information
        print("Data is a DataArray")
        print(xds)
        # Get the number of bands (assuming the first dimension is the number of bands)
        num_bands = xds.shape[0]
        print(f'Number of bands: {num_bands}')
        
        processvar = xds.isel(time=0)
        
      elif isinstance(xds, xr.Dataset):
        print("Data is a Dataset")
        # Print the Dataset information
        print(xds)
        # Get the number of data variables (each data variable might be considered a band)
        num_data_vars = len(xds.data_vars)
        print(f'Number of data variables: {num_data_vars}')
        
        processvar = xds[self.variable].isel(time=0)
        
      else:
        print("The data format is not recognized as a DataArray or Dataset.")
    
      # Write GeoTiff file
      processvar.astype('float32').rio.to_raster(os.path.join(self.output_directory,self.output_filename), driver="GTiff", compress="LZW")
      
      print("Convert NC to GeoTiff")
      print("Input NetCDF file %s from : %s" %  (self.input_filename, self.input_directory) )
      print("Output GeoTIFF file %s created in : %s" %  (self.output_filename, self.output_directory) )
    else:
      print("File %s doesn't exist ! " % (os.path.join(self.input_directory,self.input_filename)) )