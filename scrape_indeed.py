import requests
import csv
from bs4 import BeautifulSoup


page = requests.get('https://www.indeed.com/jobs?q=software+engineer&l=San+Francisco%2C+CA&radius=50&explvl=entry_level&ts=1541619643606&rq=1&fromage=last')

# Create a BeautifulSoup object
soup = BeautifulSoup(page.text, 'html.parser')

job_list = soup.find(id='resultsCol')
job_titles = job_list.find_all(class_='jobtitle')
company_list = job_list.find_all(class_='company')
locations = job_list.find_all(class_='location')

##for location in locations:
##    print (location.contents[0])

for company in company_list:
    print (company.contents[1].string)

for job_title in job_titles:
    print(job_title["title"])
