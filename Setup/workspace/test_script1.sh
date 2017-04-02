#!/bin/bash
# declare STRING variable
PhoneNumber="6479247251"
Message="Hey, I Sent this from a raspberry pi running linux"
echo -e "Please Enter a phone number: /c"
read  PhoneNumber
echo -e "You have entered : $PhoneNumber Is this correct? (y/n): /c"
read validPhone 

echo -ne 'AT\r' > /dev/ttyUSB0
sleep 0.5
echo -ne 'AT+CMGF=1\r' > /dev/ttyUSB0
sleep 0.5
echo -ne 'AT+CMGS="' > /dev/ttyUSB0
sleep 0.5
echo -ne $PhoneNumber > /dev/ttyUSB0
sleep 0.5
echo -ne '"\r' > /dev/ttyUSB0
sleep 0.5
echo -ne $Message > /dev/ttyUSB0
sleep 0.5
echo -ne '\x1a' > /dev/ttyUSB0


