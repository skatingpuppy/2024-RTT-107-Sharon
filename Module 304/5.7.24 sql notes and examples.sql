SELECT concat(contactFirstName,  , contactLastName), UPPER(concat(contactFirstName,'  ', contactLastName)) AS Fullname  -- Fullname doesn't change the actual database
FROM customers;

SELECT buyprice
FROM products
WHERE productline = "Classic Cars";
# result



-- how many customers are in each city?
SELECT COUNT(city), city, state, country FROM customers -- count aggregate. if only list city, will only show city. this shows city, staten and country columns for count
GROUP BY city, country, state    -- need to add whatever you're ordering by into the group by
ORDER BY country, state;



SELECT * FROM Customers
WHERE country IN ("USA", "France");  -- iterate through those as conditions.

-- same as:
SELECT * FROM Customers
WHERE country = "USA" OR country = "France";


SELECT distinct(city) FROM STATION
WHERE right(city, 1) in ("a", "e", "i", "o", "u"); -- this gives the last character of the city! that matches w/ vowels

SELECT distinct(city) FROM STATION
WHERE left(city, 1) IN ("a", "e", "i", "o", "u")
AND right(city, 1) IN ("a", "e", "i", "o", "u");    -- this would be for both first and last character of city being a vowel  

SELECT distinct(city) FROM STATION
WHERE left(city, 1) NOT IN ("a", "e", "i", "o", "u");  -- when first character is NOT a vowel

SELECT DISTINCT CITY FROM STATION
WHERE CITY REGEXP '^[aeiouAEIOU].*[aeiouAEIOU]$';




SELECT customers.customerNumber, customerName, orders.orderNumber, orderDate, products.productCode, productName, buyPrice
FROM customers inner join orders on customers.customerNumber = orders.customerNumber
join orderdetails on orders.orderNumber = orderdetails.orderNumber
join products on orderdetails.productCode = products.productCode;

SELECT customers.customerNumber, 
customers.customerName, 
orders.orderNumber, 
orders.orderDate, 
products.productCode, 
products.productName, 
products.buyPrice
FROM customers INNER JOIN orders USING(customerNumber)
INNER JOIN orderdetails USING(orderNumber)
INNER JOIN products USING(productCode);
