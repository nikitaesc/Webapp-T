# Web application using Azure App Service

This repository contains a web application that provides User Registration and Login functionality, a user-specific Dashboard, and a RESTful API for performing CRUD operations on user data. The application is built using [python] and [flask], and it is designed to be deployed on Azure Web App Service.

# Features

* User Registration: Users can create an account by providing their username, email, and password. Passwords are securely hashed and stored in the database. 
* User Login: Registered users can log in with their credentials (username and password). When you try loging in without registration an error message pops saying "Error: Login failed! The login information is incorrect."
* User Dashboard: Upon successful login, users are presented with a personalized dashboard that displays user-specific information.
* RESTful API: The application provides a RESTful API that allows users to perform CRUD (Create, Read, Update, Delete) operations on their data.

# Prerequisites 
- Before running or deploying this application, ensure you have the following:

* Azure Account (for Azure App Service deployment) 
* [Python] and [Flask] installed locally (for development) 
* A database service (e.g., Azure SQL Database) or a locally hosted database (e.g., PostgreSQL, MySQL) 
* Azure App Service CLI (for deployment)

# Getting Started 
Follow this link for the web app - https://applicationtriluxo.azurewebsites.net/register

* Contact If you have any questions, feel free to contact {2nikitaesc@email.com].
