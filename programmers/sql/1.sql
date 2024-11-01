-- problem name: 특정 형질을 가지는 대장균 찾기
-- problem site: https://school.programmers.co.kr/learn/courses/30/lessons/301646

-- 2번을 보유하지 않으면서 1번이나 3번을 가지는 케이스
-- 001, 101, 100

SELECT count(*) as COUNT
FROM ECOLI_DATA as e
WHERE e.GENOTYPE % 8 in (1, 5, 4);