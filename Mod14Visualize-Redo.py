"""
Name:Addison deAbreu-Reese
Date:12/06/2023
Assignment: Module 14: Dask Large Dataset
Due Date:12/03/2023
About this project: This project uses Dask to process large set of data
Assumptions:NA
All work below was performed by Addison deAbreu-Reese and Karen Works, PhD.
"""
#https://catalog.data.gov/dataset/crime-data-from-2020-to-present

import time
import dask.dataframe as ddf
from dask.diagnostics import ProgressBar
import pandas
import numpy
import dask.delayed as delayed

dtypes = {
'DR_NO': float,
'Date Rptd': str,
'DATE OCC': str,
'TIME OCC': float,
'AREA': float,
'AREA NAME': str,
'Rpt Dist No': float,
'Part 1 - 2': float,
'Crm Cd': float,
'Crm Cd Desc': str,
'Mocodes': str,
'Vict Age': float,
'Vict Sex': str,
'Vict Descent': str,
'Premis Cd': float,
'Premis Desc': str,
'Weapon Used Cd': float,
'Weapon Desc': str,
'Status': str,
'Status Desc': str,
'Crm Cd 1': float,
'Crm Cd 2': float,
'Crm Cd 3': float,
'Crm Cd 4': float,
'LOCATION': str,
'Cross Street': str,
'LAT': float,
'LON': float,
}

df = ddf.read_csv("Crime_Data_from_2020_to_Present.csv",dtype = dtypes)

with ProgressBar():
 delayed(df.groupby(['Weapon Desc'])['Vict Age'].min()).visualize("MinAgeByWeapon.png")

 delayed(df.groupby(['Weapon Desc'])['Vict Age'].max()).visualize("MaxAgeByWeapon.png")

 delayed(df.groupby(['Weapon Desc'])['Vict Age'].mean()).visualize("MeanAgeByWeapon.png")
