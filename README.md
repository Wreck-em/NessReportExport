# NessusReport
Export Nessus scans to .CSVs + append a date column for each file

**NessusExporter.py** automatically exports contents of all folder within Nessus software into CSVs, just input Nessus user and password.
<br />
**NessusDate.py** gets .csv files from folders whose filename contain the word "scan" (ex: test scan)
  -Appends column date to .csv which contains today's date
  
  References:<br />
  https://github.com/tenable/nessrest/tree/master/scripts <br />
  https://stackoverflow.com/questions/39671373/how-can-i-use-nessrest-api-python-to-export-nessus-scan-reports-in-xml
