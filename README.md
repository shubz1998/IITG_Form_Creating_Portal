# IITG-Form-Creating-Portal
to make custom forms with variable no of fields like google forms along with features of webmail authentication and file upload

___

## Requirements

**Django 1.10** and any suitable database(postgreSQL or SQLite). Currently **SQLite** is being used.

___

## Setting Up

1. Installing Django

		sudo apt-get update

		sudo apt-get install python3 python3-pip

		sudo pip3 install django=1.10

2. Migrating the Models

		./manage.py makemigrations

		./manage.py migrate		

3. Populating the Database
During deployment on a server,settings for static file has to be updated.

## User Manual
User manual for creating forms has been uploaded on google drive
https://drive.google.com/open?id=14l47Bwt-G7lLZUSA8ZOGMsZuNJ7QYmM9nHz2xLlAVFU
