# cits5505-project2

## Introduction
This Web application is a site for users to learn basic HTML, CSS, and JS skills.Users can register as new users on the site, and for registered users, they can log in directly to access the page.
After logging in, the user can view the different units available for study.Different units are divided into different chapters and sections.When learning a unit, users can view the chapters they have studied, the number of tests they have passed and the average score.You can choose to continue or start over from a chapter.
When entering the chapter, the current learning progress can be recorded, so that the progress can be viewed in the unit page.After studying a unit, you can take a quiz. After submitting the answer, you will be given the correct answer and the score.

## Getting Started
### Installing
This application can be deployed locally, install git and clone the reposistory.

Get the code:
```git
git clone https://github.com/ZhuyuPhoebe/cits5505-project2.git
```

Generate a virtual environment and install dependencies:
```
$ py -m venv venv
$ ./venv/Scripts/activate.bat
$ pip install -r requirements.txt
```

### Running
run main function in main.py
```python
py main.py
```

## Architecture
### back-end
Plug-ins, packages: flask_cors to avoid cross-domain errors; Sqlite3 database.

Main is the body file of the back end, which contains the Falsk route and code.
cits.db is the file generated by the database (need to delete this file if you want to initialize the database);
initdatabase.py is the script file that initializes the database;

### front-end
The page may not be navigated, because it is viewed layer by layer. Users can check the learning progress, exam times and scores on the unit details page.
Start way: open index. HTML page to visit
Plugins, package: Bootstrap page style, jQuery: js operation DOM plug-in library

Pages is the folder of pages; Static is the directory for static files, including CSS and JS files.

## unit test
Unit test includes user login, registration, obtaining different units, different chapters, user's learning progress, test scores and so on.

```
py .\test_mian.py
```

print:
```
----------------------------------------------------------------------
Ran 18 tests in 1.090s

OK
```

```
py .\test_db.py
```

print:
```
----------------------------------------------------------------------
Ran 9 tests in 0.012s

OK
```

## Authors

ZhuyuPhoebe 635608969@qq.com

alexxug lyxxh718@gmail.com
