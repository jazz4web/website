CREATE TABLE users(
    id serial PRIMARY KEY,
    username varchar(16) UNIQUE NOT NULL,
    message  varchar(512) DEFAULT NULL
);
