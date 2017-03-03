echo $(date) >> tgl.txt
wget https://www.timeanddate.com/worldclock/ -O  waktu.html
cp waktu.html cobacopy.txt

git commit -am "Test"
git push
