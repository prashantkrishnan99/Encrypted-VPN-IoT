import thread
import time
import csv
import json
import glob

#Go to the directory to read in all the csv files from the sensors
path = "/home/prashukk/Downloads/traffic_feb_june/*.csv"
for fname in glob.glob(path):

	file_csv = fname.rsplit("/")[-1]
	file_json = file_csv.rsplit(".")[0] + ".json"

	#print file_csv,file_json

	try:
		csvfile = open('/home/prashukk/Downloads/traffic_feb_june/'+file_csv, 'r')
		jsonfile = open('/home/prashukk/Downloads/traffic_feb_june/'+file_json, 'w')
	except:
		print file_csv + " not readable ..."
		continue

	fieldnames = ("status","avgMeasuredTime","avgSpeed","extID","medianMeasuredTime","TIMESTAMP","vehicleCount","_id","REPORT_ID")
	reader = csv.DictReader( csvfile, fieldnames)
	for row in reader:
		json.dump(row, jsonfile)
    	        jsonfile.write('\n')
