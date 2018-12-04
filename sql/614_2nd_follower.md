In facebook, there is a follow table with two columns: followee, follower.

Please write a sql query to get the amount of each follower’s follower if he/she has one.

For example:

+-------------+------------+
| followee    | follower   |
+-------------+------------+
|     A       |     B      |
|     B       |     C      |
|     B       |     D      |
|     D       |     E      |
+-------------+------------+
should output:
+-------------+------------+
| follower    | num        |
+-------------+------------+
|     B       |  2         |
|     D       |  1         |
+-------------+------------+
Explaination:
Both B and D exist in the follower list, when as a followee, B's follower is C and D, and D's follower is E. A does not exist in follower list.
Note:
Followee would not follow himself/herself in all cases.
Please display the result in follower's alphabet order.



> Liyou:
1. group by followee and count how many followers they have
2. conditioned only to people who has at least one follower

- first filter by having at lease one follower
- group by followee
- order by count desc

SELECT followee, COUNT(follower) AS num
FROM follow
WHERE follower in (SELECT DISTINCT followee FROM follow)
GROUP BY followee
ORDER BY 2 DESC;

**understand the questions totally wrong**

> Liyou improved:
1. count the follower's follower by group by follower

1. we can group by followee's follower
2. then we filter out the followee who's in follower list

SELECT followee, COUNT(DISTINCT follower)
FROM follow
GROUP BY followee
HAVING followee in (
    SELECT DISTINCT follower 
    FROM follow
)