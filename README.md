# Timetable Generator

Timetable generator for university schedule implemented in Python using genetic algorithms

# Abstract
This project implements one of possible solutions for generating university schedule. The proposed solution is based on methods of evolutionary computing, uses (1+1) evolutionary strategy and simulated hardening. The success of solution is estimated on fulfillment of given constraints and criteria. Results of testing the algorithm show that all hard constraints are satisfied, while additional criteria are optimized to a certain extent.

# Problem
The assignment is to find generic solution that will facilitate generating timetable for Polytechnic (this  problem is adjusted to Moshood Abiola Polytechnic).


# Constraints
- A department cannot have more than 14 courses per semester
- A teacher only teaches one course per week
- Maximum of 4 lectures per day
- Class should take place in one of the allowed classrooms


# Solution
The algorithm for the timetable is represented as table with its columns as classrooms and rows allowed times for classes, while the elements of the table are the specific class held in proper classroom and given time. Table is a an object of days, lectures, lecturers and rooms, where the object corresponds to total number of possible times during the week (5 workdays, 8 hours a day).


# Algorithm
The algorithm consists of the following steps:
- Filter department's courses by the specific semester
- Assign rooms to the lectures if no room is assigned to it based its capacity
- pick 4 courses for each level for each day and store into an object
- convert the object in JSON for web visualization
- store the JSON data into the database with other necessary informations such as department, semester, date created ...


# Road blocks faced during development & how we solved them
- Sqlite3 does not support json field from django models so we used a 3rd party library (django-jsonfield) to store json field in the database

- 


## Useful links

-

## Requirements

- Python / Django

## Project setup

If not using docker, you can setup a virtual environment using the command below

```sh
python -m venv env
```

then activate it with

```sh
./env/Scripts/activate   # windows or
source env/bin/activate  # linux or mac
```

Once the virtual environment has been activated, install the necessary requirements by using the command below

```
pip install -r requirements.txt
```

After installation, type the command below to migrate all migrations

```sh
python manage.py migrate
```

Start the development server using the command below

```
python manage.py runserver
```

## Contribution

If you haven't cloned the repository, use the command to clone from the terminal

```sh
git clone https://gitlab.com/tushortz/softskillspace
```

When creating a new branch, **ENSURE** that the branch name starts with the format **TG-&lt;issue-no&gt;-&lt;short-description&gt;** e.g. **TG-1-project-setup** and the main branch is from develop.

When creating a pull request, please select the target branch as `develop`.

- After writing your code, make sure to run the tests and **ENSURE** it passes before pushing to the git repository. Use the command below to run the test.

```sh
python manage.py test
```

## Pushing to the repository

Run the following command

```sh
 # if pushing for the first time
$ git push -u origin <branchname>

# if pushing normally
$ git push
```
