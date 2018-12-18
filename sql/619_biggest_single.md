Table number contains many numbers in column num including duplicated ones.
Can you write a SQL query to find the biggest number, which only appears once.
+---+
|num|
+---+
| 8 |
| 8 |
| 3 |
| 3 |
| 1 |
| 4 |
| 5 |
| 6 | 
For the sample data above, your query should return the following result:
+---+
|num|
+---+
| 6 |
Note:
If there is no such number, just output null.


> Liyou:
- MAX to get the biggest
- use WHERE to filter only the numbers which only appear once

SELECT num
FROM number
GROUP BY num
HAVING COUNT(num) = 1);

**This is wrong because I'm actually returning all the num only appear once**

> revised version:
SELECT MAX(num) AS num
FROM (SELECT num
FROM number
GROUP BY num
HAVING COUNT(num) = 1) AS t

**1. sub query has to have an alias**
**2. GROUP function and WHERE don't work together**
