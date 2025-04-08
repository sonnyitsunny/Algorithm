-- 코드를 작성해주세요


SELECT E.EMP_NO,E.EMP_NAME,
    CASE
    WHEN AVG(G.SCORE) >=96 THEN 'S'
    WHEN AVG(G.SCORE) >=90 THEN 'A'
    WHEN AVG(G.SCORE) >=80 THEN 'B'
    ELSE 'C'
    END AS GRADE,
    
    CASE
    WHEN AVG(G.SCORE) >=96 THEN E.SAL*0.2
    WHEN AVG(G.SCORE) >=90 THEN E.SAL*0.15
    WHEN AVG(G.SCORE) >=80 THEN E.SAL*0.1
    
    ELSE E.SAL*0
    END AS BONUS
FROM HR_DEPARTMENT D INNER JOIN HR_EMPLOYEES E ON D.DEPT_ID=E.DEPT_ID
INNER JOIN HR_GRADE G ON G.EMP_NO=E.EMP_NO

GROUP BY E.EMP_NO
ORDER BY E.EMP_NO;


    # (SELECT EMP_NO,AVG(SCORE) AS SCORE
    # FROM HR_GRADE
    # GROUP BY EMP_NO) AS G