# User Stories
:soon: Partially realized
:white_check_mark: Fully realized
:no_entry: Not implemented

## User
* As a user, I can create a performer :white_check_mark:
```SQL
INSERT INTO performer (date_created, date_modified, name, genre, account_id) VALUES (?)
```
* As a user, I can create an event :white_check_mark:
```SQL
INSERT INTO event (date_created, date_modified, name, date, venue, account_id) VALUES (?))
```
* As a user, I can list all performers :white_check_mark:
```SQL
SELECT name, genre FROM performer
```
* As a user, I can list all events :white_check_mark:
```SQL
SELECT name, date, venue FROM event
```
* As a user, I can view all my events :white_check_mark:
```SQL
SELECT name, date, venue FROM event
WHERE event.account_id = ?
```
* As a user, I can view all my performers :white_check_mark:
```SQL
SELECT name, genre FROM performer
WHERE performer.account_id = ?
```
* As a user, I can see how many events I've created :white_check_mark:
```SQL
SELECT COUNT(*) FROM Event e
WHERE e.account_id = ?
```
* As a user, I can see how many events a performer is scheduled for :white_check_mark:
```SQL
SELECT COUNT (*) FROM Event e
INNER JOIN event_performer_rel_table rel ON (e.id = rel.event_id)
INNER JOIN Performer p ON (rel.performer_id = ?)
WHERE p.id = ?
```
* As a user, I can create a venue :no_entry:

## Creator
* As the creator of an event, I can delete that event :white_check_mark:
```SQL
DELETE FROM event WHERE event.id = ? AND event.account_id = ?
```
* As the creator of an event, I can edit that event :white_check_mark:
```SQL
UPDATE event SET name = ?, date = ?, venue = ?
WHERE event.id = ? AND event.account_id = ?
```
* As the creator of a performer, I can delete that performer :white_check_mark:
```SQL
DELETE FROM performer WHERE performer.id = ? AND performer.account_id = ?
```
* As the creator of a performer, I can edit that performer :white_check_mark:
```SQL
UPDATE performer SET name = ?, genre = ?
WHERE performer.id = ? AND perfomer.account_id = ?
```
* As the creator of a venue, I can edit that venue :no_entry:

## Admin
* As an admin, I can edit any event :white_check_mark:
* As an admin, I can delete any event :white_check_mark:
* As an admin, I can edit any performer :white_check_mark:
* As an admin, I can delete any performer :white_check_mark:
* As an admin, I can edit any venue :no_entry:
* As an admin, I can delete any venue :no_entry:
```SQL
--These are the same as user stories, but skip WHERE x.account_id = ?
-- e.g. delete any performer
DELETE FROM performer WHERE performer.id = ?
```