#!/usr/bin/python

import urllib
import urllib2
import ssl
import base64
import json


auth = base64.standard_b64encode('admin' +b':' + 'admin')
req = urllib2.Request('https://it-isamm-apt-01.sea.oit.unlv.edu/snapshots', headers={'Content-type':'application/json','Authorization':'Basic %s' % auth, 'Accept':'application/json'})
r = urllib2.urlopen(req).read()
json_response = json.loads(r)



import urllib
import urllib2
import ssl
import base64
import json

auth = base64.standard_b64encode('admin' +b':' + 'admin')
host = "it-isamm-apt-01"
domain = ".sea.oit.unlv.edu"
url = "https://" + host + domain + "/snapshots/"
headers = {'Content-type':'application/json','Authorization':'Basic %s' % auth, 'Accept':'application/json'}
data = "{\"comment\":\"this is a test by jeremiah\"}"
snap_req = urllib2.Request(url, data, headers)
response = urllib2.urlopen(snap_req)
print response.read()
print response

id = "a4cb68838c595f41992d1318119eadf3"
snap_url = url + "download?record_ids=" + idsnap

file = urllib2.Request(snap_url, headers = {'Content-type':'application/json','Authorization':'Basic %s' % auth, 'Accept':'application/json'})
download = urllib2.urlopen(file)
with open("/tmp/testFile", "wb") as local_file:
	local_file.write(download.read())

urllib.urlretrieve(snap_url, "/tmp/snapTest")




def takeSnap(req):
	data = urllib.urlencode({'comment':'this is a test by jeremiah'})
	req.add_header(data)
	result = urllib2.Request(req)
	response = result.read()
	print response

