select *,rank()over(partition by country salary desc ) from table;


select distinct(country) from table ;