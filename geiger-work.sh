#!/bin/bash

/usr/bin/gnuplot /home/pi/gnuplot-geiger
tail -1440 /home/pi/accel.dat >/home/pi/accel24.dat
tail -60 /home/pi/accel.dat >/home/pi/accel2h.dat
/usr/bin/gnuplot /home/pi/gnuplot-geiger24
/usr/bin/gnuplot /home/pi/gnuplot-geiger2h

cp /home/pi/a.png /usr/lib/cgi-bin/.
cp /home/pi/a24.png /usr/lib/cgi-bin/.
cp /home/pi/a2h.png /usr/lib/cgi-bin/.

