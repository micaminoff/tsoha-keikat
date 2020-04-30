# tsoha-keikat

Since I was very, very sick for the last two weeks of the course, I had to reduce the scope of the project considerably.

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
* CRUD functionality for the Events and perfomers tables
* Aggregate functions in perfomer and user models
* Logging in and signing up works (even as admin!)
* Complex query for showing a performers events (visible in perfomers/<id>)

## Documentation
* Documentation can be found in the [docs](/docs) folder.
* Installation reference is [here](/docs/installation.md).
* The diagram for the database can be found [here](/docs/final_diagram.png).
* User stories can be found [here](/docs/stories.md).
* Final thoughts can be found [here](/docs/final_submission.md).
* [CREATE ALL THE TABLES.](/docs/CREATE_TABLE.md)

Test user for peer review etc is:
* test@user.com / HelloWorld

*hei katselmoija, voit antaa palautteen suomeksi jos haluat*
