import sys
import os
import io
from nessrest import ness6rest
import os
import glob
import pandas as pd
from datetime import date
import csv

file_format = 'csv'  # options: nessus, csv, db, html
dbpasswd = ''

scan = ness6rest.Scanner(url="https://nessus:8834", login="", password="", insecure=True)

scan.action(action='scans', method='get')
folders = scan.res['folders']
scans = scan.res['scans']


if scan:
    scan.action(action='scans', method='get')
    folders = scan.res['folders']
    scans = scan.res['scans']


    for f in folders:
        if not os.path.exists(f['name']):
            if not f['type'] == 'trash':
                os.mkdir(f['name'])

    for s in scans:
        scan.scan_name = s['name']
        scan.scan_id = s['id']
        folder_name = next(f['name'] for f in folders if f['id'] == s['folder_id'])
        folder_type = next(f['type'] for f in folders if f['id'] == s['folder_id'])

        # skip trash items
        if folder_type == 'trash':
            continue

        if s['status'] == 'completed':
            file_name = '%s_%s.%s' % (scan.scan_name, scan.scan_id, file_format)
            file_name = file_name.replace('\\','_')
            file_name = file_name.replace('/','_')
            file_name = file_name.strip()
            relative_path_name = folder_name + '/' + file_name
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
                    print(relative_path_name)
                else:
                    fp.write(scan.download_scan(export_format=file_format, dbpasswd=dbpasswd))
                    print(relative_path_name)