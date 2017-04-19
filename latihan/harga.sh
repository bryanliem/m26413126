#!/bin/bash

harga=$(curl -s http://www.elevenia.co.id/prd-kintakun-dluxe-sprei-king-size-180x200-dengan-pilihan-motif-18547596 |grep "price  notranslate" | sed -e 's/<[^>]*>//g' | sed -e 's/^[ \t]*//g' |sed -e 's/^[ \t]*//g' | cut -d' ' -f2 | sed -e 's/[.]//g' | sed 's/\r$//')
if [ $harga -lt 15000000 ]; then
echo "Harga sekarang adalah"$harga | mail -s "UTS-TOS" "m26413126@john.petra.ac.id"
else
echo "lala"
fi

echo $harga >> "/home/m26413126/repo/m26413126/latihan/harga.txt"
