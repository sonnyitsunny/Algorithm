-- 코드를 입력하세요

#in out left조인 , animal_id기준으로
#where out의 animal_id가 not null인 거 이면서, 호 시작일보다 입양일이 더 빠른 경우
#


SELECT O.ANIMAL_ID,O.NAME
FROM ANIMAL_INS I LEFT JOIN ANIMAL_OUTS O ON I.ANIMAL_ID=O.ANIMAL_ID
WHERE O.ANIMAL_ID IS NOT NULL AND I.DATETIME>O.DATETIME
ORDER BY I.DATETIME;

