
# Serial2web v1.0

Function: Serves as a wedge between a serial communication device and a web app. Also allows for ethernet based RS232 communication devices to be piped through to web based applications. This removes the need for clunky and expensive commercial serial to keyboard wedge solutions.

Use case:
- Barcode Readers
- Remote Sensors
- etc


## TCP/IP Ethernet to Web App (HTTP POST)

''''
$ nc -l <port> | python serial2web.py
''''

## Serial to Web APP (HTTP POST)

###Option 1
Intemediary RS232 to web server
''''
$ nc <intemediary_system> <port> < /dev/ttyS0
''''
Intemediary system to run TCP/IP listening mode using netcat


### Option 2
Without Intemediary Server
''''
$ python serial2web.py < /dev/ttyS0
''''