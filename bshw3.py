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
# Connects to BSI admissions webpage 
r = requests.get(base_url)
soup = BeautifulSoup(r.text, 'lxml')
# Converts the contents of the soup variable to a string in order to use string methods on it
string = str(soup)
new_string = ''
new_string1 = ''

# Iterates through all of image tags on the page and replaces the local images with the images provided by Colleen 
for logo in soup.find_all('img'):
	# Finds the local header image
	if str(logo.get('src')) == '/sites/default/themes/umsi/imgs/logo.png':
		new_string = string.replace(str(logo.get('src')), 'https://github.com/cvanlent/SI206/blob/master/HW3-StudentCopy/media/logo.png?raw=true')
	# finds the local footer image
	if str(logo.get('src')) == '/sites/default/themes/umsi/imgs/logo_footer.png':
		new_string1 = new_string.replace(str(logo.get('src')), 'https://github.com/cvanlent/SI206/blob/master/HW3-StudentCopy/media/logo.png?raw=true')

# Replaces student with AMAZING student
new_string2 = new_string1.replace('student', 'AMAZING student')
new_string3 = ''

# Iterates through the iframe tags, which represents the video on the original webpage
for video in soup.find_all('iframe'):
	# Replaces the contents of the source attribute for the iframe tag with my personal image
	if str(video.get('src')) == 'https://www.youtube.com/embed/mimp_3gquc4?feature=oembed':
		new_string3 = new_string2.replace(str(video.get('src')), 'colleen.jpg')

# Creates a new HTML file 
f = open('BSI.html','w')
# Writes the changes made to the original HTML file to the new HTML created
f.write(new_string3)
f.close()

