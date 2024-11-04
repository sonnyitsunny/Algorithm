-- 코드를 작성해주세요
#where에서 rarity가 legend인 거
#sum() as TOTAL_PRICE로
SELECT SUM(PRICE) AS TOTAL_PRICE
FROM ITEM_INFO
WHERE RARITY='LEGEND';