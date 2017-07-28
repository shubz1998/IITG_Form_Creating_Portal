# IITG-Form-Creating-Portal
a Form creating portal in DJANGO framework with user having full control over the form fields and fields type, option of file upload, what content is displayed and IITG webmail authentication for enhanced security. The portal can be utilised to automate tasks like feedback collection etc without making a separate portal for it.
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
