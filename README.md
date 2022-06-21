# Project setup

<h2> Steps to clone the project- </h2>

1- First clone the project to the system using the below command:

    git clone https://github.com/AnkurRathi1/albums.git
    
2- Open the project in pycharm editor or any preferred code editor.

3- open terminal:

Run below command to setup the virtual env if virtual enviornment is not setup yet.

    virtualenv venv

Check for the interpreter settings as python path will be inside the venv folder. If other python interpretor is set please configure with the venv python interpreter.

After that run below commant to activate the virtual env. you need to be in the same folder where venv folder exist.

    source venv/bin/activate
    
Now virtual enviornment is activated. Next step is to install all the dependencies using the 'requirements.txt' file.
Run below command and you need to be in the same folder to install the dependencies.

    pip install -r requirements.txt
    
Now all the dependencies for the project were installed.

4- Check if project is running or not by running below command.

    python manager.py runserver -p 5000
    
if success then below lines occured

    $ python manager.py runserver -p 5000
    Serving Flask app 'manager' (lazy loading)
    Environment: production
    WARNING: This is a development server. Do not use it in a production deployment.
    Use a production WSGI server instead.
    Debug mode: on
    Running on http://127.0.0.1:5000 (Press CTRL+C to quit)
    Restarting with stat
    Debugger is active!
    Debugger PIN: 864-077-292
    
Now project is running successfully.
<h2>Setup postgresql database</h2>
    
1- Install and run the postgresql database in your system.
 
2- Once postgresql database setup is done and running then edit the '.env' file for database url.

    DATABASE_URI_DEV="postgresql://<yourpostgreusername>:<yourpostgreuserpass>@localhost/<Name of database>"
    DATABASE_URI_TEST="postgresql://<yourpostgreusername>:<yourpostgreuserpass>@localhost/<Name of database>"
    DATABASE_URI_PROD="postgresql://<yourpostgreusername>:<yourpostgreuserpass>@localhost/<Name of database>"

Now Database path setup complete.

3- Now run the below command in terminal to initialize the db.

    flask db init

4- Run below command in terminal to migrate the tables to create the tables in db.

    flask db migrate
    
5- Run below command in terminal to upgrade reflect the table changes in the database.

    flask db upgrade
    
  * <b>Note</b> this command is used to updgrade the table for changes made in the models

Now all tables generated in the database.

Now API's can be hit form postman.


