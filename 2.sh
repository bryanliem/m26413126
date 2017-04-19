#!/bin/bash

last -w -f /var/log/wtmp.1 | awk '{print $1}' | head -n -2 | uniq -c | sort

