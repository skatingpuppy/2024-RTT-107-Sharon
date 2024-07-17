-- #1
SELECT p.`NAME` AS "Product", pt.`NAME` AS "Type"
FROM product p INNER JOIN product_type pt
ON p.product_type_cd = pt.product_type_cd;

-- #2
SELECT b.`name`, b.city, e.LAST_NAME, e.TITLE
FROM employee e INNER JOIN branch b
ON b.BRANCH_ID = e.ASSIGNED_BRANCH_ID;

-- #3
SELECT distinct TITLE FROM employee;

-- #4
SELECT e.LAST_NAME AS "Name", e.TITLE AS "Title", m.LAST_NAME AS "Boss Name", m.TITLE AS "Boss Title"
FROM employee e LEFT JOIN employee m
ON e.SUPERIOR_EMP_ID = m.EMP_ID;

-- #5
SELECT p.NAME, a.AVAIL_BALANCE, i.LAST_NAME FROM account a
INNER JOIN product p ON a.PRODUCT_CD = p.PRODUCT_CD
LEFT JOIN customer c ON a.CUST_ID = c.CUST_ID
LEFT JOIN individual i ON c.CUST_ID = i.CUST_ID;

-- #6
SELECT ac.*, i.LAST_NAME FROM acc_transaction ac
INNER JOIN account a ON ac.ACCOUNT_ID = a.ACCOUNT_ID
INNER JOIN customer c ON a.CUST_ID = c.CUST_ID
INNER JOIN individual i ON c.CUST_ID = i.CUST_ID
WHERE i.LAST_NAME RLIKE "T.*"; -- same as LIKE "T%"

