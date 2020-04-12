# airbnb
airbnb_data_analysis

To install:

CD to airbnb folder then run the following command
pip install .

To run:

>>> from airbnb_data import Data
>>> data_object = Data('price')
>>> data = data_object.load_data()
>>> data['seattle_calendar']
         listing_id        date available   price
0            241032  2016-01-04         t  $85.00
1            241032  2016-01-05         t  $85.00
2            241032  2016-01-06         f     NaN
3            241032  2016-01-07         f     NaN
4            241032  2016-01-08         f     NaN
...             ...         ...       ...     ...
1393565    10208623  2016-12-29         f     NaN
1393566    10208623  2016-12-30         f     NaN
1393567    10208623  2016-12-31         f     NaN
1393568    10208623  2017-01-01         f     NaN
1393569    10208623  2017-01-02         f     NaN