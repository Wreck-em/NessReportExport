import os
import glob
import pandas as pd
from datetime import date
import csv


today = date.today()
date = today.strftime("%Y-%m-%d")
path = "[insert path]"

#gets files in "scan" directory folders
for file in glob.glob((path+ "/*scan*/*")):
    if file.endswith(".csv"):
        df = pd.read_csv(file)
        df["Date"] = date
        print(file)
        df.to_csv(file, index=False)