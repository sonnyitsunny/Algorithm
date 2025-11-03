-- 코드를 작성해주세요
with recursive tmp as (
    select id, parent_id, 1 as GENERATION
    from ecoli_data
    where parent_id is null
    union all
    select s.id, s.parent_id, tmp.generation + 1
    from tmp join ecoli_data s
    on tmp.id = s.parent_id
)

select COUNT(*) AS COUNT,GENERATION
from tmp
WHERE id not in (SELECT parent_id 
                 FROM tmp
                 WHERE parent_id is not null
                 
                )
GROUP BY GENERATION
ORDER BY GENERATION
