DROP TABLE IF EXISTS DMOZ_ITEMS;

CREATE TABLE DMOZ_ITEMS(
	id int NOT NULL AUTO_INCREMENT,
	name varchar(255),
	url varchar(255),
	description varchar(255),
	PRIMARY KEY (id)
);