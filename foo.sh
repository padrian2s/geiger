#!/bin/bash
cdd=$(date +"%Y-%m-%d %H:%M:%S")
acceldate=$(tail -n 1 /home/a/accel.dat | awk '{split($0,ss, ","); print ss[2]}')
#echo $acceldate
seccs=$(date -d "$acceldate" +%s)

#echo $secs
rett=$(( ( $(date +'%s') - seccs ) ))

if (( $rett>180 )); then
 -- echo "hmmm... let reboot $rett"
 reboot
else
 echo "nothing to do"
fi
