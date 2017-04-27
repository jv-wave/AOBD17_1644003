import json
import os

def remove_non_ascii(text):
    return ''.join(i for i in text if ord(i)<128)

folders = os.listdir("Candidate Profile Data")

for file in folders:
	with open('Candidate Profile Data/'+file,encoding='utf8') as data_file:    
		data = json.load(data_file)
		
	a=0
	for i in data:
		data[a]['CandidateID'] = remove_non_ascii(data[a]['CandidateID'])
		data[a]['Additional-Info'] = remove_non_ascii(data[a]['Additional-Info'])
		data[a]['Skills'] = remove_non_ascii(data[a]['Skills'])
		data[a]['Work-Experience']['Company'] = remove_non_ascii(data[a]['Work-Experience']['Company'])
		data[a]['Work-Experience']['Job-Description'] = remove_non_ascii(data[a]['Work-Experience']['Job-Description'])
		data[a]['Work-Experience']['Job-Duration'] = remove_non_ascii(data[a]['Work-Experience']['Job-Duration'])
		data[a]['Work-Experience']['Job Title'] = remove_non_ascii(data[a]['Work-Experience']['Job Title'])
		data[a]['Location'] = remove_non_ascii(data[a]['Location'])
		data[a]['Education']['Institute'] = remove_non_ascii(data[a]['Education']['Institute'])
		data[a]['Education']['School-Duration'] = remove_non_ascii(data[a]['Education']['School-Duration'])
		data[a]['Education']['Qualification'] = remove_non_ascii(data[a]['Education']['Qualification'])
		data[a]['Resume-Summary'] = remove_non_ascii(data[a]['Resume-Summary'])
		a=a+1

	with open('Cleaned/'+file, 'w') as outfile:
		json.dump(data, outfile)