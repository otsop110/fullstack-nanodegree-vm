## Udacity Fullstack Nanodegree - Film Item Catalog App
This film item catalog is a full stack application that allows users to login into the system and add films to the database. Logged-in users may modify and delete the items they have created. Only authenticated users are allowed to make any changes to the database.

## Project Requirements
* Project implements a JSON endpoint that serves the same information as displayed in the app.
* App reads category and item information from a database.
* It includes forms allowing users to add new films and edit/update a current record and correctly processes submitted forms.
* Website includes a function to delete a current record from the database.
* Create, delete and update operations require authorization prior to execution.
* Page implements a third-party authentication & authorization service - login with Facebook or Google+

## Technologies used
Backend: Python Flask SQLAlchemy
Frontend: HTML, CSS, JS

## Installation and How to View This App
1. Install Vagrant and VirtualBox
2. Clone the [fullstack-nanodegree-vm](https://github.com/udacity/fullstack-nanodegree-vm) repository
3. Download this repository and move the repository to fullstack-nanodegree-vm/vagrant folder
4. Launch and connect to the Vagrant VM
```
    vagrant up
    vagrant ssh
```
5. Setup and initially populate the database
```
    # in the root directory for project:
    python database_create.py
    python lotsofgenres.py
```
6. Run the application
```
    python application_films.py
```
7. Access the application
Visit [http://localhost:5000](http://localhost:5000)

8. Remember to add your Google+ and Facebook Client secrets to client_secrets.json and fb_client_secrets.json files. Otherwise the Login authorization won't work.

### Google credentials file
* Go to https://console.cloud.google.com/apis/credentials/oauthclient and setup Google OAuth API Credentials. 
* Enter ```http://localhost:5000``` in the Authorized JavaScript origins and ```http://localhost:5000/login and http://localhost:5000/gconnect``` in the Authorized redirect URIs.
* After saving, download JSON and rename the file to ```client_secrets.json``` and replace the file with the same name in the project directory.

### Facebook credentials file
* Go to https://developers.facebook.com/apps and setup a new app.
* Add a new product "Facebook Login" and add ```http://localhost:5000``` in the site URL.
* Add your Client id and secret in the ```fb_client_secret.json``` file.

## Helpful Resources
* [Google OAuth Credentials](https://console.cloud.google.com/apis/credentials/oauthclient)
* [Facebook Deveopers](https://developers.facebook.com/apps)
* [PEP8 online checker](http://pep8online.com/)
* [Flask SQL Alchemy Documentation](http://flask-sqlalchemy.pocoo.org/2.3/)