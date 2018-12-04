In social network like Facebook or Twitter, people send friend requests and accept others' requests as well.
Table request_accepted holds the data of friend acceptance, while requester_id and accepter_id both are the id of a person.
| requester_id | accepter_id | accept_date|
|--------------|-------------|------------|
| 1            | 2           | 2016_06-03 |
| 1            | 3           | 2016-06-08 |
| 2            | 3           | 2016-06-08 |
| 3            | 4           | 2016-06-09 |
Write a query to find the the people who has most friends and the most friends number. For the sample data above, the result is:
| id | num |
|----|-----|
| 3  | 3   |
Note:
It is guaranteed there is only 1 people having the most friends.
The friend request could only been accepted once, which mean there is no multiple records with the same requester_id and accepter_id value.
Explanation:
The person with id '3' is a friend of people '1', '2' and '4', so he has 3 friends in total, which is the most number than any others.
Follow-up:
In the real world, multiple people could have the same most number of friends, can you find all these people in this case?

> Liyou:
0. outer join tables based on id, so accepter_id and requester_id can be in the same column
1. count friends number per id
2. group by distinct
3. select max count



SELECT *
FROM request_accepted a OUTER JOIN request_accepted b ON a.requester_id = b.accepter_id
GROUP BY 


**DOESN'T WORKS BECAUSE -- instead of OUTER JOIN I should use union. and to use UNION, I have to rename it the same column name. And the group by will happen before union.**

> solution 1:

SELECT id, sum(num) AS num
FROM
(SELECT requester_id AS id, count(accepter_id) AS num
FROM request_accepted 
GROUP BY requester_id

UNION ALL

SELECT accepter_id AS id, count(requester_id) AS num
FROM request_accepted
GROUP BY accepter_id) AS all
GROUP BY id
ORDER BY 2 DESC
LIMIT 1