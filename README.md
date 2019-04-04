<a href="http://fvcproductions.com"><img src="https://www.python.org/static/opengraph-icon-200x200.png" title="python" alt="python"></a>

<!-- added link for image above  -->


# Python Scripts and programs 

> Here is some programs and scripts written in python.
There will be a short discription on each program. 
Feel free to use or clone ;)

---

**List of Programs Table of contents**

- [Convert](#1.convert)
- [cycle](#2.cycle)
- [Google Command Line script](#3.Googlescript)
- [imdb script](#4.IMDB)
- [Internet](#5.Internet) 
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

```python
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
## 4.IMDB
>Here is a little program that brings up Title and year of movie from an input. 

```Python
#!/usr/bin/env python27

#Importing the modules

from BeautifulSoup import BeautifulSoup
import sys
import urllib2
import re
import json

#Ask for movie title
title = raw_input("Please enter a movie title: ")

#Ask for which year
year = raw_input("which year? ")

#Search for spaces in the title string
raw_string = re.compile(r' ')

#Replace spaces with a plus sign
searchstring = raw_string.sub('+', title)

#Prints the search string
print searchstring

#The actual query
url = "http://www.imdbapi.com/?t=" + searchstring + "&y="+year

request = urllib2.Request(url)

response = json.load(urllib2.urlopen(request))

print json.dumps(response,indent=2)

```
---

## 5.Internet
>A small program to see if your connected to the internet 


```python
from requests import get
from requests import exceptions
def internetConnection():
    try:
        get('http://Google.com', timeout = 3)
        print('Connected')
    except exceptions.ConnectionError:
        print('not connected') 

internetConnection()
```
---

### 6.Loops
> A small program that goes through loops 

```Python 

sum = 0 
for i in range(5):
    sum = sum + i 
    print sum ￼

```

---
### 7. lsname 
> A program the makes a list in in linux 

```Python 
#!/usr/bin/python3


import commands
# uses the ls command in linux to show whats in folder 
output = commands.getoutput('ls')
print output

#prints out the number of d are in there in folder 
num = output.count('d')
print num

```

---