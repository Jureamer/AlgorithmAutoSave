WITH MAX_FAVORITES AS (
    SELECT
        FOOD_TYPE,
        MAX(FAVORITES) AS FAVORITES
        FROM REST_INFO
    GROUP BY FOOD_TYPE
)

SELECT r.FOOD_TYPE,
    REST_ID,
    REST_NAME,
    r.FAVORITES
FROM REST_INFO r, MAX_FAVORITES m
WHERE r.FOOD_TYPE = m.FOOD_TYPE
AND r.FAVORITES = m.FAVORITES
GROUP BY FOOD_TYPE

ORDER BY 1 DESC