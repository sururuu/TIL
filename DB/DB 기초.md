# DB 

### 데이터 베이스(Database, DB) 정의

데이터 베이스는 여러 사람이 공유하여 사용할 목적으로 체계화해 통합, 관리하는 데이터의 집합이다.



### DBMS

데이터베이스(DB)를 관리하는 (Management) 시스템

계층형,관계형,객체지향 데이터베이스 등 존재



### RDBMS(가장 많이 이용)

관계형 모델을 기반으로하는 데이터베이스 관리시스템 

MySQL, SQLITE



### 관계형 데이터베이스

- 관계형 데이터베이스는 관계를 열과 행으로 이루어진 테이블 집합으로 구성
- 각 열의 특정 종류의 데이터를 기록
- 테이블의 행은 각 객체/엔터티와 관련된 값의 모음



### 기본 용어

- 스키마

  - 데이터베이스에서 자료의 구조와 제약 조건(구조, 표현방법, 관계 등)에 관한 전반적인 명세

- 테이블(관계)

  - 열과 행의 모델을 사용해 조작된 데이터 요소들의 집합

- column(열),속성

  - 각 열에는 고유한 데이터 형식이 있다. 

- row (행),레코드

  - 테이블의 데이터는 행으로 저장
  - 테이블에 4명의 고객정보가 저장되어 있으며 행은 4개가 존재한다.

- PK(Primary Key) 기본기

  - 각 행의 고유값으로 저장된 레코드를 고유하게 식별할 수 있는 값

  ex) 주민등록번호, 학번 등



# SQL 

### SQL 정의

| 분류                                              | 개념                                                         | 예시                         |
| ------------------------------------------------- | ------------------------------------------------------------ | ---------------------------- |
| DDL(Data Definition Language) -데이터 정의 언어   | 데이터 정의 - 관계형 데이터베이스 구조(테이블, 스키마)를 정의하기 위한 명령어 | CREATE/DROP/ALTER            |
| DML(Data Manipulation Languate) - 데이터 조작언어 | 데이터 저장, 수정, 삭제 조회 등                              | INSERT/UPDATE/DELETE/SELECT  |
| DCL(Data Control Language) - 데이터 제어 언어     | 데이터베이스 사용자의 권한 제어 등                           | GRANT/REVOKE/COMMIT/ROLLBACK |



### 기본구조

> SQL(Structured Query Language)

관계형 데이터베이스 관리시스템(REBMS)의 데이터를 관리하기 위해 설계된 특수 목적의 프로그래밍 언어 RDBMS 에서 자료의 검색과 관리, 데이터베이스 스키마 생성과 수정, 데이터베이스 접근 관리 등을 위해 고안 됨.



### 기본 데이터베이스 활용법

- SQLite3 생성/접근
  - sqlite3  `filename`
- 테이블 목록 조회
  - .tables
- 특정 테이블 스키마 조회
  - .schema `table`



### SELECT 

> SELECT문은 데이터를 읽어올 수 있으며, 특정한 테이블을 반환한다.

##### SELECT * FROM  table;



### 테이블 생성

##### CREATE TABLE table(

##### 	column1 datatype[constraints],

##### 	column2 datatype[constraints],

##### );



### Datatype(SQLite)

1. INEGER : TINYINT(1byte), SMALLINT(2bytes),MEDIUMINT(3bytes),INT(4bytes),BIGINT(8bytes),UNSIGNED BIG INT
2. TEXT : CHARACTER(20),VARCHAR(255),TEXT
3. REAL : REAL, DOUBLE, FLOAT
4. NUMERIC : NUMERIC, DECIMAL, BOOLEAN, DATE, DATETIME
5. BLOB : no datatype specifi ed



### SQL

```SQLITE
squlite> CREATE TABLE classmates(
	id INTEGER PRIMARY KEY AUTOINCREATENT,
	name TEXT NOT NULL,
	age INTEGER,
	address TEXT
);
```

`PRIMARY KEY AUTOINCREATENT` : PRIMARY KEY  자동 증가 시켜주기

`NOT NULL` : 필수값



### 테이블 삭제

##### DROP TABLE table;



## CRUD

### 추가 

>  특정 테이블에 새로운 행을 추가하여 데이터를 추가

##### INSERT INTO table(column1, ----) VALUES(VALUE1,----);

```sqlite
sqlite> INSERT INTO classmates(name,age) VALUES('홍길동',23);
```



> 모든 열에 데이터를 넣을 떄에는 column 을 명시할 필요가 없음

```sqlite
sqlite> INSERT INTO classmates VALUES(2,'홍길동',30,'서울');
```



### 읽기

> 특정 테이블에 특정 레코드를 조회

##### SELECT * FROM  table WHERE condition ;

##### SELECT  column1 ---- FROM table WHERE condition;



> 중복 없이 가져오기

##### SELECT `DISTINCT` column FROM table;

```sqlite
sqlite> SELECT DISTINCT name FROM classmates;
```



###  삭제

> 특정 테이블에 특정 레코드를 삭제

##### DELETE FROM table WHERE condition;

```sqlite
sqlite> DELETE FROM classmates WHERE id=4;
```



### 수정

> 특정 테이블에 특정 레코드를 수정

##### UPDATE table SET column1=value1, ---- WHERE condition;

```sqlite
squlite> UPDATE classmates SET name='홍길동', address='제주', WHERE id=4;
```



### 표현식 

1. 특정 테이블에 특정 레코드의 개수

- ##### SELECT `COUNT(column)` FROM table;

```sqlite
sqlite> SELECT COUNT(*) FROM classmates;
```

2. 특정 테이블에 특정 레코드의 평균

- ##### SELECT `AVG(column)` FROM table;

3. 특정 테이블에 특정 레코드의 합

- ##### SELECT `SUM(column)` FROM table;

4. 특정 테이블에 특정 레코드의 최소값

- ##### SELECT `MIN(column)` FROM table;

5. 특정 테이블에 특정 레코드의 최대값

- ##### SELECT `MAX(column)` FROM table;

```sqlite
sqlite> SELECT name,MAX(age) FROM classmates;
```

```sqlite
sqlite> SELECT MIN(age),MAX(age) FROM classmates;
```



###  WHERE

##### SELECT column FROM table WHERE condition;

ex) condition : age >=19, last_name='김', balance < 10000

```sqlite
sqlite> SELECT * FROM classmates WHERE name='김' and age>=19;
```



### LIKE

##### select * FROM table WHERE column LIKE 'pattern';

```sqlite
sqlite> SELECT * FROM classmates WHERE phone LIKE '010-%';
```



####  와일드 카드

`%` : 문자열이 있을 수도 있고 , 없을 수 도 있음

`_`: 반드시 한 개의 문자가 있다.

- 2% : 2로 시작하는 값
- %2 : 2로 끝나는 값
- %2% : 2가 들어가는 값
- _2% : 두번째가 2로 시작하는 값
- 1_ _ _ : 1로 시작하고 4자리인 값
- 2_ % _ %/ 2_ _ % : 2로 시작하고 적오도 3자리인 값



### ORDER BY

> 특정 column을 기준으로 정렬

##### SELECT columns FROM table ORDER BY column1, column2 ASC/DESC;

ASC : default ,오름차순

DESC : 내림차순

```sqlite
sqlite> SELECT * FROM classmates ORDER BY age ASC name DESC;
```



### LIMIT

> 특정 table에서 원하는 개수만큼 가져오기

> `OFFSET` : N개의 Row를 건너뛰고 출력하기

```sqlite
sqlite> SELECT name FROM classsmates LIMIT 10;
```

```sqlite
sqlite> SELECT name FROM classmantes LIMIT 1 OFFSET 2;
```



### GROUP BY

> 특정 컬럼을 기준으로 그룹화 하기

```sqlite
sqlite> SELECT sex, COUNT(name) FROM classmates GROUP BY sex;
```

