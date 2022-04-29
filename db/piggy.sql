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
    retailer_id INT REFERENCES retailers(id) ON DELETE SET NULL,
    label_id INT REFERENCES labels(id) ON DELETE SET NULL,
    value INT NOT NULL
);

INSERT INTO retailers (name, active) VALUES ('Amazon', True);
INSERT INTO retailers (name, active) VALUES ('Tesco', True);
INSERT INTO retailers (name, active) VALUES ('Costa', True);
INSERT INTO retailers (name, active) VALUES ('Disney+', True);
INSERT INTO retailers (name, active) VALUES ('Netflix', True);
INSERT INTO retailers (name, active) VALUES ('Deliveroo', True);
INSERT INTO retailers (name, active) VALUES ('The Dragonfly', True);
INSERT INTO retailers (name, active) VALUES ('Landlord', True);

INSERT INTO labels (name, active) VALUES ('Groceries', True);
INSERT INTO labels (name, active) VALUES ('Take Away', True);
INSERT INTO labels (name, active) VALUES ('Petrol', True);
INSERT INTO labels (name, active) VALUES ('Coffee', True);
INSERT INTO labels (name, active) VALUES ('Subscriptions', True);
INSERT INTO labels (name, active) VALUES ('Drinks', True);
INSERT INTO labels (name, active) VALUES ('Misc', True);
INSERT INTO labels (name, active) VALUES ('Rent', True);

INSERT INTO transactions (retailer_id , label_id, value) VALUES (1, 1, 50);
INSERT INTO transactions (retailer_id , label_id, value) VALUES (2, 3, 99);
