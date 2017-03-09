#/usr/bin/python

r = open("fruits.txt")
line = r.readline()

while line:
  print(line)
  line = r.readline()
r.close()

