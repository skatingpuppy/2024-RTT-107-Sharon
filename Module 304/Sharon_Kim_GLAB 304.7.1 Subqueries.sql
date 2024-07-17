SELECT  * FROM  departments WHERE  location_id = 1700;  -- find all departments located at the location_id is 1700

SELECT  employee_id, first_name, last_name, department_id    -- find employees that belong to the location 1700
FROM   employees
WHERE  department_id IN (1, 3, 9, 10, 11)
ORDER BY first_name, last_name;

-- Subquery with Where clause
SELECT   employee_id, first_name, last_name, department_id
FROM employees
WHERE department_id IN (SELECT department_id
        FROM      departments
        WHERE location_id = 1700)
ORDER BY first_name, last_name;

-- Subquery with NOT IN operator 
SELECT employee_id, first_name, last_name   -- find all employees' information who do not locate at location 1700
FROM  employees
WHERE  department_id NOT IN (SELECT department_id
        FROM   departments
        WHERE location_id = 1700)
ORDER BY first_name , last_name;

-- Comparison Operator (=, >, =, <= , !=)
SELECT employee_id, first_name, last_name, salary
FROM   employees
WHERE salary = (SELECT MAX(salary) FROM  employees)
ORDER BY first_name, last_name;

SELECT employee_id, first_name, last_name, salary   -- employees whose salary is higher than the average salary throughout the company
FROM employees
WHERE salary > (SELECT AVG(salary)FROM employees);

-- EXISTS / NOT EXISTS Operator
SELECT department_name   -- all departments have at least one employee with a salary greater than 10,000
FROM departments d
WHERE EXISTS ( SELECT * FROM employees e 
	WHERE salary > 10000 AND e.department_id = d.department_id)
ORDER BY department_name;

SELECT department_name    -- all departments that do not have an employee with a salary greater than 10,000
FROM departments d
WHERE NOT EXISTS ( SELECT * FROM employees e
        WHERE salary > 10000 AND e.department_id = d.department_id) ORDER BY department_name;

-- SQL Subquery in FROM clause
SELECT AVG(salary) average_salary -- average salary of every department
FROM employees GROUP BY department_id;

SELECT ROUND( AVG(average_salary), 0) -- the above using a subquery
FROM  ( SELECT AVG(salary) as average_salary FROM employees   GROUP BY department_id) department_salary;

-- example 2 in classicmodels
SELECT productCode, ROUND(SUM(quantityOrdered * priceEach)) AS sales  -- the top five products by sales revenue in 2003 from the orders and orderdetails tables
FROM orderdetails
	INNER JOIN orders USING (orderNumber)
WHERE YEAR(shippedDate) = 2003
GROUP BY productCode
ORDER BY sales DESC
LIMIT 5;