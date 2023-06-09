# Write your MySQL query statement below
SELECT name AS Employee FROM Employee AS t1 
WHERE managerId IS NOT Null 
AND salary > (SELECT salary FROM Employee WHERE id=t1.managerId)