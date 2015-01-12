# Serial (RS232 & TCP/IP) wedge to Web App (HTTP POST)
# Version 1.0


import httplib, urllib,sys


def send2web(data):
	data = data.replace("\n", "")
	params = urllib.urlencode({'devide': '1', 'datastream': data})
	headers = {"Content-type": "application/x-www-form-urlencoded",
	            "Accept": "text/plain"}

	conn = httplib.HTTPConnection("localhost:8888")
	conn.request("POST", "/scanner/add.php", params, headers)
	response = conn.getresponse()
	print response.status, response.reason
	data = response.read()
	conn.close()

if __name__ == "__main__":
	del sys.argv[0]
	if len(sys.argv):
	    for data in sys.argv:

	        send2web(data)
	if not sys.stdin.isatty():
	    while 1:
	        data = sys.stdin.readline()
	        if not data:
	            break
	        send2web(data)
