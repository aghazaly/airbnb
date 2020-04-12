"""
This model is used to instantiate a data object for data ingestion 
"""
import os
import glob
import datetime
import pandas as pd

class Data:
    """
    Target is a target column name
    """
    def __init__(self, target):
        self.target = target
    
    def load_data(self):
        data_dict = {}
        this_dir, this_filename = os.path.split(__file__)
        abs_paths = list(glob.iglob(this_dir+'/*/*.csv', recursive=True))
        for path in abs_paths:
            folder_name = path.split("/")[-2]
            file_name = path.split("/")[-1]
            data_dict[f"{folder_name}_{file_name.split('.')[0]}"] = pd.read_csv(path)
        return data_dict
    
    def prepare_data(self, df, na, features=[]):
        """
        Takes a dataframe and returns cleaned dataframe
        """
        cleaned_df = df.dropna(subset=[self.target])
        if na=='drop_na':
            cleaned_df = cleaned_df.dropna(subset=features)
        elif na=='mean':
            cleaned_df[features] = cleaned_df[features].apply(lambda x: x.fillna(x.mean()))
        else:
            a = cleaned_df.isna().mean()
            na_cols = a[a>0].index.tolist()
            
            print(f"these columns still have NaNs {na_cols}")
            
        return cleaned_df      