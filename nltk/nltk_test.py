from bs4 import BeautifulSoup
from nltk.corpus import stopwords

import urllib.request
import nltk
 
response = urllib.request.urlopen('http://php.net/')
 
html = response.read()
 
soup = BeautifulSoup(html,"html5lib")
 
text = soup.get_text(strip=True)

tokens = []

for token in text.split():
    tokens.append(token)
#tokens = [t for t in text.split()]

clean_tokens = tokens[:]
sr = stopwords.words('english')
for token in tokens:
    if token in stopwords.words('english'):
        clean_tokens.remove(token)

freq = nltk.FreqDist(clean_tokens)

for key,val in freq.items():
	print (str(key) + ':' + str(val))

freq.plot(20, cumulative=False)
 
#print (tokens)









































