from urllib.request import urlopen
 
from urllib.error import HTTPError
 
from urllib.error import URLError
 
from bs4 import BeautifulSoup
 
try:
 
    html = urlopen("https://www.python.org/")
 
except HTTPError as e:
 
    print(e)
 
except URLError:
 
    print("Server down or incorrect domain")
 
else:
 
    res = BeautifulSoup(html.read(),"html5lib")
 
    #tags = res.findAll("h2", {"class": "widget-title"})
    #tags = res.findAll("span","a")
    #tags = res.findAll("a", {"class": ["url", "readmorebtn"]})
    #tags = res.findAll(text="Python")
    #tags = res.a.findAll()
    #tags = res.span.findAll()

    for tag in tags:
        #print(tag.getText())
        print(tag)








