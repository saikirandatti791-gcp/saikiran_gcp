select *,rank()over(partition by country salary desc ) from table;


select distinct(country) from table ;



select * from emply where id = 1 and country='india' ;