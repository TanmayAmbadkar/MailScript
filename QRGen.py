import pyqrcode 
import os
from pyqrcode import QRCode 
import pandas as pd
dataset=pd.read_csv("filename.csv")
RollNo=dataset.iloc[:,[0]].values
os.mkdir("QRCodes")
for i in RollNo:
    url = pyqrcode.create(i)   
    url.svg("{}.svg".format(i), scale = 8)