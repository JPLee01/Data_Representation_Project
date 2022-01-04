# Data Representation Project

* **Author:** John Paul Lee
* **Github:** JPLee01
* **Email:** G00387906@gmit.ie
* **Created:** 08-12-2021, **Last update:** 04-01-2022
------------------------------------------------------------------------------------------------
**Data Representation:** 

This repository has been created to demonstrte an understanding in creating and consuming RESTful APIs.

**Lecturer:** Andrew Beatty

The Project instructions can be found at [here](https://github.com/JPLee01/Data_Representation_Project/blob/main/Project%20Description.pdf)

**Table of Contents**
------------------------------------------------------------------------------------------------

[Data Representation Project](#Data-Representation-Project)

[1. Introduction](#1-introduction)

[2. Project Repository](#2-project-repository)

[3. Libraries](#3-Libraries)

[4. Overview of the project](#4-Overview-of-the-project)

[5. User Guide](#5-User-Guide)

  [5.1 Downloading the Repository](#5.1-Downloading-the-Repository)

  [5.2  Running the Program](#5.2-Running-the-Program)

## 1 Introduction
------------------------------------------------------------------------------------------------
As part of the Project for the Fundamentals for Data Representation module a Project Repository has been created to create, investigate and perform RESTful APIs operations. This analysis will be conducted through a number of files including; Python code, HTML code, cURL code and Ajax code.

## 2 Project Repository
------------------------------------------------------------------------------------------------
The Project Repository is the source where all the work associated with
the project will be stored. It contains the following files and can be
located [here](https://github.com/JPLee01/Data_Representation_Project):

  **File**    |     **Description**
  ---------   |   --------------------------------------------------------
  .gitignore | A Text File explicitly explaining to Git which files or folders to ignore in the Project
  ElectronicDAO.py | DAO Pattern - CRUD operations for Electronic database  
  index.html |  HTML that uses AJAX to link to the server and provide a user interface for the Electronic database 
  initdb.sql | SQL code to create the database, create the tables and populate the tables
  LICENSE     |    MIT License for the project
  Project Description.pdf | A PDF copy of the Poject Description and Instructions
  README.md   |    This file; A Description of the project and instructions
  Server.py |  Flask server that implements a REST API that performs CRUD operations
  requirements.txt | List of necessary packages 
  Test_ElectronicDAO.py | DAO Pattern - Test CRUD operations for Electronic
  database
                                          
## 3  Libraries
------------------------------------------------------------------------------------------------
The following libraries were used in the writing of the projects code and are required to successfully run the programs:
- [mysql-connector-python](https://pypi.org/project/mysql-connector-python/)
- [Flask](https://pypi.org/project/Flask/)
- [Flask-MySQLdb](https://pypi.org/project/Flask-MySQLdb/)
- [Python 3.10.1](https://www.python.org/downloads/release/python-3101/)

* Please also check the [requirements.txt](https://github.com/JPLee01/Data_Representation_Project/blob/main/Requirements.txt) to see the other libraries used and their version.

* **Note**: Most of the languages/packages were included in the Anaconda programme. However, some of them were called through 'pip' on the command line or downloaded from the internet.

* **Note**: The computer system worked from is macOS Catalina version 10.15.07.

## 4  Overview of the project
------------------------------------------------------------------------------------------------   
1.  The data is stored in a MySQL database.
2.  The database queries are defined using the ```ElectronicDAO.py``` database access object.
3.  The ```server.py``` application server calls the queries and returns the results as JSON objects.
4.  AJAX calls are made in the ```index.html``` file and the results are displayed in nice tables in web browser.

## 5 User Guide
------------------------------------------------------------------------------------------------
This section will describe the steps required to download and run the files in the repository.

### 5.1 Downloading the Repository
The repository is stored at the following: https://github.com/JPLee01/Data_Representation_Project

To download the repository, do the following:
1.  Click on the above link to open the repository
2.  Once in the repository, click on the green “clone or download” button on the right side of the screen.
3.  Select "Download ZIP". This will open a prompt allowing you to save the file to a desired location on your computer.
4.  Navigate to where  the ZIP files are located on your computer and extract the compressed (.zip) files.

### 5.2 Running the Program
Once the repository has been downloaded, you will need to ensure that you are running it in the correct environment. It should be noted that this repository has been written using Python 3.8.2 and consequently it will require a Python version of 3.7 at a minimum to run as designed. The repository also requires a number of external libraries mentioned [above](#3-Libraries) to execute correctly. Once the correct version of Python has been installed complete with necessary libraries and the ZIP has been downloaded and extracted the user can run the program. The running of any of the programs from the command line can be executed as follows:
1. Open a virtual environment within the project folder of the repository.
2. Start mysql server. This can be achieved using [Wampserver](https://www.wampserver.com/en/) or [MAMP](https://www.mamp.info/en/windows/).
3. To create the database, the tables (items) and to insert data into the tables use the command code within ```initdb.sql```.
4. Run the Flask server named Server.py.
5. Type the following link into your browser: <http://127.0.0.1:5000/index.html> (assuming you are using the local host to serve the website).
6. Perform CRUD (Create, Read, Update and Delete) operations on the Electronic table.


