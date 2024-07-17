SELECT
	customerName, 
    contactLastName,
    contactFirstName,
    state,
    city,
    phone
FROM
	customers;

select * from customers; 

SELECT *
FROM customers
WHERE country='Germany';

select distinct productline
from productlines;

SELECT
contactLastname AS lastName;
contactFirstname As FirstName
FROM customers;

SELECT
	e.firstName,
    e.lastName
FROM
	employees e
ORDER BY e.firstName;


create table Salesfeedback(
	customerFeedback varchar(2048) DEFAULT NULL,
    createdDate datetime NOT NULL DEFAULT current_timestamp,
    customerReference varchar(15) DEFAULT 'OnlineSales',
    username varchar(50) NOT NULL
);


-- 5/6/24 notes
SELECT * FROM customers
WHERE customerName LIKE 'A%';

