import os
import glob
import pandas as pd
from datetime import date
import csv


today = date.today()
date = today.strftime("%Y-%m-%d")
path = "[insert path]"

today = date.today()
#date = today.strftime("%Y-%m-%d")
#variables for file path
mydate = datetime.datetime.now()
month = mydate.strftime("%B")
year = mydate.strftime("%Y")
yearmonth = year + " " + month
#date you want to append
date = "04/09/2022"

#gets files in "scan" folders
for file in glob.glob((path+ "/*scan*/*")):
    dir_path = os.path.dirname(os.path.realpath(file))
    if file.endswith(".csv"):
        df = pd.read_csv(file)
        df["Date"] = date
        print(file)
        df.to_csv(file, index=False)
