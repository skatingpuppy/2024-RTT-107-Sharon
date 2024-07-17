/*Valerie's list of SIMPLE Classic Models Queries.  

ALL Rooms Complete These Questions:
List all the data in the classic models database:
-- What are the tables in the database?
-- What fields are in the OrderDetails Table?
-- How Many Product Lines are there?
-- How Many Product in each product line Lines are there?

Rooms 1,2,3 are assigned the ODD numbered problems below:
Rooms 4,5,6 are assigned the EVEN numbered problems below:
	By the end of our activity, there will be solutions to all the questions in the folder for everyone to look at and share.

1. **Identify the account representative assigned to each customer.**
2. **Summarize the total payments received from Atelier graphique.**
3. **Calculate the cumulative payments received on each date.**
4. **Identify products that have never been sold.**
5. **Detail the payment amounts made by each customer.**
6. **Determine the total number of orders placed by Herkku Gifts.**
7. **Identify the employees located in Boston.**
8. **List payments exceeding $100,000, ordering the results by the highest payment first.**
9. **Calculate the total value of orders currently 'On Hold'.**
10. **Count the number of 'On Hold' orders for each customer.**/

-- 1. What are the tables in the database?
SHOW Tables;

-- 2. What fields are in the OrderDetails Table?
SELECT * FROM orderdetails;

-- 3. How Many Product Lines are there?
SELECT count(productLine) FROM products -- 110

-- 4. How Many Product in each product line Lines are there?
SELECT count(productLine) FROM productlines -- 7


-- 2. **Summarize the total payments received from Atelier graphique.**
SELECT customerNumber, customerName from customers  -- Atelier graphique is customer number 103
SELECT amount FROM payments
WHERE customerNumber = "103";
-- figure out how to add the payments?

-- 4. **Identify products that have never been sold.**
SELECT T1.productCode, T2.productCode
FROM products T1
LEFT JOIN orderdetails T2 ON T1.productCode = T2.productCode
WHERE T2.productCode = NULL;    -- output: zero. therefore, zero products not sold

SELECT count(distinct(productCode)) FROM orderdetails;  -- 2996, distinct 109
SELECT count(distinct(productCode)) FROM products;  -- 110

SELECT status FROM orders     -- # of orders cancelled. Not necessarily the comprehensive # of products not sold, but doesn't seem to be another option.
WHERE status = "Cancelled";

-- 6. **Determine the total number of orders placed by Herkku Gifts.**
SELECT T1.customerName, T1.customerNumber, T2.orderNumber
FROM customers T1
LEFT JOIN orders T2 ON T1.customerNumber = T2.customerNumber
WHERE T1.customerName = "Herkku Gifts";   -- output: 3 orders placed

-- 8. **List payments exceeding $100,000, ordering the results by the highest payment first.**
SELECT amount FROM payments
WHERE amount > 100000  -- don't need in quotes bc it's an integer
ORDER BY amount DESC;

-- 10. **Count the number of 'On Hold' orders for each customer.**
SELECT count(T1.status), T2.customerNumber
FROM orders T1
LEFT JOIN customers T2 ON T1.customerNumber = T2.customerNumber
WHERE T1.status = "On Hold";   -- output: customer 144 had 4 orders on hold