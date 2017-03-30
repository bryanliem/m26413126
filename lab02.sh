#!/bin/bash

date +%a,' '%b' '%Y' '%X' '%z | tr '\n\r' ' ' >> logfile.txt
/sbin/ifconfig | grep 'inet addr:' | cut -d ':' -f3 | cut -d ' ' -f1 | tr '\n\r' ' ' | sed G >> logfile.txt
