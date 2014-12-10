#!/bin/bash

t=0

while true; do
 echo "wait 5m..."
 sleep 5m
 ping -c 1 www.youtube.com &>/dev/null
 if [ "$?" = 0 ]; then
    echo "is alive"
    echo go >/home/a/pistat
 else
    if (( $t>40 )); then
      echo "reboot"
      echo $(date) >> /home/a/reboots
      reboot
    fi
    echo "is not alive"
    echo wait >/home/a/pistat
    t=$((t+1))
    #echo $t
 fi

 cdd=$(date +"%Y-%m-%d %H:%M:%S")
 acceldate=$(tail -n 1 /home/a/accel.dat | awk '{split($0,ss, ","); print ss[2]}')
 seccs=$(date -d "$acceldate" +%s)
 rett=$(( ( $(date +'%s') - seccs ) ))
 if (( $rett>180 )); then
  echo "hmmm... let reboot $rett"
  echo $(date) >> /home/a/reboots
  reboot
 else
  echo "nothing to do"
 fi

done