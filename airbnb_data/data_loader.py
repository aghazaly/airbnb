"""
This model is used to instantiate a data object for data ingestion
"""
import os
import glob
import typing
import pandas as pd

class Data:
    """
    Target is a target column name
    """
    def __init__(self, target: str):
        self.target = target #target column name
        self.file_path = __file__ #path to the folder where this module is located

    def load_data(self) -> typing.Dict:
        """
        This function returns a dictionary of dataframes
        """
        data_dict = {}
        this_dir, this_filename = os.path.split(self.file_path)
        abs_paths = list(glob.iglob(this_dir+'/*/*.csv', recursive=True))
        for path in abs_paths:
            folder_name = path.split("/")[-2]
            file_name = path.split("/")[-1]
            #append df to a dict
            data_dict[f"{folder_name}_{file_name.split('.')[0]}"] = pd.read_csv(path)
        return data_dict

    def prepare_data(self, df: pd.DataFrame, na_option: str, features: list) -> pd.DataFrame:
        """
        Takes a dataframe and returns cleaned dataframe
        """
        cleaned_df = df.dropna(subset=[self.target])
        if na_option == 'drop_na':
            cleaned_df = cleaned_df.dropna(subset=features)
        elif na_option == 'mean':
            cleaned_df[features] = cleaned_df[features].apply(lambda x: x.fillna(x.mean()))
        else:
            #number of nan rows divided by total number of rows
            percentage_na = cleaned_df.isna().mean()
            na_cols = percentage_na[percentage_na > 0].index.tolist()

            print(f"these columns still have NaNs {na_cols}")

        return cleaned_df
      