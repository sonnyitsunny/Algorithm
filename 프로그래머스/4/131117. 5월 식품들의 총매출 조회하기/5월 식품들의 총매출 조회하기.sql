-- 코드를 입력하세요
SELECT P.PRODUCT_ID,P.PRODUCT_NAME,P.PRICE*SUM(O.AMOUNT) AS TOTAL_SALES

FROM FOOD_PRODUCT P INNER JOIN (SELECT PRODUCT_ID,PRODUCE_DATE,AMOUNT
                               FROM FOOD_ORDER
                               WHERE PRODUCE_DATE >= '2022-05-01' AND PRODUCE_DATE <= '2022-05-31') AS O ON P.PRODUCT_ID=O.PRODUCT_ID

GROUP BY P.PRODUCT_ID

ORDER BY TOTAL_SALES DESC, P.PRODUCT_ID;