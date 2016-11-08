# Use https://www.si.umich.edu/programs/bachelor-science-
# information/bsi-admissions as a template.
# STEPS 
# Create a similar HTML file but 
# 1) Replace every occurrence of the word “student” with “AMAZING
# student.”  
# 2) Replace the main picture with a picture of yourself.
# 3) Replace any local images with the image I provided in media.  (You
# must keep the image in a separate folder than your html code.

# Deliverables
# Make sure the new page is uploaded to your GitHub account.


import requests
from bs4 import BeautifulSoup

base_url = 'https://www.si.umich.edu/programs/bachelor-science-information/bsi-admissions'
r = requests.get(base_url)
soup = BeautifulSoup(r.text, 'lxml')
string = str(soup)
new_string = ''
new_string1 = ''

for logo in soup.find_all('img'):
	if str(logo.get('src')) == '/sites/default/themes/umsi/imgs/logo.png':
		new_string = string.replace(str(logo.get('src')), 'https://github.com/cvanlent/SI206/blob/master/HW3-StudentCopy/media/logo.png?raw=true')
	if str(logo.get('src')) == '/sites/default/themes/umsi/imgs/logo_footer.png':
		new_string1 = new_string.replace(str(logo.get('src')), 'https://github.com/cvanlent/SI206/blob/master/HW3-StudentCopy/media/logo.png?raw=true')

new_string2 = new_string1.replace('student', 'AMAZING student')
new_string3 = ''

for video in soup.find_all('iframe'):
	if str(video.get('src')) == 'https://www.youtube.com/embed/mimp_3gquc4?feature=oembed':
		new_string3 = new_string2.replace(str(video.get('src')), 'colleen.jpg')

f = open('BSI.html','w')
f.write(new_string3)
f.close()

