import simplejson
import urllib2
url = ('https://ajax.googleapis.com/ajax/services/search/images?' +
...        'v=1.0&q=barack%20obama&userip=192.168.0.106')

request = urllib2.Request(url, None, {'Referer': "https://www.google.co.in/search?q=Prestige+jindal+city&source=lnms&tbm=isch"})
response = urllib2.urlopen(request)
results = simplejson.load(response)

results

{'responseData': None, 'responseDetails': 'This API is no longer available.', 'responseStatus': 403}


request = urllib2.Request(url, None, {'Referer': "https://www.google.co.in/search?q=Prestige%20jindal%20city&source=lnms&tbm=isch"})
response = urllib2.urlopen(request)
results = simplejson.load(response)

results
{'responseData': None, 'responseDetails': 'This API is no longer available.', 'responseStatus': 403}

