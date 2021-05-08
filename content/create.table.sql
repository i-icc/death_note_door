CREATE TABLE door_record (
    id INT(11) AUTO_INCREMENT,
    date_at datetime DEFAULT CURRENT_TIMESTAMP,
    is_open NOT NULL,
    PRIMARY KEY (id)
);