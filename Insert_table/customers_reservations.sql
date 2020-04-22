BEGIN TRANSACTION;
DROP TABLE IF EXISTS reservations;
DROP TABLE IF EXISTS customers;

CREATE TABLE IF NOT EXISTS customers(id INTEGER PRIMARY KEY, name TEXT);
INSERT INTO customers(Name) VALUES('Paul Novak');
INSERT INTO customers(Name) VALUES('Terry Neils');
INSERT INTO customers(Name) VALUES('Jack Fonda');
INSERT INTO customers(Name) VALUES('Tom Willis');

CREATE TABLE IF NOT EXISTS reservations(id INTEGER PRIMARY KEY, 
    customer_id INTEGER, created DATE, 
    FOREIGN KEY(customer_id) REFERENCES customers(id));
INSERT INTO reservations(customer_id, created) VALUES(1, '2018-22-11');
INSERT INTO reservations(customer_id, created) VALUES(2, '2018-28-11');
INSERT INTO reservations(customer_id, created) VALUES(2, '2018-29-11');
INSERT INTO reservations(customer_id, created) VALUES(1, '2018-29-11');
INSERT INTO reservations(customer_id, created) VALUES(3, '2018-02-12');
COMMIT;