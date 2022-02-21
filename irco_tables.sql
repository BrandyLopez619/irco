
---------CUSTOMER----------------
CREATE TABLE customers (
ID SERIAL PRIMARY KEY,
first_name TEXT NOT NULL,
last_name TEXT NOT NULL,
email TEXT NOT NULL,
contact_number TEXT NOT NULL,
credit_card TEXT NOT NULL,
billing_address TEXT NOT NULL,
password TEXT NOT NULL,
);

INSERT INTO customers(first_name, last_name, email, contact_number, credit_card, billing_address, password)
VALUES ('Brandy', 'Lopez', 'brandylopez@mail.com', '6199999999', '1234567890112233', '333 Redwood street San Diego CA 92101','super111'),
('Robert','Smith', 'robby_4_u@yahoo.com', '7603334445', '1425363748985764', '4332 apt.3 Union ave. National City CA 92221','password12'),
('Kim','Richards','kr_2000@gmail.com','6199489893','1526379876857463','665 Lakeshore st. Chula Vista CA 92333','krownrich3');


--- EQUIPMENT------------------

CREATE TABLE equipments (
ID SERIAL PRIMARY KEY,        
year INT NOT NULL,                                 
brand_name TEXT NOT NULL,
model_name TEXT NOT NULL,
serial_number TEXT NOT NULL,
current_location TEXT NOT NULL,
daily_rate INT NOT NULL,
available TEXT NOT NULL
);

INSERT INTO equipments (year,brand_name, model_name, serial_number, current_location, daily_rate, available)
VALUES (2000,'CAT','906M', '00CAT906M56788','San Diego', 800, FALSE),
(2021,'Bobcat','E10', 'BCE10202123044','National City', 400, TRUE),
(2019,'Bobcat','E26', 'BCE26201923456','National City', 500, TRUE),
(2019,'Bobcat','E88', 'BCE88201924665','San Diego', 600, FALSE),
(2019,'Bobcat','E88', 'BCE88201924665','San Diego', 600, FALSE),
(2001,'CAT','906M', '01CAT906M24665','San Diego', 800, TRUE)

---REQUEST-------------------------------

orders_table = db.Table('orders',

                        db.Column('customer_id', db.Integer,
                                  db.ForeignKey('customer.id'),
                                  primary_key=True
                                  ),

                        db.Column('equipment_id', db.Integer,
                                  db.ForeignKey('equipment.id'),
                                  primary_key=True
                                  ),

                        db.Column(
                            'request_location', db.String(50),
                            nullable=False
                        ),

                        db.Column('delivery_date', db.String(10),
                                  nullable=False
                                  ),

                        db.Column('request_time', db.DateTime,
                                  default=datetime.datetime.utcnow,
                                  nullable=False
                                  ),
                        )
CREATE TABLE requests (
ID SERIAL PRIMARY KEY,
customer_id INT NOT NULL REFERENCES customers(ID),
equipment_id INT NOT NULL REFERENCES equipments(ID),
request_location TEXT NOT NULL,
delivery_date TEXT NOT NULL,
request_time TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO requests (customer_id, equipment_id, request_location, delivery_date)
VALUES (1,6,'101 West Main, Miramesa, CA, 91910', '01/29/2022'),
INSERT INTO requests (customer_id, equipment_id, request_location, delivery_date)
VALUES (2,4,'39 Albatross, San Diego, CA, 91910', '02/22/2022')

------DRIVER------------------------

CREATE TABLE drivers (
ID SERIAL PRIMARY KEY,
first_name TEXT NOT NULL,
last_name TEXT NOT NULL,
email TEXT NOT NULL,
drivers_license TEXT NOT NULL,
contact_number CHAR(10) NOT NULL,
credit_card CHAR(16) NOT NULL,
truck_id INT NOT NULL REFERENCES trucks(ID),
available TEXT NOT NULL
);

INSERT INTO drivers (first_name, last_name, email, drivers_license, contact_number, credit_card, truck_id, available)
VALUES ('Steven', 'Wright', 'KeeponTrukin@gmail.com', 'D33K3765', 6172737989, 8392020029828372, 2, TRUE),
('Bill', 'Richards', 'BillRichards@.Billfreight.com', 'KII77789', 7899000773, 2334859699907968, 1, TRUE)

---TRUCK---------------
CREATE TABLE trucks (
ID SERIAL PRIMARY KEY,
year INT NOT NULL,                                 
brand_name TEXT NOT NULL,
model_name TEXT NOT NULL,
vin_number TEXT NOT NULL,
insurance_policy TEXT NOT NULL,
available BOOLEAN
);

INSERT INTO trucks (year, brand_name, model_name, vin_number, insurance_policy, available)
VALUES (2009,'International','A800','JDJ77488S844F', 'AS_3344_2776', TRUE),
(2009,'Kenworth','Sprint','4EE4FKW2009SCC33', '776_GEICO_339930_CA', TRUE)


----RENTAL---------------------
);
CREATE TABLE rentals (
ID SERIAL PRIMARY KEY,
first_name TEXT NOT NULL REFERENCES customers(ID)
truck_id INT NOT NULL REFERENCES trucks(ID),
last_name TEXT NOT NULL REFERENCES customer(ID),
contact_number CHAR(10) NOT NULL REFERENCES customers(ID)
first_name TEXT NOT NULL REFERENCES drivers d,
last_name TEXT NOT NULL REFERENCES drivers d,
contact_number CHAR(10) NOT NULL REFERENCES drivers d,
equipment_id INT NOT NULL REFERENCES equipments(ID),
request_location TEXT NOT NULL,
driver_location TEXT NOT NULL,
delivery_date DATE NOT NULL,
request_time TIMESTAMP NOT NULL
equipment_id INT NOT NULL,
request_location TEXT NOT NULL,
request_time TIMESTAMP NOT NULL,
customer_rating INT,
);
CREATE TABLE drivers (
ID SERIAL PRIMARY KEY,
first_name TEXT NOT NULL,
last_name TEXT NOT NULL,
email TEXT NOT NULL,
contact_number TEXT NOT NULL,
drivers_license TEXT NOT NULL,
credit_card TEXT NOT NULL,
billing_address TEXT NOT NULL,
password TEXT NOT NULL,
available TEXT NOT NULL
);

INSERT INTO drivers (first_name, last_name, email, contact_number, drivers_license, credit_card, billing_address, password, available)
VALUES ('Steven', 'Wright', 'KeeponTrukin@gmail.com','6172737989', 'D33K3765', '8392020029828372','2020 home ave. Chula vista CA 92201', 'truckinon3', TRUE),
('Bill', 'Richards', 'BillRichards@.Billfreight.com', '7899000773', 'KII77789', '2334859699907968','444 Straight st. Hillside Canyon CA 93302' 'gottem123', TRUE)
