import json
import pandas as pd
import os

folders = os.listdir("Candidate Profile Data")

for file in folders:

	with open('Cleaned/'+file,encoding='utf8') as data_file:    
		jsondata = json.load(data_file)
	usable_dataframe = pd.io.json.json_normalize(jsondata)
	
	a = file[0:len(file)-4]
	usable_dataframe.to_csv('CSV/'+a+'.csv')