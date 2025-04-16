-- 코드를 입력하세요
SELECT YEAR(S.SALES_DATE) AS YEAR,MONTH(S.SALES_DATE) AS MONTH,I.GENDER,COUNT(DISTINCT S.USER_ID) AS USERS
FROM USER_INFO I INNER JOIN ONLINE_SALE S ON I.USER_ID=S.USER_ID
WHERE I.GENDER IS NOT NULL
GROUP BY YEAR, MONTH,I.GENDER

ORDER BY YEAR,MONTH, I.GENDER