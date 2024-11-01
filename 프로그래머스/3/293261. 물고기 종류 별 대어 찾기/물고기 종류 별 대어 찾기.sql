SELECT I.ID,N.FISH_NAME,maxlength.LENGTH


FROM FISH_INFO I INNER JOIN FISH_NAME_INFO N ON I.FISH_TYPE=N.FISH_TYPE
INNER JOIN (SELECT FISH_TYPE,MAX(LENGTH) AS LENGTH 
           FROM FISH_INFO
            GROUP BY FISH_TYPE
           ) AS maxlength ON I.FISH_TYPE=maxlength.FISH_TYPE AND I.LENGTH=maxlength.LENGTH

ORDER BY I.ID;

