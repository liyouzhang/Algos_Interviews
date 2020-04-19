'''
table: Activity

+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| player_id    | int     |
| device_id    | int     |
| event_date   | date    |
| games_played | int     |
+--------------+---------+
(player_id, event_date) is the primary key of this table.
This table shows the activity of players of some game.
Each row is a record of a player who logged in and played a number of games (possibly 0) before logging out on some day using some device.

 

Write an SQL query that reports the first login date for each player.

The query result format is in the following example:

Activity table:
+-----------+-----------+------------+--------------+
| player_id | device_id | event_date | games_played |
+-----------+-----------+------------+--------------+
| 1         | 2         | 2016-03-01 | 5            |
| 1         | 2         | 2016-05-02 | 6            |
| 2         | 3         | 2017-06-25 | 1            |
| 3         | 1         | 2016-03-02 | 0            |
| 3         | 4         | 2018-07-03 | 5            |
+-----------+-----------+------------+--------------+

Result table:
+-----------+-------------+
| player_id | first_login |
+-----------+-------------+
| 1         | 2016-03-01  |
| 2         | 2017-06-25  |
| 3         | 2016-03-02  |
+-----------+-------------+
'''


-- output is two columns: player_id and the first_login_date
--  will use group by player_id and find the min of the date 

select 
    player_id
    , min (event_date) as first_login
from activity a 
group by
    player_id

'''
Write a SQL query that reports the device that is first logged in for each player.
Result table:
+-----------+-----------+
| player_id | device_id |
+-----------+-----------+
| 1         | 2         |
| 2         | 3         |
| 3         | 1         |
+-----------+-----------+
'''

-- group by player_id 
-- first find out the first_login date and use it  as the key to join the a table to find out the device 

select 
    distinct fl.player_id
    , a.device_id
from (
    select 
        player_id
        , min (event_date) as first_login
    from activity a 
    group by
        player_id
) fl 
join activity a 
    on fl.player_id = a.player_id
    and fl.first_login = a.event_date

'''
550
Write an SQL query that reports the fraction of players that logged in again on the day after the day they first logged in, rounded to 2 decimal places. In other words, you need to count the number of players that logged in for at least two consecutive days starting from their first login date, then divide that number by the total number of players.

The query result format is in the following example:

Activity table:
+-----------+-----------+------------+--------------+
| player_id | device_id | event_date | games_played |
+-----------+-----------+------------+--------------+
| 1         | 2         | 2016-03-01 | 5            |
| 1         | 2         | 2016-03-02 | 6            |
| 2         | 3         | 2017-06-25 | 1            |
| 3         | 1         | 2016-03-02 | 0            |
| 3         | 4         | 2018-07-03 | 5            |
+-----------+-----------+------------+--------------+

Result table:
+-----------+
| fraction  |
+-----------+
| 0.33      |
+-----------+
Only the player with id 1 logged back in after the first day he had logged in so the answer is 1/3 = 0.33
'''

-- select operation with divide and round to two decimiles

-- first sub query the numerator, which is num of users who log in next day after first day 
-- self join table on player_id and date = date_add + 1 
-- first have player_date level data 

-- sub query for denomiator is num of users who log in 

-- NOT SURE IF BELOW IS RIGHT
with player_date as (
    select 
        player_id
        , event_date
        , count (*) as login_per_day
    from activity a 
    group by player_id, event_date 
),

numerator as (
    select 
        count (distinct player_id) as consecutive_users 
    from player_date pd1 
    join player_date pd2 
        on pd1.player_id = pd.player_id
        and pd1.event_date = date_add('day',1,event_date)
),

denomiator as (
    select 
        count (distinct player_id) as users_loggedin
    from player_date
)

select 
    round(consecutive_users * 1.00 / users_loggedin, 2) as fraction
from numerator
cross join denomiator


