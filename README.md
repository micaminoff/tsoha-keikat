# tsoha-keikat

## Description
**tsoha-keikat** is my project for the course [Tietokantasovellus-harjoitustyö](https://materiaalit.github.io/tsoha-20/).

The app is hosted on [heroku](https://tsoha-keikat.herokuapp.com/).

The basic idea behind the app is to list shows with info about performer, venue, and date.

#### Current state of the app

* Event Table exists
* Users Table exists
* Performers Table exists
* Event and Performers many to many relation exists
* All events have an account reference
* All performers have an account reference
* Editing and deletion is restricted to the creator of an event or an admin
* Postgres running on Heroku
* CRUD functionality for the Events and perofmers tables
* Logging in and signing up works (even as admin!)
* Complex query for showing a performers events (visible in perofmers/<id>)

#### Future state of app
The app will
* Allow sorting by time/place/performer
* Allow searches by time/place/performer

## Documentation
Documentation can be found in the [docs](/docs) folder.

The diagram for the database can be found [here](/docs/Diagram.png).

User stories can be found [here](/docs/stories.md).

Test user for peer review etc is:
* test@user.com / HelloWorld
