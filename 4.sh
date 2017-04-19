#!/bin/bash

tembeliusd=$(curl -s http://bankmandiri.co.id/ | grep "td align" | sed -e 's/<[^>]*>//g' | sed -e 's/^[ \t]*//g' | sed -n '1p' | sed -e 's/[.]//g' | sed -e 's/,00//g')
temjualusd=$(curl -s http://bankmandiri.co.id/ | grep "td align" | sed -e 's/<[^>]*>//g' | sed -e 's/^[ \t]*//g' | sed -n '2p' | sed -e 's/[.]//g' | sed -e 's/,00//g')
tembelisgd=$(curl -s http://bankmandiri.co.id/ | grep "td align" | sed -e 's/<[^>]*>//g' | sed -e 's/^[ \t]*//g' | sed -n '5p' | sed -e 's/[.]//g' | sed -e 's/,00//g')
temjualsgd=$(curl -s http://bankmandiri.co.id/ | grep "td align" | sed -e 's/<[^>]*>//g' | sed -e 's/^[ \t]*//g' | sed -n '6p' | sed -e 's/[.]//g' | sed -e 's/,00//g')
tembeliaud=$(curl -s http://bankmandiri.co.id/ | grep "td align" | sed -e 's/<[^>]*>//g' | sed -e 's/^[ \t]*//g' | sed -n '9p' | sed -e 's/[.]//g' | sed -e 's/,00//g')
temjualaud=$(curl -s http://bankmandiri.co.id/ | grep "td align" | sed -e 's/<[^>]*>//g' | sed -e 's/^[ \t]*//g' | sed -n '10p' | sed -e 's/[.]//g' | sed -e 's/,00//g')

date +"%m-%d-%y %T" >> "/home/m26413126/repo/m26413126/hasil.txt"
echo "Beli USD: " $tembeliusd >> "/home/m26413126/repo/m26413126/hasil.txt" 
echo "Jual USD: " $temjualusd >> "/home/m26413126/repo/m26413126/hasil.txt"
echo "Beli SGD: " $tembelisgd >> "/home/m26413126/repo/m26413126/hasil.txt"
echo "Jual SGD: " $temjualsgd >> "/home/m26413126/repo/m26413126/hasil.txt"
echo "Beli AUD: " $tembeliaud >> "/home/m26413126/repo/m26413126/hasil.txt"
echo "Jual AUD: " $temjualaud >> "/home/m26413126/repo/m26413126/hasil.txt"

0 8,10,12,14,16 * * 1-5 bash /home/m26413126/repo/m26413126/4.sh
