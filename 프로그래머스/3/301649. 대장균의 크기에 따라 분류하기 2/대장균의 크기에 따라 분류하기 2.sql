-- 코드를 작성해주세요
SELECT A.ID,
    CASE 
        WHEN A.per>=0.75 THEN 'CRITICAL'
        WHEN A.per>=0.5 THEN 'HIGH'
        WHEN A.per>=0.25 THEN 'MEDIUM'
        ELSE 'LOW'
END AS COLONY_NAME
FROM (SELECT ID,
     PERCENT_RANK() OVER(order by SIZE_OF_COLONY ) AS per
     FROM ECOLI_DATA
     ) AS A
ORDER BY A.ID;