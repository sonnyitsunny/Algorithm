-- 코드를 작성해주세요


SELECT ID,IFNULL(LENGTH,10) AS LENGTH
FROM FISH_INFO

ORDER BY LENGTH DESC, ID ASC
LIMIT 10;