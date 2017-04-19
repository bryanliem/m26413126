#!/bin/bash

temp=$(/sbin/ifconfig | grep " inet addr" | head -n -1 | cut -f2 -d":" | sed 's/  Bcast//g')
echo "Server IP Address: "$temp

temps=$(cat /etc/passwd | wc -l)
echo "Jumlah Account Total: "$temps

tempa=$(cat /etc/passwd | grep "m264" | wc -l)
echo "Jumlah Account Mahasiswa: "$tempa

tempd=$(who | wc -l)
echo "Jumlah Account Online: "$tempd

who | tail -n 10

