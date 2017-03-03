echo $(date) >> tgl.txt
wget https://www.timeanddate.com/worldclock/ -0 watku.html
cp waktu.html cobacopy.txt

git commit -am "Test"
git push
