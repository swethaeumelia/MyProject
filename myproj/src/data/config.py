import json
import numpy as np
import pandas as pd
import glob
from os import scandir
import os
from datetime import datetime
import fnmatch

# with open('config.json', 'r') as config_file:
#     config_data = json.load(config_file)
    
class ConfigLoader:
    def __init__(self):
        """
        load config.json file and parse it. Then create function to easily call and get the values.
        """

    def load_config_file(self, configfilename):
        with open('configfilename', 'r') as config_file:
            self.config_data = json.load(config_file)
        

    def get_files(self,filepath, files_list):
        self.filepaths = filepath
        self.files = files_list
        return filepath, files

    def get_schema(self, filename, attributes, dtype):
        self.file_name = filename
        self.columns = attributes
        self.datatype = dtype


#print(config_data['properties']['age'])
#print('filenames:', config_data['files_list'])
print(config_data["Patient Database.csv"]["attributes"])
print(config_data["WBC.csv"])