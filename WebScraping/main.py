#Step 0: Installing Requirements
#pip install requests
#pip install bs4
#pip install html5lib

import requests
from bs4 import BeautifulSoup
url = "https://www.amazon.in/"

#Step 1: Get the HTML
r = requests.get(url)
htmlContent = r.content

#Step 2: Parse the HTML
soup = BeautifulSoup(htmlContent, 'html.parser')
#print(soup.prettify)

#Step 3: HTML Tree traversal
#
# #Commonly used types of objects
# print(type(title)) # 1. Tag
# print(type(title.string)) # 2. NavigableString
# print(type(soup)) # 3. BeautifulSoup
# markup = "<p><!-- this is a comment --></p>"
# soup2 = BeautifulSoup(markup)
# print(soup2.p) # 4. Comment
#
title = soup.title
paras = soup.find_all('p')

# Get first element in the HTML Page
print(soup.find('p'))
# Get classes of any element in the HTML Page
print(soup.find('p')['class'])

#find all the elements with class lead
print(soup.find_all("p", class_ ="lead"))

#Get the text from the tags/soup
print(soup.find('p').get_text())

anchors = soup.find_all('a')
#Getting links on the page
for link in anchors:
    print(link.get('href'))
    
navbar = soup.find(id = 'navbar')

# .contents - A tag's children are available as a list
# .children - A tag's children are available as a generator (faster for large pages)

for elem in navbar.children:
    print(elem)

for item in navbar.stripped_strings:
    print(item)
    
for item in navbar.parents:
    print(item.name)

print(navbar.previous_sibling.next_sibling)

#CSS Selectors
elem = soup.select('.a-section')
print(elem)

