CREATE TABLE door_record (
    id INT(11) AUTO_INCREMENT,
    date_at datetime DEFAULT CURRENT_TIMESTAMP,
    is_open boolean NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE door_record (
    id INT(11) AUTO_INCREMENT,
    date_at datetime DEFAULT CURRENT_TIMESTAMP,
    humi FLOAT NOT NULL,
    temp FLOAT NOT NULL,
    PRIMARY KEY (id)
);

