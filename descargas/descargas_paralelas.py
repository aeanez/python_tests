# import os
# import requests
 
# from time import time
# from multiprocessing.pool import ThreadPool

# def url_response(url):
#     path, url = url
#     r = requests.get(url, stream = True)
#     with open(path, 'wb') as f:
#         for ch in r:
#         	f.write(ch)

# urls = [("Event1", "https://www.python.org/events/python-events/805/"),
 
# ("Event2", "https://www.python.org/events/python-events/801/"),
# ("Event3", "https://www.python.org/events/python-events/790/"),
# ("Event4", "https://www.python.org/events/python-events/798/"),
# ("Event5", "https://www.python.org/events/python-events/807/"),
# ("Event6", "https://www.python.org/events/python-events/807/"),
# ("Event7", "https://www.python.org/events/python-events/757/"),
# ("Event8", "https://www.python.org/events/python-user-group/816/")]


# start = time()
 
# # for x in urls:
#     # url_response (x)
# ThreadPool(9).imap_unordered(url_response, urls)
 
# print(f"Time to download: {time() - start}")

import requests
 
from clint.textui import progress
 
url = 'http://do1.dr-chuck.com/pythonlearn/EN_us/pythonlearn.pdf'
 
r = requests.get(url, stream=True)
 
with open("LearnPython.pdf", "wb") as Pypdf:
 
    total_length = int(r.headers.get('content-length'))
 
    for ch in progress.bar(r.iter_content(chunk_size = 2391975), expected_size=(total_length/1024) + 1):
 
        if ch:
 
            Pypdf.write(ch)
