import pandas as pd
import os
import numpy as n
from random import randint
from pprint import pprint
import time

folder = os.listdir("CSV")
skillBreakUp = []

goal = randint(0,len(folder)-1)
str = folder[goal].replace('.csv','')
print('\n----------------------------------------------------------------------------------------------------------------------')
print('Career')
print(str)
print('----------------------------------------------------------------------------------------------------------------------')

reviews = pd.read_csv("CSV/"+folder[goal])

users = randint(0,reviews.shape[0]-1)
userDetails = reviews.iloc[0,1:13]

print('\n----------------------------------------------------------------------------------------------------------------------')
print('User Details')
print(userDetails)
print('----------------------------------------------------------------------------------------------------------------------')


skills = reviews.loc[:,'Skills']


for i in skills:
	temp = i.replace('(','')
	temp = temp.replace(')','')
	temp = temp.replace('&&',',')
	temp = temp.replace('. ',',')
	
	temp = temp.split(',')
	
	for m in temp:
		if 'year' not in m:
			if 'years' not in m:
				if m not in skillBreakUp:
					if len(m)>0:
						skillBreakUp.append(m.strip())
					
numOfSkills = len(skillBreakUp)
users = len(reviews)
skillMatrix = n.zeros((users,numOfSkills))

for i in range(0,users):
	for j in range(0,numOfSkills):
		if skillBreakUp[j] in skills[i]: # Checking if the current user has a particular skill or not
			skillMatrix[i,j] = 1
			
freq = skillMatrix.sum(axis=0) # Frequency of each skill

similarity = n.zeros((numOfSkills,numOfSkills))
t = time.clock()
for i in range(0,users):
	for j in range(0,numOfSkills):
		for k in range(0,numOfSkills):
			if skillBreakUp[j] in skills[i] and skillBreakUp[k] in skills[i]:
				similarity[j,k] = similarity[j,k] + 1

# Jaccard Index				
jaccardIndex = n.zeros((numOfSkills, numOfSkills))

for i in range(0,numOfSkills):
	for j in range(0,numOfSkills):
		jaccardIndex[i,j] = similarity[i,j]/(freq[i] + freq[j] - similarity[i,j])
	
temp = n.unique(jaccardIndex)[::-1] # Sorting in descending order of Jaccard Index
temp = temp[~n.isnan(temp)]
temp = temp[0:3]

# Suggesting Skills to User

print('\n----------------------------------------------------------------------------------------------------------------------')
print('Suggested Skills for the user for the Career Goal of',str,'\n----------------------------------------------------------------------------------------------------------------------')

suggestedSkills = []
a = -1

for i in temp:
	k = n.where(jaccardIndex==i)
	r = k[0].tolist()
	c = k[1].tolist()
	for r in c:
		for l in c:
			if r!=c and skillBreakUp[l] not in suggestedSkills:
				a = a+1
				suggestedSkills.append(skillBreakUp[l])
				
pprint(suggestedSkills)

print('\n\nTime taken:',time.clock()-t)