#!/bin/bash

defaultURL="https://github.com/ngosang/trackerslist/raw/master/trackers_best.txt"
URL=${1:-$defaultURL}
echo $URL
tracklist=$(curl -sfL "$URL")

list=$(echo $tracklist | sed -e "s/ /,/g")
echo $list
if [ -z $list ]; then
    echo "please ping github.com"
    exit 0
fi
sed -i '$ d' /root/.aria2/aria2.conf
echo bt-tracker=$list >> /root/.aria2/aria2.conf

aria2_pid=$(ps -ef | grep "[a]ria" | awk '{print $2}')
echo $aria2_pid
if [ ! -z $aria2_pid ]; then
    kill $aria2_pid
    sleep 1
fi 

aria2c --conf-path=/root/.aria2/aria2.conf -D
echo "--------success----------"
exit 0

