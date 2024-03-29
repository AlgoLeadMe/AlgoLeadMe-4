SELECT MONTH(START_DATE) AS MONTH, CAR_ID, COUNT(*) AS RECORDS 
FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY

WHERE DATE_FORMAT(START_DATE, '%Y-%m') BETWEEN '2022-08' AND '2022-10'
    -- 1) 대여 시작일 기준 2022.08 ~ 10월까지 대여 5회 이상인 차량의 데이터 먼저 추출 
    AND CAR_ID IN (SELECT CAR_ID
                   FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
                   WHERE DATE_FORMAT(START_DATE, '%Y-%m') BETWEEN '2022-08' AND '2022-10'
                   GROUP BY CAR_ID
                   HAVING COUNT(CAR_ID) >= 5)

-- 2) 월별 차ID에 따른 총 대여횟수
GROUP BY CAR_ID, MONTH(START_DATE)
-- 3) 0인 데이터 제외 - having count > 0
HAVING RECORDS > 0 
-- 4) 정렬 
ORDER BY MONTH, CAR_ID DESC