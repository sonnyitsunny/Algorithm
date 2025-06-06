-- 코드를 입력하세요

#3개 테이블 합치고 
#where절에 22년 1월
#저자이름이랑 카테고리로 그룹화
SELECT A.AUTHOR_ID,A.AUTHOR_NAME ,B.CATEGORY, SUM(B.PRICE*S.SALES) AS TOTAL_SALES
FROM BOOK B INNER JOIN BOOK_SALES S ON B.BOOK_ID=S.BOOK_ID
INNER JOIN AUTHOR A ON A.AUTHOR_ID=B.AUTHOR_ID
WHERE S.SALES_DATE LIKE '2022-01%'
GROUP BY A.AUTHOR_ID,B.CATEGORY
ORDER BY A.AUTHOR_ID,B.CATEGORY DESC;
