#!/bin/bash

read -p "What is your favorite operating system? " oper

if [ $oper = "Mac" ] || [ $oper = "Windows" ] ; then
   echo "Bad Operating System!"
elif [ $oper = "mac"  ] || [ $oper = "windows" ] ; then
   echo "Bad Operating System!"
elif [ $oper = "Linux" ] || [ $oper = "linux" ] ; then
   echo "Great Choice!"
else
   echo "Is $oper an operating system?"
fi
