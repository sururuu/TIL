# SQL - SUM,MAX,MIN 연습하기

### 가장 최근에 들어온 동물은 언제 들어왔을까

```sql
SELECT DATETIME AS '시간' FROM ANIMAL_INS
ORDER BY DATETIME DESC
LIMIT 1
```

```SQL
SELECT MAX(DATETIME) AS '시간' FROM ANIMAL_INS
```



### 보호서에 들어온 동물의 수

```SQL
SELECT COUNT(ANIMAL_ID) AS CNT FROM ANIMAL_INS
```



### 이름이 있고 중복을 제거하여 이름 갯수 구하기

```SQL
SELECT COUNT(DISTINCT NAME) FROM ANIMAL_INS
WHERE NAME IS NOT NULL
```

