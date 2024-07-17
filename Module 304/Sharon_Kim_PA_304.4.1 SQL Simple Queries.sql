-- Question 1
SELECT 
productName as "Name", 
productLine as "Product Line", 
buyPrice as "Buy Price"
FROM products
ORDER BY buyPrice DESC;

-- Question 2
SELECT
contactFirstName as "First Name",
contactLastName as "Last Name",
city as "City"
FROM customers
WHERE country='Germany'
ORDER BY contactLastName;

-- Question 3
SELECT Distinct(status) 
FROM orders
ORDER BY status;

-- Question 4
SELECT *
FROM payments
WHERE paymentDate >= '2005-1-1'
ORDER BY paymentDate DESC;

-- Question 5
SELECT * FROM employees;
SELECT
lastName,
firstName,
email,
jobTitle,
officeCode
FROM employees
WHERE officeCode="1"
ORDER BY lastName;

-- Question 6
SELECT 
productName,
productLine,
productScale, 
productVendor
FROM products
WHERE productLine="Classic Cars" or
	productLine="Vintage Cars";
CASE
	WHEN productLine="Vintage Cars" THEN 1
    WHEN productLine="Classic Cars" THEN 2
