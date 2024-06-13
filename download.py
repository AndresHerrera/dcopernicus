import os
from datetime import datetime
import copernicusmarine
import sys
from dotenv import load_dotenv
load_dotenv()

class DownloadCopernicus:
  def __init__(self, start_date, end_date,output_filename,output_directory,config):
    self.start_date = start_date
    self.end_date = end_date
    self.output_filename=output_filename
    self.output_directory = output_directory
    self.config = config
    
  def downloadSubset(self):
    
    start_datetime = datetime.strptime(self.start_date, "%Y-%m-%d")
    end_datetime = datetime.strptime(self.end_date, "%Y-%m-%d")
    
    copernicusmarine.subset(
        dataset_id=self.config["dataset_id"],
        variables=self.config["variables"],
        minimum_longitude=float(self.config["minimum_longitude"]),
        maximum_longitude=float(self.config["maximum_longitude"]),
        minimum_latitude=float(self.config["minimum_latitude"]),
        maximum_latitude=float(self.config["maximum_latitude"]),
        minimum_depth=float(self.config["minimum_depth"]),
        maximum_depth=float(self.config["maximum_depth"]),
        username=os.getenv('COPERNICUS_USERNAME'),
        password=os.getenv('COPERNICUS_PASSWORD'),
        start_datetime=start_datetime,
	      force_download=True,
        overwrite_output_data=True,
        overwrite_metadata_cache=False,
        end_datetime=end_datetime,
        output_filename=self.output_filename,
        output_directory=self.output_directory
    )