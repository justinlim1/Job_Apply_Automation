
from bs4 import BeautifulSoup as soup
import urllib.request as ur
from selenium import webdriver
import re
import sys

url = '' #url of the job search site
uCl = ur.urlopen(url)
page_html = uCl.read()
uCl.close()
page = soup(page_html, "html.parser") #parse html

driver = webdriver.Chrome()


blacklist_words = []
whitelist_words = ["intern", "internship", "software"] #List of required words in job title


