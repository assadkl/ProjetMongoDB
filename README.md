# MongoDB project template
 
## Purpose
- This application solves specific issues related to salaries dataset.  

## Dependencies
-The file **requirements.in** set the dependencies and version requirements needed.
 
## About environment
The file named **.env-template** list the required environnement variables that your project need, but **does not** contains any citical informations such as credentials. It can contains **example values**. It's purpose is to show how to build the **.env** file.
 
The **.env** needs to be listed in the **.gitignore**, it's **not versionned**, it's **only in your system**.
 
Follow he next steps to configurate avec use the application.
 
## Configuration
Here are the steps to follow to run the application:
- You need to have access to a MongoDB database
- Create a virtual environment using "python -m venv 'your_environment_name'"
- Activate the environment by runing "your_environment_name/Scripts/activate" and you must be 
  located at the root of the project file
- Install the dependencies listed in requirements.in with "pip install -r requirements.in"
- Create your .env file as :
  "MONGO_HOST=localhost
   MONGO_PORT= 'your_mango_db_port'
   MONGO_DB_NAME=salaries"
- And then, insert it in the project file
- Replaces the XXX in .env file, by the corresponding fields
 
## How to use
To launch the application:
- Import the dataset by launching setup.py
- Run the application by launching main.py
 
## Troubleshooting
List here, the common issues that the users of your app can encounter.