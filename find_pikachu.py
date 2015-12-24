"""
find_pikachu.py
The program open the wikipedia pokemon page
and count how many Pikachu listed on the page

By Scott Huang
Dec 23, 2015

"""

# import urllib.request and re modules
import urllib.request
import re

# request raw HTML for wikipedia pokemon page
url='http://en.wikipedia.org/wiki/List_of_Pokemon'
response = urllib.request.urlopen(url)
html = response.read()
# Pikachu I choose you! get list of Pikachus from the page
data = re.findall('Pikachu', str(html))
#print number of Pikachu's
print("There are %d 'Pikachu' listed on %s" %(len(data), url))



