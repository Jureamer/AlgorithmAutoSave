SELECT o.ANIMAL_ID
    ,o.NAME 
FROM ANIMAL_OUTS o LEFT OUTER JOIN
    ANIMAL_INS i
ON o.ANIMAL_ID = i.ANIMAL_ID
WHERE i.ANIMAL_ID IS NULL
ORDER BY ANIMAL_ID


# SELECT * FROM ANIMAL_OUTS
# WHERE ANIMAL_ID = 'A368930'