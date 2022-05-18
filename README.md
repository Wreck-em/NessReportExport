# NessusReport
Export Nessus vulnerability scans into .csv files + appends current date column for each file

**NessusExporter.py** automatically exports contents of folders within Nessus software into .csv's. Input your desired file path and Nessus username/password to export Nessus files to a folder entitled "[current month name] Scans."
<br />
**NessusDate.py** gets .csv files from folders whose filename contain the word "scan" (ex: test scan)
  -Appends column date to .csv which contains today's date
  
  References:<br />
  https://github.com/tenable/nessrest/tree/master/scripts <br />
  https://stackoverflow.com/questions/39671373/how-can-i-use-nessrest-api-python-to-export-nessus-scan-reports-in-xml
