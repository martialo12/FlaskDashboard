# [Flask Dashboard]()

Open-Source **admin dashboard** with **Argon** design coded in **Flask**
This is a simple customization of **Flask Argon Dashboard**

<br />

## Build from sources

1- Clone the repo
  ```
  $ git clone https://github.com/martialo12/FlaskDashboard.git
  $ cd FlaskDashboard
  ```

2- Initialize and activate a virtualenv:
  ```
    For linux or mac users:
  $ virtualenv --no-site-packages env
  $ source env/bin/activate

    For linux or mac users:
  $ virtualenv --no-site-packages env
  $ env\scripts\activate
  ```

3- Install the dependencies:
  ```
  $ pip install -r requirements.txt
  ```

4- Set the database by editing your configuration file
  ```
  $ flask shell
  $ >>> from app import db
  $ >>> db.create_all()
  ```

5- Run the development server:
  ```
    For windows users:
  > start.bat

    For linux or mac users:
  $ start.sh
  ```

6- See the running app by visiting [http://localhost:5000](http://localhost:5000) in your browser

<br />

## Features

- SQLite database
- Login, Register
- Static Build `python ./static.py`. The static build goes to `app/build` directory 
- FTP Deploy script. **Info**: this `require node.js` and the edit of `deploy.js` to add FTP server credentials. 

<br />

## Support

For issues and features request, please feel free to reach me at this address: **martialo218@gmail.com**
<br />

## App Screenshots

![Flask Dashboard](https://github.com/app-generator/flask-argon-dashboard/blob/master/screenshots/flask-argon-dashboard-login.jpg)

<br />

![Flask Dashboard](https://github.com/app-generator/flask-argon-dashboard/blob/master/screenshots/flask-argon-dashboard-profile.jpg)

<br />

