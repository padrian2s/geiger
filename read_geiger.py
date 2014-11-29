import serial
import datetime
import time

import smtplib

fromaddr = 'geigercounter2ss@gmail.com'
toaddrs  = 'adrian.paleacu@gmail.com'
msg = 'myRandom generator registered values above 40:'


# Credentials (if needed)
username = 'geigercounter2ss@gmail.com'
password = '******'


addr  = '/dev/ttyACM0'
baud  = 9600
fname = '/home/a/accel.dat'
fmode = 'ab'
reps  = 10
t=0
current  = time.strftime("%Y-%m-%d %H:%M")

with serial.Serial(addr,baud) as port, open(fname,fmode) as outf:
    while(1):
     x = port.readline()
     if current == time.strftime("%Y-%m-%d %H:%M"):
        t = t + 1
     else:
          current = time.strftime("%Y-%m-%d %H:%M")
          print (t, time.strftime("%Y-%m-%d %H:%M"))
	  a = str(t) +',' + time.strftime("%Y-%m-%d %H:%M")+'\n'
	  outf.write(a)
    	  outf.flush()
	  if t>40:
	    # The actual mail send
	    server = smtplib.SMTP('smtp.gmail.com:587')
	    server.starttls()
	    server.login(username,password)
	    server.sendmail(fromaddr, toaddrs, msg+" "+str(t))
	    server.quit()
          t = 0




