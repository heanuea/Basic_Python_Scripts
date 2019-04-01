<a href="http://fvcproductions.com"><img src="https://www.python.org/static/opengraph-icon-200x200.png" title="python" alt="python"></a>

<!-- added link for image above  -->


# Python Scripts and programs 

> Here is some programs and scripts written in python.

> There will be a short discription on each program. 

> Feel free to use or clone ;)

---

**List of Programs Table of contents**

- [Convert](#1.convert)
- [cycle](#2.cycle)
- [Google Command Line script](#3.Googlescript)
- imdb script
- Internet 
- Loops script
- Ls Name
- Pandas 
- Port scanner
- Time.
- Untitled
- Version 

---

## 1.Convert
> Here is a program to Convert a string into a list 

```Python
#Comment here 
def Convert(string):
    li = list(string.split(" "))
    return li


str1 = "python is love Python is life"

print(Convert(str1)) 
```
---

## 2.cycle
> A small program that fires a list and cycles through it til it hits it range 

```Python 
from itertools import cycle

list1 = [1,2,3]
cy = cycle(list1)

for index in range(5):
    print(next(cy))
    
```

---
## 3.Google script
> Just Querys from a Google API 

```Python
import urllib
import urllib2
import json
# Google returns JSON
url = "http://ajax.googleapis.com/ajax/services/search/web?v=1.0&"

query = raw_input("What u want to Look FOr Matey ????? ")
query = urllib.urlencode({'q': query})

#Create the response object by loading the the URL response, including the query
#e asked for above. 
response = urllib2.urlopen(url + query).read()
# Process the JSON string.
data = json.loads(response)

results = data ['responseData']['results']

for result in results:
    title = resul['title']
    url = result['url']
    print (title +';'+ url)
    

```
---