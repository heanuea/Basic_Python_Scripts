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
    
