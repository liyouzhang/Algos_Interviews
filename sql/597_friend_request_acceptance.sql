'''
In social network like Facebook or Twitter, people send friend requests and accept others’ requests as well. Now given two tables as below:
Table: friend_request
| sender_id | send_to_id |request_date|
|-----------|------------|------------|
| 1         | 2          | 2016_06-01 |
| 1         | 3          | 2016_06-01 |
| 1         | 4          | 2016_06-01 |
| 2         | 3          | 2016_06-02 |
| 3         | 4          | 2016-06-09 |
Table: request_accepted
| requester_id | accepter_id |accept_date |
|--------------|-------------|------------|
| 1            | 2           | 2016_06-03 |
| 1            | 3           | 2016-06-08 |
| 2            | 3           | 2016-06-08 |
| 3            | 4           | 2016-06-09 |
| 3            | 4           | 2016-06-10 |
Write a query to find the overall acceptance rate of requests rounded to 2 decimals, which is the number of acceptance divide the number of requests.
For the sample data above, your query should return the following result.
|accept_rate|
|-----------|
|       0.80|
Note:
The accepted requests are not necessarily from the table friend_request. 
In this case, you just need to simply count the total accepted requests (no matter whether they are in the original requests), and divide it by the number of requests to get the acceptance rate.
It is possible that a sender sends multiple requests to the same receiver, and a request could be accepted more than once. In this case, the ‘duplicated’ requests or acceptances are only counted once.
If there is no requests at all, you should return 0.00 as the accept_rate.
Explanation: There are 4 unique accepted requests, and there are 5 requests in total. So the rate is 0.80.
Follow-up:
Can you write a query to return the accept rate but for every month?
How about the cumulative accept rate for every day?
'''

-- 2020.04.16
-- output: a column with 1 row for average AR (2 decimals)
-- AR is defined as num_total_accepted/num_total_requests, return 0.00 if null 

-- thought 1
-- first, remove duplicates in each table and join tables
-- with a table has request_receiver as the key, we will have if_accepted as a column
-- lastly, count table rows as the demoninator, count if is_accepted is not null as the numerator

-- thought 2
with distinct_requests as (
    select 
        sender_id
        , send_to_id
        , count (*) as num_requested_per_pair
    from friend_request fr 
    group by sender_id, send_to_id
), 
distinct_accepts as (
    select 
        requester_id
        , accepter_id
        , count (*) as num_accepted_per_pair  
    from request_accepted ra 
    group by 1,2 
),
requests as (
    select 
        '1' as keys  
        , count(*) as num_requests 
    from distinct_requests
),
accpetance as (
    select
        '1' as keys  
        , count(*) as num_accepts 
    from distinct_accepts 
)
select 
    ifnull (num_accepts * 1.00 / num_requests, 0.00) as acceptance_rate 
from requests r 
join accpetance a 
    on r.keys = a.keys 




-- format for leetcode
select 
    ifnull (num_accepts * 1.00 / num_requests, 0.00) as acceptance_rate 
from (
    select 
        '1' as keys  
        , count(*) as num_requests 
    from (
    select 
        sender_id
        , send_to_id
        , count (*) as num_requested_per_pair
    from friend_request fr 
    group by sender_id, send_to_id
    ) dr 
) r 
join (
    select
        '1' as keys  
        , count(*) as num_accepts 
    from (
    select 
        requester_id
        , accepter_id
        , count (*) as num_accepted_per_pair  
    from request_accepted ra 
    group by 1,2 
    )da  
) a 
    on r.keys = a.keys 




-- solution 
with 