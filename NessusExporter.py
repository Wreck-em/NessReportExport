import sys
import os
import io
from nessrest import ness6rest
import os
import glob
import pandas as pd
import datetime
import DateTime.DateTime
import csv

file_format = 'csv'  # options: nessus, csv, db, html
dbpasswd = ''

#Input Nessus login info
scan = ness6rest.Scanner(url="https://nessus:8834", login="", password="", insecure=True)

mydate = datetime.datetime.now()
month = mydate.strftime("%B")
year = mydate.strftime("%Y")
yearmonth = year + " " + month
# input path
path = ""

scan.action(action='scans', method='get')
folders = scan.res['folders']
scans = scan.res['scans']

if scan:
    scan.action(action='scans', method='get')
    folders = scan.res['folders']
    scans = scan.res['scans']


    for f in folders:
        x = f['name']
        # If a folder for this current month is not created, makes new one
        newpath = path + '/' + yearmonth + " Scans" + '/' + x
        if not os.path.exists(path + '/' + yearmonth + " Scans"):
            os.mkdir(path + '/' + yearmonth + ' Scans')
        else:
            if not os.path.exists(newpath):
                if not f['type'] == 'trash':
                    os.mkdir(newpath)

    for s in scans:
        scan.scan_name = s['name']
        scan.scan_id = s['id']
        folder_name = next(f['name'] for f in folders if f['id'] == s['folder_id'])
        folder_type = next(f['type'] for f in folders if f['id'] == s['folder_id'])

        # skip trash items
        if folder_type == 'trash':
            continue

        if s['status'] == 'completed':
            # set cwd
            os.chdir(newpath)
            file_name = '%s_%s.%s' % (scan.scan_name, scan.scan_id, file_format)
            file_name = file_name.replace('\\','_')
            file_name = file_name.replace('/','_')
            file_name = file_name.strip()
            relative_path_name = "../" + folder_name + '/' + file_name
            # PDF not yet supported
            # python API wrapper nessrest returns the PDF as a string object instead of a byte object, making writing and correctly encoding the file a chore...
            # other formats can be written out in text mode
            file_modes = 'wb'
            # DB is binary mode
            #if args.format == "db":
            #  file_modes = 'wb'
            with io.open(relative_path_name, file_modes) as fp:
                if file_format != "db":
                    fp.write(scan.download_scan(export_format=file_format))
                else:
                    fp.write(scan.download_scan(export_format=file_format, dbpasswd=dbpasswd))
