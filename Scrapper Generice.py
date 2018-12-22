#! /usr/bin/python
#setup
import urllib2 , csv ,sys
from bs4 import BeautifulSoup
q = []
q = ['http://localhost/joomla/index.php/en/results,1-150', 'http://localhost/joomla/index.php/en/results,151-300', 'http://localhost/joomla/index.php/en/results,301-450', 'http://localhost/joomla/index.php/en/results,451-600', 'http://localhost/joomla/index.php/en/results,601-750', 'http://localhost/joomla/index.php/en/results,751-900']

for x in range(len(q)):
	page = urllib2.urlopen(q[x])
	soup = BeautifulSoup(page, 'html.parser')

#-----------------------------------------------------
#find the names
#	with open("products.txt", "a+") as f:
#		names = soup.find_all("a", href=True)
#		for link in names:
#			f.write(link.text.encode('utf-8'))

#find the prices
#	with open("prices.txt", "a+") as f:
#		prices= soup.body.find_all("span", {"class": "PricesalesPrice"})
#		for link2 in prices:
#			f.write(link2.text.encode('utf-8') + "\n")

#find the picture names
#	with open("pictures.txt", "a+") as f:
#		pictures=soup.find_all("img", {"class": "browseProductImage"})
#		for link3 in pictures:
#			print (link3["src"])
#			f.write(link3["src"].encode('utf-8') + "\n")
#-------------------------------------------------------

#find all the desc links
	with open("links.txt", "a+") as f:
		links=soup.find_all("a", href=True)
		for link4 in links:
#			print (link4["href"])
			f.write(link4["href"].encode('utf-8') + "\n")


#find all the description
#All_Links = open("links.txt").readlines()
#for link5 in All_Links:
#	with open("descriptions.txt", "a+") as f:
#		desc = soup.find_all("div", {"class": "product-short-description"})
#		for link6 in desc:
#			print link6.text