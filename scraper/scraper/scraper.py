import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import numpy as np

a = ['', 12, 13, 14]

df = pd.DataFrame({'Company DUNS#': a,
                              'Corporate Name': a,
                              'Tradestyle Name': a,
                              'Point of Contact': a,
                              'Title': a,
                              'Address': a,
                              'Telephone': a,
                              'Total Employees': a,
                              'Employees On Site': a,
                              'Sales Volume': a,
                              'Public/Private': a,
                              'Year Started': a,
                              'Latitude': a,
                              'Longitude': a,
                              'NAICS1': a,
                              'NAICS2': a,
                              'SIC1': a,
                              'SIC2': a})

 
writer = ExcelWriter('NAICSData.xlsx')
df.to_excel(writer,'Sheet1', index = False)
writer.save()
