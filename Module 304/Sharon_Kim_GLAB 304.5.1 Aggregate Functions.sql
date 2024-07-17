-- MOD Function
SELECT orderNumber, SUM(quantityOrdered) as Qty,
    IF(MOD(SUM(quantityOrdered),2),'Odd', 'Even') as oddOrEven
FROM    orderdetails
GROUP BY    orderNumber
ORDER BY    orderNumber;

-- TRUNCATE Function
SELECT TRUNCATE(1.555,1);

-- ROUND Function
SELECT productCode, AVG(quantityOrdered * priceEach) as avg_order_value
FROM orderDetails
GROUP BY productCode;

SELECT     productCode,   -- can round to zero decimal places
  ROUND(AVG(quantityOrdered * priceEach)) as avg_order_item_value
FROM     orderDetails
GROUP BY    productCode;
 
-- truncate vs round
SELECT   TRUNCATE(1.999,1),  ROUND(1.999,1);  -- truncate trims the decimal places, round performs rounding

-- REPLACE Function
UPDATE products 
SET productDescription = REPLACE(productDescription,'abuot','about'); -- takes all spelling mistakes abuot and fixes to about

-- DATEDIFF Function
SELECT DATEDIFF('2011-08-17','2011-08-17');  
#Result  :   0 day

SELECT DATEDIFF('2011-08-17','2011-08-08'); 
#Result:  9 days

SELECT DATEDIFF('2011-08-08','2011-08-17');  
#Result:  -9 days

SELECT orderNumber, DATEDIFF(requiredDate, shippedDate) as  daysLeft -- calculate the number of days between the required date and shipped date of the orders
FROM     orders
ORDER BY  daysLeft DESC;

SELECT orderNumber, DATEDIFF(requiredDate, orderDate) as remaining_days -- gets all orders whose status is “In Process,” and calculates the number of days between the ordered date and the required date:
FROM    orders
WHERE    status = 'In Process'
ORDER BY remaining_days;

SELECT        -- For calculating an interval in week or month, you can divide the returned value of the DATEDIFF() function by 7 or 30
    orderNumber,
    ROUND(DATEDIFF(requiredDate, orderDate) / 7, 2),
    ROUND(DATEDIFF(requiredDate, orderDate) / 30,2)
FROM     orders 
WHERE    status = 'In Process';

-- DATE_FORMAT Function
SELECT  -- select the order’s data and format the date value
    orderNumber,
    DATE_FORMAT(orderdate, '%Y-%m-%d') orderDate,
    DATE_FORMAT(requireddate, '%a %D %b %Y') requireddate,
    DATE_FORMAT(shippedDate, '%W %D %M %Y') shippedDate
FROM    orders;

SELECT     orderNumber,
    DATE_FORMAT(shippeddate, '%W %D %M %Y')  as 'Shipped date'
FROM    orders
ORDER BY shippeddate;

-- LPAD (str, len, padstr)  -- left-pads a string with another string to a certain length
SELECT LPAD('hi',4,'??');

SELECT LPAD('hi',1,'??');

SELECT firstName, LPAD(firstName,10,'kk'), LPAD(firstName,5,'kk'), LPAD(firstName,4,'kk') FROM classicmodels.employees;

-- SQL TRIM Function
SELECT TRIM(' SQL TRIM Function ');

SELECT LTRIM('  SQL LTRIM function');

SELECT RTRIM('SQL RTRIM function   ');

-- YEAR Function
SELECT YEAR('2002-01-01');

SELECT YEAR(shippeddate) as year,  COUNT(ordernumber) as orderQty
FROM    orders 
GROUP BY YEAR(shippeddate)
ORDER BY YEAR(shippeddate);

-- DAY Function
SELECT DAY('2022-01-15');

SELECT  DAY(orderdate) as dayofmonth, COUNT(*)   -- return the number of orders by day number in 2004
FROM    orders WHERE    YEAR(orderdate) = 2004
GROUP BY dayofmonth
ORDER BY dayofmonth;
