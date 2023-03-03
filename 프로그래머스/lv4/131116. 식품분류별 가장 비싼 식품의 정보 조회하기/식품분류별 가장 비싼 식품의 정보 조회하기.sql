# -- 코드를 입력하세요
# SELECT CATEGORY, MAX(PRICE) AS MAX_PRICE, PRODUCT_NAME
# FROM FOOD_PRODUCT FP
# WHERE CATEGORY IN ('과자','국','김치','식용유')
# AND PRICE IN (SELECT MAX(PRICE) FROM FOOD_PRODUCT GROUP BY CATEGORY)
# GROUP BY 1
# ORDER BY 2 DESC

SELECT CATEGORY, MAX_PRICE, PRODUCT_NAME
FROM (
        SELECT CATEGORY, PRICE AS MAX_PRICE, PRODUCT_NAME, rank() over(partition by category order by price desc) r # 그룹별 랭킹
        FROM FOOD_PRODUCT
    ) tmp
WHERE CATEGORY REGEXP '과자|국|김치|식용유'
AND r = 1
ORDER BY 2 DESC

# 과자 1950, 국 2900, 식용유 8950

# SELECT 
#     CATEGORY, 
#     PRICE,
#     PRODUCT_NAME
# FROM 
#     FOOD_PRODUCT
# WHERE 
#     CATEGORY REGEXP '과자|국|김치|식용유'
# AND 
#     PRICE IN (SELECT MAX(PRICE) FROM FOOD_PRODUCT GROUP BY CATEGORY)
# GROUP BY 1
# ORDER BY 2 DESC

















# 김치	19000	맛있는배추김치
# 식용유	8950	맛있는콩기름
# 국	2900	맛있는미역국
# 과자	1950	맛있는포카칩