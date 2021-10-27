# se-03-team-19 (SE Sprint 03, Team 19)
<p align="right"><b>Tsayem Daniela</b></p>

### Instructions to run the backend:

1. Clone repository with `git clone git@github.com:lorenzorota/se-03-team-19.git`
2. cd into backend folder with `cd se-02-team-19/beer_game_backend`
3. Run `sudo apt-get install python3-dev libmysqlclient-dev` to install some additional dependencies
4. Install python requirements with `make`
5. Install mysql-python: 
`sudo add-apt-repository 'deb http://archive.ubuntu.com/ubuntu bionic main'`
`sudo apt update`
`sudo apt install -y python-mysqldb`

For more info: https://stackoverflow.com/a/66033872 https://stackoverflow.com/a/5873259

6. Log into MySQL first with the root user (`mysql -u root -p`) and password and create a new user using the CLAMV credentials provided to you by the TA:

mysql> `CREATE USER 'seteam19'@'localhost' IDENTIFIED BY 'dvuimw';`

mysql> `GRANT ALL PRIVILEGES ON * . * TO 'seteam19'@'localhost';`

7. Log into MySQL with `mysql -u seteam19 -p` and create a database with `create database seteam19;`. 
8. . Run the backend with `python main.py`. It should be accessible at http://localhost:5000 
9. To test the backend: `pytest test_main.py`
10. The documentation can be found at beer_game_backend/docs/_build/html/index.html

### Instructions to run the frontend:

1. Check the existence of `node.js` and `npm(node package manager)` using commands
   `node --version` and `npm --version` on terminal

   If not exist, install from http://nodejs.org (npm will be installed with node.js).
   
   Now you will have both `node.js` and `npm` installed.
2. cd into frontend folder with `cd se-02-team-19/beer_game` and enter `npm install` to install requirements
3. `npm start` to start the project
4. Now you are ready to begin your project! :-)
5. Run tests with `npm test`

### Required Packages:
* material-ui/core
* material-ui/icons
* react-router (for web)
* axios
* react testing library

### Progress Report:

* Created virtual environment
* Created Makefile
* Streamline installation
* Started implementation on handling post request on the /signup route
* Started CRUD implementation for databases

### To be done:
* Sign in and Sign up should be linked with backend and database
* Multiple instructors and games should be possible
* Connect backend and frontend for creating instructors
* Auth for accessing games
* Dashboard displaying all games for an instructor
* More coverage for tests for the backend and frontend
* More thorough documentation
* Ability to enable/disable showing incoming orders/demands
* Better UI
* More descriptive error alerts on the frontend (explanations for each error can be found where the backend returns the errors in main.py)
