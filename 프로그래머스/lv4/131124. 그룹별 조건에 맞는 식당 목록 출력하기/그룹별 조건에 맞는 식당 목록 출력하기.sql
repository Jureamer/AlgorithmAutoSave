WITH REVIEW_NUMBER AS (
    SELECT
        MP.MEMBER_ID AS MEMBER_ID,
        MP.MEMBER_NAME AS MEMBER_NAME,
        COUNT(*) AS NUMBER
    FROM 
        MEMBER_PROFILE MP,
        REST_REVIEW RR
    WHERE 
        MP.MEMBER_ID = RR.MEMBER_ID
    GROUP BY
        1
    ORDER BY 
        3 DESC
    LIMIT 0, 1
    )
    
SELECT 
    MP.MEMBER_NAME,
    REVIEW_TEXT,
    LEFT(REVIEW_DATE, 10) AS REVIEW_DATE
FROM
    MEMBER_PROFILE MP,
    REST_REVIEW RR,
    REVIEW_NUMBER RN
WHERE MP.MEMBER_ID = RR.MEMBER_ID
AND RN.MEMBER_ID = MP.MEMBER_ID
AND RN.MEMBER_ID IN(RN.MEMBER_ID)
ORDER BY 3, 2
# FROM ( 
#     SELECT 
#         MEMBER_ID, MEMBER_NAME 
#     FROM 
#         REVIEW_NUMBER
#     WHERE
#         NUMBER = MAX(NUMBER)
# ) AS REVIEW_MAX_NAME

    # REVIEW_MAX_NAME AS (
    
    # )
    
# SELECT * FROM REVIEW_MAX_NAME




# MEMBER_PROFILE MP,
# REST_REVIEW RR,
# REVIEW_NUMBER RN
# WHERE MP.MEMBER_ID = RR.MEMBER_ID
# AND MP.MEMBER_ID = RN.MEMBER_ID



# 리뷰를 가장 많이 작성한 "회원의 리뷰들"을 조회
# (출력) 회원 이름, 리뷰 텍스트, 리뷰 작성일
# (정렬) 리뷰 작성일, 리뷰텍스트



