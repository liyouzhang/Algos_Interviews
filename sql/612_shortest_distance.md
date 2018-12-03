Table point_2d holds the coordinates (x,y) of some unique points (more than two) in a plane.
Write a query to find the shortest distance between these points rounded to 2 decimals.
| x  | y  |
|----|----|
| -1 | -1 |
| 0  | 0  |
| -1 | -2 |
The shortest distance is 1.00 from point (-1,-1) to (-1,2). So the output should be:
| shortest |
|----------|
| 1.00     |
Note: The longest distance among all the points are less than 10000.

> Liyou:
1. calculate distance among every point. 
sqrt((y2-y1)^2 + (x2-x1)^2)
LAG()
2. select the min

**LIYOU: don't know how to have combination of all points????**


> solution 1:
SELF JOIN! as long as x != x or y != y

SELECT MIN(ROUND(SQRT(POWER(L.x - R.x,2) + POWER(L.y - R.y, 2)))) AS shortest
FROM point_2d L JOIN point_2d R ON L.x != R.x OR L.y != R.y
