import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import re
import xlsxwriter


baseurl = "SET URL"
workbook = xlsxwriter.Workbook('Example.xlsx') 
worksheet = workbook.add_worksheet() 

response = requests.get(baseurl)
soup = BeautifulSoup(response.text, "html.parser")

h1 = soup.findAll('h1') #SEARCH FOR A HTMLTAG TO SCRAPE
row = 0
column = 0
for each in h1:

	clean = re.compile("<.*?>")
	test1 = re.sub(clean, "", str(each))

	test1 = test1.replace("[", "")
	test1 = test1.replace("]", "")



	worksheet.write(row, column, test1) 
	row += 1
      
workbook.close() 
wait = input("Warten auf User Input....")



