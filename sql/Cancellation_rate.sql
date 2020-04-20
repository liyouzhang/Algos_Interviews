'''
Write a SQL query to find the cancellation rate of requests made by unbanned users (both client and
driver must be unbanned) between Oct 1, 2013 and Oct 3, 2013. The cancellation rate is computed
by dividing the number of canceled (by client or driver) requests made by unbanned users by the
total number of requests made by unbanned users.
'''

-- filter only unbanned users
-- calculate the cancelled trips 
-- total trips requests 
-- lastly, aggregate by date 
-- round it to 2 decimles 



-- Assumptions:
-- 1. I assume unique records. Otherwise I will use distinct in select 
-- 2. I assume no null value. Otherwise I will use ifnull()

with cancelled_trips as (
    select 
        Id
        , Request_at
    from Trips t 
    where 1=1 
        and Client_Id in (select users_id from Users where banned = 'No')
        and Driver_Id in (select users_id from Users where banned = 'No')
        and Status in ('cancelled_by_drive','cancelled_by_client')
        and Request_at >= '2013-10-01'
        and Request_at <= '2013-10-03'
),

total_requests as (
    select 
        Id,
        Request_at
    from Trips t 
    where 1=1 
        and Client_Id in (select users_id from Users where banned = 'No')
        and Driver_Id in (select users_id from Users where banned = 'No')
        and Request_at >= '2013-10-01'
        and Request_at <= '2013-10-03'
),

cancelled_per_day as (
    select
        Request_at
        , count (Id) as cancelled_trips_per_day 
    from cancelled_trips ct 
    group by Request_at
),

total_per_day as (
    select
        Request_at
        , count (Id) as total_requests_per_day 
    from total_requests tr
    group by Request_at
)

select 
    Request_at as Day 
    , ROUND(cancelled_trips_per_day * 1.00 / total_requests_per_day,2) as Cancellation_rate 
from total_requests_per_day tpd 
join cancelled_per_day cpd 
    on tpd.Request_at = cpd.Request_at



