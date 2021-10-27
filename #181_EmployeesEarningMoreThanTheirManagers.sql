# Write your MySQL query statement below
SELECT F1.Name as Employee FROM Employee as F1, Employee as F2
    WHERE F1.managerId = F2.id and F1.salary > F2.salary

