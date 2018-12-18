#! /usr/bin/python
#setup
import urllib2 , csv ,sys
from bs4 import BeautifulSoup

All_Links = open("links.txt").readlines()
for x in range (len(All_Links)):
	page = urllib2.urlopen(All_Links[x])
	soup = BeautifulSoup(page, 'html.parser')
	with open("descriptions.txt", "a+") as f:
		desc = soup.find_all("div", {"class": "product-short-description"})
		for link in desc:
			f.write(link.text.encode('utf-8') + "\n")
''''
for x in range(len(All_Links)):
	page = urllib2.urlopen(All_Links[x])
	soup = BeautifulSoup(page, 'html.parser')
	with open("descriptions.txt", "a+") as f:
		desc = soup.find_all("div", {"class": "product-short-description"})
		for link in desc:
			print link
'''