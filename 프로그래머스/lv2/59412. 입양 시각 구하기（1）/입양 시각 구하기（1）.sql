-- 코드를 입력하세요
SELECT HOUR(DATETIME) AS HOUR, COUNT(ANIMAL_ID) AS COUNT
FROM ANIMAL_OUTS
WHERE HOUR(DATETIME) BETWEEN 9 AND 19
GROUP BY 1
ORDER BY 1
# 09:00 ~ 19:59까지 각 시간대별로 입양이 몇건이나 발생했는 지 조회하기