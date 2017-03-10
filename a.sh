#!/bin/bash

eco $(date) >> tgl.txt
git add tgl.txt
git commit -m "coba"
git push 

wget https://www.timeanddate.com/worldclock/ -O  waktu.html
git add waktu.html
git commit -m "update waktu "
git push 

cp waktu.html cobacopy.txt
git add cobacopy.txt
git commit -m "copy waktu"
git push 
