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

# Connects to BSI admissions webpage 
base_url = 'https://www.si.umich.edu/programs/bachelor-science-information/bsi-admissions'
r = requests.get(base_url)
soup = BeautifulSoup(r.text, 'lxml')

# Converts the contents of the soup variable to a string in order to use string methods on it
string = str(soup)

# Replaces the local header image with the image that Colleen provided 
new_string = string.replace('/sites/default/themes/umsi/imgs/logo.png', 'media/logo.png')

# Replaces the local footer image with the image that Colleen provided 
new_string1 = new_string.replace('/sites/default/themes/umsi/imgs/logo_footer.png', 'media/logo.png')
# Replaces student with AMAZING student
new_string2 = new_string1.replace('student', 'AMAZING student')

# Replaces video on the original webpage with my personal image 
new_string3 = new_string2.replace('https://www.youtube.com/embed/mimp_3gquc4?feature=oembed', 'media/colleen.jpg')

# Creates a new HTML file & writes the changes made to the original HTML file to the new HTML file
f = open('BSI.html','w')
f.write(new_string3)
f.close()

