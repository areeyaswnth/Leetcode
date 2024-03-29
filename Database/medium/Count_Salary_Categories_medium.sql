-- Write an SQL query to report the number of bank accounts of each salary category. The salary categories are:

-- "Low Salary": All the salaries strictly less than $20000.
-- "Average Salary": All the salaries in the inclusive range [$20000, $50000].
-- "High Salary": All the salaries strictly greater than $50000.
-- The result table must contain all three categories. If there are no accounts in a category, then report 0.

-- Return the result table in any order.

-- The query result format is in the following example.

 

-- Example 1:

-- Input: 
-- Accounts table:
-- +------------+--------+
-- | account_id | income |
-- +------------+--------+
-- | 3          | 108939 |
-- | 2          | 12747  |
-- | 8          | 87709  |
-- | 6          | 91796  |
-- +------------+--------+
-- Output: 
-- +----------------+----------------+
-- | category       | accounts_count |
-- +----------------+----------------+
-- | Low Salary     | 1              |
-- | Average Salary | 0              |
-- | High Salary    | 3              |
-- +----------------+----------------+
-- Explanation: 
-- Low Salary: Account 2.
-- Average Salary: No accounts.
-- High Salary: Accounts 3, 6, and 8.
SELECT * FROM (
    SELECT "Low Salary" AS 'category' ,COUNT(*) AS 'accounts_count' FROM Accounts ac WHERE ac.income <20000 
    UNION
    SELECT "Average Salary" AS 'category' ,COUNT(*) AS 'accounts_count' FROM Accounts ac WHERE ac.income BETWEEN 20000 AND 50000
    UNION
    SELECT "High Salary" AS 'category' ,COUNT(*) AS 'accounts_count' FROM Accounts ac WHERE ac.income>50000)t