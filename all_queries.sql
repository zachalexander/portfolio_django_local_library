BEGIN TRANSACTION;

select * from users.portfolio_tweets
where tweetText like '%corona%'

select * from users.portfolio_tweetscount

drop table if exists users.portfolio_tweets;
drop table if exists users.portfolio_tweetscount;

CREATE TABLE users.portfolio_tweets (
id int NOT NULL PRIMARY KEY,
tweetText varchar(255) NOT NULL,
user varchar(255) NOT NULL,
followers int NOT NULL,
date datetime NOT NULL,
location varchar(255),
coordinates_lat varchar(255),
coordinates_lon varchar(255)
);

CREATE TABLE users.portfolio_tweetscount (
id null,
count int,
date datetime NOT NULL
);

INSERT INTO users.portfolio_tweetscount (count, date)
VALUES (1, CURRENT_TIMESTAMP);


drop table if exists users.portfolio_users;

CREATE TABLE users.portfolio_users (
id int NOT NULL PRIMARY KEY,
first_name varchar(255),
last_name varchar(255),
email varchar(255)
);

INSERT INTO users.portfolio_users (id, first_name, last_name, email)
values (1, 'Zach', 'Alexander', 'alexander.d.zachary@gmail.com');
INSERT INTO portfolio_users (id, first_name, last_name, email)
values (2, 'Katie', 'Friedman', 'katherine.a.friedman@gmail.com');
INSERT INTO portfolio_users (id, first_name, last_name, email)
values (3, 'Ruggles', 'Friedman-Alexander', 'ruggles@gmail.com');
INSERT INTO portfolio_users (id, first_name, last_name, email)
values (4, 'John', 'Baimas', 'jbaimas@gmail.com');
INSERT INTO portfolio_users (id, first_name, last_name, email)
values (5, 'Nick', 'Alexander', 'nichalexander6@gmail.com');

COMMIT;