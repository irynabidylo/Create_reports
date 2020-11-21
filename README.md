These functions generate reports in 4 different types: text, csv, json or yaml. 
Data.py module reads the data from the corresponding csv file and returns the data from those files instead of the hard-coded data.
The functions that generate these reports in the reports.py module also write the report to a file (in addition to the console):
- Text Report writes to a file called <Report Filename>.txt
- CSV Report writes to a file called <Report Filename>.csv
- JSON Report writes to a file called <Report Filename>.json
- YAML Report writes to a file called <Report Filename>.yaml
Where <Report Filename> is the name of the file entered as the new command line parameter.
The extension is appended to <Report Filename> (i.e., .txt, .csv, .json or .yaml). The user only enters the base filename in the command parameters. 
For example, if the <Report Filename> is "Reportphone" it would create file reportphone.json for a json report type.
If the filename already exists, it overwrites the existing contents.
For all the report types, the list of operating systems is sorted in the output in reverse alphabetical order and there are no duplicates.
The command line parameters are as follows:
main.py <input type> <report type>
Where:
- Input Type is phone, tablet or laptop
- Report Type is text, csv, json or json
The following errors are printed to the console for invalid parameters:
- Input type must be either phone, table or laptop
- Report type must be either text, csv, json or yaml
