-- Write an SQL query to find the prices of all products on 2019-08-16. Assume the price of all products before any change is 10.

-- Return the result table in any order.

-- The query result format is in the following example.

 

-- Example 1:

-- Input: 
-- Products table:
-- +------------+-----------+-------------+
-- | product_id | new_price | change_date |
-- +------------+-----------+-------------+
-- | 1          | 20        | 2019-08-14  |
-- | 2          | 50        | 2019-08-14  |
-- | 1          | 30        | 2019-08-15  |
-- | 1          | 35        | 2019-08-16  |
-- | 2          | 65        | 2019-08-17  |
-- | 3          | 20        | 2019-08-18  |
-- +------------+-----------+-------------+
-- Output: 
-- +------------+-------+
-- | product_id | price |
-- +------------+-------+
-- | 2          | 50    |
-- | 1          | 35    |
-- | 3          | 10    |
-- +------------+-------+
SELECT p.product_id,CASE WHEN t.price IS NULL THEN 10 ELSE t.price END AS 'price' FROM (SELECT p.product_id,p.new_price AS 'price' FROM
(SELECT t.product_id,MAX(t.change_date) AS 'change_date'
    FROM (SELECT * FROM Products
            WHERE change_date <= '2019-08-16' )t
    GROUP BY t.product_id)t
    JOIN (SELECT * FROM Products )p
        ON t.change_date=p.change_date AND p.product_id=t.product_id)t 
        RIGHT JOIN 
        (SELECT * FROM Products GROUP BY product_id )p ON t.product_id=p.product_id
