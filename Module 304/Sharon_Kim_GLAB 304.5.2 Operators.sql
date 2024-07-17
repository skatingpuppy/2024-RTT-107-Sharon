-- "OR" Operator Example
SELECT    customername, country
FROM    customers
WHERE    country = 'USA' OR country = 'France';

-- "AND" Operator Example
SELECT    customername, country, creditLimit       -- return the customer's records who are located in the USA or France and have credit limits greater than 100,000
FROM    customers
WHERE (country = 'USA' OR country = 'France') AND creditlimit > 100000;

SELECT  customername, country, creditLimit FROM    customers   -- customers who are located in the USA or the customers who are located in France with a credit limit greater than 10000
WHERE    country = 'USA' OR country = 'France' AND creditlimit > 100000;

-- "BETWEEN" and "NOT BETWEEN"
SELECT     productCode,  productName,  buyPrice     -- find products whose buy prices are within the ranges of 90 and 100
FROM    products
WHERE     buyPrice BETWEEN 90 AND 100;

SELECT productCode, productName, buyPrice    -- same thing
FROM products
WHERE  buyPrice >= 90 AND buyPrice <= 100;

SELECT productCode, productName, buyPrice FROM products   -- find the product whose buy price is not between $20 and $100
WHERE buyPrice NOT BETWEEN 20 AND 100;

SELECT productCode, productName, buyPrice FROM products  -- same thing
WHERE  buyPrice < 20     OR     buyPrice > 100; 

-- "IS NULL" Operator Example
SELECT customerName, country, salesrepemployeenumber   -- find customers who do not have a sales representative
FROM customers
WHERE salesrepemployeenumber IS NULL
ORDER BY  customerName; 

SELECT customerName, country, salesrepemployeenumber   -- get the customers who have a sales representative
FROM  customers
WHERE  salesrepemployeenumber IS NOT NULL
ORDER BY customerName;

SELECT  c.customerNumber, c.customerName,  orderNumber, o.STATUS    -- find customers who have no order
FROM customers c
LEFT JOIN orders o 
ON c.customerNumber = o.customerNumber
WHERE  orderNumber IS NULL;

