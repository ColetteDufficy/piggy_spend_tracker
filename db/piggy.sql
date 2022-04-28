DROP TABLE IF EXISTS transactions;
DROP TABLE IF EXISTS retailers;
DROP TABLE IF EXISTS labels;



CREATE TABLE retailers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    active BOOLEAN
);

CREATE TABLE labels (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    active BOOLEAN
);

CREATE TABLE transactions (
    id SERIAL PRIMARY KEY,
    retailer_id INT REFERENCES retailers(id),
    label_id INT REFERENCES labels(id),
    value INT
);

