#!/bin/bash
echo "Content-type: text/html"
echo ""
echo "<html><head><title>c"
echo "</title></head><body>"
echo ""
echo "<center>Information generated on $(date)</center>"
echo "</body></html>"

echo "$(/usr/bin/sshpass -p xxxx scp pi@192.x.x.xx:/home/pi/dust.dat /home/a/dust.dat)"
echo "$(/usr/bin/gnuplot /home/a/gnuplot-dust)"

echo "<img src=\"/d24.png\">"

echo "<center>Information generated on $(date)</center>"
