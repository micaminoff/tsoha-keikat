## Account
```SQL
CREATE TABLE account (
        id INTEGER NOT NULL,
        date_created DATETIME,
        date_modified DATETIME,
        email VARCHAR(144) NOT NULL,
        password VARCHAR(144) NOT NULL,
        admin BOOLEAN,
        PRIMARY KEY (id),
        CHECK (admin IN (0, 1))
)
```
## Event
```SQL
CREATE TABLE event (
        id INTEGER NOT NULL,
        date_created DATETIME,
        date_modified DATETIME,
        name VARCHAR(144),
        date DATE NOT NULL,
        venue VARCHAR(144) NOT NULL,
        account_id INTEGER NOT NULL,
        PRIMARY KEY (id),
        FOREIGN KEY(account_id) REFERENCES account (id)
)
```
## Performer
```SQL
CREATE TABLE performer (
        id INTEGER NOT NULL,
        date_created DATETIME,
        date_modified DATETIME,
        name VARCHAR(144) NOT NULL,
        genre VARCHAR(144),
        account_id INTEGER NOT NULL,
        PRIMARY KEY (id),
        FOREIGN KEY(account_id) REFERENCES account (id)
)
```
## EventPerformer relationship table
```SQL
CREATE TABLE event_performer_rel_table (
        performer_id INTEGER NOT NULL,
        event_id INTEGER NOT NULL,
        PRIMARY KEY (performer_id, event_id),
        FOREIGN KEY(performer_id) REFERENCES performer (id),
        FOREIGN KEY(event_id) REFERENCES event (id)
)
```