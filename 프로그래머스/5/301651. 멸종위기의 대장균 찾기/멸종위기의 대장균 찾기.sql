-- 코드를 작성해주세요
with recursive tmp as (
    select id, parent_id, 1 as generation
    from ecoli_data
    where parent_id is null
    union all
    select s.id,s.parent_id,tmp.generation+1  
    from ECOLI_DATA s inner join tmp on tmp.id=s.parent_id
    
    
    )
select count(*) as COUNT,generation AS GENERATION
from tmp
where id not in (select distinct parent_id from ecoli_data where parent_id is not null)
group by generation
order by generation;