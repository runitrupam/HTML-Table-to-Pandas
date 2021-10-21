#pip install lxml  # To allow the HTML into xml format conversion and hence  allow   pd.read_html
import pandas as pd # pd.read_html
table_MN = pd.read_html('EXAMPLE ROSTER.HTML')
print(type(table_MN)) # <class 'list'>
len(table_MN) # 2 tables

print( type (table_MN[0][1]) )  # pandas <class 'pandas.core.series.Series'>


#len(table_MN[0]) Size of pandas object

res = dict()  # dictionary to be converted into json object at last

for i in range(len(table_MN[0])):
	
	
	duty = table_MN[0][i]
	if pd.isna(duty[5]): # TO STOP fetching and putting the Date as a key in dictionary . As NaN can't be Key of dict
		break
	
	d = dict()
	#print(duty)
	d['Flight_Number'] = duty[6]
	if d['Flight_Number'] == 'D/O':  # for no flights I store D/O
		res[duty[5]] = 'D/O'
		continue
		
	d['Report_Time'] = duty[7]
	d['Departure_Time'] = duty[8]
	d['Departure_Airport'] = duty[9]
	d['Arrival Time'] = duty[10]
	d['Arrival Airport'] = duty[11]
	#print(i,duty[5] , d)
	
	#if d['Flight_Number'] == 'D/O':
	res[duty[5]] = d
	#break
	
	
print(len(res))
#print(res)

import json

ret_json = json.dumps(res)  # convert dictionary into json object 
print(ret_json)
