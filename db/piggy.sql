DROP TABLE IF EXISTS transactions;
DROP TABLE IF EXISTS retailers;
DROP TABLE IF EXISTS labels;


CREATE TABLE retailers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    active BOOLEAN NOT NULL
);

CREATE TABLE labels (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    active BOOLEAN NOT NULL
);

CREATE TABLE transactions (
    id SERIAL PRIMARY KEY,
    date DATE,
    retailer_id INT REFERENCES retailers(id) ON DELETE CASCADE,
    label_id INT REFERENCES labels(id) ON DELETE CASCADE,
    value Numeric(19,2) NOT NULL
);

INSERT INTO retailers (name, active) VALUES ('Landlord', True);
INSERT INTO retailers (name, active) VALUES ('Amazon', True);
INSERT INTO retailers (name, active) VALUES ('Tesco', True);
INSERT INTO retailers (name, active) VALUES ('Sainsburys', True);
INSERT INTO retailers (name, active) VALUES ('Costa', True);
INSERT INTO retailers (name, active) VALUES ('Disney+', True);
INSERT INTO retailers (name, active) VALUES ('Netflix', True);
INSERT INTO retailers (name, active) VALUES ('Deliveroo', True);
INSERT INTO retailers (name, active) VALUES ('The Dragonfly', True);

INSERT INTO labels (name, active) VALUES ('Rent', True);
INSERT INTO labels (name, active) VALUES ('Groceries', True);
INSERT INTO labels (name, active) VALUES ('Take Away', True);
INSERT INTO labels (name, active) VALUES ('Petrol', True);
INSERT INTO labels (name, active) VALUES ('Coffee', True);
INSERT INTO labels (name, active) VALUES ('Subscriptions', True);
INSERT INTO labels (name, active) VALUES ('Drinks', True);
INSERT INTO labels (name, active) VALUES ('Misc', True);

INSERT INTO transactions (date, retailer_id , label_id, value) VALUES ('2022-02-13', 1, 1, 690);
INSERT INTO transactions (date, retailer_id , label_id, value) VALUES ('2022-04-27', 3, 2, 42.35);
INSERT INTO transactions (date, retailer_id , label_id, value) VALUES ('2022-04-11', 3, 4, 55.00);
INSERT INTO transactions (date, retailer_id , label_id, value) VALUES ('2022-05-03', 3, 2, 29.13);
INSERT INTO transactions (date, retailer_id , label_id, value) VALUES ('2022-05-01', 4, 2, 57.34);
INSERT INTO transactions (date, retailer_id , label_id, value) VALUES ('2022-05-01', 4, 4, 50.00);
INSERT INTO transactions (date, retailer_id , label_id, value) VALUES ('2022-05-01', 6, 6, 6.99);
INSERT INTO transactions (date, retailer_id , label_id, value) VALUES ('2022-05-01', 7, 6, 7.99);
INSERT INTO transactions (date, retailer_id , label_id, value) VALUES ('2022-05-01', 8, 3, 54.15);
