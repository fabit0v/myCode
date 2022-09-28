#!/bin/bash


#declaring variables to use in functions

USER=$1
GROUP=$2

#This function will create a user and group based on user input

createuser(){
sudo useradd $USER
sudo groupadd $GROUP
echo "$USER is in group $GROUP"
    #Will add user to the group
sudo usermod -aG $GROUP $USER
}


#This prompt will ask a user to enter a username and groupname

prompt(){
echo "what's your name?"
read USER
echo "what group are you in?"
read GROUP
}


#order in which functions are called

prompt
createuser



