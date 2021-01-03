# SQL - GROUP BY 연습하기

### 고양이와 개는 몇 마리 있을까

```sql
SELECT ANIMAL_TYPE, COUNT(ANIMAL_ID) AS count FROM ANIMAL_INS
GROUP BY ANIMAL_TYPE
ORDER BY count
```

```SQL
SELECT ANIMAL_TYPE, COUNT(ANIMAL_ID) AS count FROM ANIMAL_INS
GROUP BY ANIMAL_TYPE
ORDER BY count
CASE ANIMAL_TYPE 
WHEN 'Cat' THEN 1 
WHEN 'Dog' THEN 2
ELSE 3
END
```



### 동명 동물 수 찾기

```SQL
SELECT NAME, COUNT(NAME) AS count FROM ANIMAL_INS
GROUP BY NAME
HAVING COUNT(NAME) >= 2
ORDER BY NAME
```



### 입양 시각 구하기(1)

> 09:00 부터 19:59 까지 각 시간대별로 입양 건수 구하기

```SQL
SELECT HOUR(DATETIME) AS HOUR, COUNT(HOUR) AS count 
FROM ANIMAL_INS
GROUP BY HOUR(DATETIME)
HAVING HOUR >= 9 AND HOUR < 20
ORDER BY HOUR
```



### 입양 시각 구하기(2)

> 0시부터 23시까지 각 시간대별로 입양 건수 고하기

```SQL
@hour := -1;
SELECT (@hour := @hour + 1) as HOUR, 
(SELECT * FROM ANIMAL_OUTS WHERE HOUR(DATETIME) = @HOUR) AS COUNT
FROM ANIMAL_OUTS
WHERE @hour < 23;
```

