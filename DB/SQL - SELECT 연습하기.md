# SQL - SELECT 연습하기

### 모든 레코드 조회하기

```sql
SELECT * FROM ANIMAL_INS
ORDER BY ANIMAL_ID
```

> 역순으로 정렬하기 DESC



### 아픈 동물의 아이디와 이름 조회

```sql
SELECT ANIMAL_ID, NAME FROM ANIMAL_INS
WHERE INTAKE_CONDITION = 'Sick'
ORDER BY ANIMAL_ID
```



### 가장 먼저 들어온 동물의 이름 조회

```SQL
SELECT NAME FROM ANIMAL_INS
ORDER BY DATETIME
LIMIT 1
```

