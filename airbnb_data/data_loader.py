"""
This model is used to instantiate a data object for data ingestion 
"""
import os
import glob
import datetime
import pandas as pd

class Data:
    def __init__(self, target, features=[]):
        self.target = target
        self.features = features
    
    def load_data(self):
        data_dict = {}
        this_dir, this_filename = os.path.split(__file__)
        abs_paths = list(glob.iglob(this_dir+'/*/*.csv', recursive=True))
        for path in abs_paths:
            folder_name = path.split("/")[-2]
            file_name = path.split("/")[-1]
            data_dict[f"{folder_name}_{file_name.split('.')[0]}"] = pd.read_csv(path)
        return data_dict
    
    # def prepare_data(self, df, dropna=bool):
    #     """
    #     Takes a dataframe and outputs X and y 
    #     """
    #     cleaned_df = df.dropna(subset=[self.target]+self.features)
        
        