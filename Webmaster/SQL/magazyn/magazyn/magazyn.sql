DROP TABLE IF EXISTS tbOrders;
CREATE TABLE tbOrders
(
    id INTEGER PRIMARY KEY,
    customers_id INTEGER,
    subscription_id INTEGER,
    purchase_date DATE,
    FOREIGN KEY (customers_id) REFERENCES tbCustomers(id),
    FOREIGN KEY (subscription_id) REFERENCES tbSubscription(id)
);

DROP TABLE IF EXISTS tbCustomers;
CREATE TABLE tbCustomers
(
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    adress TEXT NOT NULL
);

DROP TABLE IF EXISTS tbSubscriptions;
CREATE TABLE tbSubscriptions
(
    id INTEGER PRIMARY KEY,
    description TEXT NOT NULL,
    price_per_month INTEGER,
    subscription_length
);
