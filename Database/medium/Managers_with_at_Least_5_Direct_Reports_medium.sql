-- Write an SQL query to report the managers with at least five direct reports.

-- Return the result table in any order.

-- The query result format is in the following example.

 

-- Example 1:

-- Input: 
-- Employee table:
-- +-----+-------+------------+-----------+
-- | id  | name  | department | managerId |
-- +-----+-------+------------+-----------+
-- | 101 | John  | A          | None      |
-- | 102 | Dan   | A          | 101       |
-- | 103 | James | A          | 101       |
-- | 104 | Amy   | A          | 101       |
-- | 105 | Anne  | A          | 101       |
-- | 106 | Ron   | B          | 101       |
-- +-----+-------+------------+-----------+
-- Output: 
-- +------+
-- | name |
-- +------+
-- | John |
-- +------+
SELECT em2.name FROM Employee em1 RIGHT JOIN (SELECT DISTINCT id,name FROM Employee)em2 ON em1.managerId=em2.id 
GROUP BY em2.id
HAVING COUNT(*)>=5