import urllib
import urllib2
import json
# Google returns JSON
url = "http://ajax.googleapis.com/ajax/services/search/web?v=1.0&"

query = raw_input("What u want to LookFOr Matey ????? ")
query = urllib.urlencode({'q': query})

response = urllib2.urlopen(url + query).read()

data = json.loads(response)

results = data ['responseData']['results']

for results in results

for result in results:
    title = resul['title']
    url = result['url']
    print (title +';'+ url)
    
