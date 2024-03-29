-- 코드를 입력하세요


#2022년 1월 기준
# 저자별, 카테고리별 매출액을 구하여
# 저자ID, 저자명, 카테고리, 매출액을 출력
# 저자ID 오름차순, 카테고리 내림차순


# SELECT a.AUTHOR_ID, a.AUTHOR_NAME, CATEGORY, PRICE * SALES AS TOTAL_SALES
# SELECT *
# FROM BOOK b, AUTHOR a, BOOK_SALES s
# WHERE b.BOOK_ID = s.BOOK_ID
# AND b.AUTHOR_ID = a.AUTHOR_ID
# AND s.SALES_DATE LIKE '2022-01%'
# # GROUP BY 1, 3
# ORDER BY 1, 3 DESC

# ORDER BY AUTHOR_ID ASC, CATEGORY DES

SELECT b.AUTHOR_ID, a.AUTHOR_NAME, CATEGORY, SUM(SALES * PRICE) AS TOTAL_SALES
FROM BOOK b, BOOK_SALES s, AUTHOR a
WHERE b.BOOK_ID = s.BOOK_ID
AND a.AUTHOR_ID = b.AUTHOR_ID
AND s.SALES_DATE LIKE '2022-01%'
GROUP BY b.AUTHOR_ID, b.CATEGORY
ORDER BY 1, 3 DESC;