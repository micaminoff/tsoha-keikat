# Installation

### Running locally
This only requires cloning, installing, and running - no extra steps!
* Clone the repo
* pip install -r requirements.txt
* python run.py

### Running on heroku
* Create an account on heroku
* Install heroku cli
* Create an app in heroku (e.g. `heroku create tsoha-keikat`. Replace tsoha-keikat with a unique name)
* Add a remote to you vcs (e.g. with git `heroku remote add heroku URL`, where URL depends on you app's name)
* Push to the new remote


* For persistency, consider using postgres
* `heroku config:set HEROKU=1`
* `heroku addons:add heroku-postgresql:hobby-dev`

### Usage instructions
* Create a user/admin by pressing the button in the header
* If you are a returning user - simply log in with the same button
* Create as many bands as you wish and watch them become choices in the event form
* Add up to 10 bands to any event thanks to a many-to-many relationship
* Explore events, performers, and your own account to edit events and performers