-- Example 1:

-- Input: 
-- Triangle table:
-- +----+----+----+
-- | x  | y  | z  |
-- +----+----+----+
-- | 13 | 15 | 30 |
-- | 10 | 20 | 15 |
-- +----+----+----+
-- Output: 
-- +----+----+----+----------+
-- | x  | y  | z  | triangle |
-- +----+----+----+----------+
-- | 13 | 15 | 30 | No       |
-- | 10 | 20 | 15 | Yes      |
-- +----+----+----+----------+
SELECT * , CASE WHEN x+y>z AND y+z>x AND z+x>y AND x*y*z>0 THEN 'Yes'
                ELSE 'No' 
                END AS 'triangle'
FROM Triangle