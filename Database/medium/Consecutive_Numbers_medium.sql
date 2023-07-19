-- Write an SQL query to find all numbers that appear at least three times consecutively.

-- Return the result table in any order.

-- The query result format is in the following example.

 

-- Example 1:

-- Input: 
-- Logs table:
-- +----+-----+
-- | id | num |
-- +----+-----+
-- | 1  | 1   |
-- | 2  | 1   |
-- | 3  | 1   |
-- | 4  | 2   |
-- | 5  | 1   |
-- | 6  | 2   |
-- | 7  | 2   |
-- +----+-----+
-- Output: 
-- +-----------------+
-- | ConsecutiveNums |
-- +-----------------+
-- | 1               |
-- +-----------------+
-- Explanation: 1 is the only number that appears consecutively for at least three times.
SELECT DISTINCT t1.num1 AS 'ConsecutiveNums' FROM
    (SELECT l1.num AS 'num1',l2.num AS 'num2' ,l3.num AS 'num3' FROM Logs l1  JOIN Logs l2 ON l1.id=l2.id+1 JOIN logs l3
    ON l1.id=l3.id+2)t1
WHERE t1.num1=t1.num2 AND t1.num1=t1.num3