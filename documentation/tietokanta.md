### Tietokanta

CREATE TABLE account (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	name VARCHAR(144) NOT NULL, 
	username VARCHAR(144) NOT NULL, 
	password VARCHAR(144) NOT NULL, 
	PRIMARY KEY (id)
)

CREATE TABLE task (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	name VARCHAR(144) NOT NULL, 
	done BOOLEAN NOT NULL, 
	account_id INTEGER, 
	PRIMARY KEY (id), 
	CHECK (done IN (0, 1)), 
	FOREIGN KEY(account_id) REFERENCES account (id)
)

CREATE TABLE stair (
	id INTEGER NOT NULL, 
	date_created DATETIME, 
	date_modified DATETIME, 
	stair_letter VARCHAR(144) NOT NULL, 
	account_id INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(account_id) REFERENCES account (id)
)

### Selvennys

Käyttäjään liittyy taulut task ja stair.



