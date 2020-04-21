'''
Table: Actions

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| user_id       | int     |
| post_id       | int     |
| action_date   | date    | 
| action        | enum    |
| extra         | varchar |
+---------------+---------+
There is no primary key for this table, it may have duplicate rows.
The action column is an ENUM type of ('view', 'like', 'reaction', 'comment', 'report', 'share').
The extra column has optional information about the action such as a reason for report or a type of reaction. 

 

Write an SQL query that reports the number of posts reported yesterday for each report reason. Assume today is 2019-07-05.

The query result format is in the following example:

Actions table:
+---------+---------+-------------+--------+--------+
| user_id | post_id | action_date | action | extra  |
+---------+---------+-------------+--------+--------+
| 1       | 1       | 2019-07-01  | view   | null   |
| 1       | 1       | 2019-07-01  | like   | null   |
| 1       | 1       | 2019-07-01  | share  | null   |
| 2       | 4       | 2019-07-04  | view   | null   |
| 2       | 4       | 2019-07-04  | report | spam   |
| 3       | 4       | 2019-07-04  | view   | null   |
| 3       | 4       | 2019-07-04  | report | spam   |
| 4       | 3       | 2019-07-02  | view   | null   |
| 4       | 3       | 2019-07-02  | report | spam   |
| 5       | 2       | 2019-07-04  | view   | null   |
| 5       | 2       | 2019-07-04  | report | racism |
| 5       | 5       | 2019-07-04  | view   | null   |
| 5       | 5       | 2019-07-04  | report | racism |
+---------+---------+-------------+--------+--------+

Result table:
+---------------+--------------+
| report_reason | report_count |
+---------------+--------------+
| spam          | 1            |
| racism        | 2            |
+---------------+--------------+ 
Note that we only care about report reasons with non zero number of reports.
'''
-- filter posts reported yesterday
-- aggregate by the reason
select 
    extra as report_reason
    , count(distinct post_id) as report_count
from Actions a 
where 1=1 
    and action = 'report'
    and action_date = '2019-07-04'
group by 1

'''
Table: Removals

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| post_id       | int     |
| remove_date   | date    | 
+---------------+---------+
post_id is the primary key of this table.
Each row in this table indicates that some post was removed as a result of being reported or as a result of an admin review.

 

Write an SQL query to find the average for daily percentage of posts that got removed after being reported as spam, rounded to 2 decimal places.

Result table:
+-----------------------+
| average_daily_percent |
+-----------------------+
| 75.00                 |
+-----------------------+
The percentage for 2019-07-04 is 50% because only one post of two spam reported posts was removed.
The percentage for 2019-07-02 is 100% because one post was reported as spam and it was removed.
The other days had no spam reports so the average is (50 + 100) / 2 = 75%
Note that the output is only one number and that we do not care about the remove dates.
'''

-- num of reports removed per day and num of reports per day
-- daily pct of removal
-- aggregate by average 


-- I couldn't verify my solution due to syntax
with removed_reports as (
    select 
        remove_date
        , count (distinct post_id) as removed_reports_daily
    from Removals r 
    join Actions a 
        on r.post_id = a.post_id
        and a.action = 'report'
        -- missed another criteria "SPAM"!!
        and a.extra = 'spam'
    group by 1
),

reports as (
    select
        action_date
        , count (distinct post_id) as reports_daily
    from Actions a 
    where 1=1
        and action = 'report'
        and extra = 'spam'
    group by 1
),

daily_removal_pct as (
    select 
        re.action_date
        , ROUND (removed_reports_daily * 1.00 / reports_daily,2) as daily_pct 
    from reports re 
    join removed_reports rr 
    -- use inner join here buz if there is a day there is no report then we don't need to count
        on re.action_date = rr.remove_date
)

select
    round(avg(daily_pct),2) as average_daily_percent
    -- I missed the requirement that i need to *100
from daily_removal_pct 

-- solutions
With tb1 As
(
Select action_date,cast(count(distinct a.post_id) as float) as r
From 
    actions a inner join removals r on a.post_id = r.post_id
where extra = 'spam'
group by action_date
),
tb2 As
(
select action_date,count(distinct post_id) as ts
from actions
where extra = 'spam'
group by action_date
),
tb3 As
(
    Select tb2.action_date,isnull((r/ts)*100,0) as p
    From tb2 left join tb1 on tb2.action_date = tb1.action_date)

Select round(avg(p),2) as average_daily_percent
From tb3