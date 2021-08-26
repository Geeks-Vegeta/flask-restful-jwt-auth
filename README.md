<code><img height="80" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/python/python.png"></code> <code><img height="80" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/flask/flask.png"></code> <code><img height="80" src="https://raw.githubusercontent.com/github/explore/80688e429a7d4ef2fca1e82350fe8e3517d3494d/topics/mysql/mysql.png"></code>

# flask-restful-jwt-auth

This is an simple non flask blueprint, restful services build on flask framework integrated with mysql database with flask_sqlalchemy.

This repository is really better to understand and it is also an begginer friendly.

> Read comments for better understand what is exactly going on in each function, and on each variable.

> It would be helpful if you fork and add stars to this repo and I also welcome you to make changes in this respository


To download this respository follow the following steps given below.


## Steps for setting up this respository


### ➡️ Step 1

Clone/Download this repository 

```bash
$ git clone https://github.com/Geeks-Vegeta/flask-restful-jwt-auth.git

```

after that 

```bash
$ cd [folder name]

```

Install all the given packages globally
```bash
$ pip install -r requirements.txt

```
**OR**

If you want to install the packages in virtual environment
```bash
$ pip install virtualenv

```

then create a virtual  environment in your package
```bash
$ python -m venv venv

```

activate this virtual environment
```bash
$ source venv/bin/activate

```

and if you want to deactivate this virtual environment
```bash
$ deactivate

```

> do not deactivate venv if you are running this project

Once your virtual enviroment is activate download all packages

Install all the given packages 
```bash
$ pip install -r requirements.txt

```

### ➡️ Step 2

If you are using xampp server then just create a database of name **FlaskLogin**

Once database is created open a new bash/cmd prompt in same folder and type this following steps

```bash
$ from api import db
$ db.create_all()

```

If you got any error regarding mysqlclient is not defined or allowed just install mysqlclient given in folder

```bash
$ pip install mysqlclient-1.4.6-cp37-cp37m-win32.whl
```

> this is a binary file only for python version 3.7 and it will not work on any python below 3.7 or above 3.7

If you want to download file for your requirement [click here](https://www.lfd.uci.edu/~gohlke/pythonlibs/)

one download again repeate create_all() command
if you not get any error that means it is success.


### ➡️ Step 3 

Run this repository

```bash
$ python -m app

```

If you like 😃 this project please give a star.