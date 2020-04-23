# tsoha-keikat

**olen ollut erittäin kipeä viimeiset 5 päivää, en ole voinut kehittää mitään, mutta vähän dokumentaatiota olen jaksanut kirjoittaa."

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

#### Running locally
This only requires cloning, installing, and running - no extra steps!
* Clone the repo
* pip install -r requirements.txt
* python run.py

#### Usage instructions
* Create a user/admin by pressing the button in the header
* If you are a returning user - simply log in with the same button
* Create as many bands as you wish and watch them become choices in the event form
* Add up to 4 bands to any event thanks to a many-to-many relationship

#### Next steps and restrictions
* Venues are not yet implemented, they will add another dimension to creating events
* Filtering is not implemented, though that is coming next week.
* Forms need stricter validation to adhere to SQL schema

## Misc. documentation
Documentation can be found in the [docs](/docs) folder.

The diagram for the database can be found [here](/docs/Diagram.png).

User stories can be found [here](/docs/stories.md).

Test user for peer review etc is:
* test@user.com / HelloWorld

*hei katselmoija, voit antaa palautteen suomeksi jos haluat*
