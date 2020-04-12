# Airbnb
This package instantiate a data object which includes sample data from airbnb

# To install:

After cloning this repo, CD to airbnb folder then run the following command

pip install .

# To run:

from airbnb_data import Data

data_object = Data('price')

data = data_object.load_data()

data['seattle_calendar']