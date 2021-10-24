#!/bin/bash

red="\e[0;91m"
blue="\e[0;94m"
reset="\e[0m"

read -p "[$(echo -e $blue"?"$reset)] Enter name python file : " filepy

pyinstaller $filepy

echo -e "$red if you want to see ' exe ' file go to ' dist ' Folder ... $reset"
