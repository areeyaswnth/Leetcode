-- Write an SQL query to report the IDs of all the employees with missing information. The information of an employee is missing if:

-- The employee's name is missing, or
-- The employee's salary is missing.
-- Return the result table ordered by employee_id in ascending order.

-- The query result format is in the following example.

 

-- Example 1:

-- Input: 
-- Employees table:
-- +-------------+----------+
-- | employee_id | name     |
-- +-------------+----------+
-- | 2           | Crew     |
-- | 4           | Haven    |
-- | 5           | Kristian |
-- +-------------+----------+
-- Salaries table:
-- +-------------+--------+
-- | employee_id | salary |
-- +-------------+--------+
-- | 5           | 76071  |
-- | 1           | 22517  |
-- | 4           | 63539  |
-- +-------------+--------+
-- Output: 
-- +-------------+
-- | employee_id |
-- +-------------+
-- | 1           |
-- | 2           |
-- +-------------+
-- Explanation: 
-- Employees 1, 2, 4, and 5 are working at this company.
-- The name of employee 1 is missing.
-- The salary of employee 2 is missing.
SELECT t.employee_id
FROM (
    SELECT s1.employee_id,em.name,s1.salary
    FROM Employees em
    RIGHT JOIN Salaries s1 ON em.employee_id = s1.employee_id

    UNION

    SELECT em.employee_id,em.name,s1.salary
    FROM Employees em
    LEFT JOIN Salaries s1 ON em.employee_id = s1.employee_id
) AS t
WHERE t.salary IS NULL OR t.name IS NULL
ORDER BY t.employee_id ASC