
from bs4 import BeautifulSoup
import urllib.request as ur
from selenium import webdriver
import re
import sys

blacklist_words = []
whitelist_words = ["intern", "internship", "software"] #List of required words in job title

site_url = '' #url of the job search site
