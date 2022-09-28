#!/bin/bash

# Prompts user for username to add and group name to add
userprompt(){
    echo "What is the name of user you want to create?"
    read USRNAME

    echo "In which group you want to add this user to?"
    read GRPNAME
}

# Creating user and group and adding new user to group with linux commands
createuser(){
    echo "Creating user - $USRNAME "
    sudo useradd $USRNAME
    echo "User created :$USRNAME"
    sleep 1
   
    sudo groupadd $GRPNAME
    echo "Adding $USRNAME to $GRPNAME group"
   
    sudo usermod -aG $GRPNAME $USRNAME
    echo "$USRNAME user added to $GRPNAME group."
}

# Exit option from the application
exit(){
    echo "Would you like to exit from this application afterwards? (Type exit)"
    read EXIT
}

# Welcome message for the application
echo "Welcome to My application."
sleep 1

echo "Here you can create user and add it to the group."
sleep 1

echo "You can create new group or use existing group."
sleep 1


# While loop to run application
while [ "$EXIT" != "exit" ]
do
     userprompt
     exit
     createuser
done


# Validation/check for new user that got created
echo "----------------------------------------------"
echo "Checking for new user details:"
id $USRNAME 
echo "----------------------------------------------"


echo "Thank you for using this application!"
