# Write your MySQL query statement below
SELECT today.id
FROM Weather today
JOIN Weather yesterday
On DATEDIFF(today.recordDate, yesterday.recordDate) = 1
WHERE today.temperature > yesterday.temperature
