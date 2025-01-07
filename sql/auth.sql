CREATE TABLE users (
    id             serial PRIMARY KEY,
    username       varchar(16) UNIQUE NOT NULL,
    ugroup         varchar(16),
    weight         smallint,
    registered     timestamp,
    last_visit     timestamp,
    password_hash  varchar(128),
    description    varchar(500) DEFAULT NULL,
    last_published timestamp DEFAULT NULL
);

CREATE TABLE accounts (
    id        serial PRIMARY KEY,
    address   varchar(128) UNIQUE,
    swap      varchar(128),
    requested timestamp,
    user_id   integer REFERENCES users(id) UNIQUE
);
