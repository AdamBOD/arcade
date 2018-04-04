DROP TABLE IF EXISTS snakestats;

CREATE TABLE snakestats
(
	username VARCHAR(20),
	score INT,
	PRIMARY KEY (username)
);

DROP TABLE IF EXISTS breakoutstats;

CREATE TABLE breakoutstats
(
	username VARCHAR(20),
	score INT,
	PRIMARY KEY (username)
);

DROP TABLE IF EXISTS easypongstats;

CREATE TABLE easypongstats
(
	username VARCHAR(20),
	score INT,
	PRIMARY KEY (username)
);

DROP TABLE IF EXISTS mediumpongstats;

CREATE TABLE mediumpongstats
(
	username VARCHAR(20),
	score INT,
	PRIMARY KEY (username)
);

DROP TABLE IF EXISTS hardpongstats;

CREATE TABLE hardpongstats
(
	username VARCHAR(20),
	score INT,
	PRIMARY KEY (username)
);

DROP TABLE IF EXISTS expertpongstats;

CREATE TABLE expertpongstats
(
	username VARCHAR(20),
	score INT,
	PRIMARY KEY (username)
);

DROP TABLE IF EXISTS register;

CREATE TABLE register
(
	username VARCHAR(20),
	userpassword VARCHAR(20),
	role VARCHAR(10),
	PRIMARY KEY (username)
);
SELECT *
FROM register;
