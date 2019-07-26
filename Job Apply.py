
from bs4 import BeautifulSoup
import urllib.request as ur
import re
import sys

required = ["intern", "internship", "software"] #List of required words in job title


def qualifies(title):
    title = title.lower()
    #Define a function to check if a job title is worth checking out
    for word in required:
        if word in title: return True
    return False

#test:
#qualifies("Senior Software Engineer")


url = "https://www.indeed.com/jobs?q=software+engineer+intern&l=Campbell%2C+CA"

pgno = 0
try:
        response = ur.urlopen(url)
        html_doc = response.read()
except:
        print("URL not accesible")
        exit();
soup = BeautifulSoup(html_doc, 'html.parser')

try:
    total_results = soup.find(id="searchCount").get_text()
    last_page = int(int(total_results[total_results.index("of")+2: total_results.index("jobs")].strip()) / 10) * 10
    print(last_page)
except:
    print ("No jobs found")

jobs_per_page = 10
goodlinks = []
for pgno in range(0,last_page,jobs_per_page):
    if pgno > 0:
        try:
            response = ur.urlopen(url+str(pgno))
            html_doc = response.read()
        except:
            break;
        soup = BeautifulSoup(html_doc, 'html.parser')
    for job in soup.find_all(class_='result'):
        link = job.find(class_="turnstileLink")
        try:
            jt = link.get('title')
        except:
            jt = ""
        try:
            comp = job.find(class_='company').get_text().strip()
        except:
            comp = ""

        if(qualifies(jt.lower())):
            toVisit = "http://www.indeed.com"+link.get('href')
            try:
                html_doc = ur.urlopen(toVisit).read().decode('utf-8')
            except:
                continue;



            print(jt,",",comp,":",toVisit,"\n")
            goodlinks.append(toVisit)
