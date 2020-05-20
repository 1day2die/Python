import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import re
import xlsxwriter


baseurl = "SETURL"
workbook = xlsxwriter.Workbook('Example.xlsx') 
worksheet = workbook.add_worksheet() 
row = 0
column = 0

i = 200

urls = []
# NICE FUNCTION SO SEARCH MULTIPLE DOMAINS 
while i < 300:
	url = str(baseurl)+str(i)

	urls.append(url)
	i = i+1


for each in urls:
	response = requests.get(each)
	soup = BeautifulSoup(response.text, "html.parser")

	name = soup.findAll('span', {"itemprop" : "name"})  #SEARCH FOR A HTMLTAG TO SCRAPE
	telephone = soup.findAll('span', {"itemprop" : "telephone"})  #SEARCH FOR A HTMLTAG TO SCRAPE
	email = soup.findAll('span', {"itemprop" : "email"})  #SEARCH FOR A HTMLTAG TO SCRAPE

	#all_spans = "NAME: ", name,"\n Telefon: ", telephone ,"\n Email: ", email
	all_spans = name, telephone, email
	clean = re.compile("<.*?>")
	test1 = re.sub(clean, "", str(name))
	test2 = re.sub(clean, "", str(telephone))
	test3 = re.sub(clean, "", str(email))

	test1 = test1.replace("[", "")
	test1 = test1.replace("]", "")
	test2 = test2.replace("[", "")
	test2 = test2.replace("]", "")
	test3 = test3.replace("[", "")
	test3 = test3.replace("]", "")

	worksheet.write(row, column, test1) 
	column += 1
	worksheet.write(row, column, test2) 
	column += 1
	worksheet.write(row, column, test3) 
	row += 1


