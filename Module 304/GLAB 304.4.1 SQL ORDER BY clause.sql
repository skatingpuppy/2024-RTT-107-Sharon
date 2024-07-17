-- example 1: Sort a result set by an expression.

SELECT	orderNumber, orderlinenumber, quantityOrdered * priceEach
FROM	orderdetails
ORDER BY	quantityOrdered * priceEach DESC;

SELECT
	orderNumber,
    orderLineNumber,
    quantityOrdered * priceEach AS subtotal
FROM	orderdetails
ORDER BY subtotal DESC;  -- use alias called subtotal. makes more readable



-- example 2: MySQL ORDER BY and NULL Values

SELECT	firstName, lastName, reportsTo
FROM	employees
ORDER BY reportsTo;   -- Nulls appear first in result set

SELECT	firstName, lastName, reportsTo
FROM	employees
ORDER BY reportsTO DESC;   -- Nulls appear last in result set

