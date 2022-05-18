import os
import glob
import pandas as pd
from datetime import date
import csv


today = date.today()
date = today.strftime("%Y-%m-%d")
path = "[insert path]"

today = date.today()
#variables for file path folder creation
mydate = datetime.datetime.now()
month = mydate.strftime("%B")
year = mydate.strftime("%Y")
yearmonth = year + " " + month
date = today.strftime("%Y-%m-%d")


#gets files in "scan" folders
for file in glob.glob((path+ "/*scan*/*")):
    dir_path = os.path.dirname(os.path.realpath(file))
    #Appends .csv files within folder
    if file.endswith(".csv"):
        df = pd.read_csv(file)
        df["Date"] = date
        print(file)
        df.to_csv(file, index=False)
