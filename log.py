import pandas as pd
from openpyxl import load_workbook
from logfunctions import openxlsx
import sys
from gui import *
import os.path

if os.path.isfile('circanlog.xlsx') is False:
    openxlsx()


# new dataframe with same columns
sleep = pd.DataFrame({'Days': [day],
                'Sleep': [sleep],
                'Wake': [wake],
                'Naps': [naps],
                'Steps': [steps],
                'Mood': [mood],                  
                })
#Converting format of columns to [datetime64]
sleep['Days']= pd.to_datetime(sleep['Days'])
sleep['Wake'] = pd.to_datetime(sleep['Wake'])
sleep['Sleep'] = pd.to_datetime(sleep['Sleep'])
sleep['Weekday'] = sleep['Days'].dt.day_name()
writer = pd.ExcelWriter('circanlog.xlsx', engine='openpyxl')
# try to open an existing workbook
writer.book = load_workbook('circanlog.xlsx')
# copy existing sheets
writer.sheets = dict((ws.title, ws) for ws in writer.book.worksheets)
# read existing file
reader = pd.read_excel(r'circanlog.xlsx')
# write out the new sheet
sleep.to_excel(writer,index=False,header=False,startrow=len(reader)+1)

writer.close()