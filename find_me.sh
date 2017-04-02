#!/bin/bash
#Sends GPS Data to a predefined number if a text message is received
while :
do
	gps_data="Lattitude: 43.771028 | Longitude: -79.500419"
	head -2 </dev/ttyUSB0 | tail -1 > test.txt
	count=`grep -c "^+CMTI" test.txt`
	#echo $count

	if [ $count -eq 1 ]
	then
		echo -ne 'AT\r' > /dev/ttyUSB0
		sleep 0.5
		echo -ne 'AT+CMGF=1\r' > /dev/ttyUSB0
		sleep 0.5
		echo -ne 'AT+CMGS="6479247251"\r' > /dev/ttyUSB0
		sleep 0.5
		echo -ne $gps_data > /dev/ttyUSB0
		sleep 0.5
		echo -ne '\x1a' > /dev/ttyUSB0

	fi
done
