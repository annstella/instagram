# INSTAGRAM.

This is  an application that represents the famous photo app,instagram.

## Getting Started.

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 

* $ git clone https://github.com/annstella/instagram/
* $ cd instagram
* $ source virtual/bin/activate

Install all the necessary requirements by running pip install -r requirements.txt (Python 3.6).
* $ configure your prefered database provider in the settings.
* $ ./manager.py check
* $ ./manager.py makemigrations Gram
* $ ./manager.py migrate
* $./manager.py runserver

### As a user of the application I should be able to:

* Sign in to the application to start using.
* Upload my pictures to the application.
* See my profile with all my pictures.
* Follow other users and see their pictures on my timeline.
* Like a picture and leave a comment on it.



#### Things you need to install to the software.
* Django==1.11
* django-bootstrap3==11.0.0
* Pillow==5.2.0
* psycopg2==2.7.5
* pytz==2018.5

##### Deployment

Link to a live site: 


#### Known bugs
* The function for the likes does not work,but I wil work on it later..

#### Authors

Annstella Kagai

#### License

MIT LICENSE (c) 2018,Annstella kagai

#### Acknowledgments
Inspiration